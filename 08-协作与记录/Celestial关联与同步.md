# Celestial 关联与同步

## 1. 本次修改边界

用户授权将完整智能眼镜研究与开发文档挂载到 `Celestial-Smart-Glass` 并建立中文导航。本次将该仓库作为项目权威位置，不修改其他仓库，不启用产品、CI、Runner 或远程服务。

这是文档初始化，不是运行时接线。公共索引或主系统以后需要显示本项目时，按具体导航 / 集成任务同步对应仓库；当前不宣称 Celestial-Throne 已识别、调度或执行本项目。

## 2. 仓库职责

| 仓库 | 与本项目的关系 | 数据边界 |
|---|---|---|
| Celestial-Smart-Glass | 研究范围、原型与后续产品代码、可执行契约、实验配置 | 本项目唯一实现与研究文件权威 |
| Idea-Book | 原始构想来源，已读取相关六份文件 | 只摘取本项目必要设计，保留来源与阶段说明 |
| Celestial-Design-Book | 全局架构 / 复用 / 决策方法参考 | 未来产生共享架构变化时记录固定引用，不复制全部可变方案 |
| Celestial-Mission-Book | 全局工程工作流参考 | 激活跨仓施工时登记任务与交接；本地工作书不冒充全局已领取任务 |
| Celestial-Throne | 未来可选算力或服务节点 | 不成为首年依赖，不接管设备同意和停止权 |
| Function / Evidence / Verification / Operations / Release / Navigator 系列 | 将来真实能力、运行材料、裁决、部署、发布或整体导航发生时按需更新 | 不为文档初始化制造实现、验证或发布记录 |

旧 Utopia、Boss、Hns 等冻结项目保持只读。没有明确的复用需求，不为此项目整包迁入旧架构。

## 3. 已读规范快照

核对日期：2026-10-22。规范 ID：`CEL-POLICY-20261009-v1`。

| 来源 | 完整提交 SHA | 已读文件 |
|---|---|---|
| [Celestial-Design-Book](https://github.com/zhiheng-zhang-Mera/Celestial-Design-Book/tree/5b2a0ba20f8f0d2e5996c700c46a56be37dfb0f4) | `5b2a0ba20f8f0d2e5996c700c46a56be37dfb0f4` | AGENTS；UTOPIA_MIGRATION；OPEN_SOURCE_REUSE；DECISION_PROCESS |
| [Celestial-Mission-Book](https://github.com/zhiheng-zhang-Mera/Celestial-Mission-Book/tree/5ef2a10a3aecdfa4dc2456ec067c9ff273964b29) | `5ef2a10a3aecdfa4dc2456ec067c9ff273964b29` | AGENTS；UI_FIRST_DELIVERY；CROSS_REPO_SYNC；WORKFLOW |

具体参照：[设计复用](https://github.com/zhiheng-zhang-Mera/Celestial-Design-Book/blob/5b2a0ba20f8f0d2e5996c700c46a56be37dfb0f4/docs/OPEN_SOURCE_REUSE.md)、[UI 优先](https://github.com/zhiheng-zhang-Mera/Celestial-Mission-Book/blob/5ef2a10a3aecdfa4dc2456ec067c9ff273964b29/docs/UI_FIRST_DELIVERY.md)、[影响驱动同步](https://github.com/zhiheng-zhang-Mera/Celestial-Mission-Book/blob/5ef2a10a3aecdfa4dc2456ec067c9ff273964b29/docs/CROSS_REPO_SYNC.md)。

本次沿用的原则：复用优先；UI → 入口 → 真实能力；文档 / 实现 / 验证状态分离；纯文档按差异核对；冻结来源只读；按实际影响同步；不默认启用私有 CI 或更改 GRC。

## 4. 本阶段影响清单

| 类别 | 影响 | 本次处理 |
|---|---|---|
| 目标仓库文档与导航 | 新研究和开发计划 | 写入本仓库并核对 |
| 公共协议运行版本 | 尚无可执行 schema 或已启用接口 | 仅写 draft，不要求依赖方升级 |
| 全局产品功能状态 | 没有新增运行能力 | 不登记为 IMPLEMENTED / VERIFIED |
| 部署与发布 | 无实际安装或应用发布 | `NOT_APPLICABLE` |
| Runner / CI / 费用 | 不新增工作流、不运行付费推理、不采购 | `NOT_APPLICABLE` |
| 受控研究数据 | 无参与者数据 | 只制定材料与存储边界 |
| 跨仓运行集成 | 未实现 | 后续实际需求触发单独同步 |

本阶段的核验仅针对目标仓库文档。未对其他仓库进行写入，不将其标记为跨仓产品系列已同步或已验收。

## 5. 后续同步触发

当本项目产生需要主系统消费的共享契约、远端计算入口、权限范围、导航入口、真实能力或部署时，在继续依赖方工作之前说明影响与固定版本；只更新真正受影响的位置。个人健康与对话资料不通过 GitHub Book 传输。

[返回协作记录](README.md)
