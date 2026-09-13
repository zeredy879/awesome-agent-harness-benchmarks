# Research and comparison notes

This document explains how the inventory was assembled and how to choose a benchmark for a harness question.

## Scope and method

The snapshot date is 2026-09-13. The search covered benchmark papers and project pages, official GitHub repositories, benchmark leaderboards, and evaluation runners that expose at least one execution-layer responsibility. We included a workload when the agent changes a workspace, calls a tool, observes state, interacts over multiple turns, delegates, persists memory, or must obey an action policy. We included a study when the harness itself is the treatment or when its ablation protocol provides reusable evidence. We included infrastructure only when it makes harness swapping, sandboxing, verification, or trace collection practical.

Items with the same name are kept separate when their owner, environment, or scoring protocol differs. Examples include the OpenClaw, TIGER-AI-Lab, and other projects named ClawBench. A planned protocol is never promoted to a measured benchmark result. Private or unavailable suites remain useful as context, but their `kind`, URL, and limitation make that boundary visible.

The audit script checks the public GitHub API and stores repository metadata plus README hashes. It does not execute third-party code. A successful source audit means that the cited repository was accessible at the snapshot date, not that every claim in its documentation has been independently reproduced.

## Inventory shape

| Area | Entries | What it exposes |
|---|---:|---|
| Direct harness comparisons | 11 | The harness is the treatment, or the benchmark is explicitly designed around model–harness configurations. |
| Tools and APIs | 11 | Tool choice, schema use, state dependencies, multi-step API execution and MCP integration. |
| Coding and terminal | 9 | Workspace exploration, patching, test feedback, long trajectories and artifact verification. |
| Browser | 8 | Web navigation, live-site drift, visual grounding and multi-site workflows. |
| General agents | 7 | Mixed tool, reasoning and communication workloads. |
| Memory and context | 7 | Retrieval, context selection, temporal updates, persistent state and experience reuse. |
| Safety | 6 | Permission boundaries, indirect injection, harmful requests and web attacks. |
| Long horizon | 6 | Asynchronous events, multi-day state, monitoring and human-calibrated task duration. |
| Evaluation infrastructure | 5 | Sandboxes, shared interfaces, verifiers, cost accounting and scalable runs. |
| Computer and mobile | 4 | Desktop, Windows and Android interaction. |
| Multi-agent | 4 | Routing, communication, delegation, failure cascades and recovery. |
| Research engineering | 4 | ML, scientific coding, reproduction and research workflows. |
| Skills | 2 | The effect of structured instructions, scripts and reference material mounted at runtime. |

The count is an inventory count, not a quality ranking. One entry can be relevant to several harness responsibilities, but it has one primary category so that totals remain auditable.

## What the strongest evidence looks like

The best direct comparisons hold the model endpoint, prompt, tools, task fixture, sandbox image, timeout, token budget and sampling policy fixed. They run the same instances multiple times, preserve raw traces and workspace diffs, use deterministic checks for correctness, and report variance and cost alongside the headline success rate. Harness-Bench (Qihoo360) is the broadest public example in this snapshot: its public description reports 106 sandboxed offline tasks with trace and artifact capture. HarnessRisk applies the same model–harness framing to adversarial safety across the lifecycle. Hyper-τ measures a different boundary: whether a developer agent can construct a working agent from evidence and pass a sealed downstream workload. HarnessDev extends that question to creation and iterative evolution of runnable infrastructure.

Mature workload suites remain valuable because they expose real failure surfaces. Terminal-Bench and SWE-bench reveal whether a loop can explore, edit, test and recover. τ³-bench and ToolSandbox reveal stateful tool coordination and policy adherence. Toolathlon, MCPMark and MCP-Bench stretch heterogeneous tools and MCP plumbing. WebArena and OSWorld expose browser and desktop interaction. LongMemEval-V2 and MemoryArena test whether state survives beyond one context window. AgentDojo and HarnessRisk test whether the same access that enables usefulness can be constrained safely. OrchestraBench and MAS-FIRE make routing and failure propagation observable in multi-agent pipelines.

## Comparison dimensions

| Dimension | Primary metric | Useful secondary metrics |
|---|---|---|
| Outcome | Verified task success | Partial credit, invariant violations, artifact completeness |
| Reliability | Pass^k or per-task success variance | Timeout/crash rate, retry success, recovery rate |
| Execution | Correct tool sequence and state transition | Invalid calls, duplicate calls, stale-state use |
| Efficiency | Cost per successful task | Tokens, tool calls, wall time, p50/p95 latency |
| Context and memory | Gold-context recall/precision or downstream task lift | Context size, compaction loss, retrieval latency, memory hygiene |
| Safety | Unauthorized side-effect rate / attack success rate | Detection, false positives, persistence and blast radius |
| Observability | Replayable trace and evidence completeness | Environment diff, verifier logs, attribution of failure |

Do not collapse all dimensions into one score without publishing the component scores. A verifier score can be perfect while the agent is wasteful, unsafe, or impossible to debug; an LLM process score can be persuasive while remaining judge-dependent.

## Recommended evaluation plans

For a general-purpose harness, use Harness-Bench as the direct comparison, then add Terminal-Bench, τ³-bench, OSWorld-Verified, AgentDojo, LongMemEval-V2 and OrchestraBench when the corresponding surfaces are in scope. For a coding harness, use a fixed split of SWE-bench plus Terminal-Bench, ContextBench, and a multi-run cost/reliability report. For an MCP-heavy harness, use MCPMark, Toolathlon-Verified, ToolSandbox and τ³-bench with server versions pinned. For long-running memory, pair LongMemEval-V2 or MemoryArena with a task-level workload such as ClawMark, SentinelBench or Gaia2. For a self-evolving harness, use HarnessDev or RSIBench and keep the train-side gate separate from the held-out score.

## Threats to validity

Scores can move when a live website changes, a tool server is upgraded, an evaluator uses a different judge model, a retry is counted as a fresh attempt, or a harness ships hidden skills and global configuration. Benchmark releases can also overlap in their source tasks. Every result should therefore include the exact release or commit, environment image, tool versions, model endpoint, budgets, repeat count, scorer version and whether network access was live, replayed or mocked.
