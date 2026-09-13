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
        "subtitle": "面向人类阅读和 Agent 检索的公开 Agent Harness benchmark、受控研究与评测基础设施目录。",
        "nav": "语言： [English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md)",
        "snapshot": "快照",
        "scope": "范围",
        "scope_text": "公开 benchmark、受控研究和与 Agent Harness 相关的评测基础设施；这是有日期的公开资料快照，不宣称覆盖所有私有评测。",
        "entries": "条目",
        "areas": "能力领域",
        "audit": "GitHub 来源记录",
        "links": "入口",
        "site": "人类可读 Pages",
        "agent": "Agent Markdown",
        "json": "机器可读 JSON",
        "research": "研究笔记",
        "source": "来源审计",
        "overview": "快速开始",
        "overview_text": "如果你要比较 Harness 本身，先看直接对比；如果你要测某个子系统，再选择对应能力类别。公平比较时固定模型端点、prompt、工具 schema、任务版本、sandbox、预算、重试策略和随机种子。",
        "recent": "近期新增与复核（2025–2026）",
        "recent_text": "下面列出 2026 年 9 月扫描中新增或重新核验的项目。条目名称与来源链接保持原文，避免社区项目的技术专名被误译；完整字段和局限见 Agent Markdown 与 JSON。",
        "catalog": "完整分类目录",
        "detail": "详细资料",
        "detail_text": "完整英文说明见 [README.md](README.md)。适合 Agent 直接读取的字段见 [site/agent.md](site/agent.md) 和 [data/catalog.json](data/catalog.json)。",
        "original": "原始摘要",
    },
    "ja": {
        "file": "README.ja.md",
        "title": "Agent Harness Benchmark 日本語カタログ",
        "subtitle": "人間と Agent の両方が読める、公開 Agent Harness benchmark・比較研究・評価インフラのカタログです。",
        "nav": "言語： [English](README.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)",
        "snapshot": "スナップショット",
        "scope": "範囲",
        "scope_text": "公開 benchmark、比較研究、Agent Harness に関係する評価インフラ。日付付きの公開資料インベントリであり、非公開評価を網羅する主張ではありません。",
        "entries": "エントリ数",
        "areas": "能力領域",
        "audit": "GitHub ソース記録",
        "links": "入口",
        "site": "人間向け Pages",
        "agent": "Agent Markdown",
        "json": "機械可読 JSON",
        "research": "研究ノート",
        "source": "ソース監査",
        "overview": "クイックスタート",
        "overview_text": "Harness 自体を比較する場合は直接比較から始め、特定のサブシステムを測る場合は能力カテゴリを選びます。公平な比較ではモデル、prompt、tool schema、タスク版、sandbox、予算、retry、seed を固定します。",
        "recent": "最近の追加・再確認（2025–2026）",
        "recent_text": "2026 年 9 月のスキャンで追加または再確認した項目です。固有名詞と原典リンクは誤訳を避けるため原文のままです。完全なフィールドと制約は Agent Markdown と JSON を参照してください。",
        "catalog": "完全カテゴリ一覧",
        "detail": "詳細",
        "detail_text": "完全な英語説明は [README.md](README.md) にあります。Agent 向けには [site/agent.md](site/agent.md) と [data/catalog.json](data/catalog.json) が安定した入口です。",
        "original": "原文概要",
    },
    "ko": {
        "file": "README.ko.md",
        "title": "Agent Harness Benchmark 한국어 카탈로그",
        "subtitle": "사람과 Agent가 함께 읽을 수 있는 공개 Agent Harness benchmark·비교 연구·평가 인프라 목록입니다.",
        "nav": "언어: [English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)",
        "snapshot": "스냅샷",
        "scope": "범위",
        "scope_text": "공개 benchmark, 통제된 비교 연구, Agent Harness 관련 평가 인프라를 다룹니다. 날짜가 있는 공개 자료 인벤토리이며 비공개 평가까지 모두 포함한다는 뜻은 아닙니다.",
        "entries": "항목 수",
        "areas": "능력 영역",
        "audit": "GitHub 소스 기록",
        "links": "입구",
        "site": "사람용 Pages",
        "agent": "Agent Markdown",
        "json": "기계 판독 JSON",
        "research": "연구 노트",
        "source": "소스 감사",
        "overview": "빠른 시작",
        "overview_text": "Harness 자체를 비교하려면 직접 비교 섹션부터 보고, 특정 하위 시스템은 능력 카테고리에서 고르세요. 공정한 비교를 위해 모델 endpoint, prompt, tool schema, task 버전, sandbox, 예산, retry 정책, random seed를 고정합니다.",
        "recent": "최근 추가·재검증（2025–2026）",
        "recent_text": "2026년 9월 스캔에서 추가하거나 다시 확인한 항목입니다. 프로젝트 고유명과 원문 링크는 오역을 피하기 위해 그대로 두었고, 전체 필드와 한계는 Agent Markdown과 JSON에 기록했습니다.",
        "catalog": "전체 카테고리 목록",
        "detail": "상세 정보",
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
