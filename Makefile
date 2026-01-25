.PHONY: install test serve build pdf clean

# Install Python dependencies with uv
install:
	uv sync

# Run tests
test:
	uv run pytest

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
