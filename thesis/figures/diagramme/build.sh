#!/bin/sh
# Erzeugt die Abbildungen der Arbeit aus den Mermaid-Quellen.
# Voraussetzung: Mermaid CLI 11.4.2 (npm install @mermaid-js/mermaid-cli@11.4.2)
# Aufruf aus thesis/figures/diagramme: sh build.sh
set -e
for d in d1_pipeline d3_pruefung d4_belegstaerke d7_gap; do
  mmdc -c mermaid.json -i "$d.mmd" -o "../$d.pdf" --pdfFit
done
mmdc -c mermaid_seq.json -i d2_aufruf.mmd -o ../d2_aufruf.pdf --pdfFit
