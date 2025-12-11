# Society in Silico

A book about economic simulation, the journey from academic models to policy tools, and what it means in the age of AI.

## About

This book traces the history of microsimulation from Guy Orcutt's 1957 vision through to modern tools like PolicyEngine and Cosilico. It's written to be accessible—not a textbook, but a narrative that connects:

- The personal journey of building simulation tools
- The intellectual history of modeling society computationally
- How microsimulation bridges academia and policy
- What AI means for the future of policy analysis

## Structure

```
manuscript/           # The book itself
  front-matter/       # Preface, introduction
  part-1-origins/     # History of microsimulation
  part-2-building/    # PolicyEngine & Cosilico journey
  part-3-future/      # AI age implications
research/             # Notes, references, research
  people/             # Profiles of key figures
  concepts/           # Linked concept notes
  timeline/           # Historical events
  references/         # Source materials
assets/               # Images, diagrams
build/                # Pandoc build configuration
```

## Workflow

This repo is designed to work with:
- **Obsidian** for conceptual mapping and research organization
- **Claude Code** for AI-assisted drafting and editing
- **Pandoc** for building final outputs (PDF, EPUB, etc.)

### Opening in Obsidian

Open this folder as an Obsidian vault. The `research/` folder uses wiki-style links for connecting concepts.

### Building

```bash
cd build && make pdf   # Generate PDF
cd build && make epub  # Generate EPUB
```

## Author

Max Ghenis

## License

Content is draft/unpublished. All rights reserved.
