# Awesome Agent Harness Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Choose benchmarks for AI agents: **what they test, how they score, and what their scores leave out.** Unlike a leaderboard, this catalog does not treat scores from incompatible tasks as interchangeable. Every record names the grader, environment, and a concrete limitation.

**[Browse the searchable catalog →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)** · [Full Markdown catalog](docs/catalog.md) · [Agent digest](site/agent.md) · [JSON](data/catalog.json) · [Citation](CITATION.cff)

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

**Start by workload:** [Harness comparisons](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=direct&sort=featured#directory) · [Coding](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=coding&sort=featured#directory) · [Tool use](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=tools&sort=featured#directory) · [Browser](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=browser&sort=featured#directory) · [Memory](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=memory&sort=featured#directory) · [Safety](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=safety&sort=featured#directory)

Curated shortlist · Broader research inventory: **115 resources** — 97 benchmark suites · 9 infrastructure layers · 7 studies · 2 watchlist items · 13 areas · Weekly source checks · Snapshot: September 13, 2026 · [Corrections and updates](docs/updates.md)

An **agent harness** is the software around a model: its tool loop, context, memory, permissions, and recovery. Use this guide to choose a task suite for that layer, then design a comparison that can identify what changed.

The README is the opinionated entry point. The complete catalog (`docs/catalog.md`) also retains controlled studies, evaluation infrastructure, and early watchlist items so research gaps remain visible.

> **A passing SWE-bench patch proves that a patch passed the available tests. It does not prove that a harness is cheaper, safer, or better at recovery.** Those claims need matched tasks, fixed model access, and trace-level evidence.

## Contents

- [Choose a benchmark](#choose-a-benchmark)
- [Study the harness itself](#study-the-harness-itself)
- [Browse by capability](#browse-by-capability)
- [Make a useful comparison](#make-a-useful-comparison)
- [How this list is curated](#how-this-list-is-curated)
- [Related catalogs](#related-catalogs)
- [Contribute](#contribute)

## Choose a benchmark

Start with the closest workload. These are entry points for evaluation design, not a ranking; the full catalog includes newer suites and specialized alternatives.

- **Fix repository issues** — [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Scores patch tests and regressions; pin the track and task release.
- **Complete terminal workflows** — [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) - Runs task-specific checks; sandbox and compute requirements vary by release.
- **Use stateful APIs** — [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) - Checks milestones and final state; simulated tools miss some production failures.
- **Act on websites** — [WebArena](https://github.com/web-arena-x/webarena) - Checks self-hosted web-app outcomes; environment setup and site versions matter.
- **Operate a desktop** — [OSWorld](https://github.com/xlang-ai/OSWorld) - Uses execution-based checks; VM images, applications, and action budgets affect results.
- **Remember long conversations** — [LongMemEval](https://github.com/xiaowu0162/LongMemEval) - Uses LLM-judged history QA; that is not the same as persistent multi-step work.
- **Resist tool-output injection** — [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Measures benign utility and attack success; fix the threat model and tool environment.
- **Solve mixed assistant tasks** — [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) - Scores final answers; it does not explain execution failures, side effects, or cost.

These suites score the **whole agent configuration**. To attribute a difference to the harness, control the other variables in your experiment.

## Study the harness itself

“Harness benchmark” can describe several different questions. Choose the question before choosing a score.

- **Native configuration comparison** — [Harness-Bench](https://github.com/Qihoo360/harness-bench) - Preserves model–harness behavior on offline workspaces; configuration differences stay in scope.
- **Full-stack task traces** — [ShellBench](https://github.com/openclaw/shellbench) - Includes harness, model, and defaults; formerly OpenClaw ClawBench.
- **Component intervention** — [SkillsBench](https://github.com/benchflow-ai/skillsbench) - Tests reusable skills; model and task choices still matter.
- **Harness construction** — [Hyper-τ](https://github.com/sierra-research/hyper-tau-bench) - Measures an agent building another agent, not runtime harness selection.
- **Human preference** — [Harness Arena](https://github.com/Ondemand-OSS/harness-arena) - Early blinded comparison infrastructure; preference/Elo is not task correctness.

## Browse by capability

The complete inventory retains each source's description, resource type, scoring method, environment, and limitation. Categories group resources by primary use; they are not quality rankings.

- [Harness comparisons](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=direct#directory) - A focused set of 11 harness comparisons.
- [Coding and terminal](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=coding#directory) - Twelve repository and terminal workloads.
- [Tools, APIs, and MCP](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=tools#directory) - Fifteen stateful tool-use evaluations.
- [Browser and web](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=browser#directory) - Eleven browser and web-app workloads.
- [Desktop and mobile](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=computer#directory) - Six GUI and device environments.
- [General agents](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=general#directory) - Eleven mixed assistant tasks.
- [Memory and context](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=memory#directory) - Seven memory and retrieval evaluations.
- [Long-running agents](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=long-horizon#directory) - Eight long-horizon or always-on workloads.
- [Safety and failures](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=safety#directory) - Eight adversarial or policy-sensitive suites.
- [Multi-agent systems](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=multi-agent#directory) - Four collaboration evaluations.
- [Research engineering](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=research#directory) - Nine science and experiment workflows.
- [Skills and instructions](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=skills#directory) - Two skill or instruction interventions.
- [Evaluation infrastructure](https://zeredy879.github.io/awesome-agent-harness-benchmarks/?category=infrastructure#directory) - Eleven runners and audit layers.

## Make a useful comparison

**State the intervention.** For native harnesses, record their prompts, tools, and defaults as part of the configuration; for a component ablation, change one feature and keep the rest fixed.

**Run matched tasks.** Keep the model, task release, environment, budgets, and evaluation rules aligned wherever they are outside the intervention. Repeat tasks and record failures as well as successes.

**Publish interpretable results.** Report verified success, repeatability, cost, latency, and safety separately. Link the configurations, traces, and verifier outputs.

Use the [comparison report template](docs/comparison-template.md) to document a run, or read the [research and methodology notes](docs/research.md) for experiment designs and limitations. The template is blank; this repository does not publish its own benchmark scores.

## How this list is curated

Resources are included when they expose an agent execution responsibility and have a public source describing the tasks, evaluator, study, or runner. The shortlist emphasizes distinct, understandable use cases. Inclusion in the full inventory is not an endorsement or proof of reproducibility.

**Benchmark** means a task suite with an evaluator; **study** means a comparison; **infrastructure** means a runner or evaluation layer; **watchlist** means an early candidate. These labels describe resource types, not evidence quality.

GitHub source checks run weekly. They check availability and record provenance; additions, classification changes, and research claims need review. An accessible repository has not necessarily been independently reproduced. See [data and provenance](data/README.md) for the schema, stable IDs, aliases, and audit details.

## Related catalogs

This repository focuses on **benchmark choice and harness attribution**. Nearby lists cover different questions:

- **Harness-engineering papers, tools, and implementation guidance** — [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering) - A complementary implementation-focused list.
- **Setup-cost and run-command guidance for agent benchmarks** — [Awesome AI Agent Benchmarks](https://github.com/serenakeyitan/awesome-ai-agent-benchmarks) - A general benchmark directory.
- **Evaluation platforms, frameworks, benchmarks, and methodology** — [Awesome Agent Evals](https://github.com/genai-io/awesome-agent-evals) - A compact evaluation map.

Linking adjacent catalogs is intentional: collecting every agent resource here would make the harness-specific comparison problem harder to see.

## Contribute

Found a missing benchmark? [Suggest a source](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=benchmark.yml). Found a misleading claim, duplicate, or broken link? [Report a correction](https://github.com/zeredy879/awesome-agent-harness-benchmarks/issues/new?template=correction.yml).

Source links and a short explanation are enough to start. For methodology questions or benchmark comparisons, use [Discussions](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions). For a pull request, follow the [contribution guide](CONTRIBUTING.md); coding agents should read [AGENTS.md](AGENTS.md).
