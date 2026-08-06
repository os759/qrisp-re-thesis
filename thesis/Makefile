# Makefile für thesis. Mit pdflatex, bevorzugt auf 
# Linux Rechnern und libreoffice installiert
PDFLATEX=pdflatex -interaction=nonstopmode
#PDFLATEX=latexmk -pdf -interaction=nonstopmode
BIBTEX=bibtex
SOFFICE=soffice
ZIP=zip
RM=rm
MKDIR=mkdir

STYLES=blindtext.sty
DRAWINGS=figures/zeichnung.odg figures/templateprozess.odg
IMAGES=figures/zeichnungjpg.jpg figures/zeichnungpng.png figures/zeichnungdraft.jpg figures/gnu.png figures/automata.pdf
MAIN=thesis
TEXFILES=$(MAIN).tex preamble.tex vorspann.tex hyphenations.tex
BIB=thesis.bib online.bib
INCLUDE_BIB=$(MAIN)1.bbl $(MAIN)2.bbl # Achtung spaeter nochmal manuell
TOPACK= $(STYLES) $(BIB) $(DRAWINGS) $(IMAGES) $(TEXFILES) Makefile 

$(MAIN): $(MAIN).pdf

# bewusst nicht erstes Ziel
all: bib $(MAIN).pdf LaTeXThesis.zip

LaTeXThesis.zip: $(TOPACK) 
	-$(RM) -rf LaTeXThesis
	$(MKDIR) LaTeXThesis
	cp $(TOPACK) LaTeXThesis
	$(ZIP) -r LaTeXThesis.zip LaTeXThesis
	$(RM) -rf LaTeXThesis

$(MAIN).pdf: $(TEXFILES) $(STYLES) $(INCLUDE_BIB)

# für das convert braucht man ImageMagick
figures/zeichnungjpg.jpg: figures/zeichnung.pdf
	convert figures/zeichnung.pdf figures/zeichnungjpg.jpg
figures/zeichnungpng.png: figures/zeichnung.pdf
	convert figures/zeichnung.pdf figures/zeichnungpng.png

bib: $(MAIN)1.bbl $(MAIN)2.bbl
# Bibliography geht nur manuell wegen bibtopic
# Nachteil: make erstellt bei jedem Durchlauf das PDF neu. 
# Vorteil: Es geht auch von Anfang an, für Leute (die Mehrheit),
#          die nicht schauen. 
bib: $(MAIN)1.bbl $(MAIN)2.bbl
$(MAIN)1.bbl: thesis.bib $(MAIN)1.aux
	-$(BIBTEX) $(MAIN)1
$(MAIN)2.bbl: online.bib $(MAIN)2.aux
	-$(BIBTEX) $(MAIN)2

# Das erste Mal TeXen wegen Bibliographie
# Das allererste Mal ist die Bibliographie noch nicht drin.
$(MAIN)1.aux: 
	$(PDFLATEX) $(MAIN).tex
$(MAIN)2.aux: 
	$(PDFLATEX) $(MAIN).tex

.PHONY: clean

RERUN = "(There were undefined |Rerun to get (cross-references|the bars))"

.SUFFIXES: .odg .tex .pdf

.tex.pdf: bib
	$(PDFLATEX) $*.tex

.odg.pdf:
	$(SOFFICE) --headless --convert-to pdf $*.odg

clean:
	-$(RM) $(MAIN).pdf *.log *.lot *.aux *.toc *.blg *.fdb_latexmk *.fls
	-$(RM) $(INCLUDE_BIB)

