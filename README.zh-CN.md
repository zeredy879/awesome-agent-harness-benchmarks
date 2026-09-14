# Awesome Agent Harness Benchmarks

为你的 Agent 选对评测：先看任务、判分方式和局限，再比较分数。

## [打开可搜索的评测目录 →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)

按能力筛选，查看每项评测的原始来源、运行环境和适用边界。

[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md)

资料快照：2026-09-13 · 115 条记录 · 97 个评测套件 · 13 类能力

这里的 **harness** 指模型之外负责工具调用、上下文、记忆、权限与执行控制的系统。本目录帮你找到适合测试这些环节的公开评测，并说明结果能支持什么结论。

## 你想验证什么？

下面是按用途挑选的起点，不是排名。完整目录还收录了其他任务、版本和研究。

| 评测目标 | 从这里开始 | 怎么衡量 | 比较前要注意 |
| --- | --- | --- | --- |
| 修复真实代码仓库中的问题 | [SWE-bench family](https://github.com/SWE-bench/SWE-bench) | 通过修复测试和回归测试 | 不同赛道的任务、语言和判分方式不同，分数不能直接互换。 |
| 完成复杂终端任务 | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) | 运行任务专用验证器 | 固定数据集版本；成绩同时受模型与 harness 影响。 |
| 调用工具并维护状态 | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) | 检查中间里程碑与最终状态 | 用户模拟器和工具接口都会影响结果。 |
| 操作网站完成任务 | [WebArena](https://github.com/web-arena-x/webarena) | 检查网页应用的功能状态 | 固定环境配置、任务版本和评测器修订。 |
| 跨桌面应用完成工作 | [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld) | 根据实际执行结果判分 | 虚拟机镜像、步数预算和评测版本必须一致。 |
| 从长期对话中找到并更新信息 | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) | 衡量历史信息问答准确率 | 需要完整上下文基线；答对问题不等于完成多步任务。 |
| 抵御工具环境中的提示注入 | [AgentDojo](https://github.com/ethz-spylab/agentdojo) | 同时衡量正常任务表现与攻击成功率 | 固定威胁模型和攻击预算；安全分数要与可用性一起看。 |
| 借助工具搜集信息并推理 | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) | 衡量最终答案准确率 | 最终答案难以反映执行过程中的副作用和安全问题。 |

## 这些分数说明了什么？

多数评测衡量的是整个 Agent 的表现。要把差异归因于 harness，就需要在相同模型、任务和预算下做受控比较；收录于本目录不代表某个项目已经做过这样的实验。

- **benchmark**：带任务和评测器的套件，用来运行测试。
- **study**：比较研究，用来了解实验设计与已有证据。
- **infrastructure**：运行或审计评测的工具，本身不是一组测试题。
- **watchlist**：早期或适用范围较窄的候选项目，需要进一步核实。

比较模板和评测方案只说明实验应该怎样设计，不代表已经运行的结果或榜单。

## 按问题继续查找

[完整目录](docs/catalog.md)保留所有条目的说明和来源。也可以直接跳到相关类别：

[Harness 直接对比](docs/catalog.md#direct) · [代码与终端](docs/catalog.md#coding) · [工具与状态](docs/catalog.md#tools)

[浏览器](docs/catalog.md#browser) · [桌面与移动端](docs/catalog.md#computer) · [通用任务](docs/catalog.md#general)

[记忆与上下文](docs/catalog.md#memory) · [长时间任务](docs/catalog.md#long-horizon) · [安全](docs/catalog.md#safety)

[多 Agent 协作](docs/catalog.md#multi-agent) · [研究任务](docs/catalog.md#research) · [技能与指令](docs/catalog.md#skills) · [评测基础设施](docs/catalog.md#infrastructure)

## 准备做一次比较？

从[比较记录模板](docs/comparison-template.md)开始，把实验条件和结果放在一起记录：

1. 固定模型、提示词、工具接口、任务版本、环境、预算和重试策略。
2. 分别报告任务完成率、波动、成本、延迟与安全问题，保留执行轨迹和验证输出。
3. 用[研究说明](docs/research.md)检查证据强度与可比性，再解释差异。

## 供 Agent 读取

自动检索和整理时，可直接读取以下入口：

- [带说明的 Markdown 目录](site/agent.md)
- [结构化数据](data/catalog.json)
- [字段定义](data/catalog.schema.json)
- [仓库维护约定](AGENTS.md)

## 来源与贡献

优先引用官方仓库、论文和项目页面。[来源检查记录](data/source-audit.json)反映特定时间的链接可用性与元数据，不代表独立复现。收录也不等于推荐；本目录不承诺覆盖所有公开或私有评测。

发现遗漏、失效链接或不准确的描述？欢迎按[贡献指南](CONTRIBUTING.md)提交 issue 或 PR，并附上原始来源及一项具体局限。评测方法或 benchmark 比较问题，也欢迎在[讨论区](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)交流。
