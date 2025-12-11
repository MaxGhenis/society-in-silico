# Obsidian Setup Guide

## Opening This Vault

1. Open Obsidian
2. Click "Open folder as vault"
3. Select the `society-in-silico` folder

## Recommended Community Plugins

Install these via Settings > Community Plugins > Browse:

### Essential for Book Writing

- **Longform** - Manuscript compilation and scene/chapter management
- **Dataview** - Query your notes (useful for tracking research status)
- **Templater** - Better templates for consistent note creation

### Helpful Additions

- **Excalidraw** - Visual diagrams and concept maps
- **Citations** - BibTeX integration for academic references
- **Kanban** - Visual board for chapter progress tracking
- **Calendar** - Daily notes for writing sessions

### For AI Integration

- **Text Generator** - GPT/Claude integration directly in Obsidian
- **Smart Connections** - AI-powered note linking suggestions

## Folder Structure

```
manuscript/        → Use Longform to compile chapters into full manuscript
research/          → Linked notes, wiki-style
  people/          → Biographical research
  concepts/        → Technical explanations
  timeline/        → Historical chronology
  references/      → Source materials
assets/            → Images and diagrams (auto-attached here)
```

## Workflow Tips

### Research Phase
- Create concept notes in `research/concepts/`
- Use `[[wiki-links]]` liberally to connect ideas
- Use the Graph View to visualize connections

### Writing Phase
- Draft chapters in `manuscript/` folders
- Use Longform plugin to compile and reorder
- Link to research notes with `[[concept-name]]`

### Review Phase
- Export via `build/Makefile` for formatted output
- Share DOCX with editors
- Track feedback in a `feedback/` folder (optional)

## Graph View Tips

The graph view becomes powerful as you add more notes:
- Color-code by folder
- Filter to show only manuscript OR only research
- Look for orphan notes (unlinked concepts)
