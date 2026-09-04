.PHONY: all clean

all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	latexmk -C
	rm -f articles/*.aux backmatter/*.aux frontmatter/*.aux
