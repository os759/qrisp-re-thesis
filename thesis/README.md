# Schriftliche Ausarbeitung

LaTeX-Vorlage der Hochschule RheinMain.

- `thesis.tex` Arbeit, Bau mit `make` (pdflatex und bibtex)
- `anhang_a.tex` Anhang A als digitaler Anhang, Bau mit `make anhang`
  nach `make`, weil er Verweise auf die Arbeit aus `thesis.aux` liest
- `figures/` Abbildungen; die Diagramme entstehen aus den
  Mermaid-Quellen in `figures/diagramme/` (dort `build.sh` und
  `README.md`)
