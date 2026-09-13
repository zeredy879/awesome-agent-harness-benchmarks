# Agent Harness Benchmark 한국어 카탈로그

언어: [English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

사람과 Agent 모두가 읽을 수 있는 공개 Agent Harness benchmark·비교 연구·평가 인프라 카탈로그입니다.

- 기준일: `2026-09-13`
- 항목 수: **116**
- 역량 영역: **13**
- GitHub 출처 감사 기록: **99**
- 범위: 공개 benchmark, 통제된 비교 연구, Agent Harness 관련 평가 인프라를 다룹니다. 날짜가 있는 공개 자료 인벤토리이며 비공개 평가까지 모두 포함한다는 뜻은 아닙니다.

## 빠른 링크

- [사람을 위한 Pages](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)
- [Agent Markdown](site/agent.md)
- [기계 판독 JSON](data/catalog.json)
- [연구 노트](docs/research.md)
- [소스 감사](data/source-audit.json)

## 시작하기

Harness 자체를 비교하려면 ‘직접 비교’부터 확인하고, 특정 하위 시스템은 역량 카테고리에서 고르세요. 공정한 비교를 위해 모델 endpoint, 시스템 prompt, tool schema, task 버전, sandbox 이미지, 예산, retry 정책, random seed를 고정하세요.

## 최근 추가·재검증（2025–2026）

2026년 9월 조사에서 추가하거나 다시 확인한 항목입니다. 프로젝트 고유명과 원문 링크는 오역을 피하기 위해 그대로 두었고, 전체 필드와 한계는 Agent Markdown과 JSON에 기록했습니다.

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

## 전체 역량별 카탈로그

### Harness 직접 비교

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

### 도구·API·MCP·상태

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

### 코딩·터미널

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

### 브라우저·Web

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

### 범용 에이전트

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

### 메모리·컨텍스트

- [Context-Bench (Letta, V2)](https://www.letta.com/blog/evaluating-memory-in-production-agents/)
- [ContextBench (coding retrieval)](https://arxiv.org/abs/2602.05892)
- [LoCoMo](https://github.com/snap-research/locomo)
- [LongMemEval](https://github.com/xiaowu0162/LongMemEval)
- [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2)
- [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)
- [MemoryArena](https://github.com/ZexueHe/MemoryArena)

### 안전·장애 주입

- [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)
- [AgentDojo](https://github.com/ethz-spylab/agentdojo)
- [AgentHarm](https://github.com/UKGovernmentBEIS/inspect_evals)
- [AgentShield Benchmark](https://github.com/doronp/agentshield-benchmark)
- [Cybench](https://github.com/andyzorigin/cybench)
- [HarnessRisk](https://github.com/Baiyajing/HarnessRisk)
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)
- [WASP](https://github.com/facebookresearch/wasp)

### 장기·상시 에이전트

- [AgentIF-OneDay](https://github.com/xbench-ai/AgentIF-OneDay)
- [AOBench (Agent Operations Benchmark)](https://github.com/MSKazemi/aobench)
- [Claw-Anything](https://github.com/LiberCoders/Claw-Anything)
- [ClawMark](https://github.com/evolvent-ai/ClawMark)
- [Durable-agent-harness](https://github.com/Eldergenix/Durable-agent-harness)
- [Gaia2 / Gaia2-CLI](https://github.com/facebookresearch/meta-agents-research-environments)
- [METR Task-Completion Time Horizons](https://metr.org/time-horizons/)
- [SentinelBench](https://github.com/microsoft/sentinel_environments)

### 평가 인프라

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

### 컴퓨터·모바일

- [AndroidLab](https://github.com/THUDM/Android-Lab)
- [AndroidWorld](https://github.com/google-research/android_world)
- [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld)
- [SpreadsheetBench](https://github.com/Reality2byte/spreadsheetbench)
- [SpreadsheetBench 2](https://spreadsheetbench.github.io/)
- [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)

### 멀티 에이전트

- [MAS-FIRE](https://arxiv.org/abs/2602.19843)
- [MultiAgentBench](https://github.com/MultiagentBench/MARBLE)
- [OrchestraBench](https://arxiv.org/abs/2608.05263)
- [SABOT](https://github.com/Jott2121/sabot)

### 연구 엔지니어링

- [AgentActionBench](https://arxiv.org/abs/2609.11117)
- [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench)
- [AIRS-Bench](https://github.com/facebookresearch/airs-bench)
- [CORE-Bench](https://github.com/siegelz/core-bench)
- [MLE-bench](https://github.com/openai/mle-bench)
- [PaperBench](https://github.com/openai/preparedness)
- [RE-Bench](https://github.com/METR/RE-Bench)
- [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena)
- [ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)

### Skills·지시

- [SkillsBench](https://github.com/benchflow-ai/skillsbench)
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)

## 자세한 정보

전체 영어 설명은 [README.md](README.md)를 참고하세요. Agent가 바로 읽을 안정적인 입구는 [site/agent.md](site/agent.md)와 [data/catalog.json](data/catalog.json)입니다.
