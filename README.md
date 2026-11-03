# LLM-gestützte Rekonstruktion von Softwareanforderungen aus der Entwicklungshistorie

Bachelorarbeit im Studiengang Angewandte Informatik, Hochschule RheinMain.
Fallstudie: Eclipse Qrisp (Repository `eclipse-qrisp/Qrisp`).

Dieses Repository ist der digitale Anhang der Arbeit (thesis.pdf,
Abschnitt 1.3). Es enthält Quelltext, Konfiguration, Prompts,
Arbeitsunterlagen und die Ergebnisdateien der Auswertung.

## Status

Stand zur Abgabe am 03.11.2026. Arbeitsverlauf und Einzelstände stehen
in `STATUS.md`.

## Wo anfangen?

1. **Die Arbeit lesen:** `thesis/thesis.pdf`. Einen Überblick über die
   Pipeline gibt Abbildung 4.1 (Kapitel 4), die Antworten auf die
   Forschungsfragen stehen in Abschnitt 7.1.
2. **Die Ergebnisse ansehen:** `docs/anforderungen_openai_claude.md`
   listet alle rekonstruierten Anforderungen lesbar auf. Die Zahlen aus
   Kapitel 6 stehen in `experiments/*.json`.
3. **Den Code nachvollziehen:** Jedes Programm unter `src/` beginnt mit
   einem Docstring, der Zweck, zugehörige Entscheidung und einen
   Beispielaufruf nennt. Die Reihenfolge zeigt der Abschnitt
   [Pipeline](#pipeline).
4. **Begründungen nachschlagen:** `docs/entscheidungen.md` enthält jede
   Entscheidung mit Datum und Begründung. Kennungen wie D1, E6 oder E12
   in Code und Arbeit verweisen dorthin.

## Was finde ich wo?

| Frage | Datei oder Ordner |
|---|---|
| Wo ist die Arbeit, wo Anhang A? | `thesis/thesis.pdf`, `thesis/anhang_a.pdf` |
| Wo sind die rekonstruierten Anforderungen? | Lesefassung: `docs/anforderungen_openai_claude.md`; maßgebliche Daten: `data/processed/extraction_2026-09-25_full_v2.jsonl` (OpenAI, Volllauf) und `data/processed/extraction_2026-10-21_claude_eval_v2.jsonl` (Claude, Vergleich an 20 Pull Requests) |
| Welche Links gehören zu den Belegen? | `data/processed/extraction_2026-09-25_full_v2.links.jsonl` |
| Mit welchem Modell, Prompt und Commit lief ein Lauf? | `data/processed/<Lauf>.manifest.json` |
| Welche Prompts wurden gesendet? | `prompts/extraction_system_v2.md`, `prompts/extraction_user_v2.md` (v1: Pilotlauf) |
| Wie sieht die Modellausgabe aus? | `config/requirement_schema_v2.json` (JSON-Schema), Abschnitt 4.3 der Arbeit |
| Woher stammen die Zahlen in Kapitel 6? | `experiments/*.json`, siehe Tabelle unten |
| Welche Pull Requests waren in welcher Stichprobe? | `docs/sample_*.md` |
| Wie wurde das Anforderungsformat gewählt (FF2)? | `docs/formatauswahl.md`, `docs/formatprobe_protokoll.md`, `thesis/anhang_a.pdf` |
| Wie wurde von Hand bewertet? | `eval/instrument/` (Kriterien und Anleitungen) |
| Wie wurde KI beim Erstellen der Arbeit eingesetzt? | `docs/ki-protokoll.md` |
| Welche Literatur wurde wie ausgewertet? | `literatur/literaturmatrix.md`, `literatur/suchprotokoll.md`, `literatur/notizen/` |

### Ergebnisdateien zu Kapitel 6

| Abschnitt der Arbeit | Forschungsfrage | Ergebnisdatei(en) |
|---|---|---|
| 6.1 Lokale Modelle | FF3 | Manifeste `data/processed/extraction_2026-09-30_local_*.manifest.json`, `docs/ollama_protokollauszug.md` |
| 6.2 Grundzahlen des Volllaufs | FF1 | `experiments/requirement_counts_2026-09-25_full_v2.json` |
| 6.3 Messgrößen API gegen lokal | FF3 | `experiments/ff3_measures_2026-10-09.json`, `experiments/model_comparison_eval_e2_2026-10-21.json`, `experiments/kostenschaetzung.md` |
| 6.4 Bewertung der Anforderungen | FF1 | `experiments/evaluation_e2_2026-10-08.json`, `experiments/b9_g1_comparison_2026-10-10.json` |
| 6.5 Prüfung der Klassifikation | FF1, FF4 | `experiments/classification_check_2026-10-06.json`, `experiments/dependabot_check_2026-10-06.json` |
| 6.6 Gap-Analyse | FF4 | `experiments/gap_analysis_2026-10-06.json` |

## Pipeline

Sechs Stufen, jede schreibt eigene Dateien und lässt sich einzeln
wiederholen (Abbildung 4.1 der Arbeit). Alle Befehle laufen aus der
Projektwurzel.

| Stufe | Programm(e) | Eingabe | Ausgabe |
|---|---|---|---|
| 1 Erhebung | `src/collect/fetch_pull_list.py`, `fetch_pull_details.py`, `fetch_pull_comments.py`, `fetch_pull_files.py` | GitHub-API | `data/raw/*.jsonl`, `data/manifests/` |
| 2 Aufbereitung | `src/prepare/build_interim.py` | `data/raw/` | `data/interim/pulls_prepared_2026-08-19.jsonl` |
| 3 Modelleingabe | `src/extract/build_prompt_input.py` mit `pseudonymise.py` | aufbereiteter Datensatz | `data/processed/model_input_2026-09-19.jsonl` |
| 4 Extraktion | `src/extract/run_extraction.py` mit `prompt_files.py` | Modelleingabe, Stichprobe aus `docs/sample_*.md` | `data/processed/extraction_<Lauf>.jsonl`, `.raw.jsonl`, `.manifest.json` |
| 5 Prüfung | `src/extract/validate_output.py`, `diagnose_excerpts.py`, `inspect_excerpts.py`, `add_links.py` | Extraktion, aufbereiteter Datensatz | Prüfergebnisse, `*.links.jsonl` |
| 6 Auswertung | `src/analyze/*.py`, `src/classify/check_classification.py` | Extraktion und Prüfungen | `experiments/*.json` |

Welche Datei welche Stufe abdeckt, beschreibt auch `src/README.md`.

## Installation und Tests

Python 3.14 (API-Läufe unter 3.14.6, lokale Läufe unter 3.14.7, laut
Manifest). Die Pakete mit festen Versionen stehen in `requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m pytest tests/ -q
```

Was die Tests prüfen, steht in `tests/README.md`.

## Ergebnisse nachrechnen

Ohne API-Schlüssel lassen sich die Zählungen aus vorhandenen Dateien
wiederholen, sofern `data/interim/` vorliegt (siehe [Daten](#daten)).
Beispiel für die Grundzahlen aus Abschnitt 6.2 (1 467 Anforderungen aus
392 schemagültigen Antworten):

```bash
python src/analyze/count_requirements.py \
  --input data/processed/extraction_2026-09-25_full_v2.jsonl \
  --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
  --model-input data/processed/model_input_2026-09-19.jsonl \
  --mentions-map data/interim/mention_map.json \
  --allowlist "jaspify,jax,pytest,rus"
```

Ohne `--output` gibt das Programm die Zahlen nur aus und schreibt
nichts. Bestehende Ergebnisdateien werden nie überschrieben.

Für neue Läufe gegen GitHub oder ein Sprachmodell gehören die Schlüssel
`GITHUB_TOKEN`, `OPENAI_API_KEY` bzw. `ANTHROPIC_API_KEY` in eine Datei
`.env` in der Projektwurzel. Die Einstellungen der Läufe stehen in
`config/*.toml` (siehe `config/README.md`), lokale Modelle laufen über
Ollama mit den Modelfiles in `config/ollama/`. Ein Probelauf ohne
Anfrage an das Modell:

```bash
python src/extract/run_extraction.py --sample docs/sample_pilot_a8.md \
  --run-id test --dry-run
```

## Daten

Im Git-Repository ausgeschlossen sind (Regeln in `.gitignore`):

- `data/raw/` und `data/interim/`: Rohdaten und aufbereiteter Datensatz.
  Sie enthalten Anmeldenamen und Texte Dritter (Abschnitt 5.1 der Arbeit).
- `data/processed/*` außer den Manifesten: Modelleingaben und
  Modellausgaben.
- `eval/responses/`: ausgefüllte Prüf- und Bewertungsbögen.
- Zugangsdaten (`.env`), Modellgewichte und lizenzpflichtige Volltexte
  unter `literatur/`.

Die Herkunft jeder Datei bleibt trotzdem nachvollziehbar: Jeder
Datensatzstand hat ein Manifest unter `data/manifests/` mit Zeitpunkt,
Umfang und Prüfsumme, jede Extraktion eine `*.manifest.json` unter
`data/processed/` mit Modell, Parametern, Prompt-Prüfsummen und Commit.

## Forschungsfragen

- **FF1** Inwieweit lassen sich aus der Pull-Request-Historie eines Open-Source-Projekts mithilfe von Large Language Models brauchbare, formal formulierte Softwareanforderungen rekonstruieren?
- **FF2** Welches Anforderungsformat eignet sich für die automatisierte Extraktion, und anhand welcher Kriterien ist diese Wahl zu begründen?
- **FF3** Welche Unterschiede zeigen sich zwischen API-basierten und lokal betriebenen Open-Source-Modellen hinsichtlich Qualität, Kosten und Datenkontrolle?
- **FF4** Welche von einer BSI- bzw. Common-Criteria-orientierten Prüfung erwarteten Sicherheitsanforderungen lassen sich aus der Entwicklungshistorie rekonstruieren, und wo bestehen Dokumentationslücken?

## Ausführungsumgebung

Stand der Erhebung: 31.07.2026

- Hardware: MacBook Pro, Apple M3 Pro, 36 GB Unified Memory
- Betriebssystem: macOS 26.5.2 (Build 25F84)
- Python 3.14.6 (lokale Modellläufe: 3.14.7)
- Git 2.50.1 (Apple Git-155)
