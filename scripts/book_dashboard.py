#!/usr/bin/env python3
"""
Society in Silico - Book Dashboard

Generates statistics and visualizations for the manuscript.
Run with: python scripts/book_dashboard.py
"""

import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from datetime import datetime

# Configuration
REPO_ROOT = Path(__file__).parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
RESEARCH_DIR = REPO_ROOT / "research"
REFERENCES_FILE = REPO_ROOT / "references.bib"
OUTLINE_FILE = MANUSCRIPT_DIR / "00-outline.md"

# Targets from outline
TARGETS = {
    "total_words": 80000,
    "front_matter": 5000,
    "part_1": 20000,  # 4 chapters originally, now 3
    "part_2": 25000,  # 5 chapters
    "part_3": 25000,  # 5 chapters
    "back_matter": 5000,
    "words_per_chapter": 6000,
}

PART_DIRS = {
    "front-matter": "Front Matter",
    "part-1-origins": "Part I: Origins",
    "part-2-building": "Part II: Building",
    "part-3-future": "Part III: Future",
}


def count_words(text: str) -> int:
    """Count words in text, excluding code blocks and YAML frontmatter."""
    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove citations
    text = re.sub(r"\{cite\}`[^`]+`", "", text)
    # Count words
    return len(text.split())


def extract_wiki_links(text: str) -> list[str]:
    """Extract [[wiki-links]] from text."""
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def extract_citations(text: str) -> list[str]:
    """Extract {cite}`key` citations from text."""
    return re.findall(r"\{cite\}`([^`]+)`", text)


def get_bibtex_keys() -> set[str]:
    """Get all keys from references.bib."""
    if not REFERENCES_FILE.exists():
        return set()
    content = REFERENCES_FILE.read_text()
    return set(re.findall(r"@\w+\{(\w+),", content))


def analyze_chapter(filepath: Path) -> dict:
    """Analyze a single chapter file."""
    content = filepath.read_text()

    return {
        "path": str(filepath.relative_to(REPO_ROOT)),
        "name": filepath.stem,
        "title": extract_title(content),
        "words": count_words(content),
        "wiki_links": extract_wiki_links(content),
        "citations": extract_citations(content),
        "has_references": "```{bibliography}" in content,
    }


def extract_title(content: str) -> str:
    """Extract the first H1 title from markdown."""
    match = re.search(r"^# (.+)$", content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def analyze_research_notes() -> dict:
    """Analyze research notes directory."""
    notes = {}
    if not RESEARCH_DIR.exists():
        return notes

    for md_file in RESEARCH_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(RESEARCH_DIR)
        key = md_file.stem
        content = md_file.read_text()
        notes[key] = {
            "path": str(rel_path),
            "title": extract_title(content),
            "words": count_words(content),
            "wiki_links": extract_wiki_links(content),
        }

    return notes


def build_link_graph(chapters: list[dict], notes: dict) -> dict:
    """Build a graph of connections between chapters and notes."""
    graph = {
        "nodes": [],
        "edges": [],
    }

    # Add chapter nodes
    for ch in chapters:
        graph["nodes"].append({
            "id": ch["name"],
            "type": "chapter",
            "label": ch["title"][:30],
            "words": ch["words"],
        })

    # Add note nodes that are referenced
    referenced_notes = set()
    for ch in chapters:
        referenced_notes.update(ch["wiki_links"])

    for note_key in referenced_notes:
        if note_key in notes:
            graph["nodes"].append({
                "id": note_key,
                "type": "note",
                "label": notes[note_key]["title"][:30],
                "words": notes[note_key]["words"],
            })

    # Add edges
    for ch in chapters:
        for link in ch["wiki_links"]:
            if link in notes:
                graph["edges"].append({
                    "source": ch["name"],
                    "target": link,
                })

    return graph


def calculate_progress(chapters: list[dict]) -> dict:
    """Calculate progress toward targets."""
    by_part = defaultdict(lambda: {"words": 0, "chapters": 0})

    for ch in chapters:
        path = ch["path"]
        for part_key, part_name in PART_DIRS.items():
            if part_key in path:
                by_part[part_name]["words"] += ch["words"]
                by_part[part_name]["chapters"] += 1
                break

    total_words = sum(ch["words"] for ch in chapters)

    return {
        "total": {
            "words": total_words,
            "target": TARGETS["total_words"],
            "percent": round(100 * total_words / TARGETS["total_words"], 1),
        },
        "by_part": dict(by_part),
        "chapters_complete": len(chapters),
    }


def generate_dashboard_data() -> dict:
    """Generate all data for the dashboard."""
    # Analyze chapters
    chapters = []
    for part_dir in MANUSCRIPT_DIR.iterdir():
        if part_dir.is_dir():
            for md_file in sorted(part_dir.glob("*.md")):
                if not md_file.name.startswith("00-"):  # Skip outline
                    chapters.append(analyze_chapter(md_file))

    # Analyze research notes
    notes = analyze_research_notes()

    # Get citations
    bibtex_keys = get_bibtex_keys()
    used_citations = set()
    for ch in chapters:
        used_citations.update(ch["citations"])

    # Build graph
    graph = build_link_graph(chapters, notes)

    # Calculate progress
    progress = calculate_progress(chapters)

    # Load reviews if they exist
    reviews_file = REPO_ROOT / "dashboard-app" / "public" / "reviews.json"
    reviews = []
    if reviews_file.exists():
        try:
            reviews = json.loads(reviews_file.read_text())
        except (json.JSONDecodeError, IOError):
            reviews = []

    return {
        "generated_at": datetime.now().isoformat(),
        "chapters": chapters,
        "notes_summary": {
            "total": len(notes),
            "referenced": len([n for n in notes if any(
                n in ch["wiki_links"] for ch in chapters
            )]),
        },
        "citations": {
            "total_in_bib": len(bibtex_keys),
            "used_in_manuscript": len(used_citations),
            "unused": list(bibtex_keys - used_citations),
        },
        "graph": graph,
        "progress": progress,
        "targets": TARGETS,
        "reviews": reviews,
    }


def print_summary(data: dict):
    """Print a text summary of the dashboard."""
    print("\n" + "=" * 60)
    print("📚 SOCIETY IN SILICO - BOOK DASHBOARD")
    print("=" * 60)
    print(f"Generated: {data['generated_at'][:19]}")

    # Progress bar
    progress = data["progress"]
    pct = progress["total"]["percent"]
    bar_len = 40
    filled = int(bar_len * pct / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n📊 Overall Progress: [{bar}] {pct}%")
    print(f"   {progress['total']['words']:,} / {progress['total']['target']:,} words")

    # By part
    print("\n📖 By Part:")
    for part_name, stats in progress["by_part"].items():
        print(f"   {part_name}: {stats['words']:,} words ({stats['chapters']} chapters)")

    # Chapters
    print(f"\n📝 Chapters ({len(data['chapters'])} total):")
    for ch in data["chapters"]:
        status = "✅" if ch["words"] > 1000 else "📝"
        citations = len(ch["citations"])
        links = len(ch["wiki_links"])
        print(f"   {status} {ch['title'][:40]:<40} {ch['words']:>5} words  "
              f"[{citations} cites, {links} links]")

    # Citations
    print(f"\n📚 Citations:")
    print(f"   BibTeX entries: {data['citations']['total_in_bib']}")
    print(f"   Used in manuscript: {data['citations']['used_in_manuscript']}")

    # Research notes
    print(f"\n🔬 Research Notes:")
    print(f"   Total: {data['notes_summary']['total']}")
    print(f"   Referenced from chapters: {data['notes_summary']['referenced']}")

    # Graph summary
    print(f"\n🕸️ Connection Graph:")
    print(f"   Nodes: {len(data['graph']['nodes'])}")
    print(f"   Edges: {len(data['graph']['edges'])}")

    print("\n" + "=" * 60)


def generate_html_dashboard(data: dict, output_path: Path):
    """Generate an interactive HTML dashboard."""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Society in Silico - Book Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        :root {{
            --bg: #1a1a2e;
            --card: #16213e;
            --accent: #0f3460;
            --text: #e8e8e8;
            --highlight: #00d9ff;
            --success: #4ade80;
            --warning: #fbbf24;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            padding: 2rem;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: var(--highlight);
        }}
        .dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            max-width: 1600px;
            margin: 0 auto;
        }}
        .card {{
            background: var(--card);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }}
        .card h2 {{
            font-size: 1.1rem;
            margin-bottom: 1rem;
            color: var(--highlight);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .progress-bar {{
            background: var(--accent);
            border-radius: 8px;
            height: 24px;
            overflow: hidden;
            margin: 1rem 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--highlight), var(--success));
            border-radius: 8px;
            transition: width 0.5s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.85rem;
        }}
        .stat {{
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--accent);
        }}
        .stat:last-child {{ border-bottom: none; }}
        .stat-value {{
            font-weight: bold;
            color: var(--highlight);
        }}
        .chapter-list {{
            max-height: 400px;
            overflow-y: auto;
        }}
        .chapter {{
            padding: 0.75rem;
            margin: 0.5rem 0;
            background: var(--accent);
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .chapter-title {{
            flex: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .chapter-stats {{
            display: flex;
            gap: 1rem;
            font-size: 0.85rem;
            opacity: 0.8;
        }}
        #graph {{
            width: 100%;
            height: 400px;
            background: var(--accent);
            border-radius: 8px;
        }}
        .node {{ cursor: pointer; }}
        .node text {{ font-size: 10px; fill: var(--text); }}
        .link {{ stroke: var(--highlight); stroke-opacity: 0.4; }}
        .timestamp {{
            text-align: center;
            opacity: 0.5;
            font-size: 0.85rem;
            margin-top: 2rem;
        }}
    </style>
</head>
<body>
    <h1>📚 Society in Silico</h1>

    <div class="dashboard">
        <div class="card">
            <h2>📊 Overall Progress</h2>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {data['progress']['total']['percent']}%">
                    {data['progress']['total']['percent']}%
                </div>
            </div>
            <div class="stat">
                <span>Words Written</span>
                <span class="stat-value">{data['progress']['total']['words']:,}</span>
            </div>
            <div class="stat">
                <span>Target</span>
                <span class="stat-value">{data['progress']['total']['target']:,}</span>
            </div>
            <div class="stat">
                <span>Chapters Complete</span>
                <span class="stat-value">{data['progress']['chapters_complete']}</span>
            </div>
        </div>

        <div class="card">
            <h2>📖 By Part</h2>
            {''.join(f"""
            <div class="stat">
                <span>{part}</span>
                <span class="stat-value">{stats['words']:,} words ({stats['chapters']} ch)</span>
            </div>
            """ for part, stats in data['progress']['by_part'].items())}
        </div>

        <div class="card">
            <h2>📚 Citations</h2>
            <div class="stat">
                <span>BibTeX Entries</span>
                <span class="stat-value">{data['citations']['total_in_bib']}</span>
            </div>
            <div class="stat">
                <span>Used in Manuscript</span>
                <span class="stat-value">{data['citations']['used_in_manuscript']}</span>
            </div>
            <div class="stat">
                <span>Coverage</span>
                <span class="stat-value">{round(100 * data['citations']['used_in_manuscript'] / max(1, data['citations']['total_in_bib']))}%</span>
            </div>
        </div>

        <div class="card">
            <h2>🔬 Research Notes</h2>
            <div class="stat">
                <span>Total Notes</span>
                <span class="stat-value">{data['notes_summary']['total']}</span>
            </div>
            <div class="stat">
                <span>Referenced in Chapters</span>
                <span class="stat-value">{data['notes_summary']['referenced']}</span>
            </div>
        </div>

        <div class="card" style="grid-column: span 2;">
            <h2>📝 Chapters</h2>
            <div class="chapter-list">
                {''.join(f"""
                <div class="chapter">
                    <span class="chapter-title">{'✅' if ch['words'] > 1000 else '📝'} {ch['title']}</span>
                    <span class="chapter-stats">
                        <span>{ch['words']:,} words</span>
                        <span>{len(ch['citations'])} cites</span>
                        <span>{len(ch['wiki_links'])} links</span>
                    </span>
                </div>
                """ for ch in data['chapters'])}
            </div>
        </div>

        <div class="card" style="grid-column: span 2;">
            <h2>🕸️ Chapter-Notes Graph</h2>
            <div id="graph"></div>
        </div>
    </div>

    <p class="timestamp">Generated: {data['generated_at'][:19]}</p>

    <script>
        // Graph data
        const graphData = {json.dumps(data['graph'])};

        // Create force-directed graph
        const width = document.getElementById('graph').clientWidth;
        const height = 400;

        const svg = d3.select('#graph')
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        const simulation = d3.forceSimulation(graphData.nodes)
            .force('link', d3.forceLink(graphData.edges).id(d => d.id).distance(100))
            .force('charge', d3.forceManyBody().strength(-200))
            .force('center', d3.forceCenter(width / 2, height / 2));

        const link = svg.append('g')
            .selectAll('line')
            .data(graphData.edges)
            .enter().append('line')
            .attr('class', 'link')
            .attr('stroke-width', 2);

        const node = svg.append('g')
            .selectAll('g')
            .data(graphData.nodes)
            .enter().append('g')
            .attr('class', 'node')
            .call(d3.drag()
                .on('start', dragstarted)
                .on('drag', dragged)
                .on('end', dragended));

        node.append('circle')
            .attr('r', d => d.type === 'chapter' ? 12 : 8)
            .attr('fill', d => d.type === 'chapter' ? '#00d9ff' : '#4ade80');

        node.append('text')
            .attr('dx', 15)
            .attr('dy', 4)
            .text(d => d.label);

        simulation.on('tick', () => {{
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y);
            node.attr('transform', d => `translate(${{d.x}},${{d.y}})`);
        }});

        function dragstarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x; d.fy = d.y;
        }}
        function dragged(event, d) {{
            d.fx = event.x; d.fy = event.y;
        }}
        function dragended(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null; d.fy = null;
        }}
    </script>
</body>
</html>'''

    output_path.write_text(html)
    print(f"\n✨ HTML dashboard saved to: {output_path}")


def main():
    """Main entry point."""
    import argparse
    parser = argparse.ArgumentParser(description="Book Dashboard for Society in Silico")
    parser.add_argument("--json", action="store_true", help="Output JSON data")
    parser.add_argument("--html", type=Path, help="Generate HTML dashboard to file")
    args = parser.parse_args()

    data = generate_dashboard_data()

    if args.json:
        print(json.dumps(data, indent=2))
    elif args.html:
        generate_html_dashboard(data, args.html)
    else:
        print_summary(data)
        # Also generate HTML by default
        html_path = REPO_ROOT / "dashboard.html"
        generate_html_dashboard(data, html_path)


if __name__ == "__main__":
    main()
