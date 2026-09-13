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


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_html(catalog: dict) -> str:
    entries = catalog["entries"]
    counts = Counter(entry["category"] for entry in entries)
    # Escape the JSON before embedding it in a script element.
    entries_json = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    entries_json = entries_json.replace("<", "\\u003c")
    category_options = "".join(
        f'<option value="{html.escape(category)}">{html.escape(CATEGORY_LABELS.get(category, category))}</option>'
        for category in sorted(counts)
    )
    category_rows = "".join(
        f'<div class="bar-row"><span>{html.escape(CATEGORY_LABELS.get(category, category))}</span>'
        f'<span class="bar"><i style="width:{max(8, round(count / max(counts.values()) * 100))}%"></i></span>'
        f'<b>{count}</b></div>'
        for category, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Evidence-aware catalog of agent harness benchmarks and evaluation infrastructure">
  <title>Agent Harness Benchmarks</title>
  <style>
    :root {{ --ink:#172033; --muted:#5b6578; --line:#dbe2ee; --accent:#2563eb; --panel:#f7f9fc; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; color:var(--ink); font:16px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; background:#fff; }}
    main {{ max-width:1120px; margin:0 auto; padding:42px 22px 72px; }}
    h1 {{ font-size:clamp(2rem,4vw,3.3rem); letter-spacing:-.04em; margin:0 0 8px; }}
    h2 {{ margin-top:34px; letter-spacing:-.02em; }}
    h3 {{ margin:0 0 8px; font-size:1.05rem; }}
    p {{ color:var(--muted); }}
    a {{ color:var(--accent); text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .lede {{ max-width:820px; font-size:1.08rem; }}
    .stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin:26px 0; }}
    .stat, .card {{ border:1px solid var(--line); border-radius:12px; background:var(--panel); }}
    .stat {{ padding:16px; }}
    .stat strong {{ display:block; font-size:1.8rem; }}
    .stat span {{ color:var(--muted); font-size:.9rem; }}
    .links {{ display:flex; flex-wrap:wrap; gap:14px; margin:18px 0 30px; }}
    .links a {{ border:1px solid var(--line); border-radius:999px; padding:7px 12px; background:#fff; }}
    .bars {{ display:grid; gap:8px; max-width:760px; }}
    .bar-row {{ display:grid; grid-template-columns:minmax(190px, 1fr) 2fr 40px; gap:10px; align-items:center; color:var(--muted); font-size:.92rem; }}
    .bar {{ height:9px; border-radius:99px; background:#e8edf6; overflow:hidden; }}
    .bar i {{ display:block; height:100%; border-radius:99px; background:linear-gradient(90deg,#2563eb,#7c3aed); }}
    .bar-row b {{ color:var(--ink); text-align:right; }}
    .controls {{ display:flex; gap:10px; flex-wrap:wrap; margin:18px 0; }}
    input, select {{ border:1px solid var(--line); border-radius:8px; padding:10px 12px; font:inherit; background:#fff; }}
    input {{ flex:1 1 300px; }}
    select {{ flex:0 1 260px; }}
    #result-count {{ color:var(--muted); margin:10px 0 14px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:14px; }}
    .card {{ padding:17px; }}
    .card .meta {{ color:var(--muted); font-size:.86rem; margin-bottom:10px; }}
    .card .signals {{ display:flex; flex-wrap:wrap; gap:6px; margin:12px 0; }}
    .chip {{ border-radius:999px; background:#eaf1ff; color:#1e4fae; padding:2px 8px; font-size:.78rem; }}
    footer {{ border-top:1px solid var(--line); margin-top:44px; padding-top:20px; color:var(--muted); font-size:.9rem; }}
    @media (max-width:560px) {{ .bar-row {{ grid-template-columns:1fr 1fr 32px; }} .bar-row span:first-child {{ grid-column:1 / -1; }} }}
  </style>
</head>
<body>
<main>
  <header>
    <h1>Agent Harness Benchmarks</h1>
    <p class="lede">An evidence-aware catalog of benchmark suites, controlled harness studies, and evaluation infrastructure. The same snapshot is available as Markdown and JSON for agents.</p>
    <div class="links">
      <a href="agent.md">Agent digest (Markdown)</a>
      <a href="index.md">Markdown index</a>
      <a href="catalog.json">Catalog JSON</a>
      <a href="research.md">Research notes</a>
      <a href="source-audit.json">Source audit JSON</a>
      <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.zh-CN.md">简体中文</a>
      <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.ja.md">日本語</a>
      <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks/blob/main/README.ko.md">한국어</a>
      <a href="https://github.com/zeredy879/awesome-agent-harness-benchmarks">GitHub repository</a>
    </div>
  </header>
  <section class="stats" aria-label="Snapshot statistics">
    <div class="stat"><strong>{len(entries)}</strong><span>catalog entries</span></div>
    <div class="stat"><strong>{len(counts)}</strong><span>capability areas</span></div>
    <div class="stat"><strong>{catalog['as_of']}</strong><span>snapshot date</span></div>
  </section>
  <section>
    <h2>Capability map</h2>
    <div class="bars">{category_rows}</div>
  </section>
  <section>
    <h2>Browse entries</h2>
    <div class="controls">
      <input id="search" type="search" placeholder="Search name, summary, signals, or source" aria-label="Search catalog">
      <select id="category" aria-label="Filter by category"><option value="">All categories</option>{category_options}</select>
    </div>
    <div id="result-count" role="status"></div>
    <div id="entries" class="grid"></div>
  </section>
  <footer>Snapshot {catalog['as_of']}. This is a dated public-source inventory, not a claim that every private or unindexed benchmark has been found.</footer>
</main>
<script>
const entries = {entries_json};
const labels = {json.dumps(CATEGORY_LABELS, ensure_ascii=False)};
const grid = document.getElementById('entries');
const count = document.getElementById('result-count');
const search = document.getElementById('search');
const category = document.getElementById('category');
function card(entry) {{
  const signals = entry.signals.map(s => `<span class="chip">${{s}}</span>`).join('');
  const paper = entry.paper ? ` · <a href="${{entry.paper}}">paper</a>` : '';
  return `<article class="card"><h3><a href="${{entry.url}}">${{entry.name}}</a></h3><div class="meta">${{labels[entry.category] || entry.category}} · ${{entry.kind}} · <a href="${{entry.url}}">source</a>${{paper}}</div><div>${{entry.summary}}</div><div class="signals">${{signals}}</div><div class="meta"><strong>Grading:</strong> ${{entry.grading}}<br><strong>Limitation:</strong> ${{entry.limitation}}</div></article>`;
}}
function render() {{
  const query = search.value.trim().toLowerCase();
  const selected = category.value;
  const filtered = entries.filter(entry => {{
    const haystack = JSON.stringify(entry).toLowerCase();
    return (!selected || entry.category === selected) && (!query || haystack.includes(query));
  }});
  count.textContent = `Showing ${{filtered.length}} of ${{entries.length}} entries`;
  grid.innerHTML = filtered.map(card).join('') || '<p>No matching entries.</p>';
}}
search.addEventListener('input', render);
category.addEventListener('change', render);
render();
</script>
</body>
</html>
"""


def build() -> None:
    catalog = read_json(CATALOG_PATH)
    audit = read_json(AUDIT_PATH)
    OUT.mkdir(exist_ok=True)

    (OUT / "index.html").write_text(render_html(catalog), encoding="utf-8")
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
        "- Localized READMEs: https://github.com/zeredy879/awesome-agent-harness-benchmarks#readme\n"
        "- Human interface: ./index.html\n",
        encoding="utf-8",
    )
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    build()
