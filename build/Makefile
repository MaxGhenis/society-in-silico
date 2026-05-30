# Society in Silico - Quarto wrapper targets
# Run from build/ if you want compatibility with the old subdirectory workflow.

ALL_CHAPTERS := $(shell python3 ../scripts/book_toc.py)

all: pdf

checktoc:
	@python3 ../scripts/book_toc.py --check

serve:
	cd .. && quarto preview

html: checktoc
	cd .. && quarto render --to html

pdf: checktoc
	cd .. && quarto render --to pdf

epub: checktoc
	cd .. && quarto render --to epub

docx: checktoc
	cd .. && quarto render --to docx

# Word count
wordcount: checktoc
	@wc -w $(ALL_CHAPTERS) | tail -1

# Chapter word counts
chaptercount: checktoc
	@wc -w $(ALL_CHAPTERS)

# Clean build artifacts
clean:
	rm -rf ../_book ../.quarto ../output

.PHONY: all checktoc serve html pdf epub docx wordcount chaptercount clean
