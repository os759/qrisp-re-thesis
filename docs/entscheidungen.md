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

## 2026-08-12 Korrektur zu "Evaluation reduziert" (2026-07-31)

Der Eintrag vom 31.07. ist ueberholt. Es gilt die Exposé-Variante:
Das Qrisp-Team wird durch den Professor informiert und bewertet, sobald
das Werkzeug fertig ist; ergaenzt um eine dokumentierte
Selbstbewertung. Bei mehreren Bewertenden wird ein Uebereinstimmungsmass
moeglich. Die Selbstbewertung ist Ergaenzung, nicht Ersatz.
Terminabhaengigkeit: Werkzeug bis Ende Woche 8 bewertbar, Git-Tag
thesis-v1.0.
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

## 2026-08-12 Speicherformat JSONL

Ein JSON-Datensatz je Zeile.
Begruendung: Bricht der Abruf bei PR 300 von 476 ab, bleibt jede bereits
geschriebene Zeile gueltig und der Abruf ist fortsetzbar. Eine einzelne
JSON-Datei waere in diesem Fall unbrauchbar, weil die schliessende
Klammer fehlt. CSV scheitert an verschachtelten Feldern und langen
Texten mit Zeilenumbruechen. SQLite waere technisch ueberlegen, kostet
aber SQL-Einarbeitung ohne Beitrag zu einer Forschungsfrage und laesst
sich in Git nicht vergleichen.
Bezug: FF1, Reproduzierbarkeit.

## 2026-08-12 Keine Datensaetze im Repository, Nachweis ueber Pruefsummen

data/raw/ und data/interim/ bleiben per .gitignore ausgeschlossen
(Regel aus Paket A, hier bestaetigt). Versioniert wird ausschliesslich
das Manifest unter data/manifests/.
Begruendung: Git behaelt geloeschte Dateien in der Historie. Auch der
reduzierte Datensatz enthaelt Anmeldenamen im Klartext sowie
Beschreibungs- und Kommentartexte Dritter; bei einer Veroeffentlichung
nach der Abgabe waeren sie dauerhaft enthalten. Ein zwischenzeitlicher
Vorschlag, data/interim/ zu versionieren, wurde aus diesem Grund
verworfen.
Der Nachweis der Datensatzversion erfolgt ueber eine SHA-256-Pruefsumme
im Manifest. Sie belegt die Identitaet einer lokalen Datei, ohne deren
Inhalt zu veroeffentlichen.
Bezug: Datenschutz, Reproduzierbarkeit, FF1.

## 2026-08-12 Manifest je Erhebung

Zu jedem Abruf entsteht data/manifests/manifest_JJJJ-MM-TT.json mit:
Erhebungszeitpunkt in UTC, Repository und Repository-ID, API-Version,
Abrufparametern, Anzahl Datensaetze, Dateinamen und SHA-256-Pruefsumme
der erzeugten Dateien sowie dem Git-Commit des erhebenden Codes.
Begruendung: Erfuellt die Anforderungen an Dokumentation des
Erhebungszeitpunkts und Versionierung des Datensatzes und macht die
Datenbasis in Kapitel 5 zitierfaehig, ohne personenbezogene Daten in
die Versionsverwaltung aufzunehmen.
Bezug: Reproduzierbarkeit, FF1.

## 2026-08-12 Feldauswahl und abgeleitetes Feld outcome

Uebernommen werden die Kernfelder laut Projektanweisung sowie die
Zaehlfelder additions, deletions, changed_files, comments,
review_comments, commits, ferner author_association, draft, updated_at,
base.ref, base.sha und head.sha.
Zusaetzlich wird outcome berechnet: merged, closed_unmerged oder open.
Begruendung: state kennt nur open und closed und unterscheidet nicht
zwischen zusammengefuehrt und verworfen. Ein verworfener Pull Request
belegt keine umgesetzte Anforderung.
Ausgeschlossen: alle *_url-Felder ausser html_url sowie _links, weil aus
der PR-Nummer rekonstruierbar.
Vorbehalt: assignees, milestone, requested_reviewers, requested_teams,
auto_merge und locked waren in PR #797 leer. Der Abruf zaehlt ihre
Belegung; bei nennenswerter Haeufigkeit werden sie nachtraeglich
aufgenommen.
Bezug: FF1, Datenminimierung.

## 2026-08-12 Datenminimierung beim Autorenobjekt

Vom user-Objekt wird nur login uebernommen, die uebrigen 18 Felder
werden verworfen, darunter avatar_url, followers_url, gists_url,
organizations_url, subscriptions_url und starred_url.
Begruendung: login sichert die Rueckverfolgbarkeit einer Aussage auf
ihren Urheber und damit die Belegstaerke-Systematik. Die verworfenen
Felder erschliessen Aktivitaetsprofile weit ueber die untersuchte
PR-Historie hinaus und werden fuer keine Forschungsfrage benoetigt.
Bezug: Datenschutz, FF1.

## 2026-08-12 Pseudonyme in der schriftlichen Arbeit

Im Datensatz steht der Anmeldename im Klartext. In der Arbeit erscheinen
stattdessen Kennungen A01, A02 usw. Die Zuordnungstabelle liegt unter
docs/pseudonyme.csv und ist per .gitignore ausgeschlossen.
Begruendung: Fuer die Analyse ist Unterscheidbarkeit noetig, nicht
Identifizierbarkeit. Ueber die genannte PR-Nummer bleibt die
oeffentliche Originalquelle pruefbar.
Einschraenkung: keine Anonymisierung. Bei wenigen Beitragenden sind die
Kennungen ueber die PR-Nummern rueckfuehrbar. Gehoert in die
Limitationen. Datenschutzrechtliche Bewertung mit dem Betreuer klaeren.
Bezug: Datenschutz, FF1, Limitationen.

## Offene Entscheidungen

- Anforderungsformat (FF2), Paket C
- API-Modell und lokales Modell (FF3), Paket E und F
- Ausschnitt des Sicherheitsrasters (FF4), Paket G
- Umfang gegenueber dem Qrisp-Team: Was gehoert zur Arbeit, was ist
  Weiterentwicklung? Mit Professor zu klaeren.