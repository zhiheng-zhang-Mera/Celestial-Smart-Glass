# 样本量与精度规划：可复现计算

状态：设计阶段合成 Monte Carlo 计算；不是参与者观察，不是正式研究结果，不是完整 GLMM 功效分析。

本目录仅保存计划参数、生成程序、测试、汇总结果和空白计划分配表。每一行模拟结果都是在明确假设下重复抽样的产物；allocation 中的 planned 编号不是参与者编号。

## 入口

- 研究解读与数值表：[样本量与精度规划](../../05-实验与评估/样本量与精度规划.md)。
- 确认性方法的拟议版本：[统计分析预注册草案](../../05-实验与评估/统计分析预注册草案.md)。
- 材料、分配与问卷：[详细实验材料与问卷](../../05-实验与评估/详细实验材料与问卷.md)。
- 计算程序：[precision_sensitivity.py](precision_sensitivity.py)；单元检查：[test_precision_sensitivity.py](test_precision_sensitivity.py)。
- 生成汇总：[precision_results.csv](precision_results.csv)；完整假设与运行版本：[simulation_manifest.json](simulation_manifest.json)。
- [24 人分配表](allocation_n24.csv) / [36 人分配表](allocation_n36.csv) / [48 人分配表](allocation_n48.csv)：平衡分配的计划模板，不表示人数已变更。

本次完整运行：主种子 20261022，每组合 4000 次，共 33 组合 / 132000 次有效合成研究，零个无可用配对估计的重复；八项单元检查通过。manifest 记录计算与测试源码的 SHA-256，方便检查对应版本。这里的“有效重复”只指描述估计器产生结果，不是 GLMM 拟合成功。

## 运行

环境要求 Python 3.12、NumPy、SciPy；具体已运行版本见 manifest。无需网络、付费服务、R 或真实研究数据。在本目录执行：

    python3 -B -m unittest test_precision_sensitivity.py
    python3 -B precision_sensitivity.py --repetitions 4000 --seed 20261022

若使用本项目提供的 primary runtime，请将 python3 替换为环境变量 CODEX_PRIMARY_RUNTIME_PYTHON 指向的解释器。命令会覆盖本目录中同名的生成结果；手写研究记录不得使用这些文件名。不要把真实数据放入本目录。

## 计算边界

数据生成含参与者、题目、对话、参与者×对话的截距，以及参与者和题目的条件效应异质性。它保留每人每条件12题、18段对话/36题和跨人条件×材料平衡结构；不是把全部二元作答当独立样本。

估计器是每人 C2−C0 准确率差的均值。程序报告其相对已知合成真值的重复抽样误差，**不拟合 GLMM、不产生最终分析的置信区间、不计算显著检验的功效**。未来正式 GLMM 的收敛、bootstrap 区间覆盖和检验错误率仍需单独验证。

95%绝对误差分位数表示在该合成世界下约95%的估计距离真值不超过该范围；它不是从一份真实数据得到的95%置信区间半宽。MNAR 场景故意展示有偏缺失，不能把增大样本量说成偏差修复。

## 结果字段读法

| 字段 | 单位与分母 |
| --- | --- |
| true_difference_pp / mean_estimate_pp / bias_pp | 已知合成真值、有效重复的平均配对估计、平均估计减真值；百分点 |
| sampling_sd_pp | 有效重复之间估计值的样本标准差；不是单次研究的标准误估计 |
| error_q025_pp / error_q975_pp | 有符号估计误差的分位数；不是从一份观察数据反演的置信区间 |
| abs_error_q95_pp | 相对已知真值的绝对误差 95% 分位数；正文主要精度摘要 |
| normal_equivalent_halfwidth_pp | 1.96×重复抽样 SD 的正态等价参考值；不是正式模型或研究数据的 CI 半宽 |
| mcse_mean_pp / approx_mcse_sd_pp | 有限模拟重复造成的数值误差，后者使用正态近似；不覆盖假设不确定性 |
| mean_participants_with_c0_c2 | 每个有效重复中同时拥有 C0/C2 可评分题、能贡献配对差的人数均值 |
| mean_scored_c0 / c1 / c2 | 各条件可评分二元回答总数的重复均值；不把题数当独立人数 |
| failed_repetitions | 没有人可贡献配对差、因此无法计算描述估计的重复数；不是 GLMM 拟合失败数 |
| intercept_c0 / c1 / c2 | 按各条件随机效应方差和固定设计效应校准的条件截距；不是 logit(边际正确率) |

## 已知限制

参数不是从 DHH 参与者、试点或既有论文中估计的；低/中/高异质性仅是敏感性假设。主模型拟议使用的随机效应独立正态假设、平衡分配、同一材料长度和缺失机制均可能与真实研究不同。

计算不给24人“充足”背书，也不擅自批准36或48人。最终目标须在看主研究结果前，由导师、研究资源与招募可行性共同确定并记录。

[返回实验实现导航](../README.md) · [返回实验与评估](../../05-实验与评估/README.md)
