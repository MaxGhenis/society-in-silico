# Society in Silico

*Simulating futures to build the one we want.*

A book about economic simulation, the journey from academic models to open policy
infrastructure, and what the agent era changes. By Max Ghenis.

## About

The book traces microsimulation from Guy Orcutt's 1957 vision through the
institutional era (CBO, JCT, IFS), the open-source turn (OpenFisca,
Tax-Calculator, PolicyEngine), and the agent turn — AI systems encoding law as
verified code at scale — to the prediction pole and the speculative horizon. Its
discipline, stated in chapter 3 and enforced throughout: a simulation is
admissible only where its verification chain terminates in ground truth.

Seventeen chapters in five parts:

1. **The closed stack** — origins, the tax model wars, the accuracy question,
   and the personal story that started it
2. **The open engine** — the PolicyEngine years
3. **The agent turn** — encoding the law, the verification problem,
   microsimulation anywhere, and the decomposition
4. **The prediction pole** — the uncertainty gap and the scoreboard; simulating
   opinion
5. **The horizon** — simulating democracy, simulating values, and the return to
   the fork in the road

## Structure

```
_quarto.yml           # Canonical TOC + build config
index.md              # Landing page
manuscript/
  front-matter/       # Preface, introduction
  part-1-closed-stack/
  part-2-open-engine/
  part-3-agent-turn/
  part-4-prediction/
  part-5-horizon/
references.bib        # BibTeX bibliography (Pandoc [@key] citations)
reviews/              # Dated review rounds; 2026-07-10T1227/ holds the
                      #   from-scratch design, fact sheet, and style notes
research/             # Concept notes, people, timeline (Obsidian wiki-links)
feedback/             # Earlier reader-persona reviews
website/              # Read-online site (Astro), driven by _quarto.yml
scripts/, src/        # Analysis helpers and the audiobook/concept pipeline
```

`[NEEDS CITATION: …]` and `[VERIFY: …]` markers in the manuscript are
deliberate — they mark claims awaiting source resolution. Resolve them; don't
delete them.

## Building

```bash
make serve   # Local Quarto preview
make build   # Static HTML book
make pdf     # PDF
make epub    # EPUB
make docx    # DOCX
make check   # Knowledge-layer linter
```

`make check` — concept-introduction order, retired names, marker census,
code-block provenance. Runs `scripts/check_book.py` (stdlib + PyYAML) and exits
non-zero on failure; the concept order and code-block rules are enforced from
`research/concepts/registry.yml`.

## Workflow

- **Quarto** is the build system; `_quarto.yml` is the single source of truth
  for chapter order.
- **Obsidian**: open the repo as a vault for the `research/` wiki-links.
- **AI assistants**: read `.claude/CLAUDE.md` first — it carries the voice
  rules, citation standards, and the retired-names list; the canonical fact
  sheet for claims about the author's projects is
  `reviews/2026-07-10T1227/rewrite-facts.md`.

## License

Text © Max Ghenis, licensed CC BY-NC 4.0 (see LICENSE).
