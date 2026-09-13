# Awesome Agent Harness Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Catalog](https://img.shields.io/badge/catalog-116%20entries-2563eb) ![Audit](https://img.shields.io/badge/source%20audit-2026--09--13-16a34a) [![Validate catalog](https://github.com/zeredy879/awesome-agent-harness-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/zeredy879/awesome-agent-harness-benchmarks/actions/workflows/validate.yml) ![Pages](https://img.shields.io/badge/GitHub%20Pages-live-16a34a)

> A maintained, evidence-aware map of the benchmarks that reveal how an AI agent actually works: tools, context, memory, permissions, recovery, verification, and delivery.

**Snapshot:** `2026-09-13` · **116 entries** · **13 capability areas** · **99 GitHub sources audited** · **98 benchmark suites**

An agent harness is the execution layer around a model. It constructs context, exposes and routes tools, maintains state and memory, enforces permissions, drives retries and delegation, records traces, and decides when work is complete. This catalog tracks where those responsibilities become measurable.

This is a dated public-source inventory, not a claim that every private or unindexed evaluation has been found. Each record has a stable ID, scope, source URL, grading method, environment, and known limitation. Scores are not copied unless they come from a reproducible source record.

## Contents

- [Start here](#start-here)
- [How to use this list](#how-to-use-this-list)
- [At a glance](#at-a-glance)
- [Recent 2025-2026 additions](#recent-2025-2026-additions)
- [Direct harness benchmarks and controlled comparisons](#direct-harness-benchmarks-and-controlled-comparisons)
- [Capability benchmark map](#capability-benchmark-map)
- [Evaluation infrastructure](#evaluation-infrastructure)
- [Website and Agent exports](#website-and-agent-exports)
- [Automated maintenance](#automated-maintenance)
- [Research notes](#research-notes)
- [Data and provenance](#data-and-provenance)

## Start here

**For people:** [Open the searchable GitHub Pages catalog](https://zeredy879.github.io/awesome-agent-harness-benchmarks/).

**For Agents:** [Read the Markdown digest](site/agent.md) or [load the structured catalog](data/catalog.json).

**For research:** [Read the comparison notes](docs/research.md), including evidence tiers, metrics, and threats to validity.

**For contributors:** [Follow AGENTS.md](AGENTS.md) and [the curator profile](.github/agents/benchmark-curator.agent.md).

**Read in your language:** [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## How to use this list

Start with the direct comparison section when the experimental axis is the harness. Use the capability map to choose workload benchmarks for a particular subsystem. A benchmark is a published task suite with an evaluator. A study is a controlled comparison or implementation-specific experiment. Infrastructure is a runner or environment layer that delegates scoring to an underlying benchmark.

For a fair comparison, pin the model endpoint, system prompt, tool schemas, task snapshot, sandbox image, timeout, step or token budget, retry policy, and random seeds. Repeat each task and report completion, consistency, cost, latency, tool calls, recovery, policy violations, and evidence quality. A result row should identify the complete model and harness configuration.

## At a glance

- Does the harness itself improve a fixed model? Start with `Harness-Bench`, `ShellBench`, and `Harness Arena` - isolate harness, configuration, trace, and reliability effects.
- Can the agent finish coding work? Start with `Terminal-Bench`, `SWE-bench`, and `GitTaskBench` - test repository navigation, editing, testing, and delivery.
- Can it use tools and state safely? Start with `tau3-bench`, `ToolSandbox`, and `STATE-Bench` - test stateful APIs, policies, permissions, and final state.
- Can it research or reproduce science? Start with `PaperBench`, `AIRS-Bench`, and `SciAgentArena` - test research planning, execution, evidence, and reproduction.
- Can it browse, search, or operate a computer? Start with `BrowseComp`, `BrowseComp-Plus`, and `OSWorld` - test retrieval, browser actions, visual grounding, and desktop state.
- Does it remain reliable and safe over time? Start with `LongMemEval-V2`, `AgentDojo`, and `HarnessRisk` - test memory, injection resistance, permissions, recovery, and variance.

## Recent 2025-2026 additions

The following entries were added or re-checked in the September 2026 scan. They are grouped here so the moving edge of the field is visible before the full capability map.

### Direct, runtime, and harness comparison

**ShellBench** — Full-stack harness, configuration, model, and trace diagnostics.

**AgentRace** — Runtime, scalability, communication, and tool-latency comparison across agent frameworks.

**Open AgentBench** — Performance, dialogue, hard-chat, tools, startup, memory, throughput, and reliability suites.

**AgentSuite** — One-touch execution plus component-based benchmark auditing.

**Coder Eval** — Agent-agnostic coding-agent and skill regression suites.

**Lemans** — Ruby CLI harness with digest-backed coding-agent reports.

### General, enterprise, and long-horizon work

**AgentSearchBench** — Execution-grounded search and reranking of real-world agents.

**APEX-Agents / Archipelago** — MCP-based professional-services workflows with snapshot grading.

**OmniaBench** — 1,431-task diagnostic general-agent benchmark with a challenging subset.

**AgentIF-OneDay** — Daily multimodal workflows, latent instructions, and iterative refinement.

**AgentIF** — Long, constraint-rich instruction following in agentic scenarios.

### Data, science, and infrastructure

**DataSpace** — Verifiable analytics over heterogeneous multimodal workspaces.

**Data Agent Benchmark** — Multi-database and unstructured enterprise data tasks.

**Agent-Diff** — Enterprise API sandboxes graded by state diffs.

**SciAgentArena** — Biomedical and multi-omics workflows with executable scoring.

**AIRS-Bench** — End-to-end ML research-science tasks.

**InfraBench** — Realistic Kubernetes and infrastructure operations.

**AOBench** — Role-aware, RBAC-enforced HPC operations.

**SWE-InfraBench** — Incremental AWS CDK infrastructure-code edits.

**PaperBench** — Reproduction of 20 ICML papers from scratch.

**AgentActionBench** — Trace-scored experiment reproduction across ML and AI4Science.

### Browser, spreadsheet, and repository work

**BrowserUse Agent Bench** — 210 browser tasks across 107 websites and multiple backends.

**BrowseComp** — 1,266 hard-to-find web information problems.

**BrowseComp-Plus** — Fixed-corpus deep research with retriever/agent disentanglement.

**SpreadsheetBench** — Real-world spreadsheet manipulation with OJ-style grading.

**SpreadsheetBench 2** — Business spreadsheet generation, debugging, and visualization workflows.

**GitTaskBench** — Repo-level real-world tasks from understanding to delivery.

**Version Control Bench** — Git, Jujutsu, and GitButler task comparison.

### Safety and specialized capability

**AgentShield Benchmark** — Prompt injection, exfiltration, tool abuse, and provenance threats.

**AgentRE-Bench** — Long-horizon reverse engineering of source-free binaries.

**Cybench** — Multi-step cybersecurity CTF tasks and risk.

**STATE-Bench** — Enterprise workflows with main and agent-learning tracks.

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
- [ShellBench](https://github.com/openclaw/shellbench) - Full-stack shell harness, configuration, model, and trace diagnostics.

## Capability benchmark map

These workload suites measure agents in environments. Their results include the harness unless an experiment explicitly holds it fixed or swaps it as the treatment.

### Coding, terminal, and research execution

- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) - Difficult terminal workflows with executable verifiers.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Real repository issue resolution with tests and multiple official tracks.
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
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) - Real-world repository tasks from understanding through delivery.
- [Version Control Bench](https://github.com/gitbutlerapp/version-control-bench) - Git, Jujutsu, and GitButler version-control workflows.
- [SWE-InfraBench](https://arxiv.org/abs/2606.05249) - Incremental AWS CDK infrastructure-code edits.
- [Coding harness comparison (tufantunc)](https://github.com/tufantunc/harness-benchmark) - Fixed-model coding-harness runs with reproducible scripts.

### Skills and instruction following

- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) - Skill and instruction effects on software-engineering agents.

### Tools, APIs, MCP, and state

- [BFCL V4](https://gorilla.cs.berkeley.edu/leaderboard.html) - Function selection, argument correctness, and multi-turn tool use.
- [ToolSandbox](https://github.com/apple/ToolSandbox) - State dependencies, canonicalization, and insufficient information.
- [tau3-bench](https://github.com/sierra-research/tau2-bench) - Policy-bound customer-service tool use with knowledge and voice tracks.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) - Code-driven interactions across a simulated personal app ecosystem.
- [MCPMark](https://github.com/eval-sys/mcpmark) - Stress tests for agents using pinned MCP services.
- [MCP-Bench](https://github.com/Accenture/mcp-bench) - Complex real-world tasks through MCP servers.
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon) - Long-horizon workflows over hundreds of tools and applications.
- [ToolBench and ToolEval](https://github.com/OpenBMB/ToolBench) - Large-scale API selection and composition.
- [StableToolBench](https://github.com/THUNLP-MT/StableToolBench) - Virtualized and cached tools for stable API evaluation.
- [API-Bank](https://github.com/AlibabaResearch/DAMO-ConvAI) - Dialogue API calling and planning tasks.
- [Agent-Diff](https://github.com/agent-diff-bench/agent-diff) - Enterprise API sandboxes graded by observable state diffs.
- [DataSpace](https://github.com/HKUSTDial/DataSpace) - Verifiable analytics over heterogeneous multimodal workspaces.
- [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench) - Multi-database and unstructured enterprise data-agent tasks.
- [STATE-Bench](https://github.com/microsoft/STATE-Bench) - Stateful enterprise workflows with main and agent-learning tracks.

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
- [BrowserUse Agent Bench / LexBench-Browser](https://github.com/lexmount/browseruse-agent-bench) - Browser tasks across websites and multiple agent backends.
- [BrowseComp](https://github.com/openai/simple-evals) - Hard-to-find web information problems.
- [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus) - Fixed-corpus deep research with retriever/agent disentanglement.

### Computer, spreadsheet, and mobile workflows

- [SpreadsheetBench](https://github.com/Reality2byte/spreadsheetbench) - Real-world spreadsheet manipulation with executable grading.
- [SpreadsheetBench 2](https://spreadsheetbench.github.io/) - Business spreadsheet generation, debugging, and visualization workflows.

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
- [Claw-Anything](https://github.com/LiberCoders/Claw-Anything) - Always-on personal assistant tasks with broad digital access.
- [SentinelBench](https://github.com/microsoft/sentinel_environments) - Long-running monitoring and event response.
- [METR Time Horizons](https://metr.org/time-horizons/) - Success probability as a function of human-equivalent task duration.
- [AgentSearchBench](https://github.com/Bingo-W/AgentSearchBench) - Execution-grounded search and reranking of real-world agents.
- [APEX-Agents / Archipelago](https://github.com/togethercomputer/archipelago) - MCP-based professional-services workflows with snapshot grading.
- [OmniaBench](https://github.com/scuuy/OmniaBench) - Diagnostic general-agent benchmark spanning broad real-world tasks.
- [AgentIF](https://agentif.github.io/) - Long, constraint-rich instruction following in agentic scenarios.
- [AgentIF-OneDay](https://github.com/xbench-ai/AgentIF-OneDay) - Daily multimodal workflows, latent instructions, and iterative refinement.
- [AOBench (Agent Operations Benchmark)](https://github.com/MSKazemi/aobench) - Role-aware, RBAC-enforced long-horizon HPC operations.

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
- [AgentShield Benchmark](https://github.com/doronp/agentshield-benchmark) - Prompt injection, exfiltration, tool abuse, and provenance threats.
- [Cybench](https://github.com/andyzorigin/cybench) - Multi-step cybersecurity CTF tasks and risk.

### Research engineering and specialized agents

- [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena) - Biomedical and multi-omics workflows with executable scoring.
- [AIRS-Bench](https://github.com/facebookresearch/airs-bench) - End-to-end machine-learning research-science tasks.
- [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench) - Long-horizon reverse engineering of source-free binaries.
- [AgentActionBench](https://arxiv.org/abs/2609.11117) - Trace-scored experiment reproduction across ML and AI4Science.
- [PaperBench](https://github.com/openai/preparedness) - Reproduction of published machine-learning papers from scratch.

## Evaluation infrastructure

- [Harbor](https://github.com/harbor-framework/harbor) - Versioned sandbox execution for agent benchmarks.
- [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) - Environments, verifiers, scale-out runs, and swappable harnesses.
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Reproducible evaluation implementations for Inspect AI.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) - Shared browser-agent environment interfaces.
- [Holistic Agent Leaderboard](https://hal.cs.princeton.edu/) - Cost-aware comparisons across agents, models, and task suites.
- [InfraBench](https://github.com/kubeply/infra-bench) - Realistic Kubernetes and infrastructure operations.
- [AgentSuite](https://github.com/Agent-Suite/AgentSuite) - One-touch execution plus component-based benchmark auditing.
- [Open AgentBench](https://github.com/the-open-agent/agentbench) - Performance, dialogue, tools, memory, throughput, and reliability suites.
- [Coder Eval](https://github.com/UiPath/coder_eval) - Agent-agnostic coding-agent and skill regression suites.
- [Lemans](https://github.com/rails/lemans) - Ruby CLI harness with digest-backed coding-agent reports.
- [AgentRace](https://agent-race.github.io/paper) - Runtime, scalability, communication, and tool-latency comparison.

## Website and Agent exports

The Pages site and Agent exports are the shipped interfaces for this repository. The generated `site/` directory contains `index.html` for people, `agent.md` and `index.md` for Agents, `catalog.json` and `source-audit.json` for structured ingestion, `research.md` for methodology, and `llms.txt` for discovery. The primary links are kept together near the top under **Start here**.

## Automated maintenance

The [Update sources workflow](.github/workflows/update-sources.yml) runs weekly and can be started manually. It refreshes GitHub metadata and README hashes with the audit script, then commits only changed provenance data. The [Deploy GitHub Pages workflow](.github/workflows/deploy-pages.yml) rebuilds the Markdown and HTML exports after source refreshes or normal pushes.

The `Benchmark Curator` custom agent gives GitHub Copilot a repeatable protocol for adding sources, recording limitations, validating the schema, and rebuilding the Agent exports.

## Research notes

The useful unit of comparison is a configuration: model endpoint, harness version, system prompt, tools, environment, and budgets. In a paired study, hold every factor except the treatment constant. For a component ablation, compare the same harness with one feature removed or swapped. Preserve raw traces, environment diffs, tool calls, costs, and verifier output so a headline score can be audited.

The catalog uses these capability tags: `tools`, `context`, `state`, `memory`, `planning`, `recovery`, `verification`, `permissions`, `multi-agent`, `vision`, `interaction`, `skills`, and `cost`. It records limitations because live websites, model judges, hidden state, stochastic sampling, and mutable datasets can change what a score means.

See `docs/research.md` for the inventory method, comparison dimensions, recommended benchmark stacks, and threats to validity.

## Data and provenance

The machine-readable inventory is `data/catalog.json`. Each record has a stable ID, category, type, source URL, measured signals, grading method, environment, and limitation. The GitHub availability audit is [data/source-audit.json](data/source-audit.json); it records repository metadata, default branch, star count, README commit SHA, and SHA-256 at audit time. A `needs-review` record means the URL was not accessible through the GitHub API at audit time; it is retained so the gap is visible.

Run the audit locally (requires authenticated `gh`):

```bash
python3 scripts/research_sources.py --catalog --audit
```

The script reads public GitHub metadata and README blobs, records hashes, and never executes downloaded repository code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for additions and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.
