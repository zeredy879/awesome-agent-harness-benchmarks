#!/usr/bin/env python3
"""Generate concise localized README entry points from the canonical catalog."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
ENTRIES = CATALOG["entries"]
AUDIT = json.loads((ROOT / "data" / "source-audit.json").read_text(encoding="utf-8"))
AUDIT_COUNT = len(AUDIT.get("repositories", []))

CATEGORIES = {
    "direct": {"zh": "直接 Harness 对比", "ja": "Harness 直接比較", "ko": "Harness 직접 비교"},
    "tools": {"zh": "工具、API、MCP 与状态", "ja": "ツール・API・MCP・状態", "ko": "도구·API·MCP·상태"},
    "coding": {"zh": "编码与终端", "ja": "コーディングとターミナル", "ko": "코딩·터미널"},
    "browser": {"zh": "浏览器与 Web", "ja": "ブラウザと Web", "ko": "브라우저·Web"},
    "general": {"zh": "通用 Agent", "ja": "汎用エージェント", "ko": "범용 에이전트"},
    "memory": {"zh": "记忆与上下文", "ja": "メモリとコンテキスト", "ko": "메모리·컨텍스트"},
    "safety": {"zh": "安全与故障注入", "ja": "安全性と障害注入", "ko": "안전·장애 주입"},
    "long-horizon": {"zh": "长时程与常驻 Agent", "ja": "長期・常駐エージェント", "ko": "장기·상시 에이전트"},
    "infrastructure": {"zh": "评测基础设施", "ja": "評価インフラ", "ko": "평가 인프라"},
    "computer": {"zh": "电脑与移动端", "ja": "コンピュータとモバイル", "ko": "컴퓨터·모바일"},
    "multi-agent": {"zh": "多 Agent", "ja": "マルチエージェント", "ko": "멀티 에이전트"},
    "research": {"zh": "科研工程", "ja": "研究エンジニアリング", "ko": "연구 엔지니어링"},
    "skills": {"zh": "Skills 与指令", "ja": "Skills と指示", "ko": "Skills·지시"},
}

LOCALES = {
    "zh": {
        "file": "README.zh-CN.md",
        "title": "Agent Harness Benchmark 中文目录",
        "subtitle": "面向人类与 Agent 的公开 Agent Harness 基准、受控研究和评测基础设施目录。",
        "nav": "语言： [English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md)",
        "snapshot": "快照日期",
        "scope": "收录范围",
        "scope_text": "公开 benchmark、受控研究以及与 Agent Harness 相关的评测基础设施。这是一份带日期的公开资料快照，不代表覆盖所有私有评测。",
        "entries": "条目",
        "areas": "能力领域",
        "audit": "GitHub 来源审计记录",
        "links": "快速入口",
        "site": "面向人类的 Pages",
        "agent": "Agent Markdown",
        "json": "机器可读 JSON",
        "research": "研究笔记",
        "source": "来源审计",
        "overview": "如何开始",
        "overview_text": "若要比较 Harness 本身，请先看“直接对比”；若要测试某个子系统，再按能力类别选择 benchmark。为保证比较公平，应固定模型端点、系统提示词、工具 schema、任务版本、sandbox 镜像、预算、重试策略和随机种子。",
        "recent": "近期新增与复核（2025–2026）",
        "recent_text": "以下项目是在 2026 年 9 月扫描中新增或重新核验的。项目名称和来源链接保留原文，以免误译技术专名；完整字段和局限请见 Agent Markdown 与 JSON。",
        "catalog": "按能力分类的完整目录",
        "detail": "进一步阅读",
        "detail_text": "完整的英文说明见 [README.md](README.md)。适合 Agent 直接读取的字段见 [site/agent.md](site/agent.md) 和 [data/catalog.json](data/catalog.json)。",
        "original": "原始摘要",
    },
    "ja": {
        "file": "README.ja.md",
        "title": "Agent Harness Benchmark 日本語カタログ",
        "subtitle": "人間と Agent の双方が読める、公開 Agent Harness benchmark・比較研究・評価インフラのカタログです。",
        "nav": "言語： [English](README.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)",
        "snapshot": "スナップショット日",
        "scope": "対象範囲",
        "scope_text": "公開 benchmark、比較研究、Agent Harness に関係する評価インフラを収録します。日付付きの公開資料インベントリであり、非公開評価を網羅するものではありません。",
        "entries": "エントリ数",
        "areas": "能力分野",
        "audit": "GitHub ソース監査記録",
        "links": "クイックリンク",
        "site": "人間向けの Pages",
        "agent": "Agent Markdown",
        "json": "機械可読 JSON",
        "research": "研究ノート",
        "source": "ソース監査",
        "overview": "始め方",
        "overview_text": "Harness 自体を比較する場合は「直接比較」から始め、特定のサブシステムを測る場合は能力カテゴリを選びます。公平な比較のため、モデル、システムプロンプト、tool schema、タスク版、sandbox イメージ、予算、retry 方針、random seed を固定してください。",
        "recent": "最近の追加・再確認（2025–2026）",
        "recent_text": "2026 年 9 月の調査で追加または再確認した項目です。固有名詞と原典リンクは誤訳を避けるため原文のままにしています。完全なフィールドと制約は Agent Markdown と JSON を参照してください。",
        "catalog": "全カテゴリ一覧",
        "detail": "詳しい情報",
        "detail_text": "詳しい英語の説明は [README.md](README.md) を参照してください。Agent 向けの安定した入口は [site/agent.md](site/agent.md) と [data/catalog.json](data/catalog.json) です。",
        "original": "原文概要",
    },
    "ko": {
        "file": "README.ko.md",
        "title": "Agent Harness Benchmark 한국어 카탈로그",
        "subtitle": "사람과 Agent 모두가 읽을 수 있는 공개 Agent Harness benchmark·비교 연구·평가 인프라 카탈로그입니다.",
        "nav": "언어: [English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)",
        "snapshot": "기준일",
        "scope": "범위",
        "scope_text": "공개 benchmark, 통제된 비교 연구, Agent Harness 관련 평가 인프라를 다룹니다. 날짜가 있는 공개 자료 인벤토리이며 비공개 평가까지 모두 포함한다는 뜻은 아닙니다.",
        "entries": "항목 수",
        "areas": "역량 영역",
        "audit": "GitHub 출처 감사 기록",
        "links": "빠른 링크",
        "site": "사람을 위한 Pages",
        "agent": "Agent Markdown",
        "json": "기계 판독 JSON",
        "research": "연구 노트",
        "source": "소스 감사",
        "overview": "시작하기",
        "overview_text": "Harness 자체를 비교하려면 ‘직접 비교’부터 확인하고, 특정 하위 시스템은 역량 카테고리에서 고르세요. 공정한 비교를 위해 모델 endpoint, 시스템 prompt, tool schema, task 버전, sandbox 이미지, 예산, retry 정책, random seed를 고정하세요.",
        "recent": "최근 추가·재검증（2025–2026）",
        "recent_text": "2026년 9월 조사에서 추가하거나 다시 확인한 항목입니다. 프로젝트 고유명과 원문 링크는 오역을 피하기 위해 그대로 두었고, 전체 필드와 한계는 Agent Markdown과 JSON에 기록했습니다.",
        "catalog": "전체 역량별 카탈로그",
        "detail": "자세한 정보",
        "detail_text": "전체 영어 설명은 [README.md](README.md)를 참고하세요. Agent가 바로 읽을 안정적인 입구는 [site/agent.md](site/agent.md)와 [data/catalog.json](data/catalog.json)입니다.",
        "original": "원문 요약",
    },
}


def render(locale: str, text: dict) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in ENTRIES:
        grouped[entry["category"]].append(entry)
    lines = [
        f"# {text['title']}",
        "",
        text["nav"],
        "",
        text["subtitle"],
        "",
        f"- {text['snapshot']}: `{CATALOG['as_of']}`",
        f"- {text['entries']}: **{len(ENTRIES)}**",
        f"- {text['areas']}: **{len(grouped)}**",
        f"- {text['audit']}: **{AUDIT_COUNT}**",
        f"- {text['scope']}: {text['scope_text']}",
        "",
        f"## {text['links']}",
        "",
        f"- [{text['site']}](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)",
        f"- [{text['agent']}](site/agent.md)",
        f"- [{text['json']}](data/catalog.json)",
        f"- [{text['research']}](docs/research.md)",
        f"- [{text['source']}](data/source-audit.json)",
        "",
        f"## {text['overview']}",
        "",
        text["overview_text"],
        "",
        f"## {text['recent']}",
        "",
        text["recent_text"],
        "",
    ]

    recent_ids = {
        "shellbench", "agent-race", "open-agentbench", "agentsuite", "coder-eval", "lemans",
        "agent-search-bench", "apex-agents-archipelago", "omnia-bench", "agentif-oneday", "agentif",
        "dataspace", "data-agent-benchmark", "agent-diff", "sciagentarena", "airs-bench", "infra-bench", "aobench",
        "swe-infrabench", "paperbench", "agent-action-bench", "browseruse-agent-bench", "browsecomp",
        "browsecomp-plus", "spreadsheetbench", "spreadsheetbench-2", "gittaskbench", "version-control-bench",
        "agentshield-benchmark", "agentre-bench", "cybench", "state-bench",
    }
    for entry in ENTRIES:
        if entry["id"] in recent_ids:
            lines.append(f"- [{entry['name']}]({entry['url']})")

    lines.extend(["", f"## {text['catalog']}", ""])
    for category in CATEGORIES:
        lines.extend([f"### {CATEGORIES[category][locale]}", ""])
        for entry in sorted(grouped.get(category, []), key=lambda item: item["name"].lower()):
            lines.append(f"- [{entry['name']}]({entry['url']})")
        lines.append("")

    lines.extend([f"## {text['detail']}", "", text["detail_text"], ""])
    return "\n".join(lines)


for locale, text in LOCALES.items():
    (ROOT / text["file"]).write_text(render(locale, text), encoding="utf-8")
