.PHONY: serve build pdf epub docx check clean

# Start local Quarto preview server
serve:
	quarto preview

# Build static HTML book
build:
	quarto render --to html

# Build PDF book
pdf:
	quarto render --to pdf

# Build EPUB book
epub:
	quarto render --to epub

# Build DOCX book
docx:
	quarto render --to docx

# Knowledge-layer linter: concept-introduction order, retired names,
# marker census, code-block provenance
check:
	uv run --with pyyaml scripts/check_book.py all

# Clean build artifacts
clean:
	rm -rf _book .quarto
