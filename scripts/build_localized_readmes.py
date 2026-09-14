#!/usr/bin/env python3
"""Generate localized benchmark-selection guides from the canonical inventory."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
ENTRIES = CATALOG["entries"]
BY_ID = {entry["id"]: entry for entry in ENTRIES}
KINDS = Counter(entry["kind"] for entry in ENTRIES)
CATEGORY_COUNT = len({entry["category"] for entry in ENTRIES})
SITE_URL = "https://zeredy879.github.io/awesome-agent-harness-benchmarks/"

LOCALES = {
    "zh": {
        "file": "README.zh-CN.md",
        "subtitle": "为你的 Agent 选对评测：先看任务、判分方式和局限，再比较分数。",
        "site": "打开可搜索的评测目录 →",
        "site_hint": "按能力筛选，查看每项评测的原始来源、运行环境和适用边界。",
        "nav": "[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md)",
        "stats": "资料快照：{date} · {entries} 条记录 · {benchmarks} 个评测套件 · {categories} 类能力",
        "intro": "这里的 **harness** 指模型之外负责工具调用、上下文、记忆、权限与执行控制的系统。本目录帮你找到适合测试这些环节的公开评测，并说明结果能支持什么结论。",
        "choose": "你想验证什么？",
        "choose_intro": "下面是按用途挑选的起点，不是排名。完整目录还收录了其他任务、版本和研究。",
        "columns": ("评测目标", "从这里开始", "怎么衡量", "比较前要注意"),
        "rows": [
            ("修复真实代码仓库中的问题", "swe-bench", "通过修复测试和回归测试", "不同赛道的任务、语言和判分方式不同，分数不能直接互换。"),
            ("完成复杂终端任务", "terminal-bench", "运行任务专用验证器", "固定数据集版本；成绩同时受模型与 harness 影响。"),
            ("调用工具并维护状态", "toolsandbox", "检查中间里程碑与最终状态", "用户模拟器和工具接口都会影响结果。"),
            ("操作网站完成任务", "webarena", "检查网页应用的功能状态", "固定环境配置、任务版本和评测器修订。"),
            ("跨桌面应用完成工作", "osworld", "根据实际执行结果判分", "虚拟机镜像、步数预算和评测版本必须一致。"),
            ("从长期对话中找到并更新信息", "longmemeval", "衡量历史信息问答准确率", "需要完整上下文基线；答对问题不等于完成多步任务。"),
            ("抵御工具环境中的提示注入", "agentdojo", "同时衡量正常任务表现与攻击成功率", "固定威胁模型和攻击预算；安全分数要与可用性一起看。"),
            ("借助工具搜集信息并推理", "gaia", "衡量最终答案准确率", "最终答案难以反映执行过程中的副作用和安全问题。"),
        ],
        "interpret": "这些分数说明了什么？",
        "interpret_intro": "多数评测衡量的是整个 Agent 的表现。要把差异归因于 harness，就需要在相同模型、任务和预算下做受控比较；收录于本目录不代表某个项目已经做过这样的实验。",
        "kinds": [
            "**benchmark**：带任务和评测器的套件，用来运行测试。",
            "**study**：比较研究，用来了解实验设计与已有证据。",
            "**infrastructure**：运行或审计评测的工具，本身不是一组测试题。",
            "**watchlist**：早期或适用范围较窄的候选项目，需要进一步核实。",
        ],
        "proposal": "比较模板和评测方案只说明实验应该怎样设计，不代表已经运行的结果或榜单。",
        "browse": "按问题继续查找",
        "browse_intro": "[完整目录](docs/catalog.md)保留所有条目的说明和来源。也可以直接跳到相关类别：",
        "categories": [
            ("direct", "Harness 直接对比"), ("coding", "代码与终端"), ("tools", "工具与状态"),
            ("browser", "浏览器"), ("computer", "桌面与移动端"), ("general", "通用任务"),
            ("memory", "记忆与上下文"), ("long-horizon", "长时间任务"), ("safety", "安全"),
            ("multi-agent", "多 Agent 协作"), ("research", "研究任务"), ("skills", "技能与指令"),
            ("infrastructure", "评测基础设施"),
        ],
        "compare": "准备做一次比较？",
        "compare_intro": "从[比较记录模板](docs/comparison-template.md)开始，把实验条件和结果放在一起记录：",
        "comparison": [
            "固定模型、提示词、工具接口、任务版本、环境、预算和重试策略。",
            "分别报告任务完成率、波动、成本、延迟与安全问题，保留执行轨迹和验证输出。",
            "用[研究说明](docs/research.md)检查证据强度与可比性，再解释差异。",
        ],
        "agent": "供 Agent 读取",
        "agent_intro": "自动检索和整理时，可直接读取以下入口：",
        "agent_links": [
            ("带说明的 Markdown 目录", "site/agent.md"),
            ("结构化数据", "data/catalog.json"),
            ("字段定义", "data/catalog.schema.json"),
            ("仓库维护约定", "AGENTS.md"),
        ],
        "evidence": "来源与贡献",
        "evidence_text": "优先引用官方仓库、论文和项目页面。[来源检查记录](data/source-audit.json)反映特定时间的链接可用性与元数据，不代表独立复现。收录也不等于推荐；本目录不承诺覆盖所有公开或私有评测。",
        "contribute": "发现遗漏、失效链接或不准确的描述？欢迎按[贡献指南](CONTRIBUTING.md)提交 issue 或 PR，并附上原始来源及一项具体局限。评测方法或 benchmark 比较问题，也欢迎在[讨论区](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)交流。",
    },
    "ja": {
        "file": "README.ja.md",
        "subtitle": "エージェントの目的に合う評価を選ぶために。スコアの前に、タスク・採点方法・限界を確かめる。",
        "site": "検索できる評価カタログを開く →",
        "site_hint": "能力別に絞り込み、原典・実行環境・評価の限界を確認できます。",
        "nav": "[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [한국어](README.ko.md)",
        "stats": "資料の基準日：{date} · 収録 {entries} 件 · 評価スイート {benchmarks} 件 · {categories} 分野",
        "intro": "ここでいう **harness** は、モデルの周りでツール呼び出し、コンテキスト、メモリ、権限、実行の制御を担う仕組みです。このカタログでは、それぞれを試すための公開評価を探し、結果から何が言えるのかを確認できます。",
        "choose": "何を確かめたいですか？",
        "choose_intro": "用途に応じた出発点をまとめました。ランキングではありません。全件カタログには、ほかのタスクやバージョン、比較研究も収録しています。",
        "columns": ("確かめたいこと", "最初に見る評価", "採点方法", "比較する際の注意点"),
        "rows": [
            ("実際のリポジトリで不具合を修正する", "swe-bench", "修正確認テストと回帰テスト", "トラックごとにタスク・言語・評価方法が異なり、スコアは直接比較できません。"),
            ("複雑なターミナル作業を完了する", "terminal-bench", "タスクごとの検証プログラム", "データセットの版を固定してください。成績にはモデルと harness の両方が影響します。"),
            ("状態を保ちながらツールを使う", "toolsandbox", "途中の到達点と最終状態", "ユーザーシミュレータとツールのインターフェースも結果を左右します。"),
            ("Web サイト上で作業を完了する", "webarena", "Web アプリの機能・状態の検査", "環境設定、タスク、評価器の修正を含め、バージョンを揃える必要があります。"),
            ("複数のデスクトップアプリを操作する", "osworld", "実行結果に基づく検査", "仮想マシンのイメージ、操作回数の上限、評価の版を揃えてください。"),
            ("長い会話履歴から情報を取り出す", "longmemeval", "履歴に関する質問への正答率", "履歴全体を与えるベースラインが必要です。質問応答は一連の作業の完了とは異なります。"),
            ("ツール利用中のプロンプトインジェクションに対処する", "agentdojo", "通常タスクの成績と攻撃成功率", "脅威モデルと攻撃の予算を固定し、安全性と実用性を併せて見ます。"),
            ("ツールを使って情報を集め、推論する", "gaia", "最終回答の正答率", "最終回答だけでは、途中の副作用や実行の安全性はわかりません。"),
        ],
        "interpret": "スコアからわかること",
        "interpret_intro": "多くの評価が測るのは、エージェント全体の性能です。harness による差を調べるには、同じモデル・タスク・予算で条件を揃えて比較する必要があります。収録したすべてのプロジェクトが、その実験を行っているわけではありません。",
        "kinds": [
            "**benchmark**：タスクと評価器を備えた、テストを実行するためのスイート。",
            "**study**：比較研究。実験設計や、すでに得られた根拠を確認するための資料。",
            "**infrastructure**：評価の実行や監査を支えるツール。タスク集そのものではありません。",
            "**watchlist**：公開初期、または対象が限定的な候補。追加の確認が必要です。",
        ],
        "proposal": "比較テンプレートや評価の提案は実験設計のためのもので、実測結果やランキングではありません。",
        "browse": "分野から探す",
        "browse_intro": "説明と原典を含む[全件カタログ](docs/catalog.md)も用意しています。各分野へ直接進めます：",
        "categories": [
            ("direct", "Harness の直接比較"), ("coding", "コード・ターミナル"), ("tools", "ツール・状態管理"),
            ("browser", "ブラウザ"), ("computer", "デスクトップ・モバイル"), ("general", "汎用タスク"),
            ("memory", "メモリ・コンテキスト"), ("long-horizon", "長時間のタスク"), ("safety", "安全性"),
            ("multi-agent", "複数エージェントの協調"), ("research", "研究タスク"), ("skills", "スキル・指示"),
            ("infrastructure", "評価基盤"),
        ],
        "compare": "自分で比較するには",
        "compare_intro": "[比較記録テンプレート](docs/comparison-template.md)を使い、実験条件と結果をまとめて残してください：",
        "comparison": [
            "モデル、プロンプト、ツールの仕様、タスクの版、環境、予算、再試行方針を固定する。",
            "完了率、ばらつき、費用、所要時間、安全性の問題を分けて報告し、実行履歴と検証結果を保存する。",
            "[調査ノート](docs/research.md)で根拠の強さと比較条件を確認してから、差を解釈する。",
        ],
        "agent": "エージェントから利用する",
        "agent_intro": "自動で検索・整理する場合は、次の入口を利用できます：",
        "agent_links": [
            ("説明付き Markdown カタログ", "site/agent.md"),
            ("構造化データ", "data/catalog.json"),
            ("フィールド定義", "data/catalog.schema.json"),
            ("リポジトリの保守ルール", "AGENTS.md"),
        ],
        "evidence": "出典と改善への参加",
        "evidence_text": "公式リポジトリ、論文、プロジェクトページを優先しています。[出典の確認記録](data/source-audit.json)は、ある時点のアクセス可否とメタデータを記録したもので、独立した追試ではありません。掲載は推奨を意味せず、公開・非公開の全評価を網羅するものでもありません。",
        "contribute": "掲載漏れ、リンク切れ、説明の誤りを見つけたら、[コントリビューションガイド](CONTRIBUTING.md)に沿って issue や PR をお寄せください。原典と、評価の具体的な限界も添えていただけると助かります。評価方法やベンチマーク比較の相談は、[ディスカッション](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)へどうぞ。",
    },
    "ko": {
        "file": "README.ko.md",
        "subtitle": "내 에이전트에 맞는 평가를 찾으세요. 점수를 비교하기 전에 과제, 채점 방식, 한계를 살펴볼 수 있습니다.",
        "site": "검색 가능한 평가 카탈로그 열기 →",
        "site_hint": "평가할 역량으로 범위를 좁히고, 원문 출처와 실행 환경, 평가의 한계를 확인하세요.",
        "nav": "[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어",
        "stats": "자료 기준일: {date} · 전체 {entries}개 항목 · 평가 모음 {benchmarks}개 · {categories}개 분야",
        "intro": "여기서 **harness**는 모델 주변에서 도구 호출, 컨텍스트, 메모리, 권한, 실행 흐름을 관리하는 시스템을 뜻합니다. 이 카탈로그는 각 기능을 시험할 공개 평가를 찾고, 결과가 뒷받침하는 결론의 범위를 파악하도록 돕습니다.",
        "choose": "무엇을 확인하고 싶나요?",
        "choose_intro": "목적에 따라 먼저 살펴볼 평가를 골랐습니다. 순위표는 아닙니다. 전체 카탈로그에서 다른 과제, 버전, 비교 연구도 확인할 수 있습니다.",
        "columns": ("평가할 작업", "먼저 살펴볼 평가", "채점 방식", "비교할 때 주의할 점"),
        "rows": [
            ("실제 코드 저장소의 문제 수정", "swe-bench", "수정 검증 테스트와 회귀 테스트", "트랙마다 과제, 언어, 평가 방식이 달라 점수를 그대로 비교할 수 없습니다."),
            ("복잡한 터미널 작업 완료", "terminal-bench", "과제별 검증 프로그램 실행", "데이터셋 버전을 고정해야 합니다. 점수에는 모델과 harness가 모두 영향을 줍니다."),
            ("상태를 유지하며 도구 사용", "toolsandbox", "중간 단계와 최종 상태 확인", "사용자 시뮬레이터와 도구 인터페이스도 결과에 영향을 줍니다."),
            ("웹사이트에서 작업 완료", "webarena", "웹 앱의 기능과 상태 확인", "환경 설정, 과제, 평가기의 수정 사항까지 버전을 맞춰야 합니다."),
            ("여러 데스크톱 앱을 오가며 작업", "osworld", "실행 결과에 따른 검증", "가상 머신 이미지, 최대 행동 횟수, 평가 버전이 같아야 합니다."),
            ("긴 대화 기록에서 정보 찾기", "longmemeval", "과거 기록에 대한 질의응답 정확도", "전체 컨텍스트를 제공한 기준선이 필요합니다. 정답을 찾는 것과 여러 단계의 작업을 끝내는 것은 다릅니다."),
            ("도구 환경의 프롬프트 인젝션 방어", "agentdojo", "정상 작업 성능과 공격 성공률", "위협 모델과 공격 예산을 고정하고, 안전성과 유용성을 함께 봐야 합니다."),
            ("도구로 정보를 수집하고 추론", "gaia", "최종 답변 정확도", "최종 답변만으로는 실행 중의 부작용과 안전 문제를 파악하기 어렵습니다."),
        ],
        "interpret": "점수가 말해 주는 것",
        "interpret_intro": "대부분의 평가는 에이전트 전체의 성능을 측정합니다. 차이의 원인을 harness에서 찾으려면 모델, 과제, 예산을 동일하게 두고 비교해야 합니다. 이 카탈로그에 실렸다고 해서 해당 프로젝트가 이런 실험을 수행했다는 뜻은 아닙니다.",
        "kinds": [
            "**benchmark**: 과제와 평가기를 갖춘 평가 모음으로, 테스트를 실행할 때 사용합니다.",
            "**study**: 실험 설계와 기존 근거를 살펴볼 수 있는 비교 연구입니다.",
            "**infrastructure**: 평가 실행이나 감사를 돕는 도구이며, 그 자체가 과제 모음은 아닙니다.",
            "**watchlist**: 초기 단계이거나 범위가 좁은 후보로, 추가 확인이 필요합니다.",
        ],
        "proposal": "비교 템플릿과 평가 제안은 실험 설계를 돕는 자료이며, 실제 측정 결과나 순위표가 아닙니다.",
        "browse": "분야별로 더 찾아보기",
        "browse_intro": "[전체 카탈로그](docs/catalog.md)에 각 항목의 설명과 출처를 모았습니다. 관심 있는 분야로 바로 이동할 수도 있습니다:",
        "categories": [
            ("direct", "Harness 직접 비교"), ("coding", "코드·터미널"), ("tools", "도구·상태 관리"),
            ("browser", "브라우저"), ("computer", "데스크톱·모바일"), ("general", "범용 작업"),
            ("memory", "메모리·컨텍스트"), ("long-horizon", "장시간 작업"), ("safety", "안전성"),
            ("multi-agent", "여러 에이전트의 협업"), ("research", "연구 작업"), ("skills", "스킬·지시 이행"),
            ("infrastructure", "평가 기반 도구"),
        ],
        "compare": "직접 비교하려면",
        "compare_intro": "[비교 기록 템플릿](docs/comparison-template.md)을 사용해 실험 조건과 결과를 함께 기록하세요:",
        "comparison": [
            "모델, 프롬프트, 도구 명세, 과제 버전, 환경, 예산, 재시도 정책을 고정합니다.",
            "완료율, 편차, 비용, 지연 시간, 안전 문제를 따로 보고하고 실행 기록과 검증 출력을 보관합니다.",
            "[조사 노트](docs/research.md)에서 근거의 수준과 비교 조건을 확인한 뒤 차이를 해석합니다.",
        ],
        "agent": "에이전트에서 읽기",
        "agent_intro": "자동으로 검색하거나 정리할 때는 다음 자료를 바로 읽을 수 있습니다:",
        "agent_links": [
            ("설명이 포함된 Markdown 카탈로그", "site/agent.md"),
            ("구조화된 데이터", "data/catalog.json"),
            ("필드 정의", "data/catalog.schema.json"),
            ("저장소 유지보수 규칙", "AGENTS.md"),
        ],
        "evidence": "출처와 기여",
        "evidence_text": "공식 저장소, 논문, 프로젝트 페이지를 우선합니다. [출처 확인 기록](data/source-audit.json)은 특정 시점의 접근 가능 여부와 메타데이터를 담으며, 독립적인 재현 실험을 뜻하지 않습니다. 수록 자체가 추천을 의미하지 않으며, 모든 공개·비공개 평가를 망라하지는 않습니다.",
        "contribute": "빠진 평가, 깨진 링크, 잘못된 설명을 발견했다면 [기여 안내](CONTRIBUTING.md)에 따라 issue나 PR을 보내 주세요. 원문 출처와 평가의 구체적인 한계도 함께 알려 주시면 좋습니다. 평가 방법이나 벤치마크 비교에 대한 질문은 [Discussions](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)에서 함께 이야기할 수 있습니다.",
    },
}


def render(text: dict) -> str:
    lines = [
        "# Awesome Agent Harness Benchmarks",
        "",
        text["subtitle"],
        "",
        f"## [{text['site']}]({SITE_URL})",
        "",
        text["site_hint"],
        "",
        text["nav"],
        "",
        text["stats"].format(
            date=CATALOG["as_of"], entries=len(ENTRIES),
            benchmarks=KINDS["benchmark"], categories=CATEGORY_COUNT,
        ),
        "",
        text["intro"],
        "",
        f"## {text['choose']}",
        "",
        text["choose_intro"],
        "",
        "| " + " | ".join(text["columns"]) + " |",
        "| --- | --- | --- | --- |",
    ]
    for scenario, entry_id, grading, caveat in text["rows"]:
        entry = BY_ID[entry_id]
        lines.append(f"| {scenario} | [{entry['name']}]({entry['url']}) | {grading} | {caveat} |")
    lines.extend(["", f"## {text['interpret']}", "", text["interpret_intro"], ""])
    lines.extend(f"- {kind}" for kind in text["kinds"])
    lines.extend(["", text["proposal"]])
    lines.extend(["", f"## {text['browse']}", "", text["browse_intro"], ""])
    # Group related areas into short lines rather than repeat the full inventory.
    for start, end in ((0, 3), (3, 6), (6, 9), (9, 13)):
        links = [f"[{label}](docs/catalog.md#{category})" for category, label in text["categories"][start:end]]
        lines.extend([" · ".join(links), ""])
    lines.extend([f"## {text['compare']}", "", text["compare_intro"], ""])
    lines.extend(f"{number}. {step}" for number, step in enumerate(text["comparison"], 1))
    lines.extend(["", f"## {text['agent']}", "", text["agent_intro"], ""])
    lines.extend(f"- [{label}]({url})" for label, url in text["agent_links"])
    lines.extend(["", f"## {text['evidence']}", "", text["evidence_text"], "", text["contribute"], ""])
    return "\n".join(lines)


if __name__ == "__main__":
    for text in LOCALES.values():
        (ROOT / text["file"]).write_text(render(text), encoding="utf-8")
