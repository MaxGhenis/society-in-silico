.PHONY: serve build pdf clean

# Start local dev server
serve:
	npx myst build --html

# Build static HTML (no server)
build:
	npx myst build --html --execute

# Build PDF via Typst
pdf:
	npx myst build --pdf

# Clean build artifacts
clean:
	rm -rf _build
