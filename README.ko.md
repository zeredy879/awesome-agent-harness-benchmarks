# Awesome Agent Harness Benchmarks

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme-hero-dark.svg">
  <img src="assets/readme-hero-light.svg" alt="벤치마크를 고르고, 평가 근거를 이해하세요." width="1200">
</picture>

공개 벤치마크와 관련 자료 115개를 13개 분야로 정리했습니다. AI 에이전트가 수행할 작업에 맞는 벤치마크를 찾고, 평가 내용과 채점 방식, 한계를 확인하세요.

[**벤치마크 검색하기 →**](https://zeredy879.github.io/awesome-agent-harness-benchmarks/) · [English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어

## 평가할 작업으로 고르기

| 평가할 작업 | 먼저 살펴볼 벤치마크 |
| --- | --- |
| 코드 저장소의 문제 수정 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) |
| 터미널 작업 완료 | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) |
| 상태를 관리하며 도구 사용 | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) |
| 웹사이트에서 작업 수행 | [WebArena](https://github.com/web-arena-x/webarena) |
| 데스크톱 앱 사용 | [OSWorld](https://github.com/xlang-ai/OSWorld) |
| 지난 대화를 기억하고 정보 찾기 | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) |
| 도구 출력의 프롬프트 인젝션 방어 | [AgentDojo](https://github.com/ethz-spylab/agentdojo) |
| 정보를 찾고 도구를 써서 문제 해결 | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) |

다른 후보는 [전체 카탈로그](docs/catalog.md)에서 찾아볼 수 있습니다. 각 항목에 채점 방식, 실행 환경, 구체적인 한계가 정리되어 있습니다.

## Harness 비교하기

**Agent harness**는 모델의 도구 사용, 컨텍스트, 메모리, 권한, 오류 복구를 관리하는 소프트웨어입니다. 이 부분을 평가하려면 다음 프로젝트부터 살펴보세요.

- [Harness-Bench](https://github.com/Qihoo360/harness-bench): 모델과 harness의 조합을 로컬 작업 환경에서 비교합니다.
- [ShellBench](https://github.com/openclaw/shellbench): 이전 이름은 ClawBench입니다. 실행 기록과 반복 실행을 통해 에이전트 전체 구성의 신뢰성을 평가합니다.
- [SkillsBench](https://github.com/benchflow-ai/skillsbench): 스킬 패키지가 있을 때와 없을 때의 작업 성과를 비교합니다.

## 데이터와 비교 방법

대부분의 벤치마크는 에이전트 전체의 성능을 측정합니다. harness를 비교하려면 먼저 무엇을 바꿀지 정하세요. 전체 구성을 비교할 때는 각 구성의 프롬프트, 도구, 기본 설정을 포함할 수 있습니다. 특정 기능의 효과를 확인할 때는 그 기능만 바꿉니다. 모델, 과제, 환경, 예산, 채점 기준 등 비교 대상에 포함하지 않은 조건은 동일하게 맞춥니다.

완료율, 반복 실행의 안정성, 비용, 소요 시간, 안전성을 따로 기록하고 실행 기록과 검증 결과를 보관하세요. [비교 기록 템플릿](docs/comparison-template.md)과 [연구 및 방법론](docs/research.md)을 참고할 수 있습니다.

에이전트용: [Markdown 요약](site/agent.md) · [JSON 데이터](data/catalog.json) · [필드 정의](data/catalog.schema.json) · [저장소 관리 규칙](AGENTS.md)

출처에 접근할 수 있는지 매주 확인합니다. 카탈로그에 포함되었다고 재현까지 검증된 것은 아닙니다. 자세한 내용은 [데이터와 출처 안내](data/README.md)를 참고하세요.

## 개선에 참여하기

빠진 항목, 잘못된 설명, 깨진 링크를 발견했다면 [기여 안내](CONTRIBUTING.md)에 따라 issue나 PR을 보내 주세요. 원문 링크와 짧은 설명이면 충분합니다. 평가 방법이나 비교에 관한 질문은 [Discussions](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)에서 나눌 수 있습니다.
