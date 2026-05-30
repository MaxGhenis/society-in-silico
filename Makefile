.PHONY: serve build pdf epub docx clean

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

# Clean build artifacts
clean:
	rm -rf _book .quarto
