# Agent harness comparison report

Copy this template for a real experiment. Replace the placeholders with observations and links. Empty cells mean not reported; they are not zero scores.

## Question and intervention

**Question:** [What decision should this comparison inform?]

**Design:** [Native harness comparison / component ablation / whole-agent comparison]

**Intervention:** [Exactly what changes between A and B?]

**Hypothesis and success criterion:** [Define before inspecting held-out results.]

For native harness comparisons, native prompts, tools, and defaults may be part of the intervention. For a component ablation, change only the selected feature. List all differences so readers know what the result can be attributed to.

## Configuration

| Field | Configuration A | Configuration B |
| --- | --- | --- |
| Harness name and commit | | |
| Model endpoint and dated version | | |
| System prompt / configuration link | | |
| Tools, schemas, skills, and permissions | | |
| Memory initialization and reset rules | | |
| Benchmark release, split, and task IDs | | |
| Sandbox image and network mode | | |
| Token, time, step, and monetary budgets | | |
| Sampling settings, seeds, and repeat count | | |
| Retry policy and timeout treatment | | |
| Scorer version; judge model if used | | |

## Results

| Metric | A | B | Definition / uncertainty |
| --- | --- | --- | --- |
| Verified task success | | | State denominator and handling of skipped or failed runs. |
| Repeatability | | | Define the statistic; distinguish success on every repeat from success on any repeat. |
| Cost per successful task | | | Include spend on unsuccessful attempts; define accounting boundary. |
| Wall time (median / p95) | | | State whether setup and tool latency are included. |
| Crashes, timeouts, and invalid tool calls | | | Include counts and denominators. |
| Safety or policy violations | | | State attack set / policy and retain benign-task utility. |

For matched repeated tasks, report uncertainty at the task level. Explain exclusions and judge disagreements. Do not combine incompatible benchmark scales into a single rank without a published aggregation method.

## Evidence

- Configuration and code: [versioned link]
- Raw task results, including unsuccessful attempts: [artifact link]
- Traces and verifier output: [artifact link]
- Task selection and analysis procedure: [script or written method]
- Replication command and required environment: [instructions]

## Interpretation

**Observed finding:** [What the measurements show.]

**What this cannot establish:** [Confounds, workload mismatch, judge dependence, contamination, or environment drift.]

**Decision supported:** [What you would choose for this workload, and why.]

[Back to the selection guide](../README.md) · [Methodology](research.md)
