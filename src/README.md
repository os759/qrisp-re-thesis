# Quellcode

Reihenfolge und Zusammenspiel der Stufen beschreibt das `README.md` in
der Projektwurzel (Abschnitt Pipeline). Jedes Programm nennt in seinem
Docstring Zweck, Entscheidung und einen Beispielaufruf; alle laufen aus
der Projektwurzel.

- `collect/` Stufe 1, Abruf der Pull Requests ueber die GitHub-API (FF1).
  `fetch_pull_*.py` holen Liste, Details, Kommentare und Dateien;
  `github_api.py` ist das gemeinsame Modul. `api_test.py`,
  `explore_fields.py`, `compare_objects.py` und `analyze_pull_*.py`
  dienten der Erkundung und Beschreibung der Rohdaten.
- `prepare/` Stufe 2, `build_interim.py`: Zusammenfuehren der Rohdateien,
  Feldreduktion, Normalisierung der Texte, Kuerzung der Diffs (FF1)
- `extract/` Stufen 3 bis 5 (FF1, FF2, FF3):
  - Modelleingabe: `build_prompt_input.py`, `pseudonymise.py`
  - Extraktion: `run_extraction.py`, `prompt_files.py`
  - Pruefung: `validate_output.py`, `diagnose_excerpts.py`,
    `inspect_excerpts.py`, `breakdown_rejections.py`, `add_links.py`
  - Kosten: `cost_report.py`
- `classify/` Stufe 6, `check_classification.py`: Pruefung von Typ und
  Sicherheitsbezug (FF1, FF4)
- `analyze/` Stufe 6, Auswertung fuer Kapitel 6 (FF1 bis FF4):
  Stichproben, Zaehlungen, Bewertung, Gap-Analyse, Laufvergleiche
