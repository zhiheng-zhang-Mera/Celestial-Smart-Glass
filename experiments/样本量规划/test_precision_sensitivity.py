"""设计计算的单元检查；不使用参与者数据。"""

import unittest

import numpy as np
from scipy.integrate import quad
from scipy.special import expit

from precision_sensitivity import (
    Scenario,
    allocation,
    calibrate_intercept,
    marginal_probability,
    simulate_scenario,
)


class PlanningChecks(unittest.TestCase):
    def test_balanced_allocation(self):
        for n in (6, 24, 36, 48):
            rows = allocation(n, seed=20261022)
            self.assertEqual(len(rows), n)
            orders = {}
            condition_set = np.zeros((3, 3), dtype=int)
            set_period = np.zeros((3, 3), dtype=int)
            for row in rows:
                orders[tuple(row['conditions'])] = orders.get(tuple(row['conditions']), 0) + 1
                self.assertEqual(sorted(row['conditions']), [0, 1, 2])
                self.assertEqual(sorted(row['sets']), [0, 1, 2])
                for period, (condition, material_set) in enumerate(zip(row['conditions'], row['sets'])):
                    condition_set[condition, material_set] += 1
                    set_period[material_set, period] += 1
            self.assertEqual(set(orders.values()), {n // 6})
            self.assertTrue(np.all(condition_set == n // 3))
            self.assertTrue(np.all(set_period == n // 3))

    def test_unsupported_allocation(self):
        with self.assertRaises(ValueError):
            allocation(25, 1)

    def test_zero_variance_matches_logistic(self):
        p = marginal_probability(0.8, 0.0, period_effects=(0, 0, 0), set_effects=(0, 0, 0))
        self.assertAlmostEqual(p, 1 / (1 + np.exp(-0.8)), places=12)

    def test_intercepts_match_requested_marginal_rates(self):
        for p in (0.55, 0.70, 0.85, 0.95):
            for variance in (0.0, 1.0, 2.5):
                intercept = calibrate_intercept(p, variance)
                self.assertAlmostEqual(marginal_probability(intercept, variance), p, places=9)

    def test_hermite_integral_against_independent_quadrature(self):
        for intercept, variance in ((-1.2, 0.5), (0.8, 1.0), (2.0, 2.5)):
            probabilities = []
            for period in (-0.1, 0.0, 0.1):
                for material_set in (-0.1, 0.0, 0.1):
                    value, error = quad(
                        lambda z: expit(intercept + period + material_set + np.sqrt(variance) * z)
                        * np.exp(-z * z / 2) / np.sqrt(2 * np.pi),
                        -np.inf, np.inf, epsabs=1e-11,
                    )
                    self.assertLess(error, 1e-8)
                    probabilities.append(value)
            self.assertAlmostEqual(marginal_probability(intercept, variance),
                                   float(np.mean(probabilities)), places=8)

    def test_deterministic_repeat(self):
        case = Scenario('check', 'unit check', reps=120)
        first = simulate_scenario(case, 24, seed=11)
        second = simulate_scenario(case, 24, seed=11)
        self.assertEqual(first, second)
        self.assertEqual(first['failed_repetitions'], 0)

    def test_no_random_effects_known_sampling_variance(self):
        case = Scenario(
            'independent_test', 'validation only', reps=2500,
            participant_sd=0, item_sd=0, clip_sd=0, participant_clip_sd=0,
            participant_slope_sd=0, item_slope_sd=0,
            period_effects=(0, 0, 0), set_effects=(0, 0, 0),
        )
        result = simulate_scenario(case, 24, seed=29)
        expected_sd = np.sqrt((0.7 * 0.3 + 0.8 * 0.2) / (24 * 12))
        self.assertLess(abs(result['sampling_sd_pp'] / 100 - expected_sd), 0.002)
        self.assertLess(abs(result['bias_pp']), 0.30)

    def test_uncorrelated_null_is_centred(self):
        case = Scenario('null_test', 'unit check', delta_c2=0.0, reps=1500)
        result = simulate_scenario(case, 24, seed=7)
        self.assertLess(abs(result['bias_pp']), 0.5)


if __name__ == '__main__':
    unittest.main()
