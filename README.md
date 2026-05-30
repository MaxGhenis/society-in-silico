# Society in Silico

A book about economic simulation, the journey from academic models to policy tools, and what it means in the age of AI.

## About

This book traces the history of microsimulation from Guy Orcutt's 1957 vision through to modern tools like PolicyEngine and the Axiom Foundation. It's written to be accessible—not a textbook, but a narrative that connects:

- The personal journey of building simulation tools
- The intellectual history of modeling society computationally
- How microsimulation bridges academia and policy
- What AI means for the future of policy analysis

## Structure

```
website/              # Read-online site, driven by _quarto.yml
manuscript/           # The book itself
  front-matter/       # Preface, introduction
  part-1-origins/     # History of microsimulation
  part-2-building/    # PolicyEngine & Axiom journey
  part-3-future/      # AI age implications
_quarto.yml           # Canonical TOC + primary Quarto build config
research/             # Notes, references, research
  people/             # Profiles of key figures
  concepts/           # Linked concept notes
  timeline/           # Historical events
  references/         # Source materials
assets/               # Images, diagrams
build/                # Compatibility wrappers around the root Quarto project
```

## Workflow

This repo is designed to work with:
- **Obsidian** for conceptual mapping and research organization
- **AI coding assistants** for drafting, editing, and review passes
- **Quarto** as the canonical table of contents and primary build system
- **Compatibility targets** in `build/`, also derived from `_quarto.yml`

### Opening in Obsidian

Open this folder as an Obsidian vault. The `research/` folder uses wiki-style links for connecting concepts.

### Building

```bash
make serve             # Local Quarto preview
make build             # Static HTML book build
make pdf               # PDF build
make epub              # EPUB build
make docx              # DOCX build

cd build && make pdf   # Same Quarto project, old subdir workflow
```

The source of truth for chapter order is `_quarto.yml`. The website reader and
the compatibility build targets both derive their TOC from that file.

## Author

Max Ghenis

## License

Content is draft/unpublished. All rights reserved.
