#!/usr/bin/env python3
"""check_book.py — knowledge-layer linter for *Society in Silico*.

Keeps the book's facts organized: concepts introduced once and in order, retired
names gone, code samples sourced and parseable, and citation markers censused.

Usage:
    uv run --with pyyaml scripts/check_book.py all
    uv run --with pyyaml scripts/check_book.py concepts|names|markers|code

Checks
------
concepts  For each registry entry, find the first occurrence of its name-or-alias
          across manuscript files in _quarto.yml order (case-insensitive,
          word-boundary). FAIL if that first occurrence sits in a chapter earlier
          than `introduced_in` (a concept used before it is introduced). WARN if
          the `introduced_in` file never mentions the concept, or if a later
          chapter carries a definition-shaped restatement (a double introduction).
names     FAIL on retired names in manuscript/ (Cosilico outside HTML comments;
          Brier, microplex, AutoRAC, "Axiom Labs", Farness anywhere) and on
          forecast-validation phrasing ("track record" not properly qualified,
          "beats persistence").
markers   Census of [NEEDS CITATION]/[VERIFY]/[DECISION] per file. Informational;
          never fails.
code      Every fenced code block in manuscript/ longer than 3 lines must be
          immediately preceded by `<!-- source: <repo-or-path>@<ref> [adapted] -->`
          or `<!-- source: illustrative -->`; FAIL otherwise. Also syntax-checks
          ```python (ast.parse) and ```yaml (yaml.safe_load); a failure is a WARN
          for illustrative fragments, a FAIL otherwise.

Dependencies: Python standard library + PyYAML only. Exit status is non-zero if
any check FAILs; WARNs never change the exit status.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
QUARTO = REPO_ROOT / "_quarto.yml"
REGISTRY = REPO_ROOT / "research" / "concepts" / "registry.yml"
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"

HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE = re.compile(r"^(```|~~~)")
SOURCE_COMMENT = re.compile(r"<!--\s*source:\s*(.+?)\s*-->", re.IGNORECASE)

# ANSI is avoided so output is clean in CI logs.
FAIL_TAG = "FAIL"
WARN_TAG = "WARN"
OK_TAG = "ok"


# --------------------------------------------------------------------------- #
# Shared helpers
# --------------------------------------------------------------------------- #
def load_yaml_first(path: Path):
    """Load the first YAML document (tolerates a trailing `---` doc separator)."""
    with path.open(encoding="utf-8") as fh:
        for doc in yaml.safe_load_all(fh):
            if doc is not None:
                return doc
    return None


def chapter_order() -> list[Path]:
    """Ordered list of chapter file paths from _quarto.yml (parts flattened)."""
    data = load_yaml_first(QUARTO) or {}
    chapters: list[Path] = []

    def walk(node):
        if isinstance(node, str):
            chapters.append((REPO_ROOT / node).resolve())
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            # A part: {part: "...", chapters: [...]}, or stray keys we ignore.
            if "chapters" in node:
                walk(node["chapters"])
            elif "part" in node and isinstance(node["part"], str) and node[
                "part"
            ].endswith((".md", ".qmd")):
                walk(node["part"])

    book = data.get("book", data)
    walk(book.get("chapters", []))
    return chapters


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def term_pattern(term: str) -> re.Pattern:
    """Case-insensitive, word-boundary match that tolerates leading/trailing
    non-word characters in the term (e.g. 'money-atom', 'rulespec/v1')."""
    return re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def first_match(text: str, terms: list[str]) -> tuple[int, int, str] | None:
    """Earliest (pos, line, term) among all terms in `text`, or None."""
    best: tuple[int, int, str] | None = None
    for term in terms:
        m = term_pattern(term).search(text)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), line_of(text, m.start()), term)
    return best


class Report:
    """Collects FAIL/WARN/ok lines for one check and reports pass/fail."""

    def __init__(self, name: str):
        self.name = name
        self.fails: list[str] = []
        self.warns: list[str] = []
        self.notes: list[str] = []

    def fail(self, msg: str):
        self.fails.append(msg)

    def warn(self, msg: str):
        self.warns.append(msg)

    def note(self, msg: str):
        self.notes.append(msg)

    def emit(self) -> bool:
        print(f"\n=== {self.name} ===")
        for line in self.notes:
            print(line)
        for w in self.warns:
            print(f"  [{WARN_TAG}] {w}")
        for f in self.fails:
            print(f"  [{FAIL_TAG}] {f}")
        status = FAIL_TAG if self.fails else OK_TAG
        print(
            f"  -> {self.name}: {status} "
            f"({len(self.fails)} fail, {len(self.warns)} warn)"
        )
        return not self.fails


# --------------------------------------------------------------------------- #
# concepts
# --------------------------------------------------------------------------- #
DEF_SHAPED = [
    "{t} is a ",
    "{t} is an ",
    "{t}, a ",
    "{t}, an ",
    "{t}—the ",
    "{t} — the ",
]


def check_concepts() -> Report:
    rep = Report("concepts")
    chapters = chapter_order()
    index_by_path = {p: i for i, p in enumerate(chapters)}
    texts = {p: read(p) for p in chapters}

    reg = load_yaml_first(REGISTRY) or {}
    entries = reg.get("concepts", [])
    rep.note(f"  {len(entries)} concepts; {len(chapters)} chapters in reading order.")

    for e in entries:
        cid = e.get("id", "?")
        name = e.get("name", cid)
        terms = [name] + list(e.get("aliases") or [])
        intro_path = (REPO_ROOT / e["introduced_in"]).resolve()

        if intro_path not in index_by_path:
            rep.fail(f"{cid}: introduced_in '{e['introduced_in']}' not in _quarto.yml")
            continue
        intro_idx = index_by_path[intro_path]

        # Files where an early mention is deliberate narrative foreshadowing —
        # a teaser before the owning chapter's full definition. Listed per
        # concept in the registry as `foreshadow_ok`.
        foreshadow_ok = {
            (REPO_ROOT / f).resolve() for f in e.get("foreshadow_ok", []) or []
        }

        # Earliest occurrence across the whole book, skipping sanctioned
        # foreshadow files when locating a violation.
        first_ch = None
        first_any = None
        for ch in chapters:
            hit = first_match(texts[ch], terms)
            if hit and first_any is None:
                first_any = (ch, hit)
            if hit and ch not in foreshadow_ok:
                first_ch = (ch, hit)
                break

        if first_any is None:
            rep.warn(f"{cid}: no occurrence of name/alias anywhere in the manuscript")
            continue

        if first_ch is not None:
            ch, (_, line, term) = first_ch
            first_idx = index_by_path[ch]

            if first_idx < intro_idx:
                rep.fail(
                    f"{cid}: used before introduced — first appears as '{term}' in "
                    f"{rel(ch)}:{line} (ch #{first_idx}), but introduced_in is "
                    f"{e['introduced_in']} (ch #{intro_idx}); if deliberate, add the "
                    f"file to this concept's foreshadow_ok list"
                )

        # Does the introduced_in file mention the concept at all?
        if first_match(texts[intro_path], terms) is None:
            rep.warn(
                f"{cid}: introduced_in file {e['introduced_in']} never mentions the "
                f"concept"
            )

        # Definition-shaped restatement in a LATER chapter (double introduction).
        restated = _later_restatement(chapters, texts, intro_idx, terms)
        if restated:
            rch, rline, rphrase = restated
            rep.warn(
                f"{cid}: possible re-introduction in later chapter {rel(rch)}:{rline} "
                f'("{rphrase}")'
            )

    return rep


def _later_restatement(chapters, texts, intro_idx, terms):
    for idx in range(intro_idx + 1, len(chapters)):
        ch = chapters[idx]
        text = texts[ch]
        for t in terms:
            for tmpl in DEF_SHAPED:
                needle = tmpl.format(t=re.escape(t))
                pat = re.compile(r"(?<!\w)" + needle, re.IGNORECASE)
                m = pat.search(text)
                if m:
                    start = m.start()
                    snippet = text[start : start + 48].replace("\n", " ")
                    return ch, line_of(text, start), snippet
    return None


# --------------------------------------------------------------------------- #
# names
# --------------------------------------------------------------------------- #
# Retired names that fail anywhere in the manuscript.
RETIRED_ANYWHERE = ["Brier", "microplex", "AutoRAC", "Axiom Labs", "Farness"]
# Cosilico is allowed only inside HTML comments (author DECISION notes).
COSILICO = "Cosilico"

TRACK_RECORD = re.compile(r"track record", re.IGNORECASE)
# Allowed to precede "track record" within 40 chars.
TRACK_OK = re.compile(r"\bno\b|CBO|its methodology and its", re.IGNORECASE)
BEATS_PERSISTENCE = re.compile(r"beats persistence", re.IGNORECASE)


def manuscript_files() -> list[Path]:
    return sorted(MANUSCRIPT_DIR.rglob("*.md"))


def check_names() -> Report:
    rep = Report("names")
    files = manuscript_files()
    rep.note(f"  scanning {len(files)} manuscript files.")

    for path in files:
        text = read(path)
        stripped = HTML_COMMENT.sub(" ", text)  # Cosilico allowed in comments.

        for m in term_pattern(COSILICO).finditer(stripped):
            rep.fail(
                f"retired name 'Cosilico' outside an HTML comment at "
                f"{rel(path)}:{line_of(stripped, m.start())}"
            )
        for name in RETIRED_ANYWHERE:
            for m in term_pattern(name).finditer(text):
                rep.fail(
                    f"retired name '{name}' at {rel(path)}:{line_of(text, m.start())}"
                )

        for m in TRACK_RECORD.finditer(text):
            window = text[max(0, m.start() - 40) : m.start()]
            if not TRACK_OK.search(window):
                rep.fail(
                    f"unqualified 'track record' at "
                    f"{rel(path)}:{line_of(text, m.start())} "
                    f'(preceding 40 chars: "...{window.strip()}")'
                )
        for m in BEATS_PERSISTENCE.finditer(text):
            rep.fail(
                f"forecast-validation phrase 'beats persistence' at "
                f"{rel(path)}:{line_of(text, m.start())}"
            )

    return rep


# --------------------------------------------------------------------------- #
# markers
# --------------------------------------------------------------------------- #
MARKERS = {
    "NEEDS CITATION": re.compile(r"\[NEEDS CITATION", re.IGNORECASE),
    "VERIFY": re.compile(r"\[VERIFY", re.IGNORECASE),
    "DECISION": re.compile(r"\[DECISION", re.IGNORECASE),
}


def check_markers() -> Report:
    rep = Report("markers")
    files = chapter_order()
    rows = []
    totals = {k: 0 for k in MARKERS}
    for path in files:
        text = read(path)
        counts = {k: len(pat.findall(text)) for k, pat in MARKERS.items()}
        for k in MARKERS:
            totals[k] += counts[k]
        if any(counts.values()):
            rows.append((rel(path), counts))

    name_w = max([len(r[0]) for r in rows] + [len("file")]) if rows else len("file")
    header = (
        f"  {'file':<{name_w}}  {'NEEDS CITATION':>14}  {'VERIFY':>6}  {'DECISION':>8}"
    )
    rep.note(header)
    rep.note("  " + "-" * (len(header) - 2))
    for fname, counts in rows:
        rep.note(
            f"  {fname:<{name_w}}  {counts['NEEDS CITATION']:>14}  "
            f"{counts['VERIFY']:>6}  {counts['DECISION']:>8}"
        )
    rep.note("  " + "-" * (len(header) - 2))
    rep.note(
        f"  {'TOTAL':<{name_w}}  {totals['NEEDS CITATION']:>14}  "
        f"{totals['VERIFY']:>6}  {totals['DECISION']:>8}"
    )
    rep.note("  (informational — this check never fails)")
    return rep


# --------------------------------------------------------------------------- #
# code
# --------------------------------------------------------------------------- #
def iter_code_blocks(text: str):
    """Yield (lang, start_fence_line, content_lines, preceding_source_comment)."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if FENCE.match(lines[i]):
            fence_char = lines[i][:3]
            lang = lines[i][3:].strip().split()[0] if len(lines[i]) > 3 else ""
            start = i
            body = []
            i += 1
            while i < len(lines) and not lines[i].startswith(fence_char):
                body.append(lines[i])
                i += 1
            # nearest non-blank preceding line -> is it a source comment?
            src = None
            j = start - 1
            while j >= 0 and lines[j].strip() == "":
                j -= 1
            if j >= 0:
                m = SOURCE_COMMENT.search(lines[j])
                if m:
                    src = m.group(1).strip()
            yield lang.lower(), start + 1, body, src
        i += 1


def check_code() -> Report:
    rep = Report("code")
    files = manuscript_files()
    n_blocks = 0
    for path in files:
        text = read(path)
        for lang, fence_line, body, src in iter_code_blocks(text):
            n_blocks += 1
            illustrative = bool(src) and src.lower().startswith("illustrative")

            # Provenance: required for blocks longer than 3 content lines.
            if len(body) > 3 and src is None:
                rep.fail(
                    f"{rel(path)}:{fence_line} — code block ({len(body)} lines, "
                    f"lang='{lang or 'none'}') missing a <!-- source: ... --> comment"
                )

            # Syntax check for python / yaml.
            code = "\n".join(body)
            if lang == "python":
                try:
                    ast.parse(code)
                except SyntaxError as exc:
                    msg = f"{rel(path)}:{fence_line} — python block fails ast.parse: {exc}"
                    (rep.warn if illustrative else rep.fail)(msg)
            elif lang in ("yaml", "yml"):
                try:
                    yaml.safe_load(code)
                except yaml.YAMLError as exc:
                    first = str(exc).splitlines()[0] if str(exc) else exc
                    msg = f"{rel(path)}:{fence_line} — yaml block fails safe_load: {first}"
                    (rep.warn if illustrative else rep.fail)(msg)

    rep.note(f"  scanned {n_blocks} fenced code block(s) in manuscript/.")
    return rep


# --------------------------------------------------------------------------- #
# entry point
# --------------------------------------------------------------------------- #
CHECKS = {
    "concepts": check_concepts,
    "names": check_names,
    "markers": check_markers,
    "code": check_code,
}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "check",
        choices=list(CHECKS) + ["all"],
        help="which check to run",
    )
    args = parser.parse_args(argv)

    to_run = list(CHECKS) if args.check == "all" else [args.check]
    ok = True
    for name in to_run:
        rep = CHECKS[name]()
        ok = rep.emit() and ok

    print()
    print("check_book:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
