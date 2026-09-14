#!/usr/bin/env python3
"""Build the GitHub Pages site and Agent-readable Markdown exports.

The build has no third-party dependencies.  It turns the canonical catalog
into a small static site, a full Markdown digest, and stable JSON endpoints so
humans and agents can consume the same snapshot.
"""

from __future__ import annotations

import html
import json
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
CATALOG_PATH = ROOT / "data" / "catalog.json"
AUDIT_PATH = ROOT / "data" / "source-audit.json"
RESEARCH_PATH = ROOT / "docs" / "research.md"
SITE_URL = "https://zeredy879.github.io/awesome-agent-harness-benchmarks/"

CATEGORY_LABELS = {
    "direct": "Direct harness comparisons",
    "tools": "Tools, APIs, MCP, and state",
    "coding": "Coding and terminal",
    "browser": "Browser and web",
    "general": "General agents",
    "memory": "Memory and context",
    "safety": "Safety and failure injection",
    "long-horizon": "Long horizon and always-on",
    "infrastructure": "Evaluation infrastructure",
    "computer": "Computer and mobile",
    "multi-agent": "Multi-agent",
    "research": "Research engineering",
    "skills": "Skills and instructions",
}

# A small editorial order makes the first screen useful without implying a
# leaderboard. The remaining entries are kept discoverable by the sort menu.
FEATURED_IDS = [
    "harness-bench-qihoo",
    "swe-bench",
    "terminal-bench",
    "toolsandbox",
    "webarena",
    "osworld",
    "longmemeval",
    "agentdojo",
    "gaia",
    "skillsbench",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def static_card(entry: dict) -> str:
    """Render an indexable catalog card before JavaScript enhances the page."""
    signals = "".join(
        f'<span class="chip">{html.escape(signal)}</span>' for signal in entry["signals"]
    )
    paper = (
        f' · <a href="{html.escape(entry["paper"])}" target="_blank" rel="noreferrer">paper</a>'
        if entry.get("paper") else ""
    )
    category = html.escape(CATEGORY_LABELS.get(entry["category"], entry["category"]))
    kind_class = " kind-watchlist" if entry["kind"] == "watchlist" else ""
    return (
        '<article class="card">'
        f'<div class="card-top"><span class="category-pill">{category}</span>'
        f'<span class="kind-pill{kind_class}">{html.escape(entry["kind"])}</span></div>'
        f'<h3><a href="{html.escape(entry["url"])}" target="_blank" rel="noreferrer">'
        f'{html.escape(entry["name"])}</a></h3>'
        f'<p class="card-summary">{html.escape(entry["summary"])}</p>'
        f'<div class="signals">{signals}</div>'
        '<details class="card-details"><summary>Environment &amp; limitations</summary><dl>'
        f'<dt>Environment</dt><dd>{html.escape(entry["environment"])}</dd>'
        f'<dt>Limitation</dt><dd>{html.escape(entry["limitation"])}</dd>'
        '</dl></details>'
        f'<div class="card-bottom"><small>{html.escape(entry["grading"])}{paper}</small>'
        f'<a class="source-link" href="{html.escape(entry["url"])}" target="_blank" '
        'rel="noreferrer">View source ↗</a></div></article>'
    )


def agent_markdown(catalog: dict, audit: dict) -> str:
    entries = catalog["entries"]
    counts = Counter(entry["category"] for entry in entries)
    source_records = audit["repositories"]
    accessible = sum(record.get("status") == "source-accessible" for record in source_records)

    lines = [
        "# Agent Harness Benchmarks",
        "",
        "> Machine-readable Markdown snapshot. Use `catalog.json` for structured ingestion and `research.md` for methodology.",
        "",
        f"- Snapshot date: `{catalog['as_of']}`",
        f"- Entries: `{len(entries)}`",
        f"- Categories: `{len(counts)}`",
        f"- GitHub source records: `{len(source_records)}` (`{accessible}` accessible at audit time)",
        "- Scope: public benchmarks, controlled studies, and evaluation infrastructure relevant to agent harnesses",
        "",
        "## Category counts",
        "",
    ]
    for category, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{category}` - {CATEGORY_LABELS.get(category, category)}: **{count}**")

    lines.extend(["", "## Entries", ""])
    for entry in sorted(entries, key=lambda item: (item["category"], item["name"].lower())):
        lines.extend(
            [
                f"### {entry['name']}",
                "",
                f"- ID: `{entry['id']}`",
                f"- Category: `{entry['category']}`; kind: `{entry['kind']}`",
                f"- Source: {entry['url']}",
                f"- Summary: {entry['summary']}",
                f"- Signals: {', '.join(f'`{signal}`' for signal in entry['signals'])}",
                f"- Grading: {entry['grading']}",
                f"- Environment: {entry['environment']}",
                f"- Limitation: {entry['limitation']}",
            ]
        )
        if entry.get("paper"):
            lines.append(f"- Paper: {entry['paper']}")
        if entry.get("aliases"):
            lines.append(f"- Aliases: {', '.join(entry['aliases'])}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_html(catalog: dict, audit: dict) -> str:
    entries = catalog["entries"]
    counts = Counter(entry["category"] for entry in entries)
    kind_counts = Counter(entry["kind"] for entry in entries)
    source_records = audit.get("repositories", [])
    accessible = sum(record.get("status") == "source-accessible" for record in source_records)
    # Escape the JSON before embedding it in a script element.
    entries_json = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    entries_json = entries_json.replace("<", "\\u003c").replace("</script", "<\\/script")
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Agent Harness Benchmarks",
            "description": "A decision guide and machine-readable catalog of public AI agent and harness benchmarks.",
            "url": SITE_URL,
            "dateModified": catalog["as_of"],
            "mainEntity": {
                "@type": "ItemList",
                "numberOfItems": len(entries),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": position,
                        "name": entry["name"],
                        "url": entry["url"],
                    }
                    for position, entry in enumerate(entries, 1)
                ],
            },
        },
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("<", "\\u003c").replace("</script", "<\\/script")
    featured_rank = {entry_id: index for index, entry_id in enumerate(FEATURED_IDS)}
    static_cards = "".join(
        static_card(entry)
        for entry in sorted(entries, key=lambda item: (featured_rank.get(item["id"], 9999), item["name"].lower()))
    )
    category_options = "".join(
        f'<option value="{html.escape(category)}">{html.escape(CATEGORY_LABELS.get(category, category))}</option>'
        for category in sorted(counts)
    )
    category_filters = "".join(
        f'<button class="facet{" active" if index == 0 else ""}" type="button" data-category="{html.escape(category)}">'
        f'<span>{html.escape(CATEGORY_LABELS.get(category, category))}</span><b>{counts[category]}</b></button>'
        for index, category in enumerate(sorted(counts, key=lambda item: (-counts[item], item)))
    )
    category_filters = (
        f'<button class="facet active" type="button" data-category=""><span>All areas</span><b>{len(entries)}</b></button>'
        + category_filters.replace('class="facet active"', 'class="facet"', 1)
    )
    snapshot = html.escape(catalog["as_of"])
    labels_json = json.dumps(CATEGORY_LABELS, ensure_ascii=False)

    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#101a3a">
  <meta name="description" content="Choose AI agent benchmarks by workload, scoring method, environment, and limitations. Explore coding, browser, tool-use, memory, safety, and harness evaluations.">
  <link rel="canonical" href="__SITE_URL__">
  <link rel="sitemap" type="application/xml" href="sitemap.xml">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Agent Harness Benchmarks — choose your evaluation">
  <meta property="og:description" content="Compare what AI agent benchmarks test, how they score results, and what their scores miss. A searchable catalog with source links and practical limitations.">
  <meta property="og:url" content="https://zeredy879.github.io/awesome-agent-harness-benchmarks/">
  <meta property="og:site_name" content="Agent Harness Benchmarks">
  <meta property="og:image" content="https://opengraph.githubassets.com/1/zeredy879/awesome-agent-harness-benchmarks">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Agent Harness Benchmarks — choose your evaluation">
  <meta name="twitter:description" content="Find AI agent benchmarks by workload, scoring method, environment, and limitations. Read the catalog or consume its Markdown and JSON exports.">
  <meta name="twitter:image" content="https://opengraph.githubassets.com/1/zeredy879/awesome-agent-harness-benchmarks">
  <script type="application/ld+json">__STRUCTURED_DATA__</script>
  <title>Agent Harness Benchmarks — choose your evaluation</title>
  <style>
    :root {
      --ink: #17213b; --muted: #68738a; --line: #dce3ef; --soft: #f4f7fb;
      --navy: #101a3a; --navy-2: #18295a; --blue: #4f7cff; --violet: #8b6cff;
      --mint: #b8f3db; --white: #fff; --shadow: 0 16px 42px rgba(16, 26, 58, .10);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; color: var(--ink); background: var(--soft); font: 15.5px/1.6 Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    a { color: inherit; text-decoration: none; }
    a:hover { text-decoration: underline; }
    :focus-visible { outline: 3px solid #7851d1; outline-offset: 4px; }
    .hero :focus-visible { outline-color: var(--mint); }
    .skip-link { position: fixed; top: 8px; left: 8px; z-index: 20; padding: 10px 16px; border-radius: 8px; color: var(--navy); background: var(--mint); transform: translateY(-160%); }
    .skip-link:focus { transform: translateY(0); }
    .site-nav { position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 16px max(22px, calc((100vw - 1180px) / 2)); background: rgba(255, 255, 255, .88); border-bottom: 1px solid rgba(220, 227, 239, .9); backdrop-filter: blur(16px); }
    .brand { display: inline-flex; align-items: center; gap: 10px; font-weight: 800; letter-spacing: -.02em; }
    .brand-mark { display: grid; place-items: center; width: 30px; height: 30px; border-radius: 9px; color: var(--white); background: linear-gradient(135deg, var(--blue), var(--violet)); box-shadow: 0 6px 16px rgba(79, 124, 255, .28); font-size: 13px; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 18px; color: var(--muted); font-size: .9rem; }
    .nav-links a:hover { color: var(--ink); text-decoration: none; }
    main { max-width: 1180px; margin: 0 auto; padding: 28px 22px 80px; }
    .hero { position: relative; display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(300px, .75fr); gap: 34px; overflow: hidden; padding: clamp(34px, 6vw, 70px); border-radius: 28px; color: var(--white); background: radial-gradient(circle at 90% 0%, rgba(139,108,255,.48), transparent 38%), linear-gradient(135deg, var(--navy), var(--navy-2)); box-shadow: var(--shadow); }
    .hero::after { content: ""; position: absolute; width: 330px; height: 330px; right: -125px; bottom: -190px; border: 1px solid rgba(184,243,219,.28); border-radius: 50%; box-shadow: 0 0 0 28px rgba(184,243,219,.06), 0 0 0 56px rgba(184,243,219,.04); }
    .eyebrow { margin: 0 0 14px; color: var(--mint); font-size: .72rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; }
    h1 { max-width: 760px; margin: 0; font-size: clamp(2.5rem, 6vw, 5rem); line-height: .99; letter-spacing: -.065em; }
    .hero-copy .lede { max-width: 680px; margin: 22px 0 0; color: rgba(255,255,255,.78); font-size: clamp(1.03rem, 2vw, 1.24rem); }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 11px; margin-top: 30px; }
    .button { display: inline-flex; align-items: center; justify-content: center; min-height: 43px; padding: 10px 16px; border-radius: 10px; font-weight: 750; font-size: .92rem; }
    .button.primary { color: var(--navy); background: var(--mint); box-shadow: 0 8px 18px rgba(0,0,0,.16); }
    .button.secondary { color: var(--white); border: 1px solid rgba(255,255,255,.25); background: rgba(255,255,255,.08); }
    .button:hover { text-decoration: none; transform: translateY(-1px); }
    .hero-note { display: flex; align-items: center; gap: 8px; margin-top: 19px; color: rgba(255,255,255,.60); font-size: .83rem; }
    .live-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--mint); box-shadow: 0 0 0 4px rgba(184,243,219,.12); }
    .hero-panel { position: relative; z-index: 1; align-self: end; padding: 22px; border: 1px solid rgba(255,255,255,.15); border-radius: 18px; background: rgba(255,255,255,.08); }
    .hero-panel h2 { margin: 0 0 16px; font-size: 1rem; letter-spacing: -.02em; }
    .signal { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 12px 0; border-top: 1px solid rgba(255,255,255,.12); color: rgba(255,255,255,.72); font-size: .88rem; }
    a.signal { transition: color .18s ease, padding-left .18s ease; }
    a.signal:hover { padding-left: 4px; color: var(--white); text-decoration: none; }
    .signal strong { color: var(--white); font-size: 1.15rem; }
    .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 18px 0 46px; }
    .stat { padding: 18px 19px; border: 1px solid var(--line); border-radius: 14px; background: var(--white); box-shadow: 0 4px 14px rgba(16,26,58,.04); }
    .stat strong { display: block; font-size: 1.72rem; line-height: 1.1; letter-spacing: -.04em; }
    .stat span { display: block; margin-top: 5px; color: var(--muted); font-size: .82rem; }
    .stat em { display: block; margin-top: 2px; color: #8a94a8; font-size: .72rem; font-style: normal; }
    .section { margin-top: 54px; }
    .section[id] { scroll-margin-top: 84px; }
    .section-kicker { margin: 0 0 7px; color: var(--blue); font-size: .72rem; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; }
    .section-heading { display: flex; align-items: end; justify-content: space-between; gap: 20px; margin-bottom: 19px; }
    h2 { margin: 0; font-size: clamp(1.65rem, 3vw, 2.25rem); letter-spacing: -.05em; line-height: 1.1; }
    .section-heading p { max-width: 580px; margin: 0; color: var(--muted); }
    .start-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
    .start-card { display: flex; min-height: 155px; flex-direction: column; justify-content: space-between; padding: 18px; border: 1px solid var(--line); border-radius: 15px; background: var(--white); transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease; }
    .start-card:hover { border-color: rgba(79,124,255,.45); box-shadow: 0 10px 22px rgba(16,26,58,.09); transform: translateY(-2px); text-decoration: none; }
    .start-icon { display: grid; place-items: center; width: 31px; height: 31px; border-radius: 9px; color: var(--blue); background: #eaf0ff; font-size: .88rem; font-weight: 800; }
    .start-card h3 { margin: 16px 0 5px; font-size: 1rem; letter-spacing: -.02em; }
    .start-card p { margin: 0; color: var(--muted); font-size: .85rem; }
    .start-card .arrow { align-self: end; margin-top: 13px; color: var(--blue); font-weight: 800; }
    .directory-layout { display: grid; grid-template-columns: 246px minmax(0, 1fr); gap: 25px; align-items: start; }
    .facet-panel { position: sticky; top: 82px; padding: 16px; border: 1px solid var(--line); border-radius: 15px; background: var(--white); }
    .facet-title { display: flex; justify-content: space-between; align-items: center; margin: 0 0 11px; font-size: .78rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .facet-title span { color: var(--muted); font-weight: 600; letter-spacing: 0; text-transform: none; }
    .facet-list { display: grid; gap: 4px; }
    .facet { display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 9px 10px; border: 0; border-radius: 9px; color: var(--muted); background: transparent; font: inherit; font-size: .83rem; text-align: left; cursor: pointer; }
    .facet b { min-width: 24px; padding: 1px 6px; border-radius: 20px; color: var(--muted); background: var(--soft); font-size: .74rem; text-align: center; }
    .facet:hover { color: var(--ink); background: var(--soft); }
    .facet.active { color: var(--navy); background: #eaf0ff; font-weight: 750; }
    .facet.active b { color: var(--blue); background: var(--white); }
    .facet-divider { height: 1px; margin: 15px 0; background: var(--line); }
    .data-links { display: grid; gap: 6px; color: var(--blue); font-size: .83rem; }
    .data-links a { padding: 5px 0; }
    .directory-main { min-width: 0; }
    .controls { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)) auto; gap: 9px; margin-bottom: 12px; }
    .controls input { grid-column: 1 / -1; }
    input, select { min-height: 43px; width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; color: var(--ink); background: var(--white); font: inherit; outline: none; }
    input:focus, select:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(79,124,255,.13); }
    .reset { min-height: 43px; padding: 0 12px; border: 1px solid var(--line); border-radius: 10px; color: var(--muted); background: var(--white); font: inherit; white-space: nowrap; cursor: pointer; }
    .reset:hover { color: var(--ink); border-color: var(--blue); }
    #result-count { margin: 0 0 13px; color: var(--muted); font-size: .84rem; }
    .grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
    .card { display: flex; min-height: 245px; flex-direction: column; padding: 18px; border: 1px solid var(--line); border-radius: 15px; background: var(--white); transition: border-color .18s ease, box-shadow .18s ease; }
    .card:hover { border-color: rgba(79,124,255,.45); box-shadow: 0 8px 20px rgba(16,26,58,.07); }
    .card-top { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 12px; }
    .card-top-actions { display: inline-flex; align-items: center; gap: 6px; }
    .category-pill, .kind-pill { display: inline-flex; align-items: center; min-height: 24px; padding: 3px 8px; border-radius: 99px; font-size: .7rem; font-weight: 800; }
    .category-pill { color: #3855a8; background: #edf1ff; }
    .kind-pill { color: var(--muted); background: var(--soft); font-weight: 650; }
    .kind-pill.kind-watchlist { color: #8a4b00; background: #fff1d6; }
    .card h3 { margin: 0; font-size: 1.08rem; line-height: 1.25; letter-spacing: -.025em; }
    .card h3 a:hover { color: var(--blue); }
    .card-summary { margin: 9px 0 0; color: var(--muted); font-size: .88rem; }
    .signals { display: flex; flex-wrap: wrap; gap: 5px; margin: 13px 0; }
    .chip { padding: 3px 7px; border-radius: 6px; color: #4b5b76; background: #f0f3f8; font-size: .7rem; }
    .card-details { margin-bottom: 14px; color: var(--muted); font-size: .83rem; }
    .card-details summary { padding: 4px 0; color: #3855a8; font-weight: 650; cursor: pointer; }
    .card-details dl { margin: 9px 0 0; }
    .card-details dt { margin-top: 9px; color: var(--ink); font-weight: 700; }
    .card-details dd { margin: 3px 0 0; }
    .card-bottom { display: flex; align-items: end; justify-content: space-between; gap: 12px; margin-top: auto; padding-top: 12px; border-top: 1px solid var(--line); }
    .card-bottom small { color: var(--muted); font-size: .72rem; }
    .source-link { color: var(--blue); font-size: .78rem; font-weight: 750; white-space: nowrap; }
    .compare-toggle { display: inline-flex; align-items: center; min-height: 27px; padding: 3px 8px; border: 1px solid var(--line); border-radius: 7px; color: var(--muted); background: var(--white); font: inherit; font-size: .72rem; font-weight: 750; cursor: pointer; }
    .compare-toggle:hover { border-color: var(--blue); color: var(--blue); }
    .compare-toggle[aria-pressed="true"] { border-color: #7bcfae; color: #0d6848; background: #e6fff3; }
    .load-more { display: block; min-height: 43px; margin: 18px auto 0; padding: 9px 18px; border: 1px solid var(--line); border-radius: 10px; color: var(--navy); background: var(--white); font: inherit; font-weight: 750; cursor: pointer; }
    .load-more:hover { border-color: var(--blue); color: var(--blue); }
    .compare-bar { position: fixed; left: 50%; bottom: 18px; z-index: 15; display: flex; align-items: center; justify-content: space-between; gap: 22px; width: min(700px, calc(100vw - 36px)); padding: 12px 14px 12px 17px; border: 1px solid #c9d5ed; border-radius: 14px; color: var(--navy); background: rgba(255,255,255,.96); box-shadow: 0 14px 36px rgba(16,26,58,.20); transform: translateX(-50%); backdrop-filter: blur(14px); }
    .compare-bar[hidden] { display: none; }
    .compare-bar-copy { display: flex; min-width: 0; flex-direction: column; gap: 1px; }
    .compare-bar-copy strong { font-size: .82rem; }
    .compare-names { overflow: hidden; color: var(--muted); font-size: .76rem; text-overflow: ellipsis; white-space: nowrap; }
    .compare-bar-actions { display: flex; flex-shrink: 0; gap: 7px; }
    .compare-action, .compare-copy { min-height: 34px; padding: 6px 11px; border: 1px solid var(--line); border-radius: 8px; color: var(--navy); background: var(--white); font: inherit; font-size: .78rem; font-weight: 750; cursor: pointer; }
    .compare-action.primary { border-color: var(--navy); color: var(--white); background: var(--navy); }
    .compare-action:disabled { opacity: .42; cursor: not-allowed; }
    .compare-action:hover:not(:disabled), .compare-copy:hover { border-color: var(--blue); }
    .compare-dialog { width: min(1100px, calc(100vw - 28px)); max-width: 1100px; max-height: calc(100vh - 40px); padding: 0; border: 0; border-radius: 18px; color: var(--ink); background: var(--white); box-shadow: 0 26px 80px rgba(16,26,58,.30); }
    .compare-dialog::backdrop { background: rgba(16,26,58,.56); backdrop-filter: blur(4px); }
    .compare-dialog-inner { max-height: calc(100vh - 40px); overflow: auto; padding: 24px; }
    .compare-dialog header { display: flex; align-items: start; justify-content: space-between; gap: 18px; margin-bottom: 18px; }
    .compare-dialog header h2 { margin: 0; font-size: clamp(1.35rem, 3vw, 1.9rem); }
    .compare-dialog .section-kicker { margin-bottom: 5px; }
    .compare-table { width: 100%; border-collapse: collapse; font-size: .84rem; }
    .compare-table th, .compare-table td { padding: 11px; border-top: 1px solid var(--line); vertical-align: top; text-align: left; }
    .compare-table th { min-width: 145px; color: var(--muted); font-weight: 750; }
    .compare-table td { min-width: 190px; }
    .compare-table thead th { border-top: 0; color: var(--navy); font-size: .95rem; }
    .compare-table thead th:first-child { color: var(--muted); font-size: .78rem; }
    .compare-table a { color: var(--blue); font-weight: 700; }
    .compare-dialog-note { margin: 15px 0 0; color: var(--muted); font-size: .78rem; }
    .compare-dialog-note a { color: var(--blue); }
    .compare-copy-status { margin-left: 7px; color: #0d6848; font-size: .77rem; }
    .empty { grid-column: 1 / -1; padding: 38px 20px; border: 1px dashed var(--line); border-radius: 14px; color: var(--muted); background: var(--white); text-align: center; }
    .evidence-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
    .evidence-card { padding: 20px; border: 1px solid var(--line); border-radius: 15px; background: var(--white); }
    .evidence-card h3 { margin: 0 0 8px; font-size: 1rem; }
    .evidence-card p { margin: 0 0 12px; color: var(--muted); font-size: .86rem; }
    .evidence-card a { color: var(--blue); font-size: .82rem; font-weight: 750; }
    footer { display: flex; justify-content: space-between; gap: 20px; margin-top: 62px; padding-top: 20px; border-top: 1px solid var(--line); color: var(--muted); font-size: .8rem; }
    footer a { color: var(--blue); }
    @media (max-width: 900px) { .hero { grid-template-columns: 1fr; } .hero-panel { max-width: 430px; } .start-grid { grid-template-columns: repeat(2, 1fr); } .directory-layout { grid-template-columns: 1fr; } .facet-panel { display: none; } .section-heading { align-items: flex-start; flex-direction: column; gap: 12px; } }
    @media (max-width: 620px) { .site-nav { align-items: flex-start; flex-direction: column; gap: 9px; } .nav-links { gap: 11px; } main { padding: 16px 13px 54px; } .hero { padding: 29px 23px; border-radius: 20px; } h1 { font-size: clamp(2.35rem, 13vw, 3.5rem); } .stats { grid-template-columns: repeat(2, 1fr); margin-bottom: 35px; } .start-grid, .grid, .evidence-grid { grid-template-columns: 1fr; } .controls { grid-template-columns: 1fr 1fr; } .section[id] { scroll-margin-top: 122px; } footer { flex-direction: column; } .compare-bar { left: 13px; right: 13px; bottom: 12px; width: auto; transform: none; } .compare-bar-copy { max-width: 55%; } .compare-bar-actions { gap: 5px; } .compare-action, .compare-copy { padding-inline: 9px; } .compare-dialog-inner { padding: 18px 14px; } .compare-table { font-size: .77rem; } .compare-table th { min-width: 105px; } .compare-table td { min-width: 150px; } }
    @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } *, *::before, *::after { transition: none !important; } .button:hover, .start-card:hover { transform: none; } }
  </style>
</head>
<body>
<a class="skip-link" href="#directory">Skip to benchmark catalog</a>
<nav class="site-nav" aria-label="Primary navigation">
  <a class="brand" href="./"><span class="brand-mark">AH</span><span>Agent Harness Benchmarks</span></a>
  <div class="nav-links"><a href="#start">Start here</a><a href="#directory">Directory</a><a href="#method">Method</a><a href="agent.md">For agents</a><a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/docs/updates.md">Updates</a></div>
</nav>
<main>
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-copy">
      <p class="eyebrow">Open evaluation map · Snapshot __SNAPSHOT__</p>
      <h1 id="hero-title">Choose benchmarks for your AI agent.</h1>
      <p class="lede">See what each benchmark tests, how it scores results, and what those scores miss. Find a workload for your coding, browser, tool-use, or research agent.</p>
      <div class="hero-actions"><a class="button primary" href="#directory">Browse the catalog <span aria-hidden="true">↘</span></a><a class="button secondary" href="#method">Read the research notes</a></div>
      <div class="hero-note"><span class="live-dot" aria-hidden="true"></span> Public-source catalog · research snapshot __SNAPSHOT__</div>
    </div>
    <aside class="hero-panel" aria-label="What this catalog measures">
      <h2>What becomes measurable?</h2>
      <a class="signal" href="?q=tools#directory"><span>Tools &amp; state</span><strong aria-hidden="true">↗</strong></a>
      <a class="signal" href="?q=memory#directory"><span>Memory &amp; context</span><strong aria-hidden="true">↗</strong></a>
      <a class="signal" href="?q=recovery#directory"><span>Recovery &amp; verification</span><strong aria-hidden="true">↗</strong></a>
      <a class="signal" href="?q=permissions#directory"><span>Permissions &amp; safety</span><strong aria-hidden="true">↗</strong></a>
    </aside>
  </section>

  <section class="stats" aria-label="Snapshot statistics">
    <div class="stat"><strong>__ENTRY_COUNT__</strong><span>catalog entries</span></div>
    <div class="stat"><strong>__BENCHMARK_COUNT__</strong><span>benchmark suites</span><em>__INFRASTRUCTURE_COUNT__ infra · __STUDY_COUNT__ studies · __WATCHLIST_COUNT__ watchlist</em></div>
    <div class="stat"><strong>__AREA_COUNT__</strong><span>capability areas</span></div>
    <div class="stat"><strong>__ACCESSIBLE__/__SOURCE_COUNT__</strong><span>GitHub sources checked</span><em>reachability only</em></div>
  </section>

  <section class="section" id="start" aria-labelledby="start-title">
    <div class="section-heading"><div><p class="section-kicker">Start with a question</p><h2 id="start-title">Choose your evaluation path.</h2></div><p>Each path opens the same directory with a focused filter. Start broad, then pin the model, harness, tools, and environment before comparing results.</p></div>
    <div class="start-grid">
      <a class="start-card" href="?category=direct#directory" data-category="direct"><span class="start-icon">H</span><div><h3>Compare the harness</h3><p>Same model, different control loops, tools, memory, and recovery.</p></div><span class="arrow">Explore ↗</span></a>
      <a class="start-card" href="?category=coding#directory" data-category="coding"><span class="start-icon">&lt;/&gt;</span><div><h3>Ship code reliably</h3><p>Repository navigation, editing, tests, terminals, and delivery.</p></div><span class="arrow">Explore ↗</span></a>
      <a class="start-card" href="?category=tools#directory" data-category="tools"><span class="start-icon">API</span><div><h3>Evaluate tool use</h3><p>Stateful APIs, MCP servers, tool selection, and final-state grading.</p></div><span class="arrow">Explore ↗</span></a>
      <a class="start-card" href="?category=research#directory" data-category="research"><span class="start-icon">R</span><div><h3>Run research workflows</h3><p>Evidence, reproduction, scientific coding, and long-horizon work.</p></div><span class="arrow">Explore ↗</span></a>
    </div>
  </section>

  <section class="section" id="directory" aria-labelledby="directory-title">
    <div class="section-heading"><div><p class="section-kicker">The catalog</p><h2 id="directory-title">Search the inventory.</h2></div><p>Filter by capability, entry type, or keyword. Open a card’s details for its environment and limitations. Select up to three cards to compare, then copy the URL to share your view.</p></div>
    <noscript><p>Filtering requires JavaScript; the complete catalog is shown below. You can also <a href="agent.md">read the Markdown edition</a>.</p></noscript>
    <div class="directory-layout">
      <aside class="facet-panel" aria-label="Filter by capability area"><p class="facet-title">Capability areas <span>__AREA_COUNT__</span></p><div class="facet-list">__CATEGORY_FILTERS__</div><div class="facet-divider"></div><div class="data-links"><a href="agent.md">Agent Markdown →</a><a href="catalog.json">Catalog JSON →</a><a href="source-audit.json">Source audit →</a></div></aside>
      <div class="directory-main">
        <div class="controls"><input id="search" type="search" maxlength="500" placeholder="Search benchmarks, signals, or sources…" aria-label="Search catalog"><select id="category" aria-label="Filter by category"><option value="">All areas</option>__CATEGORY_OPTIONS__</select><select id="kind" aria-label="Filter by entry type"><option value="">All types</option><option value="benchmark">Benchmark</option><option value="study">Study</option><option value="infrastructure">Infrastructure</option><option value="watchlist">Watchlist</option></select><select id="sort" aria-label="Sort results"><option value="featured">Featured starting points</option><option value="name">Name A–Z</option><option value="category">Category</option><option value="kind">Entry type</option></select><button class="reset" id="reset" type="button">Reset</button></div>
        <p id="result-count" role="status" aria-live="polite">Showing __ENTRY_COUNT__ of __ENTRY_COUNT__ entries</p><div id="entries" class="grid">__STATIC_CARDS__</div><button class="load-more" id="load-more" type="button" hidden>Load more</button>
      </div>
    </div>
  </section>

  <section class="section" id="method" aria-labelledby="method-title">
    <div class="section-heading"><div><p class="section-kicker">Evidence first</p><h2 id="method-title">Designed for decisions, not leaderboard theatre.</h2></div><p>The catalog separates workload capability from harness effects, records limitations, and keeps a dated public-source audit.</p></div>
    <div class="evidence-grid"><article class="evidence-card"><h3>Hold the treatment still</h3><p>Pin model endpoint, prompt, tools, task release, sandbox, budgets, retries, and seeds before comparing harnesses.</p><a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/docs/research.md">Read comparison guidance →</a></article><article class="evidence-card"><h3>Use the right signal</h3><p>Report verified success, pass^k, cost, latency, tool calls, recovery, policy violations, and evidence quality separately.</p><a href="agent.md">Open the Agent digest →</a></article><article class="evidence-card"><h3>Keep the trail auditable</h3><p>Each record exposes its source, grading method, environment, and one concrete limitation.</p><a href="catalog.json">Inspect the JSON →</a></article></div>
  </section>

  <section class="compare-bar" id="compare-bar" hidden aria-label="Selected benchmarks"><span class="compare-bar-copy"><strong id="compare-count">0 selected</strong><span class="compare-names" id="compare-names"></span></span><span class="compare-bar-actions"><button class="compare-action" id="compare-clear" type="button">Clear</button><button class="compare-action primary" id="compare-open" type="button" disabled>Compare</button></span></section>
  <dialog class="compare-dialog" id="compare-dialog" aria-labelledby="compare-title"><div class="compare-dialog-inner"><header><div><p class="section-kicker">Side by side</p><h2 id="compare-title">Compare selected benchmarks</h2></div><button class="compare-action" id="compare-close" type="button">Close</button></header><div id="compare-table-wrap"></div><p class="compare-dialog-note"><button class="compare-copy" id="compare-copy" type="button">Copy comparison link</button><span class="compare-copy-status" id="compare-copy-status" role="status" aria-live="polite"></span> A comparison is a structured starting point, not a shared score.</p></div></dialog>

  <footer><span>Snapshot __SNAPSHOT__. Public-source inventory, not a claim of universal completeness.</span><span><a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks">GitHub repository</a> · <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.zh-CN.md">中文</a> · <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.ja.md">日本語</a> · <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.ko.md">한국어</a></span></footer>
</main>
<script>
const entries = __ENTRIES_JSON__;
const labels = __LABELS_JSON__;
const featuredIds = __FEATURED_IDS_JSON__;
const featuredRank = new Map(featuredIds.map((id, index) => [id, index]));
const grid = document.getElementById('entries');
const count = document.getElementById('result-count');
const search = document.getElementById('search');
const category = document.getElementById('category');
const kind = document.getElementById('kind');
const sort = document.getElementById('sort');
const reset = document.getElementById('reset');
const loadMore = document.getElementById('load-more');
const compareBar = document.getElementById('compare-bar');
const compareCount = document.getElementById('compare-count');
const compareNames = document.getElementById('compare-names');
const compareClear = document.getElementById('compare-clear');
const compareOpen = document.getElementById('compare-open');
const compareDialog = document.getElementById('compare-dialog');
const compareClose = document.getElementById('compare-close');
const compareTableWrap = document.getElementById('compare-table-wrap');
const compareCopy = document.getElementById('compare-copy');
const compareCopyStatus = document.getElementById('compare-copy-status');
const facets = [...document.querySelectorAll('.facet')];
let searchTimer;
let visibleCount = 24;
let compareIds = new Set();
function esc(value) { return String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char])); }
function card(entry) {
  const signals = entry.signals.map(signal => `<span class="chip">${esc(signal)}</span>`).join('');
  const paper = entry.paper ? ` · <a href="${esc(entry.paper)}" target="_blank" rel="noreferrer">paper</a>` : '';
  const categoryLabel = labels[entry.category] || entry.category;
  const kindClass = entry.kind === 'watchlist' ? ' kind-watchlist' : '';
  const selected = compareIds.has(entry.id);
  return `<article class="card"><div class="card-top"><span class="category-pill">${esc(categoryLabel)}</span><span class="card-top-actions"><span class="kind-pill${kindClass}">${esc(entry.kind)}</span><button class="compare-toggle" type="button" data-compare-id="${esc(entry.id)}" aria-pressed="${selected}">${selected ? '✓ Selected' : '+ Compare'}</button></span></div><h3><a href="${esc(entry.url)}" target="_blank" rel="noreferrer">${esc(entry.name)}</a></h3><p class="card-summary">${esc(entry.summary)}</p><div class="signals">${signals}</div><details class="card-details"><summary>Environment & limitations</summary><dl><dt>Environment</dt><dd>${esc(entry.environment)}</dd><dt>Limitation</dt><dd>${esc(entry.limitation)}</dd></dl></details><div class="card-bottom"><small>${esc(entry.grading)}${paper}</small><a class="source-link" href="${esc(entry.url)}" target="_blank" rel="noreferrer">View source ↗</a></div></article>`;
}
function syncFacets() {
  facets.forEach(button => {
    const active = button.dataset.category === category.value;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}
function hydrate() {
  const params = new URLSearchParams(window.location.search);
  search.value = (params.get('q') || '').slice(0, 500);
  for (const [control, fallback] of [[category, ''], [kind, ''], [sort, 'featured']]) {
    const value = params.get(control.id);
    const normalized = control === sort && value === 'recommended' ? 'featured' : value;
    control.value = [...control.options].some(option => option.value === normalized) ? normalized : fallback;
  }
  const validIds = new Set(entries.map(entry => entry.id));
  compareIds = new Set((params.get('compare') || '').split(',').filter(id => validIds.has(id)).slice(0, 3));
}
function syncURL(mode = 'push', anchor = null) {
  const url = new URL(window.location.href);
  url.search = '';
  if (search.value.trim()) url.searchParams.set('q', search.value.trim());
  if (category.value) url.searchParams.set('category', category.value);
  if (kind.value) url.searchParams.set('kind', kind.value);
  if (sort.value !== 'featured') url.searchParams.set('sort', sort.value);
  if (compareIds.size) url.searchParams.set('compare', [...compareIds].join(','));
  if (anchor !== null) url.hash = anchor;
  if (url.href !== window.location.href) window.history[mode === 'replace' ? 'replaceState' : 'pushState'](null, '', url);
}
function scrollToDirectory() {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.getElementById('directory').scrollIntoView({behavior: reducedMotion ? 'instant' : 'smooth', block: 'start'});
}
function update({scroll = false} = {}) {
  window.clearTimeout(searchTimer);
  visibleCount = 24;
  syncFacets();
  render();
  syncURL('push', scroll ? 'directory' : null);
  if (scroll) scrollToDirectory();
}
function render() {
  const query = search.value.trim().toLowerCase();
  const selectedCategory = category.value;
  const selectedKind = kind.value;
  const filtered = entries.filter(entry => { const haystack = JSON.stringify(entry).toLowerCase(); return (!selectedCategory || entry.category === selectedCategory) && (!selectedKind || entry.kind === selectedKind) && (!query || haystack.includes(query)); });
  filtered.sort((a, b) => sort.value === 'name' ? a.name.localeCompare(b.name) : sort.value === 'category' ? `${a.category}${a.name}`.localeCompare(`${b.category}${b.name}`) : sort.value === 'kind' ? `${a.kind}${a.name}`.localeCompare(`${b.kind}${b.name}`) : sort.value === 'featured' ? (featuredRank.get(a.id) ?? 9999) - (featuredRank.get(b.id) ?? 9999) || a.name.localeCompare(b.name) : 0);
  const visible = filtered.slice(0, visibleCount);
  count.textContent = `Showing ${visible.length} of ${filtered.length} matching entries · ${entries.length} total`;
  grid.innerHTML = visible.map(card).join('') || '<div class="empty">No matching entries. Try a broader search or reset the filters.</div>';
  loadMore.hidden = filtered.length <= visibleCount;
  loadMore.textContent = `Load more (${filtered.length - visibleCount} remaining)`;
}
facets.forEach(button => button.addEventListener('click', () => { category.value = button.dataset.category; update({scroll: true}); }));
document.querySelectorAll('.start-card').forEach(cardLink => cardLink.addEventListener('click', event => {
  if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  event.preventDefault();
  search.value = '';
  category.value = cardLink.dataset.category;
  kind.value = '';
  sort.value = 'featured';
  update({scroll: true});
}));
grid.addEventListener('click', event => {
  const button = event.target.closest('.compare-toggle');
  if (!button) return;
  const id = button.dataset.compareId;
  if (compareIds.has(id)) {
    compareIds.delete(id);
  } else if (compareIds.size < 3) {
    compareIds.add(id);
  } else {
    compareCopyStatus.textContent = 'Select up to three at a time.';
    return;
  }
  compareCopyStatus.textContent = '';
  visibleCount = Math.max(visibleCount, 24);
  updateCompareBar();
  render();
  syncURL();
});
function updateCompareBar() {
  const selected = entries.filter(entry => compareIds.has(entry.id));
  compareBar.hidden = selected.length === 0;
  compareCount.textContent = `${selected.length} selected`;
  compareNames.textContent = selected.map(entry => entry.name).join(' · ');
  compareOpen.disabled = selected.length < 2;
}
function renderComparison() {
  const selected = entries.filter(entry => compareIds.has(entry.id));
  const rows = [
    ['Type', entry => entry.kind],
    ['Area', entry => labels[entry.category] || entry.category],
    ['Signals', entry => entry.signals.join(', ')],
    ['Grading', entry => entry.grading],
    ['Environment', entry => entry.environment],
    ['Limitation', entry => entry.limitation],
  ];
  const header = selected.map(entry => `<th scope="col">${esc(entry.name)}</th>`).join('');
  const body = rows.map(([label, value]) => `<tr><th scope="row">${esc(label)}</th>${selected.map(entry => `<td>${esc(value(entry))}</td>`).join('')}</tr>`).join('');
  const sources = selected.map(entry => `<td><a href="${esc(entry.url)}" target="_blank" rel="noreferrer">Open source ↗</a></td>`).join('');
  compareTableWrap.innerHTML = `<table class="compare-table"><thead><tr><th scope="col">Dimension</th>${header}</tr></thead><tbody>${body}<tr><th scope="row">Source</th>${sources}</tr></tbody></table>`;
}
compareOpen.addEventListener('click', () => { renderComparison(); if (typeof compareDialog.showModal === 'function') compareDialog.showModal(); else compareDialog.setAttribute('open', ''); });
compareClose.addEventListener('click', () => { if (typeof compareDialog.close === 'function') compareDialog.close(); else compareDialog.removeAttribute('open'); });
compareDialog.addEventListener('click', event => { if (event.target === compareDialog) compareClose.click(); });
compareClear.addEventListener('click', () => { compareIds.clear(); updateCompareBar(); render(); syncURL(); });
compareCopy.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(window.location.href);
    compareCopyStatus.textContent = 'Link copied.';
  } catch (error) {
    compareCopyStatus.textContent = 'Copy failed; use the address bar.';
  }
});
loadMore.addEventListener('click', () => { visibleCount += 24; render(); });
search.addEventListener('input', () => {
  window.clearTimeout(searchTimer);
  visibleCount = 24;
  render();
  searchTimer = window.setTimeout(() => syncURL(), 250);
});
search.addEventListener('change', () => update());
[category, kind, sort].forEach(control => control.addEventListener('change', () => update()));
reset.addEventListener('click', () => { search.value = ''; category.value = ''; kind.value = ''; sort.value = 'featured'; update(); });
window.addEventListener('popstate', () => {
  window.clearTimeout(searchTimer);
  hydrate();
  visibleCount = 24;
  syncFacets();
  updateCompareBar();
  render();
});
hydrate();
syncURL('replace');
syncFacets();
updateCompareBar();
render();
</script>
</body>
</html>
"""
    replacements = {
        "__SNAPSHOT__": snapshot,
        "__ENTRY_COUNT__": str(len(entries)),
        "__BENCHMARK_COUNT__": str(kind_counts.get("benchmark", 0)),
        "__INFRASTRUCTURE_COUNT__": str(kind_counts.get("infrastructure", 0)),
        "__STUDY_COUNT__": str(kind_counts.get("study", 0)),
        "__WATCHLIST_COUNT__": str(kind_counts.get("watchlist", 0)),
        "__AREA_COUNT__": str(len(counts)),
        "__ACCESSIBLE__": str(accessible),
        "__SOURCE_COUNT__": str(len(source_records)),
        "__CATEGORY_FILTERS__": category_filters,
        "__CATEGORY_OPTIONS__": category_options,
        "__ENTRIES_JSON__": entries_json,
        "__LABELS_JSON__": labels_json,
        "__FEATURED_IDS_JSON__": json.dumps(FEATURED_IDS, ensure_ascii=False),
        "__STRUCTURED_DATA__": structured_data,
        "__STATIC_CARDS__": static_cards,
        "__SITE_URL__": SITE_URL,
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def build() -> None:
    catalog = read_json(CATALOG_PATH)
    audit = read_json(AUDIT_PATH)
    OUT.mkdir(exist_ok=True)

    (OUT / "index.html").write_text(render_html(catalog, audit), encoding="utf-8")
    digest = agent_markdown(catalog, audit)
    (OUT / "agent.md").write_text(digest, encoding="utf-8")
    (OUT / "index.md").write_text(digest, encoding="utf-8")
    (OUT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "source-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(RESEARCH_PATH, OUT / "research.md")
    (OUT / "llms.txt").write_text(
        "# Agent Harness Benchmarks\n\n"
        "Evidence-aware public inventory of agent harness benchmarks.\n\n"
        "- Markdown digest: ./agent.md\n"
        "- Structured catalog: ./catalog.json\n"
        "- Research method: ./research.md\n"
        "- Source audit: ./source-audit.json\n"
        "- Sitemap: ./sitemap.xml\n"
        "- Comparison links: append `?compare=id1,id2` (up to three stable IDs) to the human page.\n"
        "- Localized READMEs: https://github.com/zeredy879/awesome-agent-harness-benchmarks#readme\n"
        "- Human interface: ./index.html\n",
        encoding="utf-8",
    )
    sitemap_urls = [
        SITE_URL,
        f"{SITE_URL}agent.md",
        f"{SITE_URL}research.md",
        f"{SITE_URL}catalog.json",
        f"{SITE_URL}source-audit.json",
        f"{SITE_URL}llms.txt",
    ]
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(
            f"  <url><loc>{html.escape(url)}</loc><lastmod>{catalog['as_of']}</lastmod></url>\n"
            for url in sitemap_urls
        )
        + "</urlset>\n"
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n",
        encoding="utf-8",
    )
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    build()
