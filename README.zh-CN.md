# Awesome Agent Harness Benchmarks

按任务挑选 AI Agent 评测，了解它测什么、如何评分，以及结果有哪些局限。

**[浏览可搜索的评测目录 →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)**

[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md)

收录 115 项公开评测及相关资料，覆盖 13 个领域。

## 按任务选评测

| 想测试什么 | 从这里开始 |
| --- | --- |
| 修复代码仓库中的问题 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) |
| 完成终端任务 | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) |
| 调用工具并维护状态 | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) |
| 操作网站完成任务 | [WebArena](https://github.com/web-arena-x/webarena) |
| 使用桌面应用 | [OSWorld](https://github.com/xlang-ai/OSWorld) |
| 记住并查找历史对话中的信息 | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) |
| 抵御工具输出中的提示注入 | [AgentDojo](https://github.com/ethz-spylab/agentdojo) |
| 查资料、用工具解决综合问题 | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) |

更多选择见[完整目录](docs/catalog.md)，每项均附有评分方式、运行环境和具体局限。

## 比较 Harness

**Agent harness** 是模型的配套软件，负责工具调用、上下文管理、记忆、权限控制和故障恢复。想研究这些部分，可以从以下项目入手：

- [Harness-Bench](https://github.com/Qihoo360/harness-bench)：比较不同模型与 harness 组合在本地工作区中的表现。
- [ShellBench](https://github.com/openclaw/shellbench)：原名 ClawBench。通过执行记录和多次运行，评估整个 Agent 配置的可靠性。
- [SkillsBench](https://github.com/benchflow-ai/skillsbench)：对照有无技能包时的任务表现。

## 数据与比较方法

多数评测衡量的是整个 Agent。比较 harness 时，先说明要改变什么：比较整套配置，可以保留各自的提示词、工具和默认设置。测试单个组件，则只改变该组件。除本次比较刻意改变的部分外，其余条件应保持一致，例如模型、任务、环境、预算和评分规则。

分别记录完成率、重复运行的稳定性、成本、耗时和安全问题，并保留执行记录与验证结果。可直接使用[比较记录模板](docs/comparison-template.md)，或查阅[研究与方法说明](docs/research.md)。

供 Agent 读取：[Markdown 摘要](site/agent.md) · [JSON 数据](data/catalog.json) · [字段定义](data/catalog.schema.json) · [维护约定](AGENTS.md)

每周检查来源可用性。收录不代表独立复现，详见[数据与来源说明](data/README.md)。

## 参与完善

发现遗漏、错误或失效链接？欢迎按[贡献指南](CONTRIBUTING.md)提交 issue 或 PR，附上原始来源和简短说明。评测方法与比较问题可在[讨论区](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)交流。
