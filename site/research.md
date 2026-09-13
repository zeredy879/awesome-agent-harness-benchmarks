# Research and comparison notes

This document explains how the inventory was assembled and how to choose a benchmark for a harness question.

## Scope and method

The snapshot date is 2026-09-13. The September 2026 refresh searched benchmark papers and project pages, official GitHub repositories, benchmark leaderboards, and evaluation runners that expose at least one execution-layer responsibility. We included a workload when the agent changes a workspace, calls a tool, observes state, interacts over multiple turns, delegates, persists memory, or must obey an action policy. We included a study when the harness itself is the treatment or when its ablation protocol provides reusable evidence. We included infrastructure only when it makes harness swapping, sandboxing, verification, or trace collection practical.

Items with the same name are kept separate when their owner, environment, or scoring protocol differs. Examples include the OpenClaw, TIGER-AI-Lab, and other projects named ClawBench. A planned protocol is never promoted to a measured benchmark result. Private or unavailable suites remain useful as context, but their `kind`, URL, and limitation make that boundary visible.

The audit script checks the public GitHub API and stores repository metadata plus README hashes. It does not execute third-party code. A successful source audit means that the cited repository was accessible at the snapshot date, not that every claim in its documentation has been independently reproduced.

## Inventory shape

| Area | Entries | What it exposes |
|---|---:|---|
| Direct harness comparisons | 12 | The harness is the treatment, or the benchmark is explicitly designed around model–harness configurations. |
| Tools and APIs | 15 | Tool choice, schema use, state dependencies, multi-step API execution and MCP integration. |
| Coding and terminal | 12 | Workspace exploration, patching, test feedback, long trajectories and artifact verification. |
| Browser | 11 | Web navigation, live-site drift, visual grounding and multi-site workflows. |
| General agents | 11 | Mixed tool, reasoning and communication workloads. |
| Memory and context | 7 | Retrieval, context selection, temporal updates, persistent state and experience reuse. |
| Safety | 8 | Permission boundaries, indirect injection, harmful requests and web attacks. |
| Long horizon | 8 | Asynchronous events, multi-day state, monitoring and human-calibrated task duration. |
| Evaluation infrastructure | 11 | Sandboxes, shared interfaces, verifiers, cost accounting and scalable runs. |
| Computer and mobile | 6 | Desktop, Windows, Android, and spreadsheet interaction. |
| Multi-agent | 4 | Routing, communication, delegation, failure cascades and recovery. |
| Research engineering | 9 | ML, scientific coding, reverse engineering, reproduction and research workflows. |
| Skills | 2 | The effect of structured instructions, scripts and reference material mounted at runtime. |

The count is an inventory count, not a quality ranking. One entry can be relevant to several harness responsibilities, but it has one primary category so that totals remain auditable.

This refresh raises the inventory from 84 to **116 entries**. The new edge is concentrated in enterprise workflows, data agents, research reproduction, infrastructure operations, full-stack runtime diagnostics, and browser/deep-search evaluation. The [machine-readable catalog](../data/catalog.json) is the countable source of truth; this table is a human-oriented aggregation.

## Recent scan and evidence tiers

The scan intentionally separates evidence levels. A benchmark with a public task/evaluator and a paper or maintained repository is included as a measured `benchmark`. A reusable runner or auditing layer is `infrastructure`. A controlled framework comparison without a fixed public task corpus is `study`. A public but early or narrow project can be kept as `watchlist` when it is useful for discovery, but this snapshot does not promote it to a leaderboard claim.

Recent high-signal additions include [AgentSearchBench](https://github.com/Bingo-W/AgentSearchBench) (execution-grounded agent retrieval), [SciAgentArena](https://github.com/HelloWorldLTY/SciAgentArena) (scientific workflows), [InfraBench](https://github.com/kubeply/infra-bench) and [AOBench](https://github.com/MSKazemi/aobench) (infrastructure operations), [APEX-Agents/Archipelago](https://github.com/togethercomputer/archipelago) and [STATE-Bench](https://github.com/microsoft/STATE-Bench) (enterprise stateful work), [AIRS-Bench](https://github.com/facebookresearch/airs-bench) and [PaperBench](https://github.com/openai/preparedness) (research execution), [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus) (retriever/agent disentanglement), [SpreadsheetBench 2](https://spreadsheetbench.github.io/) (business spreadsheet workflows), [AgentActionBench](https://arxiv.org/abs/2609.11117) (trace-scored reproduction), [AgentRE-Bench](https://github.com/agentrebench/AgentRE-Bench) and [Cybench](https://github.com/andyzorigin/cybench) (specialized security capability), and [ShellBench](https://github.com/openclaw/shellbench)/[Coder Eval](https://github.com/UiPath/coder_eval)/[Lemans](https://github.com/rails/lemans) (harness and regression infrastructure). Each entry records its primary source and a limitation rather than merging incompatible scores.

The scan also checked active GitHub search results for emerging projects. Low-evidence personal experiments, result-only repositories, duplicate catalogs, and repositories without a stable evaluator remain discoverable through GitHub search but are not silently counted as formal benchmark suites. This keeps the headline count useful while leaving an explicit path for later `watchlist` additions.

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

For a general-purpose harness, use Harness-Bench or ShellBench as the direct comparison, then add Terminal-Bench, τ³-bench, STATE-Bench, OSWorld-Verified, AgentDojo, LongMemEval-V2 and OrchestraBench when the corresponding surfaces are in scope. For a coding harness, use a fixed split of SWE-bench plus Terminal-Bench, GitTaskBench, Version Control Bench, ContextBench, and a multi-run cost/reliability report. For an MCP or enterprise-data harness, use MCPMark, Toolathlon-Verified, ToolSandbox, Agent-Diff, DataSpace, DAB and τ³-bench with server versions pinned. For long-running memory and daily workflows, pair LongMemEval-V2 or MemoryArena with AgentIF-OneDay, ClawMark, SentinelBench or Gaia2. For research automation, use PaperBench, AIRS-Bench, SciAgentArena or AgentActionBench and keep any train-side gate separate from the held-out score. For a self-evolving harness, use HarnessDev or RSIBench and keep the train-side gate separate from the held-out score.

## Threats to validity

Scores can move when a live website changes, a tool server is upgraded, an evaluator uses a different judge model, a retry is counted as a fresh attempt, or a harness ships hidden skills and global configuration. Benchmark releases can also overlap in their source tasks. Every result should therefore include the exact release or commit, environment image, tool versions, model endpoint, budgets, repeat count, scorer version and whether network access was live, replayed or mocked.

## Sources / references

The following primary sources anchor the recent scan; the catalog links the canonical source for every entry.

- [AgentSearchBench paper](https://arxiv.org/abs/2604.22436) and [repository](https://github.com/Bingo-W/AgentSearchBench)
- [SciAgentArena paper](https://arxiv.org/abs/2606.12736) and [repository](https://github.com/HelloWorldLTY/SciAgentArena)
- [InfraBench paper](https://arxiv.org/abs/2608.11234) and [repository](https://github.com/kubeply/infra-bench)
- [APEX-Agents paper](https://arxiv.org/abs/2601.14242) and [Archipelago runner](https://github.com/togethercomputer/archipelago)
- [DataSpace paper](https://arxiv.org/abs/2608.03451) and [repository](https://github.com/HKUSTDial/DataSpace)
- [DAB paper](https://arxiv.org/abs/2603.20576) and [repository](https://github.com/ucbepic/DataAgentBench)
- [AIRS-Bench paper](https://arxiv.org/abs/2602.06855) and [repository](https://github.com/facebookresearch/airs-bench)
- [AgentIF-OneDay paper](https://arxiv.org/abs/2601.20613) and [repository](https://github.com/xbench-ai/AgentIF-OneDay)
- [OmniaBench paper](https://arxiv.org/abs/2607.14989) and [repository](https://github.com/scuuy/OmniaBench)
- [Agent-Diff paper](https://arxiv.org/abs/2602.11224) and [repository](https://github.com/agent-diff-bench/agent-diff)
- [STATE-Bench repository](https://github.com/microsoft/STATE-Bench)
- [BrowseComp paper](https://arxiv.org/abs/2504.12516) and [simple-evals repository](https://github.com/openai/simple-evals)
- [BrowseComp-Plus paper](https://arxiv.org/abs/2508.06600) and [repository](https://github.com/texttron/BrowseComp-Plus)
- [SpreadsheetBench 2 paper](https://arxiv.org/abs/2606.29955) and [project page](https://spreadsheetbench.github.io/)
- [GitTaskBench repository](https://github.com/QuantaAlpha/GitTaskBench)
- [PaperBench paper](https://arxiv.org/abs/2504.01848) and [Frontier Evals repository](https://github.com/openai/preparedness)
- [Cybench paper](https://arxiv.org/abs/2408.08926) and [repository](https://github.com/andyzorigin/cybench)
- [AgentRE-Bench repository](https://github.com/agentrebench/AgentRE-Bench)
- [AgentActionBench paper](https://arxiv.org/abs/2609.11117)
- [AgentRace paper](https://agent-race.github.io/paper)
