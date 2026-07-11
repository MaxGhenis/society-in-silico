#!/usr/bin/env python3
"""Build the listen edition: the full book as one TTS-friendly document.

Strips citations, draft marks, HTML comments, and tables; inlines footnotes;
spells out symbols that read badly aloud. Output: exports/society-in-silico-listen.md
(render to docx/pdf with quarto for Speechify et al.).
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "exports" / "society-in-silico-listen.md"

ROMAN = ["I", "II", "III", "IV", "V", "VI"]


def inline_footnotes(text: str) -> str:
    """^[note] -> (Footnote: note) with bracket counting (notes contain brackets)."""
    out, i = [], 0
    while i < len(text):
        if text[i] == "^" and i + 1 < len(text) and text[i + 1] == "[":
            depth, j = 1, i + 2
            while j < len(text) and depth:
                depth += text[j] == "["
                depth -= text[j] == "]"
                j += 1
            note = text[i + 2 : j - 1].strip()
            out.append(f" (Footnote: {note})")
            i = j
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def strip_tables(text: str) -> str:
    lines, out, in_table = text.split("\n"), [], False
    for line in lines:
        if re.match(r"^\s*\|.*\|\s*$", line):
            if not in_table:
                out.append("(A table appears here in the print and web editions.)")
                in_table = True
            continue
        in_table = False
        out.append(line)
    return "\n".join(out)


def clean(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\{\{<\s*include[^>]*>\}\}", "", text)
    text = re.sub(r"^## References\s*$", "", text, flags=re.M)
    text = inline_footnotes(text)
    # Draft marks vanish for listening; the repo tracks them.
    text = re.sub(r"\[NEEDS CITATION[^\]]*\]", "", text)
    text = re.sub(r"\[VERIFY[^\]]*\]", "", text)
    text = re.sub(r"\[DECISION[^\]]*\]", "", text)
    # Pandoc citations: drop, tidy stranded space before punctuation.
    text = re.sub(r"\s*\[[^\]]*@[\w:-][^\]]*\]", "", text)
    # Wiki-links -> their text.
    text = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).replace("-", " "), text)
    text = strip_tables(text)
    # Symbols that read badly.
    text = text.replace("§", "Section ").replace("§§", "Sections ")
    text = text.replace("≈", "about ").replace("→", " to ")
    text = re.sub(r"[ \t]+([.,;:!?])", r"\1", text)  # space before punctuation
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text())
    book = config["book"]
    pieces = [
        f"# {book['title']}\n\n*{book['subtitle']}.*\n\nBy {book['author']}. "
        "This listen edition drops citations, tables, and editorial marks — "
        "the web edition at societyinsilico.com carries them all.\n"
    ]

    part_num = 0
    for entry in book["chapters"]:
        if isinstance(entry, str):
            if entry == "index.md":
                continue
            pieces.append(clean((ROOT / entry).read_text()))
            continue
        part_num += 1
        title = re.sub(r"^Part\s+\S+\s*:\s*", "", entry["part"])
        pieces.append(f"# Part {ROMAN[part_num - 1]}: {title}")
        for chapter in entry.get("chapters", []):
            pieces.append(clean((ROOT / chapter).read_text()))

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n\n\n".join(pieces) + "\n")
    words = len(OUT.read_text().split())
    print(f"wrote {OUT.relative_to(ROOT)} ({words:,} words, ~{words // 150} min at 150 wpm)")


if __name__ == "__main__":
    main()
