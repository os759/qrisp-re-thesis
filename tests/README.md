# Tests

Tests fuer die Komponenten in `src/`. Ausfuehren aus der Projektwurzel:

    python -m pytest tests/ -v

Stand 21.10.2026: 673 Tests, alle bestanden (629 zum Stand der Arbeit
vom 10.10.2026, dazu nach der Abgabe 29 fuer den Aufrufweg zur
Anthropic-Schnittstelle und 15 fuer den Vergleich zweier Laeufe nach
E12). Die aktuelle Zahl zeigt

    python -m pytest tests/ --collect-only -q

`conftest.py` legt den Importpfad fest. pytest liest die Datei
automatisch, bevor ein Test laeuft. Ohne sie finden die Tests die
Module unter `src/collect`, `src/prepare` und `src/extract` nicht.
Einige Testdateien setzen ihren Importpfad zusaetzlich selbst. Welche
es sind, zeigt `grep -l sys.path tests/*.py`.

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
| `test_schema_validation.py` | Schema, Belegstaerke nach E6 und Zitatregeln des Prompts, seit 27.09.2026 auch Leerraum am Rand eines Zitats | erfundenes oder falsch verortetes Zitat gilt als belegt, Belegstaerke falsch |
| `test_prompt_input.py` | Auswahl und Budget der Modelleingabe (E5) | Quelldaten still weggelassen oder Budget ueberschritten |
| `test_prompt_files.py` | Prompt v1 und v2 gegen das Schema; v2 darf nur die Regeln fuer Zitate aus Diffs aendern | Prompt und Schema passen nicht zusammen, v2 aendert unbemerkt mehr |
| `test_pseudonymise.py` | Ersetzung von Erwaehnungen (E9) | Anmeldename gelangt unersetzt in die Modelleingabe |
| `test_draw_sample.py` | Schalter `--sizes` und `--exclude` (E10 a) | Stichprobe falsch zusammengesetzt |
| `test_run_extraction.py` | Aufrufprogramm ohne Netz, mit erfundenen Antworten; seit 21.10.2026 auch der Aufrufweg zur Anthropic-Schnittstelle, geprueft gegen 22 absichtlich eingebaute Fehler (21 erkannt, einer ohne Wirkung) | Antwort oder Laufdaten falsch festgehalten |
| `test_diagnose_excerpts.py` | Zuordnung jedes abgelehnten Zitats zu Ursache und Regel; gleiche Ablehnungen wie `validate_output.py`; keine Zitatinhalte in der Ausgabe | Ablehnung der falschen Regel zugeordnet, Zitatinhalt im Terminal |
| `test_inspect_excerpts.py` | Auswahl der Zitate nach Regel 3 wie im Suchprogramm, Hinweis H1, Schutz gegen Umleitung, Zuordnungstabelle ohne Inhalte, Auszaehlung | falsches Zitat angezeigt, Inhalt landet in einer Datei, fehlerhafte Tabelle wird gezaehlt |
| `test_breakdown_rejections.py` | Ablehnungen nach der ersten verletzten Pruefung, Abgleich mit `validate_output.py`, keine Modelltexte in der Ausgabe | Ablehnung der falschen Pruefung zugeschrieben, Summe weicht still ab |
| `test_cost_report.py` | Abschnitt 6.3 aus dem Manifest, Abgleich der Bezugswerte mit ihren Quelldateien, Anhaengen nur einmal und nur am Ende | Messwert falsch uebertragen, Abschnitt doppelt oder an falscher Stelle |
| `test_add_links.py` | Ein Link je Beleg, nur aus von GitHub gelieferten Links, nur fuer denselben Pull Request | Beleg zeigt auf den falschen Kommentar oder eine fremde Adresse |
| `test_count_requirements.py` | Zaehlung nach F3 (M2) und G1: gefundene Belege, Belegstaerke nur aus gefundenen Belegen, keine eigene Pruefregel | Anforderung falsch als belegt oder unbelegt gezaehlt |
| `test_check_classification.py` | Pruefung der Klassifikation nach G4 und G5: Mengen, verblindeter Pruefbogen, Pruefung der Antworten, Sperre per Pruefsumme, Dependabot-Sichtung | falsche Menge geprueft, Etikett des Modells auf dem Bogen, Antwort nachtraeglich geaendert |
| `test_gap_analysis.py` | Gap-Analyse nach G6: Kandidaten, Kategorien, Gegenprobe senkt nur | Eintrag in zu hoher Kategorie, Gegenprobe hebt eine Belegstaerke |
| `test_evaluate_requirements.py` | Bewertung nach E2 und Kriterienliste v1: verblindeter Bogen, Pruefung und Sperre der Antworten, B8 bis B10, Nebenteil, Auszaehlung und Regel brauchbar | Etikett des Modells auf dem Bogen, Antwort nachtraeglich geaendert, Kriterium falsch gezaehlt |
| `test_count_ff3_measures.py` | M1 Teil b, M3 und Angabe (i) nach F3, Abgleich mit der Zaehldatei | Fundstellen falsch verglichen, Abweichung von der Zaehldatei bleibt unbemerkt |
| `test_compare_b9_g1.py` | Abgleich von B9 und Belegbegriff G1 je Anforderung, Abgleich mit beiden Ergebnisdateien, Pruefsumme des Programms | gleiche Zahlen gelten als gleiche Mengen, Grund einer Abweichung falsch zugeordnet |
| `test_compare_runs.py` | Vergleich zweier Laeufe an einer Stichprobe nach E12 j, seit 21.10.2026; geprueft gegen 17 absichtlich eingebaute Fehler (16 erkannt, einer ohne Wirkung) | Laeufe vermischt, Ablehnungen anders gezaehlt als von validate_output.py, Modelltext in der Ausgabe |

## Test gegen absichtlich eingebaute Fehler

In Paket D schlugen bei vertauschtem `outcome` und bei einer Reinigung
ohne Abschlussmarker sechs der damals 26 Tests fehl. Seit Paket D
Teil 3 wird jede neue Testdatei so geprueft. Am 27.09.2026:
23 absichtlich eingebaute Fehler in `validate_output.py` und
`diagnose_excerpts.py`, jeder von mindestens einem Test erkannt.
Am 28.09.2026 fuer die vier neuen Dateien: 18 eingebaute Fehler in
`inspect_excerpts.py` und `breakdown_rejections.py`, alle erkannt;
16 in `cost_report.py` und `add_links.py`, davon 15 erkannt, einer
ohne Wirkung, weil eine zweite Pruefung denselben Fall abfaengt. Die
Nachweise liefen in der Umgebung von Claude.
Fuer die drei Dateien aus Paket G: `count_requirements.py` gegen 16
eingebaute Fehler geprueft, `check_classification.py` gegen 22,
`gap_analysis.py` gegen 22, davon 21 erkannt und einer ohne Wirkung.
Paket H: `evaluate_requirements.py` gegen 30 eingebaute Fehler,
alle erkannt; `count_ff3_measures.py` gegen 18, alle erkannt (Chat
vom 08./09.10.2026). `compare_b9_g1.py` am 10.10.2026 gegen 22,
davon 19 erkannt und 3 ohne Wirkung: Sie vertauschen Werte, die in
der betroffenen Teilmenge nach den Regeln immer gleich sind.

## Noch nicht abgedeckt

- Die Netzschicht in `github_api.py` (Wiederholung, Ratengrenzen,
  Paginierung). Sie wurde im Betrieb geprueft, nicht automatisiert.
- Die Auswertungsskripte unter `src/collect/`.
- `draw_sample.py` ausserhalb der Schalter `--sizes` und `--exclude`
  (siehe D4a).
