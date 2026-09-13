# Agent Harness Benchmarks

> Machine-readable Markdown snapshot. Use `catalog.json` for structured ingestion and `research.md` for methodology.

- Snapshot date: `2026-09-13`
- Entries: `116`
- Categories: `13`
- GitHub source records: `99` (`99` accessible at audit time)
- Scope: public benchmarks, controlled studies, and evaluation infrastructure relevant to agent harnesses

## Category counts

- `tools` - Tools, APIs, MCP, and state: **15**
- `coding` - Coding and terminal: **12**
- `direct` - Direct harness comparisons: **12**
- `browser` - Browser and web: **11**
- `general` - General agents: **11**
- `infrastructure` - Evaluation infrastructure: **11**
- `research` - Research engineering: **9**
- `long-horizon` - Long horizon and always-on: **8**
- `safety` - Safety and failure injection: **8**
- `memory` - Memory and context: **7**
- `computer` - Computer and mobile: **6**
- `multi-agent` - Multi-agent: **4**
- `skills` - Skills and instructions: **2**

## Entries

### BrowseComp

- ID: `browsecomp`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/openai/simple-evals
- Summary: Tests whether browsing agents can find entangled, hard-to-locate information on the web.
- Signals: `tools`, `planning`, `verification`, `context`
- Grading: Short-answer exact or semantic correctness over 1,266 problems
- Environment: Web search and browsing with live or provider-specific retrieval
- Limitation: Live web changes and search API differences can dominate results; preserve query and retrieval settings.
- Paper: https://arxiv.org/abs/2504.12516

### BrowseComp-Plus

- ID: `browsecomp-plus`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/texttron/BrowseComp-Plus
- Summary: Disentangles retriever and agent effects for deep-research evaluation over a fixed document corpus.
- Signals: `tools`, `retrieval`, `context`, `planning`, `verification`
- Grading: Question pass rate with reproducible retrieval indexes and semantic judging
- Environment: Local corpus, retriever, and deep-research agent loop
- Limitation: Corpus/index versions and judge prompts must be pinned; full evaluation is expensive.

### BrowserUse Agent Bench / LexBench-Browser

- ID: `browseruse-agent-bench`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/lexmount/browseruse-agent-bench
- Summary: Compares browser agents across 210 tasks, 107 websites, browser backends, and models.
- Signals: `tools`, `vision`, `planning`, `verification`
- Grading: Reproducible task outcomes and submitted leaderboard runs
- Environment: Live and controlled browser sites with multiple agent backends
- Limitation: Live-site changes, anti-bot defenses, and browser backend differences affect comparability.

### ClawBench (TIGER-AI-Lab)

- ID: `clawbench-tiger`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/TIGER-AI-Lab/ClawBench
- Summary: Tests everyday browser tasks across live websites.
- Signals: `tools`, `vision`, `planning`
- Grading: Task outcome grading
- Environment: Live web
- Limitation: Different project from openclaw/clawbench and clawbenchlabs; live-site drift remains.

### Online-Mind2Web

- ID: `online-mind2web`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/OSU-NLP-Group/Online-Mind2Web
- Summary: Evaluates realistic tasks on live websites with human-reviewed outcomes.
- Signals: `tools`, `vision`, `planning`
- Grading: Human evaluation with supporting automated tooling
- Environment: Live web browser
- Limitation: Task validity changes with websites; pin the task list and submission schema.

### VisualWebArena

- ID: `visualwebarena`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/web-arena-x/visualwebarena
- Summary: Adds visually grounded tasks to realistic web environments.
- Signals: `tools`, `vision`, `state`, `verification`
- Grading: Functional task evaluation
- Environment: Browser with screenshots and self-hosted sites
- Limitation: Visual observations and action interfaces must match across runs.

### WebArena

- ID: `webarena`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/web-arena-x/webarena
- Summary: Evaluates autonomous workflows on self-hosted web applications.
- Signals: `tools`, `state`, `planning`, `verification`
- Grading: Functional web-state checks
- Environment: Self-hosted sites and browser
- Limitation: Environment setup and task/evaluator fixes must be pinned.

### WebArena-Verified

- ID: `webarena-verified`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/ServiceNow/webarena-verified
- Summary: Revisits WebArena tasks and evaluation for reproducible browser-agent testing.
- Signals: `tools`, `state`, `verification`
- Grading: Revised functional evaluation
- Environment: Self-hosted web environments
- Limitation: Derivative of WebArena; do not count overlapping tasks as independent evidence.

### WebChoreArena

- ID: `webchorearena`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/WebChoreArena/WebChoreArena
- Summary: Stresses long, repetitive and memory-intensive web workflows.
- Signals: `tools`, `planning`, `context`, `state`
- Grading: Task-specific web evaluators
- Environment: WebArena-derived environments
- Limitation: Shared infrastructure is not an independent measure of deployment reliability.

### WebVoyager

- ID: `webvoyager`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/MinorJerry/WebVoyager
- Summary: Evaluates browser agents on tasks across live websites.
- Signals: `tools`, `vision`, `planning`
- Grading: Trajectory/screenshot-based task evaluation
- Environment: Live browser and internet
- Limitation: Website drift, access restrictions and evaluator reliability affect repeatability.

### WorkArena / WorkArena++

- ID: `workarena`
- Category: `browser`; kind: `benchmark`
- Source: https://github.com/ServiceNow/WorkArena
- Summary: Tests enterprise browser work and compositional knowledge-work tasks.
- Signals: `tools`, `planning`, `state`, `verification`
- Grading: Task-specific enterprise state checks
- Environment: ServiceNow instances and browser
- Limitation: Requires platform access; levels and composed tasks must be reported separately.

### Aider Polyglot

- ID: `aider-polyglot`
- Category: `coding`; kind: `benchmark`
- Source: https://aider.chat/docs/leaderboards/
- Summary: Tests editing and repair on coding exercises across languages.
- Signals: `tools`, `verification`, `cost`
- Grading: Exercise test suites
- Environment: Aider benchmark environments
- Limitation: Compact coding exercises; harness edit format and retry allowance strongly affect interpretation.

### Commit0

- ID: `commit0`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/commit-0/commit0
- Summary: Evaluates implementing software libraries from specifications and tests.
- Signals: `planning`, `context`, `verification`
- Grading: Library tests
- Environment: Repository-scale Python environments
- Limitation: From-scratch implementation differs from maintaining an existing production repository.

### GitTaskBench

- ID: `gittaskbench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/QuantaAlpha/GitTaskBench
- Summary: Repo-level real-world tasks spanning repository understanding, setup, iterative fixing, and delivery.
- Signals: `tools`, `context`, `planning`, `recovery`, `verification`, `cost`
- Grading: Task success, patch quality, and cost-aware alpha metrics
- Environment: 54 fixed GitHub repositories and reproducible repository workspaces
- Limitation: Fixed repositories can age; repository access, dependencies, and task contamination must be tracked.

### MiHaCoBench

- ID: `mihacobench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/HangYu8123/MiHaCoBench
- Summary: Grades artifacts produced by configurable coding harnesses on Python tasks.
- Signals: `tools`, `planning`, `verification`
- Grading: Weighted independent pytest graders
- Environment: Python task workspaces
- Limitation: 95 tasks in README; largely constructed problems rather than a broad industrial issue sample.

### SWE-bench family

- ID: `swe-bench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/SWE-bench/SWE-bench
- Summary: Tests issue resolution in real repositories; includes Verified and other official tracks.
- Signals: `tools`, `context`, `verification`
- Grading: Fail-to-pass and regression tests
- Environment: Versioned repository containers
- Limitation: Tracks have different languages, task sets and evaluators; published scores are not interchangeable.
- Paper: https://www.swebench.com/

### SWE-bench Live

- ID: `swe-bench-live`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/microsoft/SWE-bench-Live
- Summary: Uses a refreshed issue-resolution task collection to study coding agents.
- Signals: `tools`, `context`, `verification`
- Grading: Executable repository tests
- Environment: Containerized repositories
- Limitation: Rolling datasets require an explicit snapshot and contamination checks.

### SWE-bench Pro

- ID: `swe-bench-pro`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/scaleapi/SWE-bench_Pro-os
- Summary: Evaluates longer repository-level software-engineering tasks.
- Signals: `tools`, `planning`, `context`, `verification`
- Grading: Repository test suites
- Environment: Docker task environments
- Limitation: Public and private sets must be distinguished; coverage differs from SWE-bench Verified.

### SWE-InfraBench

- ID: `swe-infrabench`
- Category: `coding`; kind: `benchmark`
- Source: https://arxiv.org/abs/2606.05249
- Summary: Tests incremental cloud infrastructure-code edits in the AWS CDK rather than greenfield generation.
- Signals: `tools`, `context`, `verification`, `recovery`
- Grading: Infrastructure-code test and patch correctness
- Environment: AWS CDK repository tasks and cloud-infrastructure code
- Limitation: Narrow AWS CDK scope and dataset distribution constraints limit generalization.

### SWE-Lancer

- ID: `swe-lancer`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/openai/SWELancer-Benchmark
- Summary: Tests economically grounded freelance engineering and managerial decisions.
- Signals: `tools`, `planning`, `verification`
- Grading: Task-specific end-to-end grading
- Environment: Repository and application environments
- Limitation: Task value is not a universal productivity measure; manager and implementation tracks differ.

### SWE-rebench

- ID: `swe-rebench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/SWE-rebench/SWE-rebench-V2
- Summary: Provides continuously collected, reproducible software issue tasks.
- Signals: `tools`, `context`, `verification`
- Grading: Repository test outcomes
- Environment: Docker repositories
- Limitation: Freeze release and task IDs; the changing task distribution affects trend comparisons.

### Terminal-Bench

- ID: `terminal-bench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/harbor-framework/terminal-bench
- Summary: Evaluates difficult terminal workflows through executable environment checks.
- Signals: `tools`, `planning`, `recovery`, `verification`, `cost`
- Grading: Task-specific executable verifiers
- Environment: Containerized terminal environments
- Limitation: Pin a dataset release; task scores combine model and harness effects.
- Paper: https://arxiv.org/abs/2601.11868

### Version Control Bench

- ID: `version-control-bench`
- Category: `coding`; kind: `benchmark`
- Source: https://github.com/gitbutlerapp/version-control-bench
- Summary: Benchmarks agents on version-control tasks using Git, Jujutsu, and GitButler workflows.
- Signals: `tools`, `state`, `recovery`, `verification`
- Grading: Repository state and version-control outcome checks
- Environment: Local repositories with multiple version-control backends
- Limitation: Tool semantics differ across backends; task coverage is narrower than general software engineering.

### AndroidLab

- ID: `androidlab`
- Category: `computer`; kind: `benchmark`
- Source: https://github.com/THUDM/Android-Lab
- Summary: Provides Android interaction tasks and agent evaluation tooling.
- Signals: `tools`, `vision`, `state`
- Grading: Task-specific mobile evaluation
- Environment: Android emulator and applications
- Limitation: Platform-specific control; scores do not transfer directly to desktop or web.

### AndroidWorld

- ID: `androidworld`
- Category: `computer`; kind: `benchmark`
- Source: https://github.com/google-research/android_world
- Summary: Evaluates agents on parameterized tasks in Android apps.
- Signals: `tools`, `vision`, `state`, `verification`
- Grading: Programmatic app-state validation
- Environment: Android emulator
- Limitation: Device, app versions and generated task parameters must be fixed.

### OSWorld / OSWorld-Verified

- ID: `osworld`
- Category: `computer`; kind: `benchmark`
- Source: https://github.com/xlang-ai/OSWorld
- Summary: Evaluates multi-application desktop work in real operating systems.
- Signals: `tools`, `vision`, `state`, `verification`
- Grading: Execution-based task checks
- Environment: Virtual machines with desktop applications
- Limitation: VM images, step budgets and benchmark revisions must match; check newer versions upstream.
- Paper: https://os-world.github.io/

### SpreadsheetBench

- ID: `spreadsheetbench`
- Category: `computer`; kind: `benchmark`
- Source: https://github.com/Reality2byte/spreadsheetbench
- Summary: Evaluates real-world spreadsheet manipulation with multi-test-case online-judge style grading.
- Signals: `tools`, `verification`, `context`, `vision`
- Grading: Workbook outputs compared over multiple recalculated test cases
- Environment: Excel workbooks and code-execution agents
- Limitation: Office engines, formula recalculation, and platform differences can change results.

### SpreadsheetBench 2

- ID: `spreadsheetbench-2`
- Category: `computer`; kind: `benchmark`
- Source: https://spreadsheetbench.github.io/
- Summary: Workflow-level spreadsheet benchmark covering generation, debugging, and visualization in business workbooks.
- Signals: `tools`, `state`, `verification`, `vision`
- Grading: End-to-end workbook task outcomes with official evaluation code
- Environment: Complex multi-sheet business spreadsheets and multi-turn agents
- Limitation: A new release with complementary product baselines; version and submission status matter.
- Paper: https://arxiv.org/abs/2606.29955

### Windows Agent Arena

- ID: `windows-agent-arena`
- Category: `computer`; kind: `benchmark`
- Source: https://github.com/microsoft/WindowsAgentArena
- Summary: Adapts desktop-agent evaluation to Windows applications.
- Signals: `tools`, `vision`, `state`, `verification`
- Grading: OS/task state checks
- Environment: Windows virtual machines
- Limitation: Windows licensing and infrastructure requirements affect deployment cost.

### ClawBench (OpenClaw)

- ID: `clawbench-openclaw`
- Category: `direct`; kind: `benchmark`
- Source: https://github.com/openclaw/clawbench
- Summary: Scores full-stack configurations using traces and reliability diagnostics.
- Signals: `tools`, `state`, `recovery`, `cost`
- Grading: Trace scoring and repeated-run diagnostics
- Environment: OpenClaw-oriented task runner
- Limitation: Small curated task set; distinct from the TIGER-AI-Lab live-web benchmark.

### Coding harness comparison (tufantunc)

- ID: `tufantunc-harness`
- Category: `direct`; kind: `study`
- Source: https://github.com/tufantunc/harness-benchmark
- Summary: Adapts Aider Polyglot tasks for same-model coding harness comparisons.
- Signals: `tools`, `verification`, `cost`
- Grading: Polyglot tests through Inspect AI
- Environment: Docker and coding CLIs
- Limitation: A workload adapter and study; not a new independent task corpus.

### Harness Arena

- ID: `harness-arena`
- Category: `direct`; kind: `infrastructure`
- Source: https://github.com/Ondemand-OSS/harness-arena
- Summary: Runs blind pairwise comparisons of harness outputs.
- Signals: `tools`, `cost`
- Grading: Human preference and Elo aggregation
- Environment: Isolated agent runs; web service
- Limitation: Preference ranking does not establish functional correctness; model matching must be enforced.

### harness-bench (LamaSu)

- ID: `lamasu-harness`
- Category: `direct`; kind: `watchlist`
- Source: https://github.com/LamaSu/harness-bench
- Summary: Proposes component ablations across control, tools, memory, subagents and verification.
- Signals: `planning`, `tools`, `memory`, `multi-agent`, `permissions`, `verification`
- Grading: Inspect-based task and ablation design
- Environment: Inspect AI adapters
- Limitation: README advertises 37 ablation arms; adapter completeness and empirical results require inspection.

### Harness-Bench (Qihoo360)

- ID: `harness-bench-qihoo`
- Category: `direct`; kind: `benchmark`
- Source: https://github.com/Qihoo360/harness-bench
- Summary: Compares native model–harness configurations on offline workspace workflows.
- Signals: `tools`, `context`, `state`, `recovery`, `verification`, `cost`
- Grading: Artifact oracles plus LLM process rubrics
- Environment: Local workspaces; provider access
- Limitation: Public code and paper snapshot differ in adapter inventory; composite scores depend on the judge.
- Paper: https://arxiv.org/abs/2605.27922

### harness-bench (zenixos)

- ID: `zenixos-harness`
- Category: `direct`; kind: `watchlist`
- Source: https://github.com/zenixos/harness-bench
- Summary: Proposes a fixed-model comparison of coding CLIs on SWE-bench.
- Signals: `tools`, `context`, `cost`
- Grading: Official SWE-bench evaluator; paired statistics planned
- Environment: Docker and a frozen pilot split
- Limitation: README explicitly says scored runs and paper are TBD; do not treat planned results as measured.

### HarnessDev

- ID: `harness-dev`
- Category: `direct`; kind: `benchmark`
- Source: https://arxiv.org/abs/2609.01437
- Summary: Evaluates creation and iterative evolution of runnable agent infrastructure.
- Signals: `construction`, `tools`, `context`, `verification`
- Grading: Downstream performance of constructed harnesses
- Environment: Seed infrastructure and held-out task environments
- Limitation: Measures a developer agent's construction ability; code availability needs separate verification.

### Hyper-τ / τ^τ-bench

- ID: `hyper-tau`
- Category: `direct`; kind: `benchmark`
- Source: https://github.com/sierra-research/hyper-tau-bench
- Summary: Builds customer-service agents from realistic evidence and scores their held-out performance.
- Signals: `construction`, `tools`, `state`, `verification`
- Grading: Built agent's success on τ³ tasks
- Environment: Pinned Docker construction kit; model APIs
- Limitation: 53 release contracts in README; distinguish developer model from the model in the submitted agent.

### Nexus Harness Benchmark

- ID: `nexus-harness`
- Category: `direct`; kind: `benchmark`
- Source: https://github.com/nexus-research-lab/nexus-harness-benchmark
- Summary: Tests workspace delivery using executable contracts and recorded evidence.
- Signals: `tools`, `state`, `recovery`, `permissions`, `verification`, `cost`
- Grading: Deterministic checks; optional qualitative review
- Environment: Isolated workspaces
- Limitation: Community project; task coverage and independent reproduction need further validation.

### Same-model harness study (d1-m4ss)

- ID: `d1-harness`
- Category: `direct`; kind: `study`
- Source: https://github.com/d1-m4ss/harness-benchmark
- Summary: Compares coding harnesses with shared underlying models.
- Signals: `tools`, `context`, `cost`
- Grading: Task correctness plus runtime and usage
- Environment: CLI agents and shared tasks
- Limitation: Small author-run study; task and configuration choices limit generalization.

### Same-model harness study (rajshah4)

- ID: `rajshah-harness`
- Category: `direct`; kind: `study`
- Source: https://github.com/rajshah4/harness-benchmark
- Summary: Publishes task verifiers, token ledgers and comparison artifacts for coding agents.
- Signals: `tools`, `verification`, `cost`
- Grading: Task verifiers and provider accounting
- Environment: CLI agents
- Limitation: Model-bound control must be separated from same-model comparisons.

### ShellBench

- ID: `shellbench`
- Category: `direct`; kind: `benchmark`
- Source: https://github.com/openclaw/shellbench
- Summary: Scores the full agent stack—harness, configuration, and model—with trace-based reliability diagnostics.
- Signals: `tools`, `verification`, `recovery`, `cost`, `state`
- Grading: Trace-aware task outcomes, reliability metrics, and configuration diagnostics
- Environment: Containerized coding and agent workflow tasks
- Limitation: A fast-moving project; benchmark versions and model/harness coupling must be recorded.

### AgentBench

- ID: `agentbench`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/THUDM/AgentBench
- Summary: Evaluates agents across heterogeneous interactive environments.
- Signals: `tools`, `planning`, `state`
- Grading: Environment-specific rewards and success
- Environment: Multiple environment backends
- Limitation: Aggregate scores mix different action spaces and task distributions.

### AgentIF

- ID: `agentif`
- Category: `general`; kind: `benchmark`
- Source: https://agentif.github.io/
- Summary: Measures instruction following under long, complex, constraint-rich agent prompts and tool specifications.
- Signals: `context`, `tools`, `permissions`, `verification`
- Grading: Code, LLM, and hybrid constraint-level evaluation
- Environment: Instructions collected from 50 real-world agent applications
- Limitation: Instruction-following is only one layer of end-to-end agent competence; synthetic task construction remains a factor.
- Paper: https://arxiv.org/abs/2505.16944

### AgentSearchBench

- ID: `agent-search-bench`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/Bingo-W/AgentSearchBench
- Summary: Evaluates retrieval and reranking of real-world agents using execution-grounded relevance.
- Signals: `tools`, `retrieval`, `planning`, `multi-agent`
- Grading: NDCG, completeness, and execution-grounded relevance
- Environment: Agent catalog and execution traces from multiple providers
- Limitation: Provider coverage, agent availability, and execution costs can change the candidate pool.
- Paper: https://arxiv.org/abs/2604.22436

### APEX-Agents / Archipelago

- ID: `apex-agents-archipelago`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/togethercomputer/archipelago
- Summary: Evaluates agents on professional-services tasks through MCP environments, runners, and snapshot grading.
- Signals: `tools`, `state`, `planning`, `verification`, `cost`
- Grading: Before/after snapshot graders with optional trajectory signals
- Environment: Dockerized MCP applications and professional-services workspaces
- Limitation: LLM-graded trajectory signals are evolving and professional task access is controlled.
- Paper: https://arxiv.org/abs/2601.14242

### AssistantBench

- ID: `assistantbench`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/oriyor/assistantbench
- Summary: Tests practical information-seeking tasks for web assistants.
- Signals: `tools`, `planning`
- Grading: Answer-level evaluation
- Environment: Web browsing and search
- Limitation: Answer correctness is a useful proxy but does not certify workspace or side-effect correctness.

### Claw-Eval

- ID: `claw-eval`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/claw-eval/claw-eval
- Summary: Evaluates general, multimodal and multi-turn agent tasks.
- Signals: `tools`, `vision`, `interaction`, `permissions`, `verification`
- Grading: Trajectory rubrics; completion, safety and consistency
- Environment: Sandbox plus service/web dependencies
- Limitation: Author README discloses API-error reruns; report retry policy and grader versions.

### Claw-Eval-Live

- ID: `claw-eval-live`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/Claw-Eval-Live/Claw-Eval-Live
- Summary: Builds evolving workflow tests from marketplace demand signals.
- Signals: `tools`, `skills`, `verification`
- Grading: Workflow-specific evaluation
- Environment: Task-specific services
- Limitation: Moving corpus requires snapshot IDs; distinct from static Claw-Eval results.

### GAIA

- ID: `gaia`
- Category: `general`; kind: `benchmark`
- Source: https://huggingface.co/datasets/gaia-benchmark/GAIA
- Summary: Tests tool-assisted information gathering and multimodal reasoning.
- Signals: `tools`, `planning`, `vision`
- Grading: Final-answer accuracy
- Environment: Web, files and selected tools
- Limitation: Final answers reveal less about intermediate side effects and execution safety.
- Paper: https://arxiv.org/abs/2311.12983

### OmniaBench

- ID: `omnia-bench`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/scuuy/OmniaBench
- Summary: Broad diagnostic evaluation of general-purpose agents across diverse tasks and environments.
- Signals: `tools`, `planning`, `state`, `verification`, `cost`
- Grading: Task success and aggregate diagnostic metrics
- Environment: Mixed agent tasks with released full and challenging subsets
- Limitation: Heterogeneous environments make a single aggregate less diagnostic than per-family scores.
- Paper: https://arxiv.org/abs/2607.14989

### PinchBench

- ID: `pinchbench`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/pinchbench/skill
- Summary: Evaluates models running as OpenClaw agents on practical assistant tasks.
- Signals: `tools`, `planning`, `verification`
- Grading: Task-specific grading
- Environment: OpenClaw runtime
- Limitation: Default setup holds one harness fixed; cross-harness use requires an explicit adapter.

### TheAgentCompany

- ID: `theagentcompany`
- Category: `general`; kind: `benchmark`
- Source: https://github.com/TheAgentCompany/TheAgentCompany
- Summary: Simulates digital workplace tasks with apps, files and coworkers.
- Signals: `tools`, `planning`, `interaction`, `verification`
- Grading: Task and intermediate checkpoint grading
- Environment: Self-hosted workplace services
- Limitation: Large setup; simulated coworkers and partial-credit definitions affect results.

### AgentRace

- ID: `agent-race`
- Category: `infrastructure`; kind: `study`
- Source: https://agent-race.github.io/paper
- Summary: Controlled comparison of LLM agent frameworks on runtime, scalability, communication, and tool latency.
- Signals: `tools`, `cost`, `multi-agent`, `recovery`
- Grading: Runtime performance, scalability, communication overhead, and tool latency
- Environment: Representative workloads across popular agent frameworks
- Limitation: Paper and release snapshots may not track framework versions at the same pace.

### AgentSuite

- ID: `agentsuite`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/Agent-Suite/AgentSuite
- Summary: One-touch platform for running agent benchmarks with component audits and benchmark variants.
- Signals: `tools`, `verification`, `cost`, `recovery`
- Grading: Delegates to selected benchmark implementations and audit checks
- Environment: Configurable benchmark runners and agent adapters
- Limitation: A runner and auditing layer; it does not make underlying task suites interchangeable.

### BrowserGym

- ID: `browsergym`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/ServiceNow/BrowserGym
- Summary: Provides a shared interface for browser-agent environments.
- Signals: `tools`, `vision`, `state`
- Grading: Underlying browser benchmark evaluators
- Environment: Browser environments
- Limitation: Common API does not make different task suites or observation settings comparable.

### Coder Eval

- ID: `coder-eval`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/UiPath/coder_eval
- Summary: Agent-agnostic sandbox and YAML task framework for coding-agent, skill, and CI regression evaluation.
- Signals: `tools`, `verification`, `skills`, `cost`, `recovery`
- Grading: Weighted criteria, activation checks, artifacts, and telemetry
- Environment: Sandboxed coding agents including Claude Code, Codex, Gemini, OpenCode, and Pi
- Limitation: Bring-your-own tasks and scorers; local suites are not directly comparable without shared fixtures.

### Harbor

- ID: `harbor`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/harbor-framework/harbor
- Summary: Runs agent evaluations across versioned sandbox environments and datasets.
- Signals: `tools`, `verification`, `cost`
- Grading: Delegates scoring to selected benchmark
- Environment: Containers and remote sandbox providers
- Limitation: An evaluation platform, not an independent benchmark score.

### Holistic Agent Leaderboard (HAL)

- ID: `hal`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://hal.cs.princeton.edu/
- Summary: Compares agents using reproducible, cost-aware evaluation across tasks.
- Signals: `cost`, `verification`
- Grading: Benchmark scores and cost-aware comparisons
- Environment: Multiple task suites
- Limitation: Cross-benchmark cost and success must retain original units and configurations.
- Paper: https://arxiv.org/abs/2510.11977

### InfraBench

- ID: `infra-bench`
- Category: `infrastructure`; kind: `benchmark`
- Source: https://github.com/kubeply/infra-bench
- Summary: Runs realistic Kubernetes and infrastructure tasks with Harbor-compatible sandboxes.
- Signals: `tools`, `state`, `recovery`, `permissions`, `verification`
- Grading: Task verifiers over infrastructure state and command outcomes
- Environment: Ephemeral Kubernetes and infrastructure environments
- Limitation: Terraform and observability tracks are still expanding; cluster setup can dominate run cost.
- Paper: https://arxiv.org/abs/2608.11234

### Inspect Evals

- ID: `inspect-evals`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/UKGovernmentBEIS/inspect_evals
- Summary: Collects reproducible evaluation implementations for Inspect AI.
- Signals: `tools`, `verification`, `permissions`
- Grading: Benchmark-dependent scorers
- Environment: Inspect solvers and sandboxes
- Limitation: Preserve upstream task and scorer versions; collection entries are not all harness benchmarks.

### Lemans

- ID: `lemans`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/rails/lemans
- Summary: Ruby CLI harness for reproducible coding-agent benchmarks with Docker or Daytona sandboxes.
- Signals: `tools`, `verification`, `recovery`, `cost`
- Grading: Task verifier and digest-backed result reports
- Environment: Docker or Daytona coding sandboxes
- Limitation: Execution layer rather than a fixed task suite; benchmark quality depends on user-authored tasks.

### NeMo Gym

- ID: `nemo-gym`
- Category: `infrastructure`; kind: `infrastructure`
- Source: https://github.com/NVIDIA-NeMo/Gym
- Summary: Supports composable environments and configurable agent evaluation.
- Signals: `tools`, `verification`, `cost`
- Grading: Environment-specific rewards
- Environment: Configured agent and environment services
- Limitation: Harness comparison requires fixed model, dataset, environment and repeat count.
- Paper: https://docs.nvidia.com/nemo/gym/evaluation/harness/

### Open AgentBench

- ID: `open-agentbench`
- Category: `infrastructure`; kind: `benchmark`
- Source: https://github.com/the-open-agent/agentbench
- Summary: Runtime benchmark for agent performance, dialogue, tools, startup, memory, throughput, and reliability.
- Signals: `tools`, `memory`, `cost`, `recovery`, `state`
- Grading: Suite-specific functional, latency, throughput, and consistency metrics
- Environment: OpenClaw, OpenAgent, Hermes, and compatible agent runtimes
- Limitation: Runtime-specific adapters and a young leaderboard limit cross-harness comparability.

### AgentIF-OneDay

- ID: `agentif-oneday`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/xbench-ai/AgentIF-OneDay
- Summary: Tests daily work, life, and study workflows with attachments, latent instructions, and iterative refinement.
- Signals: `context`, `planning`, `state`, `verification`, `vision`
- Grading: Instance rubrics combining LLM verification and human alignment
- Environment: Multimodal daily scenarios with file-based deliverables
- Limitation: Many tasks depend on subjective rubric judgments and long-horizon context management.
- Paper: https://arxiv.org/abs/2601.20613

### AOBench (Agent Operations Benchmark)

- ID: `aobench`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/MSKazemi/aobench
- Summary: Role-aware, permission-enforced evaluation of agents operating HPC systems and facilities.
- Signals: `tools`, `permissions`, `state`, `verification`, `recovery`
- Grading: Trace-scored task outcomes with hard-fail policy violations
- Environment: Deterministic HPC operational environments, SLURM, telemetry, and RBAC
- Limitation: Deterministic facility snapshots cannot cover every live-cluster failure mode.

### Claw-Anything

- ID: `claw-anything`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/LiberCoders/Claw-Anything
- Summary: Evaluates always-on assistants with broad access to a user's digital environment.
- Signals: `tools`, `state`, `memory`, `interaction`
- Grading: Generated tasks and task-specific graders
- Environment: Simulated personal digital environment
- Limitation: Construction pipeline and verification level vary; preserve task provenance.

### ClawMark

- ID: `clawmark`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/evolvent-ai/ClawMark
- Summary: Tests multi-turn, multi-day, multimodal coworker behavior in an evolving world.
- Signals: `state`, `memory`, `interaction`, `vision`
- Grading: Task and world-state evaluation
- Environment: Living-world simulation
- Limitation: Multi-day simulated workloads are not evidence of uninterrupted production uptime.

### Durable-agent-harness

- ID: `durable-harness`
- Category: `long-horizon`; kind: `study`
- Source: https://github.com/Eldergenix/Durable-agent-harness
- Summary: Uses controlled simulations to ablate memory, checkpoints and recovery logic.
- Signals: `memory`, `state`, `recovery`, `cost`
- Grading: Machine-graded simulation outcomes and paired experiments
- Environment: Deterministic simulation; optional live provider
- Limitation: Simulation evidence must not be reported as full real-agent deployment reliability.

### Gaia2 / Gaia2-CLI

- ID: `gaia2`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/facebookresearch/meta-agents-research-environments
- Summary: Tests dynamic environments, temporal constraints, ambiguity and asynchronous events.
- Signals: `tools`, `state`, `interaction`, `multi-agent`, `recovery`
- Grading: Write-action verifier
- Environment: Agents Research Environments; CLI variant
- Limitation: Variants change the action interface; the simulated clock is not ordinary wall-clock runtime.
- Paper: https://arxiv.org/abs/2602.11964

### METR Task-Completion Time Horizons

- ID: `metr-horizon`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://metr.org/time-horizons/
- Summary: Estimates task difficulty in human-time units at a chosen agent success threshold.
- Signals: `planning`, `tools`, `verification`
- Grading: Success curve fitted to human task duration
- Environment: Software, ML and cybersecurity tasks
- Limitation: Human-equivalent horizon is not how long an agent runs; full task access is limited.

### SentinelBench

- ID: `sentinelbench`
- Category: `long-horizon`; kind: `benchmark`
- Source: https://github.com/microsoft/sentinel_environments
- Summary: Tests monitoring agents reacting to events over extended timelines.
- Signals: `state`, `interaction`, `planning`
- Grading: Server-side environment state checks
- Environment: Synthetic web environments and event streams
- Limitation: Monitor performance depends on clock, wake-up policy and event schedule.

### Context-Bench (Letta, V2)

- ID: `context-bench-letta`
- Category: `memory`; kind: `benchmark`
- Source: https://www.letta.com/blog/evaluating-memory-in-production-agents/
- Summary: Tests file navigation and relationship tracing under context constraints.
- Signals: `context`, `tools`, `planning`
- Grading: Answer and file-operation task evaluation
- Environment: File-based task environments
- Limitation: Distinct from code-context retrieval benchmarks with similar names.

### ContextBench (coding retrieval)

- ID: `contextbench-code`
- Category: `memory`; kind: `benchmark`
- Source: https://arxiv.org/abs/2602.05892
- Summary: Evaluates the context gathered by coding agents from repositories.
- Signals: `context`, `tools`
- Grading: Context-retrieval evaluation
- Environment: Repository retrieval tasks
- Limitation: Retrieval quality is a component metric; code-fix success needs separate tests.

### LoCoMo

- ID: `locomo`
- Category: `memory`; kind: `benchmark`
- Source: https://github.com/snap-research/locomo
- Summary: Tests long-term conversational memory over extended dialogue histories.
- Signals: `memory`, `context`
- Grading: QA and task-specific language metrics
- Environment: Recorded/generated conversation histories
- Limitation: Small conversation sample and judge choice limit broad memory-system conclusions.

### LongMemEval

- ID: `longmemeval`
- Category: `memory`; kind: `benchmark`
- Source: https://github.com/xiaowu0162/LongMemEval
- Summary: Tests information extraction, temporal reasoning and updates across long histories.
- Signals: `memory`, `context`
- Grading: Question-answering accuracy
- Environment: Stored conversational histories
- Limitation: Full-context baselines are essential; QA retrieval is not closed-loop task execution.

### LongMemEval-V2

- ID: `longmemeval-v2`
- Category: `memory`; kind: `benchmark`
- Source: https://github.com/xiaowu0162/LongMemEval-V2
- Summary: Tests experience retrieval from long histories of multimodal agent trajectories.
- Signals: `memory`, `context`, `vision`, `cost`
- Grading: Answer accuracy and query latency
- Environment: Stored web and enterprise trajectories
- Limitation: Measures evidence retrieval for downstream QA; not end-to-end repeated task completion.

### MemoryAgentBench

- ID: `memoryagentbench`
- Category: `memory`; kind: `benchmark`
- Source: https://github.com/HUST-AI-HYZ/MemoryAgentBench
- Summary: Tests incremental memory through retrieval, learning, understanding and forgetting.
- Signals: `memory`, `context`
- Grading: Task-specific accuracy
- Environment: Incrementally delivered text streams
- Limitation: Different subsets probe different operations; aggregates hide trade-offs.

### MemoryArena

- ID: `memoryarena`
- Category: `memory`; kind: `benchmark`
- Source: https://github.com/ZexueHe/MemoryArena
- Summary: Tests memory within interdependent tasks spread across agent sessions.
- Signals: `memory`, `state`, `planning`
- Grading: Domain-specific task success
- Environment: Memory–agent–environment loops
- Limitation: Setup and external domain dependencies need verification; stronger task signal than QA alone.

### MAS-FIRE

- ID: `mas-fire`
- Category: `multi-agent`; kind: `benchmark`
- Source: https://arxiv.org/abs/2602.19843
- Summary: Injects faults to evaluate reliability of multi-agent systems.
- Signals: `multi-agent`, `recovery`, `state`
- Grading: Fault detection and reliability evaluation
- Environment: Multi-agent frameworks
- Limitation: Fault model and intervention point are part of the treatment.

### MultiAgentBench

- ID: `multiagentbench`
- Category: `multi-agent`; kind: `benchmark`
- Source: https://github.com/MultiagentBench/MARBLE
- Summary: Evaluates collaboration across multi-agent tasks and coordination patterns.
- Signals: `multi-agent`, `planning`, `interaction`
- Grading: Task and collaboration evaluation
- Environment: MARBLE environments
- Limitation: Agent count, communication budgets and task decomposition must be controlled.

### OrchestraBench

- ID: `orchestrabench`
- Category: `multi-agent`; kind: `benchmark`
- Source: https://arxiv.org/abs/2608.05263
- Summary: Uses controlled faults to diagnose routing, recovery and failure cascades.
- Signals: `multi-agent`, `recovery`, `state`
- Grading: Cascade radius and per-mode recovery
- Environment: Templated workflows and controlled mechanism probes
- Limitation: Small controlled probes; do not extrapolate measured recovery to all business workflows.

### SABOT

- ID: `sabot`
- Category: `multi-agent`; kind: `study`
- Source: https://github.com/Jott2121/sabot
- Summary: Tests whether pipeline-native checks detect planted faults.
- Signals: `multi-agent`, `recovery`, `verification`
- Grading: Fault-detection outcomes and traces
- Environment: Framework-specific fault-injection experiments
- Limitation: Author-reported study; distinguish native detection from external adjudication.

### AgentActionBench

- ID: `agent-action-bench`
- Category: `research`; kind: `benchmark`
- Source: https://arxiv.org/abs/2609.11117
- Summary: Process-oriented evaluation of agents reproducing experiments from ML and AI-for-science papers.
- Signals: `tools`, `planning`, `verification`, `recovery`
- Grading: Paper-specific trace rubrics with human-validated rubric augmentation
- Environment: MCP-recorded experiment reproduction workflows
- Limitation: Newest shared-task release; public code and scoring details may continue changing.

### AgentRE-Bench

- ID: `agentre-bench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/agentrebench/AgentRE-Bench
- Summary: Measures long-horizon reverse engineering of unseen binaries with constrained tools and evidence capture.
- Signals: `tools`, `planning`, `verification`, `recovery`
- Grading: Deterministic expert-grounded claims, coverage, and tool-use metrics
- Environment: Isolated Linux and Windows binary workspaces without source code
- Limitation: Versioned binary ladders are not directly comparable across major releases.

### AIRS-Bench

- ID: `airs-bench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/facebookresearch/airs-bench
- Summary: Measures end-to-end AI research ability through open-ended research-science tasks.
- Signals: `tools`, `planning`, `verification`, `cost`
- Grading: Normalized task scores with multi-seed leaderboard reporting
- Environment: Research workflows with code, data, and experiment artifacts
- Limitation: Open-ended research quality and expensive model calls make scores judge- and budget-sensitive.
- Paper: https://arxiv.org/abs/2602.06855

### CORE-Bench

- ID: `core-bench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/siegelz/core-bench
- Summary: Tests computational reproduction using scientific code and artifacts.
- Signals: `tools`, `context`, `recovery`, `verification`
- Grading: Reproduction task answers and artifacts
- Environment: Scientific repositories and containers
- Limitation: Availability of original artifacts and environment drift constrain repeatability.

### MLE-bench

- ID: `mle-bench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/openai/mle-bench
- Summary: Evaluates autonomous ML engineering on competition tasks.
- Signals: `tools`, `planning`, `verification`, `cost`
- Grading: Competition-specific held-out metrics
- Environment: Data, containers and often GPUs
- Limitation: Hardware, runtime and access to prior solutions are major controls.

### PaperBench

- ID: `paperbench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/openai/preparedness
- Summary: Tests whether agents can reproduce 20 ICML 2024 research papers from scratch.
- Signals: `tools`, `planning`, `verification`, `cost`
- Grading: Hierarchical paper-specific rubrics over reproduced code and experiments
- Environment: Three-stage containerized rollout, reproduction, and grading pipeline
- Limitation: GPU, data, and judge costs are high; rubric-based grading remains partially model-assisted.
- Paper: https://arxiv.org/abs/2504.01848

### RE-Bench

- ID: `re-bench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/METR/RE-Bench
- Summary: Tests AI research engineering against human baselines.
- Signals: `tools`, `planning`, `verification`, `cost`
- Grading: Task-specific objective scores
- Environment: Research engineering environments
- Limitation: Small expert task collection; time and compute budgets affect comparisons.

### SciAgentArena

- ID: `sciagentarena`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/HelloWorldLTY/SciAgentArena
- Summary: Evaluates scientific agents across biomedical and multi-omics workflows with stepwise scoring.
- Signals: `tools`, `planning`, `verification`, `multi-agent`
- Grading: Automated domain-specific scores and execution outputs
- Environment: Scientific Python workflows across seven benchmark families
- Limitation: Domain packages and scientific validity are difficult to reproduce outside the pinned environments.
- Paper: https://arxiv.org/abs/2606.12736

### ScienceAgentBench

- ID: `scienceagentbench`
- Category: `research`; kind: `benchmark`
- Source: https://github.com/OSU-NLP-Group/ScienceAgentBench
- Summary: Evaluates executable programs for data-driven scientific tasks.
- Signals: `tools`, `planning`, `verification`
- Grading: Program execution and scientific task metrics
- Environment: Scientific datasets and Python environments
- Limitation: Scientific validity extends beyond passing the benchmark's tests.

### Agent-SafetyBench

- ID: `agent-safetybench`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/thu-coai/Agent-SafetyBench
- Summary: Evaluates safety behavior in interactive agent environments.
- Signals: `permissions`, `tools`, `interaction`
- Grading: Scenario-specific safety evaluation
- Environment: Simulated tool environments
- Limitation: Safety taxonomy and judge dependence need disclosure alongside usefulness.

### AgentDojo

- ID: `agentdojo`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/ethz-spylab/agentdojo
- Summary: Tests prompt-injection attacks and defenses in stateful tool environments.
- Signals: `permissions`, `tools`, `state`
- Grading: Benign utility and attack success
- Environment: Simulated tools with adversarial external data
- Limitation: Threat model and attack budget must be held constant; utility must accompany safety.

### AgentHarm

- ID: `agentharm`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/UKGovernmentBEIS/inspect_evals
- Summary: Tests whether agents execute harmful multi-step requests.
- Signals: `permissions`, `tools`
- Grading: Harmful task completion and refusal evaluation
- Environment: Inspect Evals agentharm tasks
- Limitation: Distinct from indirect prompt injection; suite repository contains many unrelated evals.
- Paper: https://arxiv.org/abs/2410.09024

### AgentShield Benchmark

- ID: `agentshield-benchmark`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/doronp/agentshield-benchmark
- Summary: Tests agent-security tools against prompt injection, exfiltration, tool abuse, and provenance threats.
- Signals: `permissions`, `tools`, `verification`, `recovery`
- Grading: Attack success, detection, and policy-violation metrics
- Environment: Isolated adversarial tool and provenance scenarios
- Limitation: Security coverage and attack realism evolve quickly; results are not a complete risk assessment.

### Cybench

- ID: `cybench`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/andyzorigin/cybench
- Summary: Evaluates cybersecurity agent capability and risk over multi-step Capture the Flag tasks.
- Signals: `tools`, `planning`, `recovery`, `permissions`
- Grading: Task and subtask completion across CTF challenge categories
- Environment: Containerized cybersecurity tasks and tool-using agent
- Limitation: Dual-use tasks require careful isolation; CTF performance does not equal production security.

### HarnessRisk

- ID: `harness-risk`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/Baiyajing/HarnessRisk
- Summary: Tests adversarial artifacts across six stages of the harness lifecycle.
- Signals: `permissions`, `memory`, `recovery`, `tools`
- Grading: Utility, attack success, persistence and detection
- Environment: Mock services and workspace; use OS isolation
- Limitation: 128 cases per paper; recognizing an attack is distinct from preventing its side effects.
- Paper: https://arxiv.org/abs/2608.17597

### InjecAgent

- ID: `injecagent`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/uiuc-kang-lab/InjecAgent
- Summary: Tests indirect prompt injections through tool outputs.
- Signals: `permissions`, `tools`
- Grading: Attack success checks
- Environment: Tool-response injection cases
- Limitation: Narrow attack setup; does not cover the entire permissions or persistence lifecycle.

### WASP

- ID: `wasp`
- Category: `safety`; kind: `benchmark`
- Source: https://github.com/facebookresearch/wasp
- Summary: Evaluates web-agent susceptibility to adversarial website content.
- Signals: `permissions`, `tools`, `vision`
- Grading: Attack success and task utility
- Environment: Adversarial web environments
- Limitation: Browser attack surface differs from API tool-response injection.

### SkillsBench

- ID: `skillsbench`
- Category: `skills`; kind: `benchmark`
- Source: https://github.com/benchflow-ai/skillsbench
- Summary: Measures the task-level contribution of reusable instruction and script packages.
- Signals: `skills`, `tools`, `verification`, `cost`
- Grading: Executable task verifiers; paired skill conditions
- Environment: Task-specific environments and coding agents
- Limitation: Version 1.1 differs from paper-v1; compare identical task and skill snapshots.
- Paper: https://www.skillsbench.ai/blogs/skillsbench-1-1

### SWE-Skills-Bench

- ID: `swe-skills-bench`
- Category: `skills`; kind: `benchmark`
- Source: https://arxiv.org/abs/2603.15401
- Summary: Studies the marginal utility of skills for software-engineering requirements.
- Signals: `skills`, `context`, `verification`
- Grading: Requirement-driven SWE evaluation
- Environment: Repository tasks
- Limitation: Paper accessible; the paper-linked GitHub repository returned 404 during this review.

### Agent-Diff

- ID: `agent-diff`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/agent-diff-bench/agent-diff
- Summary: Evaluates enterprise API agents in interactive sandboxes using state-diff grading.
- Signals: `tools`, `state`, `verification`, `permissions`
- Grading: Before/after state diffs and task-specific checks
- Environment: Slack, Linear, Box, and Google Calendar-style API sandboxes
- Limitation: Third-party API replicas and scenario coverage must be pinned for meaningful comparisons.
- Paper: https://arxiv.org/abs/2602.11224

### API-Bank

- ID: `api-bank`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/AlibabaResearch/DAMO-ConvAI
- Summary: Provides dialogue tasks involving API calling and planning.
- Signals: `tools`, `interaction`
- Grading: API-call and response evaluation
- Environment: API-Bank subdirectory in a multi-project repository
- Limitation: Inspect the API-Bank task split; repository-wide metadata is not benchmark-specific.

### AppWorld

- ID: `appworld`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/StonyBrookNLP/appworld
- Summary: Tests code-driven interactions with a simulated ecosystem of personal apps.
- Signals: `tools`, `state`, `planning`, `verification`
- Grading: Programmatic task and state checks
- Environment: Locally simulated app APIs
- Limitation: Requires adaptation to its API/code interface; final state checks have workload-specific scope.

### Berkeley Function Calling Leaderboard (BFCL)

- ID: `bfcl`
- Category: `tools`; kind: `benchmark`
- Source: https://gorilla.cs.berkeley.edu/leaderboard.html
- Summary: Diagnoses function selection, arguments and increasingly agentic multi-turn tool use.
- Signals: `tools`, `interaction`
- Grading: AST, execution and track-specific metrics
- Environment: Track-specific tool environments
- Limitation: Single-call tracks are component tests; the aggregate is not a full harness reliability score.

### Data Agent Benchmark (DAB)

- ID: `data-agent-benchmark`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/ucbepic/DataAgentBench
- Summary: Evaluates data agents on multi-database integration, joins, text transformation, and domain knowledge.
- Signals: `tools`, `context`, `state`, `verification`
- Grading: Task-level data correctness and leaderboard scoring
- Environment: Enterprise-style data workspaces and heterogeneous databases
- Limitation: Database connectors and hidden evaluation data must stay version-pinned for fair comparison.
- Paper: https://arxiv.org/abs/2603.20576

### DataSpace

- ID: `dataspace`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/HKUSTDial/DataSpace
- Summary: Tests verifiable analytics over heterogeneous workspaces containing structured and unstructured artifacts.
- Signals: `tools`, `context`, `state`, `verification`, `vision`
- Grading: Exact and semantic table comparison with type-aware checks
- Environment: CSV, JSON, SQLite, Markdown, PDF, and video workspaces
- Limitation: Large artifacts and multimodal dependencies make local reproduction resource-intensive.
- Paper: https://arxiv.org/abs/2608.03451

### Hermes tool-performance evals

- ID: `hermes-toolperf`
- Category: `tools`; kind: `study`
- Source: https://github.com/NousResearch/hermes-toolperf-evals
- Summary: Provides tool-efficiency regression cases for Hermes changes.
- Signals: `tools`, `recovery`, `cost`
- Grading: Tool-specific A/B checks and traces
- Environment: Hermes development environment
- Limitation: Vendor-specific regression suite; not a neutral cross-harness leaderboard.

### MCP-Bench (Accenture)

- ID: `mcp-bench`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/Accenture/mcp-bench
- Summary: Evaluates multi-step tasks over diverse MCP servers.
- Signals: `tools`, `planning`
- Grading: Task-level and tool-use evaluation
- Environment: MCP services and model endpoints
- Limitation: Live dependencies and scoring configuration influence comparability.

### MCPMark

- ID: `mcpmark`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/eval-sys/mcpmark
- Summary: Stress-tests task execution through real MCP services.
- Signals: `tools`, `state`, `verification`
- Grading: Service-specific task verifiers
- Environment: MCP servers; local or account-backed services
- Limitation: Freeze server versions and initial state; some services require dedicated accounts.

### StableToolBench

- ID: `stabletoolbench`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/THUNLP-MT/StableToolBench
- Summary: Adds virtualized and cached tools for more stable ToolBench-style evaluation.
- Signals: `tools`, `planning`
- Grading: StableToolEval and simulated execution
- Environment: Virtual API server
- Limitation: Simulator fidelity is a confounder; not identical to evaluation on live APIs.

### STATE-Bench

- ID: `state-bench`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/microsoft/STATE-Bench
- Summary: Evaluates multi-step enterprise travel, support, and shopping workflows with an optional learning track.
- Signals: `tools`, `state`, `memory`, `permissions`, `verification`
- Grading: Task completion pass@1, pass^5, UX, and cost per task
- Environment: Task-local enterprise databases, policy tools, and simulated users
- Limitation: Synthetic data and LLM-judged UX require careful interpretation alongside deterministic state checks.

### Toolathlon / Toolathlon-Verified

- ID: `toolathlon`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/hkust-nlp/Toolathlon
- Summary: Evaluates long workflows spanning many applications and tools.
- Signals: `tools`, `state`, `planning`, `verification`
- Grading: Dedicated execution-based evaluators
- Environment: Containers and application services
- Limitation: Verified release changes prompts and evaluators; distinguish local mocks from live service execution.

### ToolBench / ToolEval

- ID: `toolbench`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/OpenBMB/ToolBench
- Summary: Tests selecting and composing a large collection of external APIs.
- Signals: `tools`, `planning`
- Grading: ToolEval solution and preference judgments
- Environment: API-backed tool execution
- Limitation: Historical API availability and model-judge behavior can limit reproducibility.

### ToolSandbox

- ID: `toolsandbox`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/apple/ToolSandbox
- Summary: Tests conversational tool use with implicit state dependencies and missing information.
- Signals: `tools`, `state`, `interaction`, `recovery`
- Grading: Intermediate milestones and final state
- Environment: Stateful tool sandbox with user simulator
- Limitation: Measures deployed agent behavior; simulator and tool interface are experimental variables.

### τ-bench family (τ / τ² / τ³)

- ID: `tau-bench`
- Category: `tools`; kind: `benchmark`
- Source: https://github.com/sierra-research/tau2-bench
- Summary: Evaluates customer-service tool use, policy compliance and interactive coordination.
- Signals: `tools`, `state`, `interaction`, `verification`
- Grading: Domain state and task-specific evaluation
- Environment: User simulator and domain tools; voice optional
- Limitation: Repository name remains tau2-bench; τ³ task fixes and knowledge/voice tracks require version labels.
