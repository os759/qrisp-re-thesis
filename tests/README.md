# Tests

Tests fuer die Komponenten in `src/`. Ausfuehren aus der Projektwurzel:

    python -m pytest tests/ -v

`conftest.py` legt den Importpfad fest. pytest liest die Datei
automatisch, bevor ein Test laeuft. Ohne sie finden die Tests die
Module unter `src/collect` und `src/prepare` nicht.

## Getestete Bereiche

Nach Entscheidung D4 vom 19.08.2026 wird dort getestet, wo ein Fehler
still Daten verfaelscht, nicht dort, wo er sichtbar zum Abbruch fuehrt.

| Datei | Geprueft wird | Stiller Fehler waere |
|---|---|---|
| `test_resume.py` | Wiederaufnahme abgebrochener Abrufe | Pull Requests doppelt geholt oder uebersprungen |
| `test_outcome.py` | Ableitung des Feldes `outcome` | verworfene Aenderung gilt als umgesetzt |
| `test_normalisation.py` | Zeilenenden und Reinigung der Fliesstextfelder | echter Text geloescht oder Quellcode veraendert |
| `test_jsonl_io.py` | JSONL-Ein- und Ausgabe | Datensatz verloren, Umlaut zerstoert |
| `test_truncation.py` | Die drei Kuerzungsstufen aus D1 | Quellcode still entfernt oder Budget ueberschritten |

Die Tests wurden gegen absichtlich eingebrachte Fehler geprueft: Bei
vertauschtem `outcome` und bei einer Reinigung ohne Abschlussmarker
schlugen sechs der 26 Tests fehl.

## Noch nicht abgedeckt

- Die Netzschicht in `github_api.py` (Wiederholung, Ratengrenzen,
  Paginierung). Sie wurde im Betrieb geprueft, nicht automatisiert.
- Die Auswertungsskripte unter `src/collect/`.
- Schemavalidierung der LLM-Ausgaben, vorgesehen fuer Paket E.
