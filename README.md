# Awesome Agent Harness Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Choose benchmarks for AI agents: **what they test, how they score, and what their scores leave out.**

**[Browse the searchable catalog →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)** · [Full Markdown catalog](docs/catalog.md) · [Agent digest](site/agent.md) · [JSON](data/catalog.json)

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

115 resources across 13 areas · Source snapshot: September 13, 2026 · [Corrections and updates](docs/updates.md)

An **agent harness** is the software around a model: its tool loop, context, memory, permissions, and recovery. Use this guide to choose a task suite for that layer, then design a comparison that can identify what changed.

## Contents

- [Choose a benchmark](#choose-a-benchmark)
- [Study the harness itself](#study-the-harness-itself)
- [Browse by capability](#browse-by-capability)
- [Make a useful comparison](#make-a-useful-comparison)
- [How this list is curated](#how-this-list-is-curated)
- [Contribute](#contribute)

## Choose a benchmark

Start with the row closest to your workload. These are entry points for evaluation design; the full catalog includes newer suites and specialized alternatives.

| You want to evaluate…                  | Starting point                                                       | What gets scored                                                 | Main caveat                                                                                    |
| -------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Fixing issues in a repository          | [SWE-bench](https://github.com/SWE-bench/SWE-bench)                  | Whether patches pass issue tests and avoid regressions.          | Pin the track and task release; a passing patch only covers the available tests.               |
| Completing terminal workflows          | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) | Task-specific checks of the resulting environment.               | Sandbox and compute requirements depend on the release and task.                               |
| Using stateful APIs                    | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)    | Intermediate milestones and final state.                         | Simulated tools do not cover every production API failure.                                     |
| Acting on websites                     | [WebArena](https://github.com/web-arena-x/webarena)                  | Functional outcomes on self-hosted web applications.             | Requires environment setup; the sites differ from the live web.                                |
| Operating a desktop                    | [OSWorld](https://github.com/xlang-ai/OSWorld)                       | Execution-based checks across desktop applications.              | VM, application versions, and observation/action settings affect results.                      |
| Remembering past conversations         | [LongMemEval](https://github.com/xiaowu0162/LongMemEval)             | LLM-judged answers to questions over long interaction histories. | Pin the history split and judge; QA does not measure all persistent agent behavior.            |
| Resisting tool-output prompt injection | [AgentDojo](https://github.com/ethz-spylab/agentdojo)                | Benign task utility and attack success.                          | Results depend on the attack suite and tool environment.                                       |
| Solving mixed assistant tasks          | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)          | Final-answer correctness on tool-assisted tasks.                 | Specify the level and split; correct answers alone do not explain execution failures or costs. |

These suites score the **whole agent configuration**. To attribute a difference to the harness, control the other variables in your experiment.

## Study the harness itself

“Harness benchmark” can describe several different questions. Choose the question before choosing a score.

| Resource                                                       | Question it helps investigate                                                  | Interpretation                                                                                |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| [Harness-Bench](https://github.com/Qihoo360/harness-bench)     | How do native model–harness configurations perform on offline workspace tasks? | Preserves native execution behavior; configuration differences remain part of the comparison. |
| [ShellBench](https://github.com/openclaw/shellbench)           | Where does a full agent stack succeed or fail in task traces?                  | Includes harness, model, and configuration effects. Formerly OpenClaw ClawBench.              |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench)     | What changes when reusable skills are available?                               | A skill condition is one component intervention; model and task choices still matter.         |
| [Hyper-τ](https://github.com/sierra-research/hyper-tau-bench)  | Can a developer agent build an agent that passes held-out tasks?               | Measures agent construction, a different question from runtime harness selection.             |
| [Harness Arena](https://github.com/Ondemand-OSS/harness-arena) | Which harness outputs do people prefer in blinded comparisons?                 | Early comparison infrastructure; preference/Elo is distinct from task correctness.            |

## Browse by capability

The complete inventory retains each source's description, resource type, scoring method, environment, and limitation. Categories group resources by their primary use; they are not quality rankings.

| Area                                                        | Area                                                | Area                                              |
| ----------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- |
| [Harness comparisons](docs/catalog.md#direct)               | [Coding and terminal](docs/catalog.md#coding)       | [Tools, APIs, and MCP](docs/catalog.md#tools)     |
| [Browser and web](docs/catalog.md#browser)                  | [Desktop and mobile](docs/catalog.md#computer)      | [General agents](docs/catalog.md#general)         |
| [Memory and context](docs/catalog.md#memory)                | [Long-running agents](docs/catalog.md#long-horizon) | [Safety and failures](docs/catalog.md#safety)     |
| [Multi-agent systems](docs/catalog.md#multi-agent)          | [Research engineering](docs/catalog.md#research)    | [Skills and instructions](docs/catalog.md#skills) |
| [Evaluation infrastructure](docs/catalog.md#infrastructure) |                                                     |                                                   |

## Make a useful comparison

**State the intervention.** For native harnesses, record their prompts, tools, and defaults as part of the configuration; for a component ablation, change one feature and keep the rest fixed.

**Run matched tasks.** Keep the model, task release, environment, budgets, and evaluation rules aligned wherever they are outside the intervention. Repeat tasks and record failures as well as successes.

**Publish interpretable results.** Report verified success, repeatability, cost, latency, and safety separately. Link the configurations, traces, and verifier outputs.

Use the [comparison report template](docs/comparison-template.md) to document a run, or read the [research and methodology notes](docs/research.md) for experiment designs and limitations. The template is blank; this repository does not publish its own benchmark scores.

## How this list is curated

Resources are included when they expose an agent execution responsibility and have a public source describing the tasks, evaluator, study, or runner. The shortlist emphasizes distinct, understandable use cases. Inclusion in the full inventory is not an endorsement or proof of reproducibility.

**Benchmark** means a task suite with an evaluator; **study** means a comparison; **infrastructure** means a runner or evaluation layer; **watchlist** means an early candidate. These labels describe resource types, not evidence quality.

GitHub source checks run weekly. They check availability and record provenance; additions, classification changes, and research claims need review. An accessible repository has not necessarily been independently reproduced. See [data and provenance](data/README.md) for the schema, stable IDs, aliases, and audit details.

## Contribute

Found a missing benchmark? [Suggest a source](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=benchmark.yml). Found a misleading claim, duplicate, or broken link? [Report a correction](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=correction.yml).

Source links and a short explanation are enough to start. For a pull request, follow the [contribution guide](CONTRIBUTING.md); coding agents should read [AGENTS.md](AGENTS.md).
