# Agent benchmark catalog

[Selection guide](../README.md) · [Search and filter online](https://zeredy879.github.io/awesome-agent-harness-benchmarks/) · [JSON](../data/catalog.json)

115 resources across 13 areas. Source snapshot: 2026-09-13.

Generated from the canonical inventory. Resource types describe what a project provides, not its quality or independent verification. Every record includes a limitation.

## Contents

- [Direct harness comparisons](#direct) (11)
- [Tools, APIs, MCP, and state](#tools) (15)
- [Coding and terminal](#coding) (12)
- [Browser and web](#browser) (11)
- [General agents](#general) (11)
- [Memory and context](#memory) (7)
- [Safety and failure injection](#safety) (8)
- [Long horizon and always-on](#long-horizon) (8)
- [Evaluation infrastructure](#infrastructure) (11)
- [Computer and mobile](#computer) (6)
- [Multi-agent](#multi-agent) (4)
- [Research engineering](#research) (9)
- [Skills and instructions](#skills) (2)

<a id="direct"></a>

## Direct harness comparisons

<a id="tufantunc-harness"></a>

### [Coding harness comparison (tufantunc)](https://github.com/tufantunc/harness-benchmark)

**study** · ID: `tufantunc-harness`

Adapts Aider Polyglot tasks for same-model coding harness comparisons.

- Measures: tools, verification, cost.
- Grading: Polyglot tests through Inspect AI
- Environment: Docker and coding CLIs
- Limitation: A workload adapter and study; not a new independent task corpus.

<a id="harness-arena"></a>

### [Harness Arena](https://github.com/Ondemand-OSS/harness-arena)

**infrastructure** · ID: `harness-arena`

Runs blind pairwise comparisons of harness outputs.

- Measures: tools, cost.
- Grading: Human preference and Elo aggregation
- Environment: Isolated agent runs; web service
- Limitation: Preference ranking does not establish functional correctness; model matching must be enforced.

<a id="lamasu-harness"></a>

### [harness-bench (LamaSu)](https://github.com/LamaSu/harness-bench)

**watchlist** · ID: `lamasu-harness`

Proposes component ablations across control, tools, memory, subagents and verification.

- Measures: planning, tools, memory, multi-agent, permissions, verification.
- Grading: Inspect-based task and ablation design
- Environment: Inspect AI adapters
- Limitation: README advertises 37 ablation arms; adapter completeness and empirical results require inspection.

<a id="harness-bench-qihoo"></a>

### [Harness-Bench (Qihoo360)](https://github.com/Qihoo360/harness-bench)

**benchmark** · ID: `harness-bench-qihoo`

Compares native model–harness configurations on offline workspace workflows.

- Measures: tools, context, state, recovery, verification, cost.
- Grading: Artifact oracles plus LLM process rubrics
- Environment: Local workspaces; provider access
- Limitation: Public code and paper snapshot differ in adapter inventory; composite scores depend on the judge.
- [Paper / technical report](https://arxiv.org/abs/2605.27922)

<a id="zenixos-harness"></a>

### [harness-bench (zenixos)](https://github.com/zenixos/harness-bench)

**watchlist** · ID: `zenixos-harness`

Proposes a fixed-model comparison of coding CLIs on SWE-bench.

- Measures: tools, context, cost.
- Grading: Official SWE-bench evaluator; paired statistics planned
- Environment: Docker and a frozen pilot split
- Limitation: README explicitly says scored runs and paper are TBD; do not treat planned results as measured.

<a id="harness-dev"></a>

### [HarnessDev](https://arxiv.org/abs/2609.01437)

**benchmark** · ID: `harness-dev`

Evaluates creation and iterative evolution of runnable agent infrastructure.

- Measures: construction, tools, context, verification.
- Grading: Downstream performance of constructed harnesses
- Environment: Seed infrastructure and held-out task environments
- Limitation: Measures a developer agent's construction ability; code availability needs separate verification.

<a id="hyper-tau"></a>

### [Hyper-τ / τ^τ-bench](https://github.com/sierra-research/hyper-tau-bench)

**benchmark** · ID: `hyper-tau`

Builds customer-service agents from realistic evidence and scores their held-out performance.

- Measures: construction, tools, state, verification.
- Grading: Built agent's success on τ³ tasks
- Environment: Pinned Docker construction kit; model APIs
- Limitation: 53 release contracts in README; distinguish developer model from the model in the submitted agent.

<a id="nexus-harness"></a>

### [Nexus Harness Benchmark](https://github.com/nexus-research-lab/nexus-harness-benchmark)

**benchmark** · ID: `nexus-harness`

Tests workspace delivery using executable contracts and recorded evidence.

- Measures: tools, state, recovery, permissions, verification, cost.
- Grading: Deterministic checks; optional qualitative review
- Environment: Isolated workspaces
- Limitation: Community project; task coverage and independent reproduction need further validation.

<a id="d1-harness"></a>

### [Same-model harness study (d1-m4ss)](https://github.com/d1-m4ss/harness-benchmark)

**study** · ID: `d1-harness`

Compares coding harnesses with shared underlying models.

- Measures: tools, context, cost.
- Grading: Task correctness plus runtime and usage
- Environment: CLI agents and shared tasks
- Limitation: Small author-run study; task and configuration choices limit generalization.

<a id="rajshah-harness"></a>

### [Same-model harness study (rajshah4)](https://github.com/rajshah4/harness-benchmark)

**study** · ID: `rajshah-harness`

Publishes task verifiers, token ledgers and comparison artifacts for coding agents.

- Measures: tools, verification, cost.
- Grading: Task verifiers and provider accounting
- Environment: CLI agents
- Limitation: Model-bound control must be separated from same-model comparisons.

<a id="clawbench-openclaw"></a>

<a id="shellbench"></a>

### [ShellBench (formerly ClawBench)](https://github.com/openclaw/shellbench)

**benchmark** · ID: `clawbench-openclaw`

Scores full agent configurations, including the harness and model, using traces and reliability diagnostics.

- Measures: tools, state, recovery, cost.
- Grading: Trace scoring and repeated-run diagnostics
- Environment: OpenClaw-oriented task runner
- Limitation: Full-stack scores include model and configuration effects. Formerly OpenClaw ClawBench; distinct from TIGER-AI-Lab ClawBench.
- Former record IDs: `shellbench`


<a id="tools"></a>

## Tools, APIs, MCP, and state

<a id="agent-diff"></a>

### [Agent-Diff](https://github.com/agent-diff-bench/agent-diff)

**benchmark** · ID: `agent-diff`

Evaluates enterprise API agents in interactive sandboxes using state-diff grading.

- Measures: tools, state, verification, permissions.
- Grading: Before/after state diffs and task-specific checks
- Environment: Slack, Linear, Box, and Google Calendar-style API sandboxes
- Limitation: Third-party API replicas and scenario coverage must be pinned for meaningful comparisons.
- [Paper / technical report](https://arxiv.org/abs/2602.11224)

<a id="api-bank"></a>

### [API-Bank](https://github.com/AlibabaResearch/DAMO-ConvAI)

**benchmark** · ID: `api-bank`

Provides dialogue tasks involving API calling and planning.

- Measures: tools, interaction.
- Grading: API-call and response evaluation
- Environment: API-Bank subdirectory in a multi-project repository
- Limitation: Inspect the API-Bank task split; repository-wide metadata is not benchmark-specific.

<a id="appworld"></a>

### [AppWorld](https://github.com/StonyBrookNLP/appworld)

**benchmark** · ID: `appworld`

Tests code-driven interactions with a simulated ecosystem of personal apps.

- Measures: tools, state, planning, verification.
- Grading: Programmatic task and state checks
- Environment: Locally simulated app APIs
- Limitation: Requires adaptation to its API/code interface; final state checks have workload-specific scope.

<a id="bfcl"></a>

### [Berkeley Function Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html)

**benchmark** · ID: `bfcl`

Diagnoses function selection, arguments and increasingly agentic multi-turn tool use.

- Measures: tools, interaction.
- Grading: AST, execution and track-specific metrics
- Environment: Track-specific tool environments
- Limitation: Single-call tracks are component tests; the aggregate is not a full harness reliability score.

<a id="data-agent-benchmark"></a>

### [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench)

**benchmark** · ID: `data-agent-benchmark`

Evaluates data agents on multi-database integration, joins, text transformation, and domain knowledge.

- Measures: tools, context, state, verification.
- Grading: Task-level data correctness and leaderboard scoring
- Environment: Enterprise-style data workspaces and heterogeneous databases
- Limitation: Database connectors and hidden evaluation data must stay version-pinned for fair comparison.
- [Paper / technical report](https://arxiv.org/abs/2603.20576)

<a id="dataspace"></a>

### [DataSpace](https://github.com/HKUSTDial/DataSpace)

**benchmark** · ID: `dataspace`

Tests verifiable analytics over heterogeneous workspaces containing structured and unstructured artifacts.

- Measures: tools, context, state, verification, vision.
- Grading: Exact and semantic table comparison with type-aware checks
- Environment: CSV, JSON, SQLite, Markdown, PDF, and video workspaces
- Limitation: Large artifacts and multimodal dependencies make local reproduction resource-intensive.
- [Paper / technical report](https://arxiv.org/abs/2608.03451)

<a id="hermes-toolperf"></a>

### [Hermes tool-performance evals](https://github.com/NousResearch/hermes-toolperf-evals)

**study** · ID: `hermes-toolperf`

Provides tool-efficiency regression cases for Hermes changes.

- Measures: tools, recovery, cost.
- Grading: Tool-specific A/B checks and traces
- Environment: Hermes development environment
- Limitation: Vendor-specific regression suite; not a neutral cross-harness leaderboard.

<a id="mcp-bench"></a>

### [MCP-Bench (Accenture)](https://github.com/Accenture/mcp-bench)

**benchmark** · ID: `mcp-bench`

Evaluates multi-step tasks over diverse MCP servers.

- Measures: tools, planning.
- Grading: Task-level and tool-use evaluation
- Environment: MCP services and model endpoints
- Limitation: Live dependencies and scoring configuration influence comparability.

<a id="mcpmark"></a>

### [MCPMark](https://github.com/eval-sys/mcpmark)

**benchmark** · ID: `mcpmark`

Stress-tests task execution through real MCP services.

- Measures: tools, state, verification.
- Grading: Service-specific task verifiers
- Environment: MCP servers; local or account-backed services
- Limitation: Freeze server versions and initial state; some services require dedicated accounts.

<a id="stabletoolbench"></a>

### [StableToolBench](https://github.com/THUNLP-MT/StableToolBench)

**benchmark** · ID: `stabletoolbench`

Adds virtualized and cached tools for more stable ToolBench-style evaluation.

- Measures: tools, planning.
- Grading: StableToolEval and simulated execution
- Environment: Virtual API server
- Limitation: Simulator fidelity is a confounder; not identical to evaluation on live APIs.

<a id="state-bench"></a>

### [STATE-Bench](https://github.com/microsoft/STATE-Bench)

**benchmark** · ID: `state-bench`

Evaluates multi-step enterprise travel, support, and shopping workflows with an optional learning track.

- Measures: tools, state, memory, permissions, verification.
- Grading: Task completion pass@1, pass^5, UX, and cost per task
- Environment: Task-local enterprise databases, policy tools, and simulated users
- Limitation: Synthetic data and LLM-judged UX require careful interpretation alongside deterministic state checks.

<a id="toolathlon"></a>

### [Toolathlon / Toolathlon-Verified](https://github.com/hkust-nlp/Toolathlon)

**benchmark** · ID: `toolathlon`

Evaluates long workflows spanning many applications and tools.

- Measures: tools, state, planning, verification.
- Grading: Dedicated execution-based evaluators
- Environment: Containers and application services
- Limitation: Verified release changes prompts and evaluators; distinguish local mocks from live service execution.

<a id="toolbench"></a>

### [ToolBench / ToolEval](https://github.com/OpenBMB/ToolBench)

**benchmark** · ID: `toolbench`

Tests selecting and composing a large collection of external APIs.

- Measures: tools, planning.
- Grading: ToolEval solution and preference judgments
- Environment: API-backed tool execution
- Limitation: Historical API availability and model-judge behavior can limit reproducibility.

<a id="toolsandbox"></a>

### [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)

**benchmark** · ID: `toolsandbox`

Tests conversational tool use with implicit state dependencies and missing information.

- Measures: tools, state, interaction, recovery.
- Grading: Intermediate milestones and final state
- Environment: Stateful tool sandbox with user simulator
- Limitation: Measures deployed agent behavior; simulator and tool interface are experimental variables.

<a id="tau-bench"></a>

### [τ-bench family (τ / τ² / τ³)](https://github.com/sierra-research/tau2-bench)

**benchmark** · ID: `tau-bench`

Evaluates customer-service tool use, policy compliance and interactive coordination.

- Measures: tools, state, interaction, verification.
- Grading: Domain state and task-specific evaluation
- Environment: User simulator and domain tools; voice optional
- Limitation: Repository name remains tau2-bench; τ³ task fixes and knowledge/voice tracks require version labels.


<a id="coding"></a>

## Coding and terminal

<a id="aider-polyglot"></a>

### [Aider Polyglot](https://aider.chat/docs/leaderboards/)

**benchmark** · ID: `aider-polyglot`

Tests editing and repair on coding exercises across languages.

- Measures: tools, verification, cost.
- Grading: Exercise test suites
- Environment: Aider benchmark environments
- Limitation: Compact coding exercises; harness edit format and retry allowance strongly affect interpretation.

<a id="commit0"></a>

### [Commit0](https://github.com/commit-0/commit0)

**benchmark** · ID: `commit0`

Evaluates implementing software libraries from specifications and tests.

- Measures: planning, context, verification.
- Grading: Library tests
- Environment: Repository-scale Python environments
- Limitation: From-scratch implementation differs from maintaining an existing production repository.

<a id="gittaskbench"></a>

### [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench)

**benchmark** · ID: `gittaskbench`

Repo-level real-world tasks spanning repository understanding, setup, iterative fixing, and delivery.

- Measures: tools, context, planning, recovery, verification, cost.
- Grading: Task success, patch quality, and cost-aware alpha metrics
- Environment: 54 fixed GitHub repositories and reproducible repository workspaces
- Limitation: Fixed repositories can age; repository access, dependencies, and task contamination must be tracked.

<a id="mihacobench"></a>

### [MiHaCoBench](https://github.com/HangYu8123/MiHaCoBench)

**benchmark** · ID: `mihacobench`

Grades artifacts produced by configurable coding harnesses on Python tasks.

- Measures: tools, planning, verification.
- Grading: Weighted independent pytest graders
- Environment: Python task workspaces
- Limitation: 95 tasks in README; largely constructed problems rather than a broad industrial issue sample.

<a id="swe-bench"></a>

### [SWE-bench family](https://github.com/SWE-bench/SWE-bench)

**benchmark** · ID: `swe-bench`

Tests issue resolution in real repositories; includes Verified and other official tracks.

- Measures: tools, context, verification.
- Grading: Fail-to-pass and regression tests
- Environment: Versioned repository containers
- Limitation: Tracks have different languages, task sets and evaluators; published scores are not interchangeable.
- [Paper / technical report](https://www.swebench.com/)

<a id="swe-bench-live"></a>

### [SWE-bench Live](https://github.com/microsoft/SWE-bench-Live)

**benchmark** · ID: `swe-bench-live`

Uses a refreshed issue-resolution task collection to study coding agents.

- Measures: tools, context, verification.
- Grading: Executable repository tests
- Environment: Containerized repositories
- Limitation: Rolling datasets require an explicit snapshot and contamination checks.

<a id="swe-bench-pro"></a>

### [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os)

**benchmark** · ID: `swe-bench-pro`

Evaluates longer repository-level software-engineering tasks.

- Measures: tools, planning, context, verification.
- Grading: Repository test suites
- Environment: Docker task environments
- Limitation: Public and private sets must be distinguished; coverage differs from SWE-bench Verified.

<a id="swe-infrabench"></a>

### [SWE-InfraBench](https://arxiv.org/abs/2606.05249)

**benchmark** · ID: `swe-infrabench`

Tests incremental cloud infrastructure-code edits in the AWS CDK rather than greenfield generation.

- Measures: tools, context, verification, recovery.
- Grading: Infrastructure-code test and patch correctness
- Environment: AWS CDK repository tasks and cloud-infrastructure code
- Limitation: Narrow AWS CDK scope and dataset distribution constraints limit generalization.

<a id="swe-lancer"></a>

### [SWE-Lancer](https://github.com/openai/SWELancer-Benchmark)

**benchmark** · ID: `swe-lancer`

Tests economically grounded freelance engineering and managerial decisions.

- Measures: tools, planning, verification.
- Grading: Task-specific end-to-end grading
- Environment: Repository and application environments
- Limitation: Task value is not a universal productivity measure; manager and implementation tracks differ.

<a id="swe-rebench"></a>

### [SWE-rebench](https://github.com/SWE-rebench/SWE-rebench-V2)

**benchmark** · ID: `swe-rebench`

Provides continuously collected, reproducible software issue tasks.

- Measures: tools, context, verification.
- Grading: Repository test outcomes
- Environment: Docker repositories
- Limitation: Freeze release and task IDs; the changing task distribution affects trend comparisons.

<a id="terminal-bench"></a>

### [Terminal-Bench](https://github.com/harbor-framework/terminal-bench)

**benchmark** · ID: `terminal-bench`

Evaluates difficult terminal workflows through executable environment checks.

- Measures: tools, planning, recovery, verification, cost.
- Grading: Task-specific executable verifiers
- Environment: Containerized terminal environments
- Limitation: Pin a dataset release; task scores combine model and harness effects.
- [Paper / technical report](https://arxiv.org/abs/2601.11868)

<a id="version-control-bench"></a>

### [Version Control Bench](https://github.com/gitbutlerapp/version-control-bench)

**benchmark** · ID: `version-control-bench`

Benchmarks agents on version-control tasks using Git, Jujutsu, and GitButler workflows.

- Measures: tools, state, recovery, verification.
- Grading: Repository state and version-control outcome checks
- Environment: Local repositories with multiple version-control backends
- Limitation: Tool semantics differ across backends; task coverage is narrower than general software engineering.


<a id="browser"></a>

## Browser and web

<a id="browsecomp"></a>

### [BrowseComp](https://github.com/openai/simple-evals)

**benchmark** · ID: `browsecomp`

Tests whether browsing agents can find entangled, hard-to-locate information on the web.

- Measures: tools, planning, verification, context.
- Grading: Short-answer exact or semantic correctness over 1,266 problems
- Environment: Web search and browsing with live or provider-specific retrieval
- Limitation: Live web changes and search API differences can dominate results; preserve query and retrieval settings.
- [Paper / technical report](https://arxiv.org/abs/2504.12516)

<a id="browsecomp-plus"></a>

### [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus)

**benchmark** · ID: `browsecomp-plus`

Disentangles retriever and agent effects for deep-research evaluation over a fixed document corpus.

- Measures: tools, retrieval, context, planning, verification.
- Grading: Question pass rate with reproducible retrieval indexes and semantic judging
- Environment: Local corpus, retriever, and deep-research agent loop
- Limitation: Corpus/index versions and judge prompts must be pinned; full evaluation is expensive.

<a id="browseruse-agent-bench"></a>

### [BrowserUse Agent Bench / LexBench-Browser](https://github.com/lexmount/browseruse-agent-bench)

**benchmark** · ID: `browseruse-agent-bench`

Compares browser agents across 210 tasks, 107 websites, browser backends, and models.

- Measures: tools, vision, planning, verification.
- Grading: Reproducible task outcomes and submitted leaderboard runs
- Environment: Live and controlled browser sites with multiple agent backends
- Limitation: Live-site changes, anti-bot defenses, and browser backend differences affect comparability.

<a id="clawbench-tiger"></a>

### [ClawBench (TIGER-AI-Lab)](https://github.com/TIGER-AI-Lab/ClawBench)

**benchmark** · ID: `clawbench-tiger`

Tests everyday browser tasks across live websites.

- Measures: tools, vision, planning.
- Grading: Task outcome grading
- Environment: Live web
- Limitation: Different project from openclaw/clawbench and clawbenchlabs; live-site drift remains.

<a id="online-mind2web"></a>

### [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web)

**benchmark** · ID: `online-mind2web`

Evaluates realistic tasks on live websites with human-reviewed outcomes.

- Measures: tools, vision, planning.
- Grading: Human evaluation with supporting automated tooling
- Environment: Live web browser
- Limitation: Task validity changes with websites; pin the task list and submission schema.

<a id="visualwebarena"></a>

### [VisualWebArena](https://github.com/web-arena-x/visualwebarena)

**benchmark** · ID: `visualwebarena`

Adds visually grounded tasks to realistic web environments.

- Measures: tools, vision, state, verification.
- Grading: Functional task evaluation
- Environment: Browser with screenshots and self-hosted sites
- Limitation: Visual observations and action interfaces must match across runs.

<a id="webarena"></a>

### [WebArena](https://github.com/web-arena-x/webarena)

**benchmark** · ID: `webarena`

Evaluates autonomous workflows on self-hosted web applications.

- Measures: tools, state, planning, verification.
- Grading: Functional web-state checks
- Environment: Self-hosted sites and browser
- Limitation: Environment setup and task/evaluator fixes must be pinned.

<a id="webarena-verified"></a>

### [WebArena-Verified](https://github.com/ServiceNow/webarena-verified)

**benchmark** · ID: `webarena-verified`

Revisits WebArena tasks and evaluation for reproducible browser-agent testing.

- Measures: tools, state, verification.
- Grading: Revised functional evaluation
- Environment: Self-hosted web environments
- Limitation: Derivative of WebArena; do not count overlapping tasks as independent evidence.

<a id="webchorearena"></a>

### [WebChoreArena](https://github.com/WebChoreArena/WebChoreArena)

**benchmark** · ID: `webchorearena`

Stresses long, repetitive and memory-intensive web workflows.

- Measures: tools, planning, context, state.
- Grading: Task-specific web evaluators
- Environment: WebArena-derived environments
- Limitation: Shared infrastructure is not an independent measure of deployment reliability.

<a id="webvoyager"></a>

### [WebVoyager](https://github.com/MinorJerry/WebVoyager)

**benchmark** · ID: `webvoyager`

Evaluates browser agents on tasks across live websites.

- Measures: tools, vision, planning.
- Grading: Trajectory/screenshot-based task evaluation
- Environment: Live browser and internet
- Limitation: Website drift, access restrictions and evaluator reliability affect repeatability.

<a id="workarena"></a>

### [WorkArena / WorkArena++](https://github.com/ServiceNow/WorkArena)

**benchmark** · ID: `workarena`

Tests enterprise browser work and compositional knowledge-work tasks.

- Measures: tools, planning, state, verification.
- Grading: Task-specific enterprise state checks
- Environment: ServiceNow instances and browser
- Limitation: Requires platform access; levels and composed tasks must be reported separately.


<a id="general"></a>

## General agents

<a id="agentbench"></a>

### [AgentBench](https://github.com/THUDM/AgentBench)

**benchmark** · ID: `agentbench`

Evaluates agents across heterogeneous interactive environments.

- Measures: tools, planning, state.
- Grading: Environment-specific rewards and success
- Environment: Multiple environment backends
- Limitation: Aggregate scores mix different action spaces and task distributions.

<a id="agentif"></a>

### [AgentIF](https://agentif.github.io/)

**benchmark** · ID: `agentif`

Measures instruction following under long, complex, constraint-rich agent prompts and tool specifications.

- Measures: context, tools, permissions, verification.
- Grading: Code, LLM, and hybrid constraint-level evaluation
- Environment: Instructions collected from 50 real-world agent applications
- Limitation: Instruction-following is only one layer of end-to-end agent competence; synthetic task construction remains a factor.
- [Paper / technical report](https://arxiv.org/abs/2505.16944)

<a id="agent-search-bench"></a>

### [AgentSearchBench](https://github.com/Bingo-W/AgentSearchBench)

**benchmark** · ID: `agent-search-bench`

Evaluates retrieval and reranking of real-world agents using execution-grounded relevance.

- Measures: tools, retrieval, planning, multi-agent.
- Grading: NDCG, completeness, and execution-grounded relevance
- Environment: Agent catalog and execution traces from multiple providers
- Limitation: Provider coverage, agent availability, and execution costs can change the candidate pool.
- [Paper / technical report](https://arxiv.org/abs/2604.22436)

<a id="apex-agents-archipelago"></a>

### [APEX-Agents / Archipelago](https://github.com/togethercomputer/archipelago)

**benchmark** · ID: `apex-agents-archipelago`

Evaluates agents on professional-services tasks through MCP environments, runners, and snapshot grading.

- Measures: tools, state, planning, verification, cost.
- Grading: Before/after snapshot graders with optional trajectory signals
- Environment: Dockerized MCP applications and professional-services workspaces
- Limitation: LLM-graded trajectory signals are evolving and professional task access is controlled.
- [Paper / technical report](https://arxiv.org/abs/2601.14242)

<a id="assistantbench"></a>

### [AssistantBench](https://github.com/oriyor/assistantbench)

**benchmark** · ID: `assistantbench`

Tests practical information-seeking tasks for web assistants.

- Measures: tools, planning.
- Grading: Answer-level evaluation
- Environment: Web browsing and search
- Limitation: Answer correctness is a useful proxy but does not certify workspace or side-effect correctness.

<a id="claw-eval"></a>

### [Claw-Eval](https://github.com/claw-eval/claw-eval)

**benchmark** · ID: `claw-eval`

Evaluates general, multimodal and multi-turn agent tasks.

- Measures: tools, vision, interaction, permissions, verification.
- Grading: Trajectory rubrics; completion, safety and consistency
- Environment: Sandbox plus service/web dependencies
- Limitation: Author README discloses API-error reruns; report retry policy and grader versions.

<a id="claw-eval-live"></a>

### [Claw-Eval-Live](https://github.com/Claw-Eval-Live/Claw-Eval-Live)

**benchmark** · ID: `claw-eval-live`

Builds evolving workflow tests from marketplace demand signals.

- Measures: tools, skills, verification.
- Grading: Workflow-specific evaluation
- Environment: Task-specific services
- Limitation: Moving corpus requires snapshot IDs; distinct from static Claw-Eval results.

<a id="gaia"></a>

### [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)

**benchmark** · ID: `gaia`

Tests tool-assisted information gathering and multimodal reasoning.

- Measures: tools, planning, vision.
- Grading: Final-answer accuracy
- Environment: Web, files and selected tools
- Limitation: Final answers reveal less about intermediate side effects and execution safety.
- [Paper / technical report](https://arxiv.org/abs/2311.12983)

<a id="omnia-bench"></a>

### [OmniaBench](https://github.com/scuuy/OmniaBench)

**benchmark** · ID: `omnia-bench`

Broad diagnostic evaluation of general-purpose agents across diverse tasks and environments.

- Measures: tools, planning, state, verification, cost.
- Grading: Task success and aggregate diagnostic metrics
- Environment: Mixed agent tasks with released full and challenging subsets
- Limitation: Heterogeneous environments make a single aggregate less diagnostic than per-family scores.
- [Paper / technical report](https://arxiv.org/abs/2607.14989)

<a id="pinchbench"></a>

### [PinchBench](https://github.com/pinchbench/skill)

**benchmark** · ID: `pinchbench`

Evaluates models running as OpenClaw agents on practical assistant tasks.

- Measures: tools, planning, verification.
- Grading: Task-specific grading
- Environment: OpenClaw runtime
- Limitation: Default setup holds one harness fixed; cross-harness use requires an explicit adapter.

<a id="theagentcompany"></a>

### [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)

**benchmark** · ID: `theagentcompany`

Simulates digital workplace tasks with apps, files and coworkers.

- Measures: tools, planning, interaction, verification.
- Grading: Task and intermediate checkpoint grading
- Environment: Self-hosted workplace services
- Limitation: Large setup; simulated coworkers and partial-credit definitions affect results.


<a id="memory"></a>

## Memory and context

<a id="context-bench-letta"></a>

### [Context-Bench (Letta, V2)](https://www.letta.com/blog/evaluating-memory-in-production-agents/)

**benchmark** · ID: `context-bench-letta`

Tests file navigation and relationship tracing under context constraints.

- Measures: context, tools, planning.
- Grading: Answer and file-operation task evaluation
- Environment: File-based task environments
- Limitation: Distinct from code-context retrieval benchmarks with similar names.

<a id="contextbench-code"></a>

### [ContextBench (coding retrieval)](https://arxiv.org/abs/2602.05892)

**benchmark** · ID: `contextbench-code`

Evaluates the context gathered by coding agents from repositories.

- Measures: context, tools.
- Grading: Context-retrieval evaluation
- Environment: Repository retrieval tasks
- Limitation: Retrieval quality is a component metric; code-fix success needs separate tests.

<a id="locomo"></a>

### [LoCoMo](https://github.com/snap-research/locomo)

**benchmark** · ID: `locomo`

Tests long-term conversational memory over extended dialogue histories.

- Measures: memory, context.
- Grading: QA and task-specific language metrics
- Environment: Recorded/generated conversation histories
- Limitation: Small conversation sample and judge choice limit broad memory-system conclusions.

<a id="longmemeval"></a>

### [LongMemEval](https://github.com/xiaowu0162/LongMemEval)

**benchmark** · ID: `longmemeval`

Tests information extraction, temporal reasoning and updates across long histories.

- Measures: memory, context.
- Grading: LLM-judged question-answering accuracy
- Environment: Stored conversational histories
- Limitation: Full-context baselines are essential; QA retrieval is not closed-loop task execution.

<a id="longmemeval-v2"></a>

### [LongMemEval-V2](https://github.com/xiaowu0162/LongMemEval-V2)

**benchmark** · ID: `longmemeval-v2`

Tests experience retrieval from long histories of multimodal agent trajectories.

- Measures: memory, context, vision, cost.
- Grading: Answer accuracy and query latency
- Environment: Stored web and enterprise trajectories
- Limitation: Measures evidence retrieval for downstream QA; not end-to-end repeated task completion.

<a id="memoryagentbench"></a>

### [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

**benchmark** · ID: `memoryagentbench`

Tests incremental memory through retrieval, learning, understanding and forgetting.

- Measures: memory, context.
- Grading: Task-specific accuracy
- Environment: Incrementally delivered text streams
- Limitation: Different subsets probe different operations; aggregates hide trade-offs.

<a id="memoryarena"></a>

### [MemoryArena](https://github.com/ZexueHe/MemoryArena)

**benchmark** · ID: `memoryarena`

Tests memory within interdependent tasks spread across agent sessions.

- Measures: memory, state, planning.
- Grading: Domain-specific task success
- Environment: Memory–agent–environment loops
- Limitation: Setup and external domain dependencies need verification; stronger task signal than QA alone.


<a id="safety"></a>

## Safety and failure injection

<a id="agent-safetybench"></a>

### [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)

**benchmark** · ID: `agent-safetybench`

Evaluates safety behavior in interactive agent environments.

- Measures: permissions, tools, interaction.
- Grading: Scenario-specific safety evaluation
- Environment: Simulated tool environments
- Limitation: Safety taxonomy and judge dependence need disclosure alongside usefulness.

<a id="agentdojo"></a>

### [AgentDojo](https://github.com/ethz-spylab/agentdojo)

**benchmark** · ID: `agentdojo`

Tests prompt-injection attacks and defenses in stateful tool environments.

- Measures: permissions, tools, state.
- Grading: Benign utility and attack success
- Environment: Simulated tools with adversarial external data
- Limitation: Threat model and attack budget must be held constant; utility must accompany safety.

<a id="agentharm"></a>

### [AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)

**benchmark** · ID: `agentharm`

Tests whether agents execute harmful multi-step requests.

- Measures: permissions, tools.
- Grading: Harmful task completion and refusal evaluation
- Environment: Inspect Evals agentharm tasks
- Limitation: Distinct from indirect prompt injection; suite repository contains many unrelated evals.
- [Paper / technical report](https://arxiv.org/abs/2410.09024)

<a id="agentshield-benchmark"></a>

### [AgentShield Benchmark](https://github.com/doronp/agentshield-benchmark)

**benchmark** · ID: `agentshield-benchmark`

Tests agent-security tools against prompt injection, exfiltration, tool abuse, and provenance threats.

- Measures: permissions, tools, verification, recovery.
- Grading: Attack success, detection, and policy-violation metrics
- Environment: Isolated adversarial tool and provenance scenarios
- Limitation: Security coverage and attack realism evolve quickly; results are not a complete risk assessment.

<a id="cybench"></a>

### [Cybench](https://github.com/andyzorigin/cybench)

**benchmark** · ID: `cybench`

Evaluates cybersecurity agent capability and risk over multi-step Capture the Flag tasks.

- Measures: tools, planning, recovery, permissions.
- Grading: Task and subtask completion across CTF challenge categories
- Environment: Containerized cybersecurity tasks and tool-using agent
- Limitation: Dual-use tasks require careful isolation; CTF performance does not equal production security.

<a id="harness-risk"></a>

### [HarnessRisk](https://github.com/Baiyajing/HarnessRisk)

**benchmark** · ID: `harness-risk`

Tests adversarial artifacts across six stages of the harness lifecycle.

- Measures: permissions, memory, recovery, tools.
- Grading: Utility, attack success, persistence and detection
- Environment: Mock services and workspace; use OS isolation
- Limitation: 128 cases per paper; recognizing an attack is distinct from preventing its side effects.
- [Paper / technical report](https://arxiv.org/abs/2608.17597)

<a id="injecagent"></a>

### [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)

**benchmark** · ID: `injecagent`

Tests indirect prompt injections through tool outputs.

- Measures: permissions, tools.
- Grading: Attack success checks
- Environment: Tool-response injection cases
- Limitation: Narrow attack setup; does not cover the entire permissions or persistence lifecycle.

<a id="wasp"></a>

### [WASP](https://github.com/facebookresearch/wasp)

**benchmark** · ID: `wasp`

Evaluates web-agent susceptibility to adversarial website content.

- Measures: permissions, tools, vision.
- Grading: Attack success and task utility
- Environment: Adversarial web environments
- Limitation: Browser attack surface differs from API tool-response injection.


<a id="long-horizon"></a>

## Long horizon and always-on

<a id="agentif-oneday"></a>

### [AgentIF-OneDay](https://github.com/xbench-ai/AgentIF-OneDay)

**benchmark** · ID: `agentif-oneday`

Tests daily work, life, and study workflows with attachments, latent instructions, and iterative refinement.

- Measures: context, planning, state, verification, vision.
- Grading: Instance rubrics combining LLM verification and human alignment
- Environment: Multimodal daily scenarios with file-based deliverables
- Limitation: Many tasks depend on subjective rubric judgments and long-horizon context management.
- [Paper / technical report](https://arxiv.org/abs/2601.20613)

<a id="aobench"></a>

### [AOBench (Agent Operations Benchmark)](https://github.com/MSKazemi/aobench)

**benchmark** · ID: `aobench`

Role-aware, permission-enforced evaluation of agents operating HPC systems and facilities.

- Measures: tools, permissions, state, verification, recovery.
- Grading: Trace-scored task outcomes with hard-fail policy violations
- Environment: Deterministic HPC operational environments, SLURM, telemetry, and RBAC
- Limitation: Deterministic facility snapshots cannot cover every live-cluster failure mode.

<a id="claw-anything"></a>

### [Claw-Anything](https://github.com/LiberCoders/Claw-Anything)

**benchmark** · ID: `claw-anything`

Evaluates always-on assistants with broad access to a user's digital environment.

- Measures: tools, state, memory, interaction.
- Grading: Generated tasks and task-specific graders
- Environment: Simulated personal digital environment
- Limitation: Construction pipeline and verification level vary; preserve task provenance.

<a id="clawmark"></a>

### [ClawMark](https://github.com/evolvent-ai/ClawMark)

**benchmark** · ID: `clawmark`

Tests multi-turn, multi-day, multimodal coworker behavior in an evolving world.

- Measures: state, memory, interaction, vision.
- Grading: Task and world-state evaluation
- Environment: Living-world simulation
- Limitation: Multi-day simulated workloads are not evidence of uninterrupted production uptime.

<a id="durable-harness"></a>

### [Durable-agent-harness](https://github.com/Eldergenix/Durable-agent-harness)

**study** · ID: `durable-harness`

Uses controlled simulations to ablate memory, checkpoints and recovery logic.

- Measures: memory, state, recovery, cost.
- Grading: Machine-graded simulation outcomes and paired experiments
- Environment: Deterministic simulation; optional live provider
- Limitation: Simulation evidence must not be reported as full real-agent deployment reliability.

<a id="gaia2"></a>

### [Gaia2 / Gaia2-CLI](https://github.com/facebookresearch/meta-agents-research-environments)

**benchmark** · ID: `gaia2`

Tests dynamic environments, temporal constraints, ambiguity and asynchronous events.

- Measures: tools, state, interaction, multi-agent, recovery.
- Grading: Write-action verifier
- Environment: Agents Research Environments; CLI variant
- Limitation: Variants change the action interface; the simulated clock is not ordinary wall-clock runtime.
- [Paper / technical report](https://arxiv.org/abs/2602.11964)

<a id="metr-horizon"></a>

### [METR Task-Completion Time Horizons](https://metr.org/time-horizons/)

**benchmark** · ID: `metr-horizon`

Estimates task difficulty in human-time units at a chosen agent success threshold.

- Measures: planning, tools, verification.
- Grading: Success curve fitted to human task duration
- Environment: Software, ML and cybersecurity tasks
- Limitation: Human-equivalent horizon is not how long an agent runs; full task access is limited.

<a id="sentinelbench"></a>

### [SentinelBench](https://github.com/microsoft/sentinel_environments)

**benchmark** · ID: `sentinelbench`

Tests monitoring agents reacting to events over extended timelines.

- Measures: state, interaction, planning.
- Grading: Server-side environment state checks
- Environment: Synthetic web environments and event streams
- Limitation: Monitor performance depends on clock, wake-up policy and event schedule.


<a id="infrastructure"></a>

## Evaluation infrastructure

<a id="agent-race"></a>

### [AgentRace](https://agent-race.github.io/paper)

**study** · ID: `agent-race`

Controlled comparison of LLM agent frameworks on runtime, scalability, communication, and tool latency.

- Measures: tools, cost, multi-agent, recovery.
- Grading: Runtime performance, scalability, communication overhead, and tool latency
- Environment: Representative workloads across popular agent frameworks
- Limitation: Paper and release snapshots may not track framework versions at the same pace.

<a id="agentsuite"></a>

### [AgentSuite](https://github.com/Agent-Suite/AgentSuite)

**infrastructure** · ID: `agentsuite`

One-touch platform for running agent benchmarks with component audits and benchmark variants.

- Measures: tools, verification, cost, recovery.
- Grading: Delegates to selected benchmark implementations and audit checks
- Environment: Configurable benchmark runners and agent adapters
- Limitation: A runner and auditing layer; it does not make underlying task suites interchangeable.

<a id="browsergym"></a>

### [BrowserGym](https://github.com/ServiceNow/BrowserGym)

**infrastructure** · ID: `browsergym`

Provides a shared interface for browser-agent environments.

- Measures: tools, vision, state.
- Grading: Underlying browser benchmark evaluators
- Environment: Browser environments
- Limitation: Common API does not make different task suites or observation settings comparable.

<a id="coder-eval"></a>

### [Coder Eval](https://github.com/UiPath/coder_eval)

**infrastructure** · ID: `coder-eval`

Agent-agnostic sandbox and YAML task framework for coding-agent, skill, and CI regression evaluation.

- Measures: tools, verification, skills, cost, recovery.
- Grading: Weighted criteria, activation checks, artifacts, and telemetry
- Environment: Sandboxed coding agents including Claude Code, Codex, Gemini, OpenCode, and Pi
- Limitation: Bring-your-own tasks and scorers; local suites are not directly comparable without shared fixtures.

<a id="harbor"></a>

### [Harbor](https://github.com/harbor-framework/harbor)

**infrastructure** · ID: `harbor`

Runs agent evaluations across versioned sandbox environments and datasets.

- Measures: tools, verification, cost.
- Grading: Delegates scoring to selected benchmark
- Environment: Containers and remote sandbox providers
- Limitation: An evaluation platform, not an independent benchmark score.

<a id="hal"></a>

### [Holistic Agent Leaderboard (HAL)](https://hal.cs.princeton.edu/)

**infrastructure** · ID: `hal`

Compares agents using reproducible, cost-aware evaluation across tasks.

- Measures: cost, verification.
- Grading: Benchmark scores and cost-aware comparisons
- Environment: Multiple task suites
- Limitation: Cross-benchmark cost and success must retain original units and configurations.
- [Paper / technical report](https://arxiv.org/abs/2510.11977)

<a id="infra-bench"></a>

### [InfraBench](https://github.com/kubeply/infra-bench)

**benchmark** · ID: `infra-bench`

Runs realistic Kubernetes and infrastructure tasks with Harbor-compatible sandboxes.

- Measures: tools, state, recovery, permissions, verification.
- Grading: Task verifiers over infrastructure state and command outcomes
- Environment: Ephemeral Kubernetes and infrastructure environments
- Limitation: Terraform and observability tracks are still expanding; cluster setup can dominate run cost.
- [Paper / technical report](https://arxiv.org/abs/2608.11234)

<a id="inspect-evals"></a>

### [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals)

**infrastructure** · ID: `inspect-evals`

Collects reproducible evaluation implementations for Inspect AI.

- Measures: tools, verification, permissions.
- Grading: Benchmark-dependent scorers
- Environment: Inspect solvers and sandboxes
- Limitation: Preserve upstream task and scorer versions; collection entries are not all harness benchmarks.

<a id="lemans"></a>

### [Lemans](https://github.com/rails/lemans)

**infrastructure** · ID: `lemans`

Ruby CLI harness for reproducible coding-agent benchmarks with Docker or Daytona sandboxes.

- Measures: tools, verification, recovery, cost.
- Grading: Task verifier and digest-backed result reports
- Environment: Docker or Daytona coding sandboxes
- Limitation: Execution layer rather than a fixed task suite; benchmark quality depends on user-authored tasks.

<a id="nemo-gym"></a>

### [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)

**infrastructure** · ID: `nemo-gym`

Supports composable environments and configurable agent evaluation.

- Measures: tools, verification, cost.
- Grading: Environment-specific rewards
- Environment: Configured agent and environment services
- Limitation: Harness comparison requires fixed model, dataset, environment and repeat count.
- [Paper / technical report](https://docs.nvidia.com/nemo/gym/evaluation/harness/)

<a id="open-agentbench"></a>

### [Open AgentBench](https://github.com/the-open-agent/agentbench)

**benchmark** · ID: `open-agentbench`

Runtime benchmark for agent performance, dialogue, tools, startup, memory, throughput, and reliability.

- Measures: tools, memory, cost, recovery, state.
- Grading: Suite-specific functional, latency, throughput, and consistency metrics
- Environment: OpenClaw, OpenAgent, Hermes, and compatible agent runtimes
- Limitation: Runtime-specific adapters and a young leaderboard limit cross-harness comparability.


<a id="computer"></a>

## Computer and mobile

<a id="androidlab"></a>

### [AndroidLab](https://github.com/THUDM/Android-Lab)

**benchmark** · ID: `androidlab`

Provides Android interaction tasks and agent evaluation tooling.

- Measures: tools, vision, state.
- Grading: Task-specific mobile evaluation
- Environment: Android emulator and applications
- Limitation: Platform-specific control; scores do not transfer directly to desktop or web.

<a id="androidworld"></a>

### [AndroidWorld](https://github.com/google-research/android_world)

**benchmark** · ID: `androidworld`

Evaluates agents on parameterized tasks in Android apps.

- Measures: tools, vision, state, verification.
- Grading: Programmatic app-state validation
- Environment: Android emulator
- Limitation: Device, app versions and generated task parameters must be fixed.

<a id="osworld"></a>

### [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld)

**benchmark** · ID: `osworld`

Evaluates multi-application desktop work in real operating systems.

- Measures: tools, vision, state, verification.
- Grading: Execution-based task checks
- Environment: Virtual machines with desktop applications
- Limitation: VM images, step budgets and benchmark revisions must match; check newer versions upstream.
- [Paper / technical report](https://os-world.github.io/)

<a id="spreadsheetbench"></a>

### [SpreadsheetBench](https://github.com/Reality2byte/spreadsheetbench)

**benchmark** · ID: `spreadsheetbench`

Evaluates real-world spreadsheet manipulation with multi-test-case online-judge style grading.

- Measures: tools, verification, context, vision.
- Grading: Workbook outputs compared over multiple recalculated test cases
- Environment: Excel workbooks and code-execution agents
- Limitation: Office engines, formula recalculation, and platform differences can change results.

<a id="spreadsheetbench-2"></a>

### [SpreadsheetBench 2](https://spreadsheetbench.github.io/)

**benchmark** · ID: `spreadsheetbench-2`

Workflow-level spreadsheet benchmark covering generation, debugging, and visualization in business workbooks.

- Measures: tools, state, verification, vision.
- Grading: End-to-end workbook task outcomes with official evaluation code
- Environment: Complex multi-sheet business spreadsheets and multi-turn agents
- Limitation: A new release with complementary product baselines; version and submission status matter.
- [Paper / technical report](https://arxiv.org/abs/2606.29955)

<a id="windows-agent-arena"></a>

### [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)

**benchmark** · ID: `windows-agent-arena`

Adapts desktop-agent evaluation to Windows applications.

- Measures: tools, vision, state, verification.
- Grading: OS/task state checks
- Environment: Windows virtual machines
- Limitation: Windows licensing and infrastructure requirements affect deployment cost.


<a id="multi-agent"></a>

## Multi-agent

<a id="mas-fire"></a>

### [MAS-FIRE](https://arxiv.org/abs/2602.19843)

**benchmark** · ID: `mas-fire`

Injects faults to evaluate reliability of multi-agent systems.

- Measures: multi-agent, recovery, state.
- Grading: Fault detection and reliability evaluation
- Environment: Multi-agent frameworks
- Limitation: Fault model and intervention point are part of the treatment.

<a id="multiagentbench"></a>

### [MultiAgentBench](https://github.com/MultiagentBench/MARBLE)

**benchmark** · ID: `multiagentbench`

Evaluates collaboration across multi-agent tasks and coordination patterns.

- Measures: multi-agent, planning, interaction.
- Grading: Task and collaboration evaluation
- Environment: MARBLE environments
- Limitation: Agent count, communication budgets and task decomposition must be controlled.

<a id="orchestrabench"></a>

### [OrchestraBench](https://arxiv.org/abs/2608.05263)

**benchmark** · ID: `orchestrabench`

Uses controlled faults to diagnose routing, recovery and failure cascades.

- Measures: multi-agent, recovery, state.
- Grading: Cascade radius and per-mode recovery
- Environment: Templated workflows and controlled mechanism probes
- Limitation: Small controlled probes; do not extrapolate measured recovery to all business workflows.

<a id="sabot"></a>

### [SABOT](https://github.com/Jott2121/sabot)

**study** · ID: `sabot`

Tests whether pipeline-native checks detect planted faults.

- Measures: multi-agent, recovery, verification.
- Grading: Fault-detection outcomes and traces
- Environment: Framework-specific fault-injection experiments
- Limitation: Author-reported study; distinguish native detection from external adjudication.


<a id="research"></a>

## Research engineering

<a id="agent-action-bench"></a>

### [AgentActionBench](https://arxiv.org/abs/2609.11117)

**benchmark** · ID: `agent-action-bench`

Process-oriented evaluation of agents reproducing experiments from ML and AI-for-science papers.

- Measures: tools, planning, verification, recovery.
- Grading: Paper-specific trace rubrics with human-validated rubric augmentation
- Environment: MCP-recorded experiment reproduction workflows
- Limitation: Newest shared-task release; public code and scoring details may continue changing.

<a id="agentre-bench"></a>

### [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench)

**benchmark** · ID: `agentre-bench`

Measures long-horizon reverse engineering of unseen binaries with constrained tools and evidence capture.

- Measures: tools, planning, verification, recovery.
- Grading: Deterministic expert-grounded claims, coverage, and tool-use metrics
- Environment: Isolated Linux and Windows binary workspaces without source code
- Limitation: Versioned binary ladders are not directly comparable across major releases.

<a id="airs-bench"></a>

### [AIRS-Bench](https://github.com/facebookresearch/airs-bench)

**benchmark** · ID: `airs-bench`

Measures end-to-end AI research ability through open-ended research-science tasks.

- Measures: tools, planning, verification, cost.
- Grading: Normalized task scores with multi-seed leaderboard reporting
- Environment: Research workflows with code, data, and experiment artifacts
- Limitation: Open-ended research quality and expensive model calls make scores judge- and budget-sensitive.
- [Paper / technical report](https://arxiv.org/abs/2602.06855)

<a id="core-bench"></a>

### [CORE-Bench](https://github.com/siegelz/core-bench)

**benchmark** · ID: `core-bench`

Tests computational reproduction using scientific code and artifacts.

- Measures: tools, context, recovery, verification.
- Grading: Reproduction task answers and artifacts
- Environment: Scientific repositories and containers
- Limitation: Availability of original artifacts and environment drift constrain repeatability.

<a id="mle-bench"></a>

### [MLE-bench](https://github.com/openai/mle-bench)

**benchmark** · ID: `mle-bench`

Evaluates autonomous ML engineering on competition tasks.

- Measures: tools, planning, verification, cost.
- Grading: Competition-specific held-out metrics
- Environment: Data, containers and often GPUs
- Limitation: Hardware, runtime and access to prior solutions are major controls.

<a id="paperbench"></a>

### [PaperBench](https://github.com/openai/preparedness)

**benchmark** · ID: `paperbench`

Tests whether agents can reproduce 20 ICML 2024 research papers from scratch.

- Measures: tools, planning, verification, cost.
- Grading: Hierarchical paper-specific rubrics over reproduced code and experiments
- Environment: Three-stage containerized rollout, reproduction, and grading pipeline
- Limitation: GPU, data, and judge costs are high; rubric-based grading remains partially model-assisted.
- [Paper / technical report](https://arxiv.org/abs/2504.01848)

<a id="re-bench"></a>

### [RE-Bench](https://github.com/METR/RE-Bench)

**benchmark** · ID: `re-bench`

Tests AI research engineering against human baselines.

- Measures: tools, planning, verification, cost.
- Grading: Task-specific objective scores
- Environment: Research engineering environments
- Limitation: Small expert task collection; time and compute budgets affect comparisons.

<a id="sciagentarena"></a>

### [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena)

**benchmark** · ID: `sciagentarena`

Evaluates scientific agents across biomedical and multi-omics workflows with stepwise scoring.

- Measures: tools, planning, verification, multi-agent.
- Grading: Automated domain-specific scores and execution outputs
- Environment: Scientific Python workflows across seven benchmark families
- Limitation: Domain packages and scientific validity are difficult to reproduce outside the pinned environments.
- [Paper / technical report](https://arxiv.org/abs/2606.12736)

<a id="scienceagentbench"></a>

### [ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)

**benchmark** · ID: `scienceagentbench`

Evaluates executable programs for data-driven scientific tasks.

- Measures: tools, planning, verification.
- Grading: Program execution and scientific task metrics
- Environment: Scientific datasets and Python environments
- Limitation: Scientific validity extends beyond passing the benchmark's tests.


<a id="skills"></a>

## Skills and instructions

<a id="skillsbench"></a>

### [SkillsBench](https://github.com/benchflow-ai/skillsbench)

**benchmark** · ID: `skillsbench`

Measures the task-level contribution of reusable instruction and script packages.

- Measures: skills, tools, verification, cost.
- Grading: Executable task verifiers; paired skill conditions
- Environment: Task-specific environments and coding agents
- Limitation: Version 1.1 differs from paper-v1; compare identical task and skill snapshots.
- [Paper / technical report](https://www.skillsbench.ai/blogs/skillsbench-1-1)

<a id="swe-skills-bench"></a>

### [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)

**benchmark** · ID: `swe-skills-bench`

Studies the marginal utility of skills for software-engineering requirements.

- Measures: skills, context, verification.
- Grading: Requirement-driven SWE evaluation
- Environment: Repository tasks
- Limitation: Paper accessible; the paper-linked GitHub repository returned 404 during this review.
