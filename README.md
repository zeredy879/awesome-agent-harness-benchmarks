# Awesome Agent Harness Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Catalog](https://img.shields.io/badge/catalog-84%20entries-2563eb) ![Audit](https://img.shields.io/badge/source%20audit-2026--09--13-16a34a)

An evidence-aware catalog of benchmarks, controlled studies, and evaluation infrastructure for AI agent harnesses.

An agent harness is the execution layer around a model. It constructs context, exposes and routes tools, maintains state and memory, enforces permissions, drives retries and delegation, records traces, and decides when work is complete. This catalog tracks where those responsibilities become measurable.

The inventory contains 84 entries across 13 areas. It is a dated research inventory rather than a claim that every private evaluation has been found. Each entry has a stable ID, scope, source URL, grading method, environment, and known limitation. Scores are not copied unless they come from a reproducible source record.

## Contents

- [How to use this list](#how-to-use-this-list)
- [Direct harness benchmarks and controlled comparisons](#direct-harness-benchmarks-and-controlled-comparisons)
- [Capability benchmark map](#capability-benchmark-map)
- [Evaluation infrastructure](#evaluation-infrastructure)
- [Research notes](#research-notes)
- [Data and provenance](#data-and-provenance)

## How to use this list

Start with the direct comparison section when the experimental axis is the harness. Use the capability map to choose workload benchmarks for a particular subsystem. A benchmark is a published task suite with an evaluator. A study is a controlled comparison or implementation-specific experiment. Infrastructure is a runner or environment layer that delegates scoring to an underlying benchmark.

For a fair comparison, pin the model endpoint, system prompt, tool schemas, task snapshot, sandbox image, timeout, step or token budget, retry policy, and random seeds. Repeat each task and report completion, consistency, cost, latency, tool calls, recovery, policy violations, and evidence quality. A result row should identify the complete model and harness configuration.

## Direct harness benchmarks and controlled comparisons

- [Harness-Bench (Qihoo360)](https://github.com/Qihoo360/harness-bench) - Native model and harness configurations over offline workspace workflows; broadest public direct comparison in this snapshot.
- [HarnessRisk](https://github.com/Baiyajing/HarnessRisk) - Lifecycle safety benchmark covering configuration, extension, runtime, persistence, action control, and recovery.
- [HarnessDev](https://arxiv.org/abs/2609.01437) - Evaluates an agent that creates and iteratively evolves runnable harness infrastructure.
- [Hyper-tau / tau-tau-bench](https://github.com/sierra-research/hyper-tau-bench) - A coding harness builds a customer-service agent from evidence, then the built agent faces held-out tau3 tasks.
- [SkillsBench](https://github.com/benchflow-ai/skillsbench) - Measures the task-level contribution of mounted skills, scripts, and reference material.
- [Nexus Harness Benchmark](https://github.com/nexus-research-lab/nexus-harness-benchmark) - Evidence-producing end-to-end execution in isolated workspaces.
- [harness-bench (zenixos)](https://github.com/zenixos/harness-bench) - Fixed-model CLI coding comparison with a public protocol; scored runs are marked TBD.
- [harness-bench (LamaSu)](https://github.com/LamaSu/harness-bench) - Proposed component ablations across control loop, tools, memory, subagents, safety, and verification.
- [Harness Arena](https://github.com/Ondemand-OSS/harness-arena) - Blind pairwise preference and Elo comparison of coding harnesses.
- [Durable-agent-harness](https://github.com/Eldergenix/Durable-agent-harness) - Controlled ablations of checkpoints, verification loops, recovery, and memory.
- [MiHaCoBench](https://github.com/HangYu8123/MiHaCoBench) - Independent artifact graders for 95 Python coding tasks.
- [Same-model harness study (d1-m4ss)](https://github.com/d1-m4ss/harness-benchmark) - Codex, Pi, Claude Code, and OpenCode under a shared model.
- [Same-model harness study (rajshah4)](https://github.com/rajshah4/harness-benchmark) - OpenHands, Pi, and OpenCode with verifiers and token ledgers.
- [Hermes tool-performance evals](https://github.com/NousResearch/hermes-toolperf-evals) - Vendor-specific tool-efficiency regression cases from production traces.

## Capability benchmark map

These workload suites measure agents in environments. Their results include the harness unless an experiment explicitly holds it fixed or swaps it as the treatment.

### Coding, terminal, and research execution

- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) - Difficult terminal workflows with executable verifiers.
- [SWE-bench](https://www.swebench.com/) - Real repository issue resolution with tests and multiple official tracks.
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) - Longer and contamination-resistant repository tasks.
- [SWE-bench Live](https://github.com/microsoft/SWE-bench-Live) - Refreshed issue-resolution tasks.
- [SWE-rebench](https://github.com/SWE-rebench/SWE-rebench-V2) - Continuously collected software issue environments.
- [SWE-Lancer](https://github.com/openai/SWELancer-Benchmark) - Economically grounded freelance software tasks.
- [Aider Polyglot](https://aider.chat/docs/leaderboards/) - Compact multi-language editing and repair tasks.
- [Commit0](https://github.com/commit-0/commit0) - Library implementation from specifications and tests.
- [MLE-bench](https://github.com/openai/mle-bench) - Autonomous ML engineering on competition tasks.
- [RE-Bench](https://github.com/METR/RE-Bench) - Research engineering tasks calibrated against human experts.
- [CORE-Bench](https://github.com/siegelz/core-bench) - Computational reproduction and artifact delivery.
- [ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench) - Executable programs for data-driven science tasks.

### Tools, APIs, MCP, and state

- [BFCL V4](https://gorilla.cs.berkeley.edu/leaderboard) - Function selection, argument correctness, and multi-turn tool use.
- [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) - State dependencies, canonicalization, and insufficient information.
- [tau3-bench](https://github.com/sierra-research/tau2-bench) - Policy-bound customer-service tool use with knowledge and voice tracks.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) - Code-driven interactions across a simulated personal app ecosystem.
- [MCPMark](https://github.com/eval-sys/mcpmark) - Stress tests for agents using pinned MCP services.
- [MCP-Bench](https://github.com/Accenture/mcp-bench) - Complex real-world tasks through MCP servers.
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon) - Long-horizon workflows over hundreds of tools and applications.
- [ToolBench and ToolEval](https://github.com/OpenBMB/ToolBench) - Large-scale API selection and composition.
- [StableToolBench](https://github.com/THUNLP-MT/StableToolBench) - Virtualized and cached tools for stable API evaluation.
- [API-Bank](https://github.com/AlibabaResearch/DAMO-ConvAI) - Dialogue API calling and planning tasks.

### Browser, desktop, and mobile computer use

- [WebArena](https://github.com/web-arena-x/webarena) - Self-hosted realistic web applications and functional checks.
- [WebArena-Verified](https://github.com/ServiceNow/webarena-verified) - Revised WebArena task and evaluator release.
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena) - Visually grounded web tasks.
- [WorkArena and WorkArena++](https://github.com/ServiceNow/WorkArena) - Enterprise browser work and compositional tasks.
- [WebVoyager](https://github.com/MinorJerry/WebVoyager) - Live-web browser tasks.
- [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web) - Refreshed live-web tasks with human review.
- [WebChoreArena](https://github.com/WebChoreArena/WebChoreArena) - Long, repetitive, and memory-heavy web workflows.
- [OSWorld-Verified](https://github.com/xlang-ai/OSWorld) - Open-ended desktop work across real applications.
- [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena) - Windows desktop agent evaluation.
- [AndroidWorld](https://github.com/google-research/android_world) - Parameterized Android app tasks with state validation.
- [AndroidLab](https://github.com/THUDM/Android-Lab) - Android interaction tasks and evaluation tooling.
- [ClawBench (TIGER-AI-Lab)](https://github.com/TIGER-AI-Lab/ClawBench) - Everyday live-web tasks; separate from other ClawBench projects.

### General, long-horizon, and always-on agents

- [AgentBench](https://github.com/THUDM/AgentBench) - Heterogeneous interactive environments.
- [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) - Tool-assisted multimodal general assistant questions.
- [Gaia2 and Gaia2-CLI](https://github.com/facebookresearch/meta-agents-research-environments) - Dynamic, asynchronous environments and temporal constraints.
- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) - Simulated digital workplace tasks.
- [AssistantBench](https://github.com/oriyor/assistantbench) - Practical information-seeking tasks.
- [Claw-Eval](https://github.com/claw-eval/claw-eval) - Human-verified general, multimodal, and multi-turn agent tasks.
- [Claw-Eval-Live](https://github.com/Claw-Eval-Live/Claw-Eval-Live) - Evolving workflow tasks from marketplace signals.
- [ClawBench (OpenClaw)](https://github.com/openclaw/clawbench) - Trace-scored full-stack agent diagnostics.
- [PinchBench](https://github.com/pinchbench/skill) - Practical assistant tasks with the OpenClaw runtime.
- [ClawMark](https://github.com/evolvent-ai/ClawMark) - Multi-turn, multi-day, multimodal coworker simulation.
- [Claw-Anything](https://github.com/LiberCoders/CLaw-Anything) - Always-on personal assistant tasks with broad digital access.
- [SentinelBench](https://github.com/microsoft/sentinel_environments) - Long-running monitoring and event response.
- [METR Time Horizons](https://metr.org/time-horizons/) - Success probability as a function of human-equivalent task duration.

### Memory and context

- [LongMemEval](https://github.com/xiaowu0162/LongMemEval) - Long-term conversational memory.
- [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2) - Experience retrieval from multimodal agent trajectories.
- [LoCoMo](https://github.com/snap-research/locomo) - Long conversational memory.
- [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench) - Incremental retrieval, learning, understanding, and forgetting.
- [MemoryArena](https://github.com/ZexueHe/MemoryArena) - Interdependent multi-session agent tasks.
- [Context-Bench (Letta, V2)](https://www.letta.com/blog/evaluating-memory-in-production-agents/) - Private production-memory evaluation covering adherence, retrieval, generation, and hygiene.
- [ContextBench (coding retrieval)](https://arxiv.org/abs/2602.05892) - Repository context gathering by coding agents.

### Safety, permission, and failure injection

- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Prompt injection attacks and defenses in stateful tool environments.
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) - Indirect injections through tool outputs.
- [AgentHarm](https://arxiv.org/abs/2410.09024) - Harmful multi-step requests and refusal behavior.
- [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) - Safety in interactive agent environments.
- [WASP](https://github.com/facebookresearch/wasp) - Adversarial web content against web agents.
- [OrchestraBench](https://arxiv.org/abs/2608.05263) - Routing, decomposition, failure cascades, and recovery.
- [MAS-FIRE](https://arxiv.org/abs/2602.19843) - Fault injection for multi-agent reliability.
- [MultiAgentBench and MARBLE](https://github.com/MultiagentBench/MARBLE) - Collaboration and coordination patterns.
- [SABOT](https://github.com/Jott2121/sabot) - Whether agent pipelines detect planted faults.

## Evaluation infrastructure

- [Harbor](https://github.com/harbor-framework/harbor) - Versioned sandbox execution for agent benchmarks.
- [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) - Environments, verifiers, scale-out runs, and swappable harnesses.
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Reproducible evaluation implementations for Inspect AI.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) - Shared browser-agent environment interfaces.
- [Holistic Agent Leaderboard](https://hal.cs.princeton.edu/) - Cost-aware comparisons across agents, models, and task suites.

## Research notes

The useful unit of comparison is a configuration: model endpoint, harness version, system prompt, tools, environment, and budgets. In a paired study, hold every factor except the treatment constant. For a component ablation, compare the same harness with one feature removed or swapped. Preserve raw traces, environment diffs, tool calls, costs, and verifier output so a headline score can be audited.

The catalog uses these capability tags: `tools`, `context`, `state`, `memory`, `planning`, `recovery`, `verification`, `permissions`, `multi-agent`, `vision`, `interaction`, `skills`, and `cost`. It records limitations because live websites, model judges, hidden state, stochastic sampling, and mutable datasets can change what a score means.

See [docs/research.md](docs/research.md) for the inventory method, comparison dimensions, recommended benchmark stacks, and threats to validity.

## Data and provenance

The machine-readable inventory is [data/catalog.json](data/catalog.json). Each record has a stable ID, category, type, source URL, measured signals, grading method, environment, and limitation. The GitHub availability audit is [data/source-audit.json](data/source-audit.json); it records repository metadata, default branch, star count, README commit SHA, and SHA-256 at audit time. A `needs-review` record means the URL was not accessible through the GitHub API at audit time; it is retained so the gap is visible.

Run the audit locally (requires authenticated `gh`):

```bash
python3 scripts/research_sources.py --catalog --audit
```

The script reads public GitHub metadata and README blobs, records hashes, and never executes downloaded repository code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for additions and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.
