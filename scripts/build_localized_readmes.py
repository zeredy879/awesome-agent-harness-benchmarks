#!/usr/bin/env python3
"""Generate concise localized selection guides from the canonical inventory."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
ENTRIES = CATALOG["entries"]
BY_ID = {entry["id"]: entry for entry in ENTRIES}
CATEGORY_COUNT = len({entry["category"] for entry in ENTRIES})
SITE_URL = "https://zeredy879.github.io/awesome-agent-harness-benchmarks/"
# Keep first-time-reader labels short; the catalog retains full record names.
DISPLAY_NAMES = {
    "swe-bench": "SWE-bench",
    "osworld": "OSWorld",
    "harness-bench-qihoo": "Harness-Bench",
    "clawbench-openclaw": "ShellBench",
}

LOCALES = {
    "zh": {
        "file": "README.zh-CN.md",
        "subtitle": "按任务挑选 AI Agent 评测，了解它测什么、如何评分，以及结果有哪些局限。",
        "site": "浏览可搜索的评测目录 →",
        "nav": "[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md)",
        "scope": "收录 {entries} 项公开评测及相关资料，覆盖 {categories} 个领域。",
        "choose": "按任务选评测",
        "columns": ("想测试什么", "从这里开始"),
        "rows": [
            ("修复代码仓库中的问题", "swe-bench"),
            ("完成终端任务", "terminal-bench"),
            ("调用工具并维护状态", "toolsandbox"),
            ("操作网站完成任务", "webarena"),
            ("使用桌面应用", "osworld"),
            ("记住并查找历史对话中的信息", "longmemeval"),
            ("抵御工具输出中的提示注入", "agentdojo"),
            ("查资料、用工具解决综合问题", "gaia"),
        ],
        "more": "更多选择见[完整目录](docs/catalog.md)，每项均附有评分方式、运行环境和具体局限。",
        "harness": "比较 Harness",
        "definition": "**Agent harness** 是模型的配套软件，负责工具调用、上下文管理、记忆、权限控制和故障恢复。想研究这些部分，可以从以下项目入手：",
        "harness_rows": [
            ("harness-bench-qihoo", "比较不同模型与 harness 组合在本地工作区中的表现。"),
            ("clawbench-openclaw", "原名 ClawBench。通过执行记录和多次运行，评估整个 Agent 配置的可靠性。"),
            ("skillsbench", "对照有无技能包时的任务表现。"),
        ],
        "separator": "：",
        "data": "数据与比较方法",
        "method": "多数评测衡量的是整个 Agent。比较 harness 时，先说明要改变什么：比较整套配置，可以保留各自的提示词、工具和默认设置。测试单个组件，则只改变该组件。除本次比较刻意改变的部分外，其余条件应保持一致，例如模型、任务、环境、预算和评分规则。",
        "report": "分别记录完成率、重复运行的稳定性、成本、耗时和安全问题，并保留执行记录与验证结果。可直接使用[比较记录模板](docs/comparison-template.md)，或查阅[研究与方法说明](docs/research.md)。",
        "agent_links": "供 Agent 读取：[Markdown 摘要](site/agent.md) · [JSON 数据](data/catalog.json) · [字段定义](data/catalog.schema.json) · [维护约定](AGENTS.md)",
        "provenance": "每周检查来源可用性。收录不代表独立复现，详见[数据与来源说明](data/README.md)。",
        "contribute": "参与完善",
        "contribution": "发现遗漏、错误或失效链接？欢迎按[贡献指南](CONTRIBUTING.md)提交 issue 或 PR，附上原始来源和简短说明。评测方法与比较问题可在[讨论区](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)交流。",
    },
    "ja": {
        "file": "README.ja.md",
        "subtitle": "AI エージェントで試したい作業に合うベンチマークを選び、評価内容・採点方法・限界を確認できます。",
        "site": "ベンチマークを検索する →",
        "nav": "[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [한국어](README.ko.md)",
        "scope": "公開ベンチマークや関連資料を {entries} 件、{categories} 分野にわたって収録しています。",
        "choose": "試したい作業から選ぶ",
        "columns": ("試したいこと", "まず見るベンチマーク"),
        "rows": [
            ("コードの不具合を修正する", "swe-bench"),
            ("ターミナルで作業を完了する", "terminal-bench"),
            ("状態を管理しながらツールを使う", "toolsandbox"),
            ("Web サイト上で作業する", "webarena"),
            ("デスクトップアプリを使う", "osworld"),
            ("過去の会話を覚えて情報を取り出す", "longmemeval"),
            ("ツール出力からのプロンプトインジェクションを防ぐ", "agentdojo"),
            ("情報を調べ、ツールを使って問題を解く", "gaia"),
        ],
        "more": "ほかの候補は[全件カタログ](docs/catalog.md)にまとめています。各項目で採点方法、実行環境、評価の限界を確認できます。",
        "harness": "Harness を比較する",
        "definition": "**Agent harness** は、モデルのツール利用、会話の文脈や記憶、権限、エラーからの復旧を管理するソフトウェアです。これらを調べるには、次のプロジェクトが参考になります。",
        "harness_rows": [
            ("harness-bench-qihoo", "モデルと harness の組み合わせを、ローカルの作業環境で比較します。"),
            ("clawbench-openclaw", "旧 ClawBench。実行記録と繰り返しの試行から、エージェント全体の信頼性を評価します。"),
            ("skillsbench", "スキルパッケージの有無で、タスクの成績がどう変わるかを調べます。"),
        ],
        "separator": "：",
        "data": "データと比較方法",
        "method": "多くのベンチマークが測るのは、エージェント全体の性能です。harness を比較する際は、何を変えるかを先に決めます。構成全体の比較なら、各構成のプロンプト、ツール、標準設定を含めて比較できます。一つの機能の効果を調べるなら、その機能だけを変えます。モデル、タスク、環境、予算、採点基準など、比較対象に含めない条件は揃えます。",
        "report": "完了率、繰り返したときの安定性、費用、所要時間、安全性を分けて記録し、実行履歴と検証結果を残します。[比較記録テンプレート](docs/comparison-template.md)と[調査・方法論ノート](docs/research.md)を利用できます。",
        "agent_links": "エージェント向け：[Markdown 要約](site/agent.md) · [JSON データ](data/catalog.json) · [フィールド定義](data/catalog.schema.json) · [保守ルール](AGENTS.md)",
        "provenance": "出典にアクセスできるかを毎週確認しています。掲載は独立した追試を意味しません。詳しくは[データと出典について](data/README.md)をご覧ください。",
        "contribute": "改善に参加する",
        "contribution": "掲載漏れ、説明の誤り、リンク切れは、[貢献ガイド](CONTRIBUTING.md)に沿って issue や PR でお知らせください。原典へのリンクと短い説明があれば十分です。評価方法や比較の相談には[ディスカッション](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)をご利用ください。",
    },
    "ko": {
        "file": "README.ko.md",
        "subtitle": "AI 에이전트가 수행할 작업에 맞는 벤치마크를 찾고, 평가 내용과 채점 방식, 한계를 확인하세요.",
        "site": "벤치마크 검색하기 →",
        "nav": "[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어",
        "scope": "공개 벤치마크와 관련 자료 {entries}개를 {categories}개 분야로 정리했습니다.",
        "choose": "평가할 작업으로 고르기",
        "columns": ("평가할 작업", "먼저 살펴볼 벤치마크"),
        "rows": [
            ("코드 저장소의 문제 수정", "swe-bench"),
            ("터미널 작업 완료", "terminal-bench"),
            ("상태를 관리하며 도구 사용", "toolsandbox"),
            ("웹사이트에서 작업 수행", "webarena"),
            ("데스크톱 앱 사용", "osworld"),
            ("지난 대화를 기억하고 정보 찾기", "longmemeval"),
            ("도구 출력의 프롬프트 인젝션 방어", "agentdojo"),
            ("정보를 찾고 도구를 써서 문제 해결", "gaia"),
        ],
        "more": "다른 후보는 [전체 카탈로그](docs/catalog.md)에서 찾아볼 수 있습니다. 각 항목에 채점 방식, 실행 환경, 구체적인 한계가 정리되어 있습니다.",
        "harness": "Harness 비교하기",
        "definition": "**Agent harness**는 모델의 도구 사용, 컨텍스트, 메모리, 권한, 오류 복구를 관리하는 소프트웨어입니다. 이 부분을 평가하려면 다음 프로젝트부터 살펴보세요.",
        "harness_rows": [
            ("harness-bench-qihoo", "모델과 harness의 조합을 로컬 작업 환경에서 비교합니다."),
            ("clawbench-openclaw", "이전 이름은 ClawBench입니다. 실행 기록과 반복 실행을 통해 에이전트 전체 구성의 신뢰성을 평가합니다."),
            ("skillsbench", "스킬 패키지가 있을 때와 없을 때의 작업 성과를 비교합니다."),
        ],
        "separator": ": ",
        "data": "데이터와 비교 방법",
        "method": "대부분의 벤치마크는 에이전트 전체의 성능을 측정합니다. harness를 비교하려면 먼저 무엇을 바꿀지 정하세요. 전체 구성을 비교할 때는 각 구성의 프롬프트, 도구, 기본 설정을 포함할 수 있습니다. 특정 기능의 효과를 확인할 때는 그 기능만 바꿉니다. 모델, 과제, 환경, 예산, 채점 기준 등 비교 대상에 포함하지 않은 조건은 동일하게 맞춥니다.",
        "report": "완료율, 반복 실행의 안정성, 비용, 소요 시간, 안전성을 따로 기록하고 실행 기록과 검증 결과를 보관하세요. [비교 기록 템플릿](docs/comparison-template.md)과 [연구 및 방법론](docs/research.md)을 참고할 수 있습니다.",
        "agent_links": "에이전트용: [Markdown 요약](site/agent.md) · [JSON 데이터](data/catalog.json) · [필드 정의](data/catalog.schema.json) · [저장소 관리 규칙](AGENTS.md)",
        "provenance": "출처에 접근할 수 있는지 매주 확인합니다. 카탈로그에 포함되었다고 재현까지 검증된 것은 아닙니다. 자세한 내용은 [데이터와 출처 안내](data/README.md)를 참고하세요.",
        "contribute": "개선에 참여하기",
        "contribution": "빠진 항목, 잘못된 설명, 깨진 링크를 발견했다면 [기여 안내](CONTRIBUTING.md)에 따라 issue나 PR을 보내 주세요. 원문 링크와 짧은 설명이면 충분합니다. 평가 방법이나 비교에 관한 질문은 [Discussions](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)에서 나눌 수 있습니다.",
    },
}


def entry_link(entry_id: str) -> str:
    entry = BY_ID[entry_id]
    name = DISPLAY_NAMES.get(entry_id, entry["name"])
    return f"[{name}]({entry['url']})"


def render(text: dict) -> str:
    lines = [
        "# Awesome Agent Harness Benchmarks",
        "",
        text["subtitle"],
        "",
        f"**[{text['site']}]({SITE_URL})**",
        "",
        text["nav"],
        "",
        text["scope"].format(entries=len(ENTRIES), categories=CATEGORY_COUNT),
        "",
        f"## {text['choose']}",
        "",
        f"| {text['columns'][0]} | {text['columns'][1]} |",
        "| --- | --- |",
    ]
    for scenario, entry_id in text["rows"]:
        lines.append(f"| {scenario} | {entry_link(entry_id)} |")
    lines.extend([
        "", text["more"],
        "", f"## {text['harness']}",
        "", text["definition"], "",
    ])
    for entry_id, description in text["harness_rows"]:
        lines.append(f"- {entry_link(entry_id)}{text['separator']}{description}")
    lines.extend([
        "", f"## {text['data']}",
        "", text["method"],
        "", text["report"],
        "", text["agent_links"],
        "", text["provenance"],
        "", f"## {text['contribute']}",
        "", text["contribution"], "",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    for text in LOCALES.values():
        (ROOT / text["file"]).write_text(render(text), encoding="utf-8")
