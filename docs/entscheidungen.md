# Designentscheidungen

Je Entscheidung: Datum, Entscheidung, Begruendung, Alternativen,
Bezug zur Forschungsfrage, Status.

## 2026-07-31 Repository privat

Begruendung: Veroeffentlichung der Arbeit laut Vorlage auf Nein;
PR-Daten enthalten Klarnamen Dritter. Nach Abgabe umstellbar.
Bezug: Datenschutz, FF1.

## 2026-07-31 Evaluation reduziert

Bewertung durch den Betreuer, ergaenzt um dokumentierte
Selbstbewertung. Abweichung vom Exposé (dort zusaetzlich Qrisp-Team).
Schriftliche Bestaetigung ausstehend.
Folge: kein Uebereinstimmungsmass in der Evaluation; stattdessen
Abgleich LLM-Klassifikation gegen manuelle Klassifikation.
Bezug: FF1, FF2.

## 2026-08-05 Vorlage nicht in Einzeldateien aufgeteilt

Die HSRM-Vorlage raet bei 30-50 Seiten ausdruecklich davon ab,
Kapitel auszulagern. Alle Kapitel stehen in thesis.tex.
Bezug: formale Vorgaben.

## 2026-08-05 BibTeX-Eintragstyp misc statt standard

Der Stil plain kennt @standard nicht. Getestet: @misc kompiliert
fehlerfrei und stellt die Norm korrekt dar.
Bezug: formale Vorgaben.

## 2026-08-12 API-Version 2022-11-28, explizit und konfigurierbar

Jede Anfrage sendet X-GitHub-Api-Version: 2022-11-28. Der Wert steht in
config/collect.toml, nicht im Quelltext.
Begruendung: Ohne den Header wandert die Version still mit dem
GitHub-Standard mit; der Datensatz waere dann nicht reproduzierbar.
2022-11-28 ist ab Maerz 2026 noch mindestens 24 Monate unterstuetzt,
also weit ueber den Abgabetermin hinaus.
Alternative 2026-03-10 geprueft: entfernt merge_commit_sha und das
Einzelfeld assignee aus PR-Antworten. Beide werden nicht verwendet, der
Wechsel braechte keinen Vorteil. Als Wartungspunkt in den Ausblick.
Bezug: Reproduzierbarkeit, FF1.

## 2026-08-12 Codesprache Englisch

Bezeichner, Dateinamen und Kommentare im Quelltext sind englisch.
Begruendung: Qrisp ist ein Eclipse-Projekt mit englischer
Arbeitssprache und soll das Werkzeug nutzen koennen; Python-Schluessel-
woerter sind englisch, Mischsprache waere inkonsistent.
Die deutschsprachige Erlaeuterung erfolgt in Kapitel 5.
Bezug: Nachvollziehbarkeit, Uebergabe an das Qrisp-Team.

## 2026-08-12 Commit-Praefix code:

Neben lit:, bib:, tex: und chore: gilt code: fuer Quelltext.
Begruendung: chore: bezeichnet Hilfsarbeiten; die Implementierung ist
Kern der Arbeit und braucht ein eigenes Praefix.
Bezug: Nachvollziehbarkeit.

## 2026-08-12 Keine README.md in Unterordnern von src/

src/README.md beschreibt alle Unterordner. Zusaetzliche Dateien je
Unterordner leisten keinen Beitrag zu einer Forschungsfrage.
Bezug: keiner - bewusst gestrichen.

## 2026-08-12 Detailabruf je Pull Request notwendig

Belegt an PR #797: Listenendpunkt 36 Felder, Detailendpunkt 48, keine
Felder nur in der Liste. Nur im Detailabruf: additions, deletions,
changed_files, comments, commits, review_comments.
Begruendung: Diese Zaehlfelder geben die Groesse von Diff und
Diskussion an, bevor sie abgerufen werden. Sie sind die Grundlage fuer
den Umgang mit sehr grossen Diffs und ersparen leere Kommentarabrufe.
Aufwand: 5 Listenanfragen plus 476 Detailanfragen, innerhalb des
Stundenkontingents von 5000.
Bezug: FF1, Reproduzierbarkeit.

## 2026-08-12 Ausschluss volatiler Felder aus dem Datensatz

mergeable, mergeable_state und rebaseable werden nicht gespeichert.
Begruendung: GitHub berechnet sie zum Anfragezeitpunkt gegen den
aktuellen Hauptzweig. Sie aendern sich ohne Zutun der Autoren und sind
damit nicht reproduzierbar. merge_commit_sha entfaellt zusaetzlich, weil
es in API-Version 2026-03-10 nicht mehr geliefert wird.
Bezug: Reproduzierbarkeit, FF1.

## Offene Entscheidungen

- Anforderungsformat (FF2), Paket C
- API-Modell und lokales Modell (FF3), Paket E und F
- Ausschnitt des Sicherheitsrasters (FF4), Paket G
- Umfang gegenueber dem Qrisp-Team: Was gehoert zur Arbeit, was ist
  Weiterentwicklung? Mit Professor zu klaeren.
