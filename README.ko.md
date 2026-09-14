# Awesome Agent Harness Benchmarks

내 에이전트에 맞는 평가를 찾으세요. 점수를 비교하기 전에 과제, 채점 방식, 한계를 살펴볼 수 있습니다.

## [검색 가능한 평가 카탈로그 열기 →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)

평가할 역량으로 범위를 좁히고, 원문 출처와 실행 환경, 평가의 한계를 확인하세요.

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어

자료 기준일: 2026-09-13 · 전체 115개 항목 · 평가 모음 97개 · 13개 분야

여기서 **harness**는 모델 주변에서 도구 호출, 컨텍스트, 메모리, 권한, 실행 흐름을 관리하는 시스템을 뜻합니다. 이 카탈로그는 각 기능을 시험할 공개 평가를 찾고, 결과가 뒷받침하는 결론의 범위를 파악하도록 돕습니다.

## 무엇을 확인하고 싶나요?

목적에 따라 먼저 살펴볼 평가를 골랐습니다. 순위표는 아닙니다. 전체 카탈로그에서 다른 과제, 버전, 비교 연구도 확인할 수 있습니다.

| 평가할 작업 | 먼저 살펴볼 평가 | 채점 방식 | 비교할 때 주의할 점 |
| --- | --- | --- | --- |
| 실제 코드 저장소의 문제 수정 | [SWE-bench family](https://github.com/SWE-bench/SWE-bench) | 수정 검증 테스트와 회귀 테스트 | 트랙마다 과제, 언어, 평가 방식이 달라 점수를 그대로 비교할 수 없습니다. |
| 복잡한 터미널 작업 완료 | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) | 과제별 검증 프로그램 실행 | 데이터셋 버전을 고정해야 합니다. 점수에는 모델과 harness가 모두 영향을 줍니다. |
| 상태를 유지하며 도구 사용 | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) | 중간 단계와 최종 상태 확인 | 사용자 시뮬레이터와 도구 인터페이스도 결과에 영향을 줍니다. |
| 웹사이트에서 작업 완료 | [WebArena](https://github.com/web-arena-x/webarena) | 웹 앱의 기능과 상태 확인 | 환경 설정, 과제, 평가기의 수정 사항까지 버전을 맞춰야 합니다. |
| 여러 데스크톱 앱을 오가며 작업 | [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld) | 실행 결과에 따른 검증 | 가상 머신 이미지, 최대 행동 횟수, 평가 버전이 같아야 합니다. |
| 긴 대화 기록에서 정보 찾기 | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) | 과거 기록에 대한 질의응답 정확도 | 전체 컨텍스트를 제공한 기준선이 필요합니다. 정답을 찾는 것과 여러 단계의 작업을 끝내는 것은 다릅니다. |
| 도구 환경의 프롬프트 인젝션 방어 | [AgentDojo](https://github.com/ethz-spylab/agentdojo) | 정상 작업 성능과 공격 성공률 | 위협 모델과 공격 예산을 고정하고, 안전성과 유용성을 함께 봐야 합니다. |
| 도구로 정보를 수집하고 추론 | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) | 최종 답변 정확도 | 최종 답변만으로는 실행 중의 부작용과 안전 문제를 파악하기 어렵습니다. |

## 점수가 말해 주는 것

대부분의 평가는 에이전트 전체의 성능을 측정합니다. 차이의 원인을 harness에서 찾으려면 모델, 과제, 예산을 동일하게 두고 비교해야 합니다. 이 카탈로그에 실렸다고 해서 해당 프로젝트가 이런 실험을 수행했다는 뜻은 아닙니다.

- **benchmark**: 과제와 평가기를 갖춘 평가 모음으로, 테스트를 실행할 때 사용합니다.
- **study**: 실험 설계와 기존 근거를 살펴볼 수 있는 비교 연구입니다.
- **infrastructure**: 평가 실행이나 감사를 돕는 도구이며, 그 자체가 과제 모음은 아닙니다.
- **watchlist**: 초기 단계이거나 범위가 좁은 후보로, 추가 확인이 필요합니다.

비교 템플릿과 평가 제안은 실험 설계를 돕는 자료이며, 실제 측정 결과나 순위표가 아닙니다.

## 분야별로 더 찾아보기

[전체 카탈로그](docs/catalog.md)에 각 항목의 설명과 출처를 모았습니다. 관심 있는 분야로 바로 이동할 수도 있습니다:

[Harness 직접 비교](docs/catalog.md#direct) · [코드·터미널](docs/catalog.md#coding) · [도구·상태 관리](docs/catalog.md#tools)

[브라우저](docs/catalog.md#browser) · [데스크톱·모바일](docs/catalog.md#computer) · [범용 작업](docs/catalog.md#general)

[메모리·컨텍스트](docs/catalog.md#memory) · [장시간 작업](docs/catalog.md#long-horizon) · [안전성](docs/catalog.md#safety)

[여러 에이전트의 협업](docs/catalog.md#multi-agent) · [연구 작업](docs/catalog.md#research) · [스킬·지시 이행](docs/catalog.md#skills) · [평가 기반 도구](docs/catalog.md#infrastructure)

## 직접 비교하려면

[비교 기록 템플릿](docs/comparison-template.md)을 사용해 실험 조건과 결과를 함께 기록하세요:

1. 모델, 프롬프트, 도구 명세, 과제 버전, 환경, 예산, 재시도 정책을 고정합니다.
2. 완료율, 편차, 비용, 지연 시간, 안전 문제를 따로 보고하고 실행 기록과 검증 출력을 보관합니다.
3. [조사 노트](docs/research.md)에서 근거의 수준과 비교 조건을 확인한 뒤 차이를 해석합니다.

## 에이전트에서 읽기

자동으로 검색하거나 정리할 때는 다음 자료를 바로 읽을 수 있습니다:

- [설명이 포함된 Markdown 카탈로그](site/agent.md)
- [구조화된 데이터](data/catalog.json)
- [필드 정의](data/catalog.schema.json)
- [저장소 유지보수 규칙](AGENTS.md)

## 출처와 기여

공식 저장소, 논문, 프로젝트 페이지를 우선합니다. [출처 확인 기록](data/source-audit.json)은 특정 시점의 접근 가능 여부와 메타데이터를 담으며, 독립적인 재현 실험을 뜻하지 않습니다. 수록 자체가 추천을 의미하지 않으며, 모든 공개·비공개 평가를 망라하지는 않습니다.

빠진 평가, 깨진 링크, 잘못된 설명을 발견했다면 [기여 안내](CONTRIBUTING.md)에 따라 issue나 PR을 보내 주세요. 원문 출처와 평가의 구체적인 한계도 함께 알려 주시면 좋습니다. 평가 방법이나 벤치마크 비교에 대한 질문은 [Discussions](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)에서 함께 이야기할 수 있습니다.
