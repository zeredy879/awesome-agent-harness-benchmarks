# Agent Harness Benchmark 中文目录

语言： [English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

面向人类阅读和 Agent 检索的公开 Agent Harness benchmark、受控研究与评测基础设施目录。

- 快照: `2026-09-13`
- 条目: **116**
- 能力领域: **13**
- GitHub 来源记录: **99**
- 范围: 公开 benchmark、受控研究和与 Agent Harness 相关的评测基础设施；这是有日期的公开资料快照，不宣称覆盖所有私有评测。

## 入口

- [人类可读 Pages](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)
- [Agent Markdown](site/agent.md)
- [机器可读 JSON](data/catalog.json)
- [研究笔记](docs/research.md)
- [来源审计](data/source-audit.json)

## 快速开始

如果你要比较 Harness 本身，先看直接对比；如果你要测某个子系统，再选择对应能力类别。公平比较时固定模型端点、prompt、工具 schema、任务版本、sandbox、预算、重试策略和随机种子。

## 近期新增与复核（2025–2026）

下面列出 2026 年 9 月扫描中新增或重新核验的项目。条目名称与来源链接保持原文，避免社区项目的技术专名被误译；完整字段和局限见 Agent Markdown 与 JSON。

- [AgentSearchBench](https://github.com/Bingo-W/AgentSearchBench)
- [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena)
- [InfraBench](https://github.com/kubeply/infra-bench)
- [APEX-Agents / Archipelago](https://github.com/togethercomputer/archipelago)
- [DataSpace](https://github.com/HKUSTDial/DataSpace)
- [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench)
- [AIRS-Bench](https://github.com/facebookresearch/airs-bench)
- [AgentIF-OneDay](https://github.com/xbench-ai/AgentIF-OneDay)
- [OmniaBench](https://github.com/scuuy/OmniaBench)
- [BrowserUse Agent Bench / LexBench-Browser](https://github.com/lexmount/browseruse-agent-bench)
- [AgentSuite](https://github.com/Agent-Suite/AgentSuite)
- [Open AgentBench](https://github.com/the-open-agent/agentbench)
- [Agent-Diff](https://github.com/agent-diff-bench/agent-diff)
- [Version Control Bench](https://github.com/gitbutlerapp/version-control-bench)
- [AgentShield Benchmark](https://github.com/doronp/agentshield-benchmark)
- [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench)
- [STATE-Bench](https://github.com/microsoft/STATE-Bench)
- [ShellBench](https://github.com/openclaw/shellbench)
- [Coder Eval](https://github.com/UiPath/coder_eval)
- [Lemans](https://github.com/rails/lemans)
- [AgentRace](https://agent-race.github.io/paper)
- [AgentActionBench](https://arxiv.org/abs/2609.11117)
- [PaperBench](https://github.com/openai/preparedness)
- [Cybench](https://github.com/andyzorigin/cybench)
- [BrowseComp](https://github.com/openai/simple-evals)
- [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus)
- [SpreadsheetBench](https://github.com/Reality2byte/spreadsheetbench)
- [SpreadsheetBench 2](https://spreadsheetbench.github.io/)
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench)
- [AgentIF](https://agentif.github.io/)
- [AOBench (Agent Operations Benchmark)](https://github.com/MSKazemi/aobench)
- [SWE-InfraBench](https://arxiv.org/abs/2606.05249)

## 完整分类目录

### 直接 Harness 对比

- [ClawBench (OpenClaw)](https://github.com/openclaw/clawbench)
- [Coding harness comparison (tufantunc)](https://github.com/tufantunc/harness-benchmark)
- [Harness Arena](https://github.com/Ondemand-OSS/harness-arena)
- [harness-bench (LamaSu)](https://github.com/LamaSu/harness-bench)
- [Harness-Bench (Qihoo360)](https://github.com/Qihoo360/harness-bench)
- [harness-bench (zenixos)](https://github.com/zenixos/harness-bench)
- [HarnessDev](https://arxiv.org/abs/2609.01437)
- [Hyper-τ / τ^τ-bench](https://github.com/sierra-research/hyper-tau-bench)
- [Nexus Harness Benchmark](https://github.com/nexus-research-lab/nexus-harness-benchmark)
- [Same-model harness study (d1-m4ss)](https://github.com/d1-m4ss/harness-benchmark)
- [Same-model harness study (rajshah4)](https://github.com/rajshah4/harness-benchmark)
- [ShellBench](https://github.com/openclaw/shellbench)

### 工具、API、MCP 与状态

- [Agent-Diff](https://github.com/agent-diff-bench/agent-diff)
- [API-Bank](https://github.com/AlibabaResearch/DAMO-ConvAI)
- [AppWorld](https://github.com/StonyBrookNLP/appworld)
- [Berkeley Function Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench)
- [DataSpace](https://github.com/HKUSTDial/DataSpace)
- [Hermes tool-performance evals](https://github.com/NousResearch/hermes-toolperf-evals)
- [MCP-Bench (Accenture)](https://github.com/Accenture/mcp-bench)
- [MCPMark](https://github.com/eval-sys/mcpmark)
- [StableToolBench](https://github.com/THUNLP-MT/StableToolBench)
- [STATE-Bench](https://github.com/microsoft/STATE-Bench)
- [Toolathlon / Toolathlon-Verified](https://github.com/hkust-nlp/Toolathlon)
- [ToolBench / ToolEval](https://github.com/OpenBMB/ToolBench)
- [ToolSandbox](https://github.com/apple/ToolSandbox)
- [τ-bench family (τ / τ² / τ³)](https://github.com/sierra-research/tau2-bench)

### 编码与终端

- [Aider Polyglot](https://aider.chat/docs/leaderboards/)
- [Commit0](https://github.com/commit-0/commit0)
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench)
- [MiHaCoBench](https://github.com/HangYu8123/MiHaCoBench)
- [SWE-bench family](https://github.com/SWE-bench/SWE-bench)
- [SWE-bench Live](https://github.com/microsoft/SWE-bench-Live)
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os)
- [SWE-InfraBench](https://arxiv.org/abs/2606.05249)
- [SWE-Lancer](https://github.com/openai/SWELancer-Benchmark)
- [SWE-rebench](https://github.com/SWE-rebench/SWE-rebench-V2)
- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench)
- [Version Control Bench](https://github.com/gitbutlerapp/version-control-bench)

### 浏览器与 Web

- [BrowseComp](https://github.com/openai/simple-evals)
- [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus)
- [BrowserUse Agent Bench / LexBench-Browser](https://github.com/lexmount/browseruse-agent-bench)
- [ClawBench (TIGER-AI-Lab)](https://github.com/TIGER-AI-Lab/ClawBench)
- [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web)
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena)
- [WebArena](https://github.com/web-arena-x/webarena)
- [WebArena-Verified](https://github.com/ServiceNow/webarena-verified)
- [WebChoreArena](https://github.com/WebChoreArena/WebChoreArena)
- [WebVoyager](https://github.com/MinorJerry/WebVoyager)
- [WorkArena / WorkArena++](https://github.com/ServiceNow/WorkArena)

### 通用 Agent

- [AgentBench](https://github.com/THUDM/AgentBench)
- [AgentIF](https://agentif.github.io/)
- [AgentSearchBench](https://github.com/Bingo-W/AgentSearchBench)
- [APEX-Agents / Archipelago](https://github.com/togethercomputer/archipelago)
- [AssistantBench](https://github.com/oriyor/assistantbench)
- [Claw-Eval](https://github.com/claw-eval/claw-eval)
- [Claw-Eval-Live](https://github.com/Claw-Eval-Live/Claw-Eval-Live)
- [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)
- [OmniaBench](https://github.com/scuuy/OmniaBench)
- [PinchBench](https://github.com/pinchbench/skill)
- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)

### 记忆与上下文

- [Context-Bench (Letta, V2)](https://www.letta.com/blog/evaluating-memory-in-production-agents/)
- [ContextBench (coding retrieval)](https://arxiv.org/abs/2602.05892)
- [LoCoMo](https://github.com/snap-research/locomo)
- [LongMemEval](https://github.com/xiaowu0162/LongMemEval)
- [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2)
- [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)
- [MemoryArena](https://github.com/ZexueHe/MemoryArena)

### 安全与故障注入

- [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)
- [AgentDojo](https://github.com/ethz-spylab/agentdojo)
- [AgentHarm](https://github.com/UKGovernmentBEIS/inspect_evals)
- [AgentShield Benchmark](https://github.com/doronp/agentshield-benchmark)
- [Cybench](https://github.com/andyzorigin/cybench)
- [HarnessRisk](https://github.com/Baiyajing/HarnessRisk)
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)
- [WASP](https://github.com/facebookresearch/wasp)

### 长时程与常驻 Agent

- [AgentIF-OneDay](https://github.com/xbench-ai/AgentIF-OneDay)
- [AOBench (Agent Operations Benchmark)](https://github.com/MSKazemi/aobench)
- [Claw-Anything](https://github.com/LiberCoders/Claw-Anything)
- [ClawMark](https://github.com/evolvent-ai/ClawMark)
- [Durable-agent-harness](https://github.com/Eldergenix/Durable-agent-harness)
- [Gaia2 / Gaia2-CLI](https://github.com/facebookresearch/meta-agents-research-environments)
- [METR Task-Completion Time Horizons](https://metr.org/time-horizons/)
- [SentinelBench](https://github.com/microsoft/sentinel_environments)

### 评测基础设施

- [AgentRace](https://agent-race.github.io/paper)
- [AgentSuite](https://github.com/Agent-Suite/AgentSuite)
- [BrowserGym](https://github.com/ServiceNow/BrowserGym)
- [Coder Eval](https://github.com/UiPath/coder_eval)
- [Harbor](https://github.com/harbor-framework/harbor)
- [Holistic Agent Leaderboard (HAL)](https://hal.cs.princeton.edu/)
- [InfraBench](https://github.com/kubeply/infra-bench)
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals)
- [Lemans](https://github.com/rails/lemans)
- [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)
- [Open AgentBench](https://github.com/the-open-agent/agentbench)

### 电脑与移动端

- [AndroidLab](https://github.com/THUDM/Android-Lab)
- [AndroidWorld](https://github.com/google-research/android_world)
- [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld)
- [SpreadsheetBench](https://github.com/Reality2byte/spreadsheetbench)
- [SpreadsheetBench 2](https://spreadsheetbench.github.io/)
- [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)

### 多 Agent

- [MAS-FIRE](https://arxiv.org/abs/2602.19843)
- [MultiAgentBench](https://github.com/MultiagentBench/MARBLE)
- [OrchestraBench](https://arxiv.org/abs/2608.05263)
- [SABOT](https://github.com/Jott2121/sabot)

### 科研工程

- [AgentActionBench](https://arxiv.org/abs/2609.11117)
- [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench)
- [AIRS-Bench](https://github.com/facebookresearch/airs-bench)
- [CORE-Bench](https://github.com/siegelz/core-bench)
- [MLE-bench](https://github.com/openai/mle-bench)
- [PaperBench](https://github.com/openai/preparedness)
- [RE-Bench](https://github.com/METR/RE-Bench)
- [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena)
- [ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)

### Skills 与指令

- [SkillsBench](https://github.com/benchflow-ai/skillsbench)
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)

## 详细资料

完整英文说明见 [README.md](README.md)。适合 Agent 直接读取的字段见 [site/agent.md](site/agent.md) 和 [data/catalog.json](data/catalog.json)。
