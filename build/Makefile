# Society in Silico - Build System
# Requires: pandoc, pdflatex (for PDF output)

MANUSCRIPT_DIR = ../manuscript
OUTPUT_DIR = ../output
METADATA = metadata.yaml

# Collect all markdown files in order
FRONT_MATTER = $(sort $(wildcard $(MANUSCRIPT_DIR)/front-matter/*.md))
PART1 = $(sort $(wildcard $(MANUSCRIPT_DIR)/part-1-origins/*.md))
PART2 = $(sort $(wildcard $(MANUSCRIPT_DIR)/part-2-building/*.md))
PART3 = $(sort $(wildcard $(MANUSCRIPT_DIR)/part-3-future/*.md))

ALL_CHAPTERS = $(FRONT_MATTER) $(PART1) $(PART2) $(PART3)

# Default target
all: pdf

# Create output directory
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# PDF output
pdf: $(OUTPUT_DIR)
	pandoc $(ALL_CHAPTERS) \
		--metadata-file=$(METADATA) \
		--toc \
		--toc-depth=2 \
		-o $(OUTPUT_DIR)/society-in-silico.pdf

# EPUB output
epub: $(OUTPUT_DIR)
	pandoc $(ALL_CHAPTERS) \
		--metadata-file=$(METADATA) \
		--toc \
		--toc-depth=2 \
		-o $(OUTPUT_DIR)/society-in-silico.epub

# DOCX output (for sharing with editors)
docx: $(OUTPUT_DIR)
	pandoc $(ALL_CHAPTERS) \
		--metadata-file=$(METADATA) \
		--toc \
		-o $(OUTPUT_DIR)/society-in-silico.docx

# HTML output (for web preview)
html: $(OUTPUT_DIR)
	pandoc $(ALL_CHAPTERS) \
		--metadata-file=$(METADATA) \
		--toc \
		--standalone \
		-o $(OUTPUT_DIR)/society-in-silico.html

# Word count
wordcount:
	@wc -w $(ALL_CHAPTERS) | tail -1

# Chapter word counts
chaptercount:
	@wc -w $(ALL_CHAPTERS)

# Clean build artifacts
clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: all pdf epub docx html wordcount chaptercount clean
