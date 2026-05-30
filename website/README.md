# Society in Silico Website

Astro site for the public-facing read-online experience.

## Source Of Truth

The book's chapter order and metadata come from the repo-root `_quarto.yml`. The
website does not maintain its own chapter manifest anymore.

If you rename, reorder, or add chapters:

1. Update `../_quarto.yml`
2. Update the manuscript files themselves
3. Rebuild the site

## Commands

Run these from `website/`:

| Command | Action |
| :------ | :----- |
| `bun install` | Install site dependencies |
| `bun dev` | Start the Astro dev server |
| `bun build` | Build the production site |
| `bun preview` | Preview the production build locally |
