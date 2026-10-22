"""设计阶段精度敏感性计算；只有合成随机变量，没有参与者数据。

重要：生成交叉 logistic 随机效应数据，但不拟合 GLMM、不估计检验功效。
报告配对平均准确率差的重复抽样误差，不能替代最终 GLMM 区间覆盖验证。
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import platform
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import brentq
from scipy.special import expit


NODES, WEIGHTS = hermgauss(60)
DEFAULT_SEED = 20261022


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    description: str
    reps: int = 4000
    baseline: float = 0.70
    delta_c2: float = 0.10
    items: int = 36
    participant_sd: float = 0.75
    item_sd: float = 0.60
    clip_sd: float = 0.25
    participant_clip_sd: float = 0.20
    participant_slope_sd: float = 0.35
    item_slope_sd: float = 0.25
    dropout_probability: float = 0.0
    response_missing_probability: float = 0.0
    additional_c2_wrong_missing: float = 0.0
    period_effects: tuple[float, ...] = (-0.10, 0.0, 0.10)
    set_effects: tuple[float, ...] = (-0.10, 0.0, 0.10)


def allocation(n: int, seed: int = DEFAULT_SEED) -> list[dict]:
    """六行正交块：每个条件×集合、集合×时期每块恰出现两次。"""
    if n < 6 or n % 6:
        raise ValueError("n must be a positive multiple of six")
    block = []
    for direction in (1, -1):
        for shift in range(3):
            conditions = [(shift + direction * period) % 3 for period in range(3)]
            sets = [(2 * shift + direction * period) % 3 for period in range(3)]
            block.append({"conditions": conditions, "sets": sets})
    rng = np.random.default_rng(seed)
    rows = [dict(conditions=r["conditions"][:], sets=r["sets"][:])
            for _ in range(n // 6) for r in block]
    rows = [rows[index] for index in rng.permutation(n)]
    return rows


def marginal_probability(
    intercept: float,
    variance: float,
    period_effects=(-0.10, 0.0, 0.10),
    set_effects=(-0.10, 0.0, 0.10),
) -> float:
    """对正态随机效应和九个时期×集合组合积分，不使用 logit 逆变换近似。"""
    shifts = np.asarray([a + b for a in period_effects for b in set_effects])
    latent = intercept + shifts[:, None] + np.sqrt(2 * variance) * NODES[None, :]
    return float(np.mean(expit(latent) @ WEIGHTS / np.sqrt(np.pi)))


def calibrate_intercept(
    target_probability: float,
    variance: float,
    period_effects=(-0.10, 0.0, 0.10),
    set_effects=(-0.10, 0.0, 0.10),
) -> float:
    if not 0 < target_probability < 1 or variance < 0:
        raise ValueError("Invalid target probability or variance")
    return float(brentq(
        lambda x: marginal_probability(x, variance, period_effects, set_effects)
        - target_probability, -20, 20, xtol=1e-12,
    ))


def design_arrays(n: int, items: int, seed: int):
    if items % 6:
        raise ValueError("items must be divisible by six (three sets, two questions per clip)")
    rows = allocation(n, seed)
    item_sets = np.repeat(np.arange(3), items // 3)
    conditions = np.empty((n, items), dtype=int)
    periods = np.empty((n, items), dtype=int)
    for participant, row in enumerate(rows):
        for period, (condition, material_set) in enumerate(zip(row["conditions"], row["sets"])):
            mask = item_sets == material_set
            conditions[participant, mask] = condition
            periods[participant, mask] = period
    return conditions, periods, item_sets


def simulate_scenario(case: Scenario, n: int, seed: int = DEFAULT_SEED) -> dict:
    if case.reps < 2:
        raise ValueError("At least two repetitions are needed")
    conditions, periods, item_sets = design_arrays(n, case.items, seed)
    c1 = (conditions == 1)[None, :, :]
    c2 = (conditions == 2)[None, :, :]
    masks = [(conditions == c)[None, :, :] for c in range(3)]
    base_variance = (case.participant_sd ** 2 + case.item_sd ** 2
                     + case.clip_sd ** 2 + case.participant_clip_sd ** 2)
    slope_variance = case.participant_slope_sd ** 2 + case.item_slope_sd ** 2
    targets = [case.baseline, case.baseline + case.delta_c2 / 2,
               case.baseline + case.delta_c2]
    intercepts = [
        calibrate_intercept(
            probability, base_variance + (0 if condition == 0 else slope_variance),
            case.period_effects, case.set_effects,
        )
        for condition, probability in enumerate(targets)
    ]
    fixed = (np.asarray(intercepts)[conditions]
             + np.asarray(case.period_effects)[periods]
             + np.asarray(case.set_effects)[item_sets][None, :])
    rng = np.random.default_rng(seed)
    all_estimates = []
    retained_counts = []
    response_counts = []
    failed = 0
    batch_size = 100
    for start in range(0, case.reps, batch_size):
        batch = min(batch_size, case.reps - start)
        eta = np.broadcast_to(fixed, (batch, n, case.items)).copy()
        eta += rng.normal(0, case.participant_sd, (batch, n, 1))
        eta += rng.normal(0, case.item_sd, (batch, 1, case.items))
        eta += np.repeat(rng.normal(0, case.clip_sd, (batch, 1, case.items // 2)), 2, axis=2)
        eta += np.repeat(
            rng.normal(0, case.participant_clip_sd, (batch, n, case.items // 2)), 2, axis=2
        )
        for contrast in (c1, c2):
            slope = (rng.normal(0, case.participant_slope_sd, (batch, n, 1))
                     + rng.normal(0, case.item_slope_sd, (batch, 1, case.items)))
            eta += slope * contrast
        outcomes = rng.binomial(1, expit(eta)).astype(float)
        observed = np.ones(outcomes.shape, dtype=bool)
        if case.dropout_probability:
            observed &= rng.random((batch, n, 1)) >= case.dropout_probability
        missing_probability = (case.response_missing_probability
                               + case.additional_c2_wrong_missing * c2 * (1 - outcomes))
        if np.any(missing_probability):
            observed &= rng.random(outcomes.shape) >= missing_probability
        means, counts = [], []
        for mask in masks:
            available = observed & mask
            count = available.sum(axis=2)
            score_sum = (outcomes * available).sum(axis=2)
            mean = np.divide(score_sum, count, out=np.full_like(score_sum, np.nan), where=count > 0)
            means.append(mean)
            counts.append(count)
        valid = np.isfinite(means[0]) & np.isfinite(means[2])
        participants = valid.sum(axis=1)
        differences = np.where(valid, means[2] - means[0], 0.0).sum(axis=1)
        estimates = np.divide(differences, participants,
                              out=np.full_like(differences, np.nan), where=participants > 0)
        success = np.isfinite(estimates)
        all_estimates.extend(estimates[success].tolist())
        retained_counts.extend(participants[success].tolist())
        response_counts.extend(np.stack([x.sum(axis=1) for x in counts], axis=1)[success].tolist())
        failed += int((~success).sum())
    estimates = np.asarray(all_estimates)
    error = estimates - case.delta_c2
    sd = float(np.std(estimates, ddof=1))
    counts_mean = np.mean(response_counts, axis=0)
    result = {
        "scenario_id": case.scenario_id,
        "description": case.description,
        "n_randomized": n,
        "items_total": case.items,
        "items_per_condition_per_person": case.items // 3,
        "repetitions": case.reps,
        "seed": seed,
        "true_p_c0": case.baseline,
        "true_p_c2": case.baseline + case.delta_c2,
        "true_difference_pp": 100 * case.delta_c2,
        "mean_estimate_pp": 100 * float(np.mean(estimates)),
        "bias_pp": 100 * float(np.mean(error)),
        "sampling_sd_pp": 100 * sd,
        "error_q025_pp": 100 * float(np.quantile(error, 0.025)),
        "error_q975_pp": 100 * float(np.quantile(error, 0.975)),
        "abs_error_q95_pp": 100 * float(np.quantile(np.abs(error), 0.95)),
        "normal_equivalent_halfwidth_pp": 100 * 1.96 * sd,
        "mcse_mean_pp": 100 * sd / np.sqrt(len(estimates)),
        "approx_mcse_sd_pp": 100 * sd / np.sqrt(2 * (len(estimates) - 1)),
        "mean_participants_with_c0_c2": float(np.mean(retained_counts)),
        "mean_scored_c0": float(counts_mean[0]),
        "mean_scored_c1": float(counts_mean[1]),
        "mean_scored_c2": float(counts_mean[2]),
        "failed_repetitions": failed,
        "intercept_c0": intercepts[0],
        "intercept_c1": intercepts[1],
        "intercept_c2": intercepts[2],
    }
    return result


def scenarios(reps: int) -> list[Scenario]:
    base = Scenario("medium_70_d10", "中异质性；C0=70%，C2=80%；完整观察", reps=reps)
    return [
        replace(base, scenario_id="low_70_d10", description="低异质性；70%到80%",
                participant_sd=0.40, item_sd=0.35, clip_sd=0.15,
                participant_clip_sd=0.10, participant_slope_sd=0.15, item_slope_sd=0.10),
        base,
        replace(base, scenario_id="high_70_d10", description="高异质性；70%到80%",
                participant_sd=1.00, item_sd=0.80, clip_sd=0.40,
                participant_clip_sd=0.35, participant_slope_sd=0.60, item_slope_sd=0.45),
        replace(base, scenario_id="medium_70_d00", description="中异质性；零平均效应", delta_c2=0.0),
        replace(base, scenario_id="medium_70_d05", description="中异质性；70%到75%", delta_c2=0.05),
        replace(base, scenario_id="medium_70_d15", description="中异质性；70%到85%", delta_c2=0.15),
        replace(base, scenario_id="medium_55_d10", description="中异质性；55%到65%", baseline=0.55),
        replace(base, scenario_id="medium_85_d10", description="中异质性；85%到95%", baseline=0.85),
        replace(base, scenario_id="medium_mcar", description="中异质性；10%整人退出及10%题级MCAR",
                dropout_probability=0.10, response_missing_probability=0.10),
        replace(base, scenario_id="medium_mnar", description="中异质性；基础缺失5%，C2错题额外增加25个百分点缺失",
                response_missing_probability=0.05, additional_c2_wrong_missing=0.25),
        replace(base, scenario_id="medium_items72", description="中异质性；72题/36段，仅资源敏感性",
                items=72),
    ]


def save_allocation(folder: Path, n: int, seed: int):
    records = []
    for index, row in enumerate(allocation(n, seed), 1):
        record = {"planned_slot": f"planned-{index:03d}", "synthetic_schedule_only": True}
        for period, (condition, material_set) in enumerate(zip(row["conditions"], row["sets"]), 1):
            record[f"period_{period}_condition"] = f"C{condition}"
            record[f"period_{period}_set"] = "ABC"[material_set]
        records.append(record)
    with (folder / f"allocation_n{n}.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repetitions", type=int, default=4000)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cases = scenarios(args.repetitions)
    results = []
    for index, (case, n) in enumerate(itertools.product(cases, (24, 36, 48))):
        scenario_seed = int(np.random.SeedSequence([args.seed, index]).generate_state(1)[0])
        result = simulate_scenario(case, n, scenario_seed)
        results.append(result)
        print(f"{case.scenario_id}, N={n}: error95={result['abs_error_q95_pp']:.2f}pp, "
              f"bias={result['bias_pp']:.2f}pp, SD={result['sampling_sd_pp']:.2f}pp", flush=True)
    with (args.output_dir / "precision_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    metadata = {
        "data_kind": "SYNTHETIC_DESIGN_SIMULATION_ONLY",
        "not_participant_observations": True,
        "does_not_fit_glmm": True,
        "does_not_estimate_power": True,
        "not_fitted_confidence_interval_coverage": True,
        "seed": args.seed,
        "repetitions_per_scenario_n": args.repetitions,
        "n_values": [24, 36, 48],
        "independent_random_effects": [
            "participant intercept", "item intercept", "clip intercept",
            "participant-by-clip intercept", "participant C1/C2 slopes", "item C1/C2 slopes",
        ],
        "estimand": "population marginal probability C2 minus C0, standardized across periods and sets",
        "estimator": "mean participant paired difference between observed C2 and C0 item accuracies",
        "scope": "new participants and new items/clips in each repetition; same balanced allocation",
        "precision_definition": "95th percentile of absolute estimation error relative to known simulation truth",
        "mcse_sd_is_normal_approximation": True,
        "scenarios": [asdict(case) for case in cases],
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_source_sha256": hashlib.sha256(
            Path(__file__).with_name("test_precision_sensitivity.py").read_bytes()
        ).hexdigest(),
    }
    with (args.output_dir / "simulation_manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
        print(file=handle)
    for n in (24, 36, 48):
        save_allocation(args.output_dir, n, args.seed)
    print(f"Completed {len(results)} scenario/sample-size combinations; no real data used.")


if __name__ == "__main__":
    main()
