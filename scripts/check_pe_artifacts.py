"""Check the executed receipts and their links/numbers in the built HTML book.

Run after the notebook and `make build`; this does not execute simulations.
"""

from __future__ import annotations

import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "scripts/results/pe-computed-numbers"


class Page(HTMLParser):
    def __init__(self, path: Path):
        super().__init__()
        self.path = path
        self.links = []
        self.ids = set()
        self.text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs)

    def handle_data(self, data):
        self.text.append(data)


def main():
    script = ROOT / "scripts/pe_computed_numbers.py"
    source_hash = hashlib.sha256(script.read_bytes()).hexdigest()
    national = json.loads((RESULTS / "national.json").read_text())
    households = json.loads((RESULTS / "households.json").read_text())
    for receipt in (national, households):
        assert receipt["provenance"]["script_sha256"] == source_hash, (
            "Receipt is stale: execute the final notebook source"
        )
    notebook = ROOT / "scripts/notebooks/pe-computed-numbers.ipynb"
    nb = json.loads(notebook.read_text())
    cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
    assert [c["execution_count"] for c in cells] == list(range(1, len(cells) + 1))
    assert not any(
        o["output_type"] == "error" for c in cells for o in c.get("outputs", [])
    ), "Notebook contains an execution error"
    output_text = "".join(
        "".join(o.get("text", [])) for c in cells for o in c.get("outputs", [])
    )
    assert str(national["net_fiscal_cost"]) in output_text
    assert national["provenance"]["us_release"]["build_id"] in output_text

    built = ROOT / "_book"
    pages = [
        Page(built / "manuscript/part-2-open-engine/06-the-household-and-the-society.html"),
        Page(built / "manuscript/part-4-prediction/13-the-uncertainty-gap.html"),
    ]
    poverty = national["poverty"]
    expected = [
        f"${national['net_fiscal_cost'] / 1e9:.1f} billion",
        f"{poverty['percentage_point_reduction']:.2f} percentage points",
        f"{poverty['baseline']['child_poverty_rate'] * 100:.2f} to "
        f"{poverty['reform']['child_poverty_rate'] * 100:.2f} percent",
        f"{poverty['children_lifted_out'] / 1e6:.2f} million fewer children",
    ]
    for page in pages:
        rendered_text = "".join(page.text)
        for phrase in expected:
            assert phrase in rendered_text, (page.path.name, phrase)
    source_pages = [
        Page(built / "manuscript/part-1-closed-stack/03-the-accuracy-question.html"),
        Page(built / "manuscript/part-2-open-engine/07-three-ingredients.html"),
    ]
    for page in pages + source_pages:
        for link in page.links:
            href = link["href"]
            if href.startswith("#"):
                assert href[1:] in page.ids, (page.path.name, "missing anchor", href)
        assert 'class="chapter-number"' not in page.path.read_text(), (
            "Automatic numbering duplicates the authored chapter headings"
        )
    downloads = [link for link in pages[0].links if "download" in link]
    assert any(link["download"] == notebook.name for link in downloads)
    for link in downloads:
        target = (pages[0].path.parent / link["href"]).resolve()
        assert target.is_file(), ("Missing download", target)
        if target.suffix == ".ipynb":
            assert target.read_bytes() == notebook.read_bytes(), "Built notebook is stale"
    resources = (
        script,
        ROOT / "scripts/pe_numbers_report.py",
        ROOT / "scripts/execute_pe_notebook.py",
        notebook.parent / "README.md",
        notebook.parent / "requirements.txt",
        *RESULTS.glob("*"),
    )
    for source in resources:
        if source.is_file():
            target = built / source.relative_to(ROOT)
            assert target.read_bytes() == source.read_bytes(), ("Stale resource", target)
    print("PASS: executed receipts, source hashes, chapter numbers, anchors, notebook download, and bundled resources")


if __name__ == "__main__":
    main()
