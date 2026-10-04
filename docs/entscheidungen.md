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

## 2026-08-16 Paket D Teil 2: Datengrundlage der Entscheidungen D1 bis D4

Alle Zahlen in den folgenden vier Entscheidungen stammen aus
pull_details_2026-08-14.jsonl, 476 Datensaetze, SHA-256
19bc97ad11d3e097e873eb72cc84df283d20c9fffb61d8a1f7013151dfa03bd9.
Vollstaendiger Befund in docs/findings_pull_details.md, erzeugt von
src/collect/analyze_pull_details.py.

### 2026-08-16 D1 Umgang mit sehr grossen Diffs

Zweistufig. Bei der Erhebung wird nicht gekuerzt; der Abruf holt alle
Seiten. Gekuerzt wird erst in der Aufbereitung nach data/interim/.
Gekuerzte Datensaetze werden markiert. Die Dateiliste bleibt immer
vollstaendig, gekuerzt wird nur der Patch-Text.

Begruendung: Rohdaten sind ein getreues Abbild. Eine Kuerzung beim
Abruf waere unumkehrbar und jede spaetere Aenderung der Schwelle
erforderte einen vollstaendigen Neuabruf. Groesster PR: 575 geaenderte
Dateien, damit unterhalb der API-Grenze von 3000 Dateien je Pull
Request; durch die API selbst gehen keine Dateien verloren.

Vorgemerkte Schwelle: 2000 Zeilen (additions + deletions) je Pull
Request. Damit bleiben 421 von 476 Pull Requests (88,4 %) unveraendert.
Verteilung: Median 162 Zeilen, p90 2424, p99 18474, Maximum 30166.
55 Pull Requests (11,6 %) liegen ueber 2000 Zeilen und enthalten
76,6 Prozent aller geaenderten Zeilen.

Alternativen: Kuerzung schon beim Abruf, verworfen wegen
Unumkehrbarkeit. Feste Schwelle ohne Messung, verworfen, weil sie in
der Diskussion nicht begruendbar waere.

Status: Schwelle vorgemerkt, endgueltige Festlegung nach dem
Dateiabruf. Erst dann ist bekannt, ob die grossen Diffs aus erzeugten
Dateien bestehen; in diesem Fall waere eine Regel nach Dateityp
geeigneter als eine nach Zeilenzahl.
Bezug: FF1, Reproduzierbarkeit.

### 2026-08-19 D1 endgueltig: dreistufige Kuerzung in der Aufbereitung

Ersetzt die vorgemerkte Schwelle von 2000 Zeilen aus dem Eintrag vom
16.08. Datengrundlage: pull_files_2026-08-19.jsonl, 8424 Dateisaetze,
SHA-256 7315f5254a914278618c85c23422d7f2a04d1460ee8d8c6c6733f4e91533bbdc.
Befund in docs/findings_pull_files.md.

Die am 16.08. offene Frage ist beantwortet: Die grossen Pull Requests
bestehen NICHT aus erzeugten Dateien. Auf .py entfallen 81,0 Prozent
des Aenderungstextes, auf src und tests zusammen 80,7 Prozent. Die
beiden groessten, PR 674 und PR 676, sind zu 100 Prozent Python bei 574
bzw. 575 Dateien. Eine Regel allein nach Dateityp reicht daher nicht.

Stufe 1, Typausschluss. Kein Patch-Text fuer .ipynb, .drawio, .bkp und
.svg sowie fuer Dateien ohne patch-Feld. Dateiname, status, additions
und deletions bleiben erhalten. Begruendung: kein von Menschen
geschriebener Inhalt. Ein .ipynb-Diff besteht ueberwiegend aus
serialisierter Ausgabe. Wirkung: 170 Dateien, 11,0 Prozent des
Aenderungstextes. Bei PR 532 sind .drawio und .bkp zusammen 91 Prozent.

Stufe 2, Obergrenze je Datei: 10000 Zeichen. Wirkung: p90 der Dateien
liegt bei 9534 Zeichen, rund 90 Prozent bleiben unveraendert.
Verhindert, dass eine einzelne Datei das Budget eines Pull Requests
aufbraucht.

Stufe 3, Budget je Pull Request: 50000 Zeichen. Wirkung: 377 von 471
Pull Requests mit Dateien (80,0 Prozent) bleiben vollstaendig; 94
werden gekuerzt. Bei rund 3,5 Zeichen je Token entspricht das etwa
14000 Token Codeanteil je Pull Request.

Alle drei Werte stehen in der Konfiguration, nicht im Quelltext. Jede
Kuerzung wird am Datensatz markiert und geht in die Belegstaerke ein.
Der Wert der Stufe 3 wird in Paket E bestaetigt oder angepasst, sobald
Modell und Kontextgroesse feststehen; 50000 ist eine begruendete
Voreinstellung, keine Ableitung aus einem Modell.

Alternativen: reine Zeilenschwelle, verworfen, weil sie handgeschriebenen
Python-Code genauso trifft wie serialisierte Notebook-Ausgabe. Reine
Typregel, durch den Befund widerlegt.

Status: festgelegt, Stufe 3 unter Vorbehalt Paket E.
Bezug: FF1, Reproduzierbarkeit.

### 2026-08-16 D2 Bot-Beitraege

Regel: Ein Beitrag gilt als Bot-Beitrag, wenn user.type gleich "Bot"
ist ODER der Login auf "[bot]" endet. Bot-Beitraege werden nicht
geloescht, sondern mit dem abgeleiteten Feld author_is_bot markiert.
Der Ausschluss erfolgt erst in der Aufbereitung.

Begruendung: Loeschen beim Abruf ist unumkehrbar und waere gegenueber
dem Betreuer nicht belegbar. Markieren ist dokumentiert und umkehrbar.

Gemessen: 31 von 476 Pull Requests (6,5 %) von zwei Konten,
dependabot[bot] (28) und Copilot (3). Copilot endet nicht auf "[bot]"
und wird ausschliesslich ueber user.type erkannt. Eine Regel allein
ueber den Namen haette drei Pull Requests uebersehen.

Alternativen: Loeschen beim Abruf, verworfen. Erkennung nur ueber den
Namen, durch die Messung widerlegt.

Status: festgelegt. Fuer Kommentare gilt dieselbe Regel; sie ist nach
dem Kommentarabruf erneut zu pruefen, weil dort andere Konten auftreten
koennen.
Bezug: FF1, Absicherung der Pipeline.

### 2026-08-16 D3 Dateiaufteilung der Rohdaten

Eine Rohdatei je Endpunkt unter data/raw/, Zusammenfuehrung erst in
data/interim/. Jedes Manifest ab Paket D Teil 2 enthaelt das Feld
source_dataset mit Dateiname und Pruefsumme der zugrunde liegenden
Listendatei.

Begruendung: Die Endpunkte haben unterschiedliche
Mengenverhaeltnisse - ein Detaildatensatz je Pull Request, aber null
bis viele Kommentare und geaenderte Dateien. Getrennte Dateien bleiben
zeilenweise fortsetzbar nach Abbruch, und die Pruefsumme einer
abgeschlossenen Erhebung aendert sich nicht, wenn ein weiterer Abruf
folgt. Das Feld source_dataset belegt die Herkunftskette, auch wenn die
Dateien unterschiedliche Erhebungsdaten tragen.

Alternativen: eine zusammengefuehrte Rohdatei, verworfen wegen
notwendiger Verschachtelung und verlorener Fortsetzbarkeit.

Status: festgelegt.
Bezug: Reproduzierbarkeit, FF1.

### 2026-08-16 D4 Umfang der Tests

pytest. Getestet werden ausschliesslich reine Funktionen, deren Fehler
Daten unbemerkt verfaelschen: Wiederaufnahme abgebrochener Abrufe,
Ableitung von outcome, Normalisierung der Zeilenenden, JSONL-Ein- und
Ausgabe. Kein Nachbau der GitHub-API, keine Integrationstests, keine
Abdeckungsmessung.

Begruendung: Robustheit dient der wissenschaftlichen
Nachvollziehbarkeit und ist erwuenscht. Produktreife ist laut
Abgrenzung nicht Gegenstand der Arbeit. Getestet wird deshalb nur, wo
ein Fehler still Daten verfaelscht, nicht wo er sichtbar zum Abbruch
fuehrt.

Alternativen: unittest aus der Standardbibliothek, ohne neue
Abhaengigkeit, aber mit deutlich laengerem Testcode.

Status: festgelegt, Tests noch nicht geschrieben.
Bezug: Reproduzierbarkeit.

### 2026-08-16 Befunde mit Folgen fuer spaetere Pakete

- Durchgehend leer und damit endgueltig ausgeschlossen:
  requested_teams, auto_merge, active_lock_reason (je 0 von 476).
- labels nur bei 36 von 476 Pull Requests (7,6 %) belegt. Eine
  Klassifikation oder Vergleichsgrundlage auf Basis von Labels ist
  nicht moeglich. Relevant fuer Paket G.
- assignee 44 (9,2 %), assignees 47 (9,9 %), requested_reviewers 63
  (13,2 %), milestone 66 (13,9 %). Keine nennenswerte Haeufigkeit; der
  Vorbehalt im Eintrag vom 2026-08-12 zur Feldauswahl ist damit
  erledigt, die Felder bleiben ausgeschlossen.
- mergeable und rebaseable nur bei 136 von 476 belegt. Bestaetigt den
  Ausschluss als volatile Felder; GitHub berechnet den Wert in einem
  nachgelagerten Vorgang und liefert bis dahin null.
- 222 Pull Requests (46,6 %) haben keinerlei Kommentare. Nur 113
  (23,7 %) haben Review-Kommentare. Die Belegstaerke wird sich deshalb
  systematisch nach der Gespraechigkeit eines Pull Requests
  unterscheiden. Fuer Kapitel 7.
- 56 Pull Requests (11,8 %) haben keinen Beschreibungstext.
- Vorlagentext ("<!--") in 124 von 420 vorhandenen Beschreibungen
  (29,5 %). CRLF-Zeilenenden in 259 (61,7 %). Beide
  Aufbereitungsschritte sind noetig, aber nicht bei allen Datensaetzen.
- 61 Autoren; die drei aktivsten schrieben 236 der 476 Pull Requests
  (49,6 %), die zehn aktivsten rund 79 Prozent. Bedrohung der externen
  Validitaet, fuer Kapitel 7.
- locked ist in allen 476 Datensaetzen False. Das Feld ist konstant,
  traegt keine Information und wird nicht uebernommen.
- draft ist in 66 von 476 Datensaetzen True (13,9 %). Das Feld wird
  uebernommen. Bei 53 offenen Pull Requests sind mindestens 13 Entwuerfe
  bereits geschlossen. Ein als Entwurf geschlossener, nicht
  zusammengefuehrter Pull Request ist ein schwacher Beleg; in der
  Belegstaerke-Systematik zu beruecksichtigen.
- author_association nimmt nur zwei Werte an: CONTRIBUTOR (435) und
  NONE (41). Die Werte OWNER, MEMBER und COLLABORATOR kommen nicht vor,
  auch nicht beim aktivsten Konto mit 95 Pull Requests. Das Feld
  unterscheidet in diesem Repository nicht zwischen Kernentwicklung und
  externem Beitrag. Der Grund dafuer ist nicht untersucht. Soll diese
  Unterscheidung spaeter getroffen werden, ist sie anders herzuleiten,
  etwa ueber die Zahl der Beitraege oder ueber merged_by.

### 2026-08-16 Aenderung im Vorgehen

Ab sofort gilt: erst Quelltext committen, dann abrufen.
Begruendung: Beim Detailabruf am 14.08. war der ausfuehrende Code noch
nicht committet. Das Feld collector_commit im Manifest verweist daher
auf den Stand davor und identifiziert den ausfuehrenden Code nicht
eindeutig. Die Luecke wurde mit Commit fe95a1a geschlossen. In
Kapitel 5 zu benennen.
Bezug: Reproduzierbarkeit.

### 2026-08-19 Befunde aus dem Dateiabruf

Erhebung 19.08.2026 mit Commit 44c669f. Erstmals stimmt
collector_commit exakt mit dem ausfuehrenden Code ueberein.

- 8424 Dateisaetze zu 471 Pull Requests, 32557763 Zeichen
  Aenderungstext, 0 fehlgeschlagene Anfragen.
- GitHub liefert bei 331 von 8424 Dateien (3,9 Prozent) kein
  patch-Feld. Damit ist gemessen, dass die API selbst kuerzt. Betroffen
  vor allem Binaerdateien (.png 151, .jpg 7, .docx 2, .pptx 1), aber
  auch 128 .py-Dateien, vermutlich wegen Ueberschreitung der
  Groessengrenzen. Untere Grenze der Datenlage, nicht beeinflussbar.
- Eine Abweichung: PR 470, erwartet 7, geholt 14. Geklaert: updated_at
  ist von 2026-06-13 auf 2026-08-17 gewandert, die Commits von 16 auf
  22. Der Pull Request wurde nach dem Detailabruf weiterbearbeitet.
- Fuenf Pull Requests ohne jede Codeaenderung: 169, 332, 407, 408, 578.
  Bereits am 14.08. changed_files=0, additions=0, deletions=0, alle
  geschlossen und nicht zusammengefuehrt. Fuer diese Pull Requests
  bleiben nur Titel, Beschreibung und Kommentare als Quelle. In der
  Belegstaerke-Systematik zu beruecksichtigen.
- 32557763 Zeichen entsprechen bei rund 3,5 Zeichen je Token grob 9
  Millionen Token. Kein Modell verarbeitet das am Stueck. Die
  Aufbereitung ist damit zwingend, nicht optional.

Bezug: FF1, Reproduzierbarkeit, Limitationen.

### 2026-08-19 Sprache der Programmausgaben

Programme unter src/ geben ihre Meldungen und Berichte auf Englisch
aus, einschliesslich der Dateinamen erzeugter Berichte. Eigene
Arbeitsunterlagen unter docs/ und literatur/ bleiben deutsch.
Begruendung: Praezisierung der Entscheidung vom 12.08. Die Ausgabe
eines Programms gehoert zum Programm; das Qrisp-Team soll das Werkzeug
benutzen koennen. Die Entscheidungs- und Literaturdateien sind
Vorstufen der deutschsprachigen Arbeit.
Folge: befund_pull_details.md und befund_pull_files.md ersetzt durch
findings_pull_details.md und findings_pull_files.md. Zahlen unveraendert,
gegen die alte Fassung geprueft.
Bezug: Nachvollziehbarkeit, Uebergabe an das Qrisp-Team.

## 2026-08-19 Kommentarabruf und vier Abweichungen

Erhebung 19.08.2026 mit Commit c4f0dee. Zwei Rohdateien nach D3:
issue_comments_2026-08-19.jsonl (639 Kommentare) und
review_comments_2026-08-19.jsonl (1713 Kommentare), je 476 von 476 Pull
Requests, 0 fehlgeschlagene Anfragen. Erwartungswerte aus den
Zaehlfeldern comments und review_comments des Detailabrufs vom
14.08.2026.

Vier Pull Requests weichen vom Erwartungswert ab. Alle vier wurden
einzeln geprueft.

PR 639, allgemeine Kommentare, erwartet 1, geholt 4: geklaert. Drei
Kommentare tragen das Datum 18.08.2026, liegen also nach dem
Detailabruf. Der heutige Zaehlstand bestaetigt den Zuwachs
(comments 1 -> 4). Es fehlt nichts; der Erwartungswert war veraltet.
Belegt zugleich, dass sich die Datenbasis innerhalb weniger Tage
messbar aendert, und begruendet Zeitstempel und Pruefsumme je
Erhebung.

PR 331 (154/153), PR 344 (1/0) und PR 767 (5/4), Review-Kommentare:
nicht aufloesbar. Die heutigen Zaehlstaende sind unveraendert, ein
Zeitversatz scheidet damit aus. Eine erneute Abfrage liefert
reproduzierbar dieselben Werte wie der Abruf. Der Endpunkt
pulls/{nr}/comments gibt also dauerhaft weniger Kommentare heraus, als
das Zaehlfeld review_comments angibt.

Bei PR 344 listet der Endpunkt pulls/{nr}/reviews kein einziges Review,
obwohl ein Review-Kommentar gezaehlt wird. Vermutet, aber nicht
belegbar: ein nicht abgeschicktes Review im Zustand pending, das nur
seinem Verfasser sichtbar ist. Eine Pruefung waere nur mit dem Konto
der jeweiligen Person moeglich und unterbleibt.

Umfang: 3 von 1716 Review-Kommentaren, 0,17 Prozent. Keine Korrektur,
keine Schaetzung, kein Ersatzwert. Die Abweichungen stehen je Erhebung
im Manifest unter deviations und gehen als Limitation in Kapitel 7.

Status: dokumentiert, nicht aufgeklaert.
Bezug: FF1, Limitationen.

## 2026-08-21 Paket D Teil 3: Aufbereitung nach data/interim/

Alle Zahlen in den folgenden Entscheidungen stammen aus dem Lauf von
src/prepare/build_interim.py am 19.08.2026 mit Commit f7f8c52.
Ergebnisdatei data/interim/pulls_prepared_2026-08-19.jsonl, 476
Datensaetze, SHA-256
138e60ce47c1e6508d14ea6cec113c11e72772407fef2232870e2b1b981a4683.
Manifest data/manifests/manifest_prepared_2026-08-19.json.

### 2026-08-21 D5 Ein Datensatz je Pull Request, Teile eingebettet

Die vier Rohdateien werden zu einer JSONL-Datei zusammengefuehrt. Eine
Zeile entspricht einem Pull Request und enthaelt Kommentare und
geaenderte Dateien als eingebettete Listen. Verbindendes Feld ist
collected_pull_number aus den Abrufskripten.

Begruendung: Die Verarbeitungseinheit in Paket E ist ein Pull Request.
Ein Prompt erhaelt Titel, Beschreibung, Diskussion und Codeauszuege
eines einzelnen Pull Requests. Lagen diese Teile in vier Dateien,
muesste jedes spaetere Skript sie erneut zusammenfuehren. Die
Begruendung von D3 traegt hier nicht: sie stuetzt sich auf
Fortsetzbarkeit nach Abbruch und Stabilitaet der Pruefsumme des
Netzabrufs. Die Aufbereitung laeuft lokal, ist in unter zwei Minuten
wiederholbar und jederzeit aus data/raw/ reproduzierbar. Ausserdem
rechnet Stufe 3 aus D1 je Pull Request; dazu muessen alle Dateien eines
Pull Requests gleichzeitig vorliegen.

Alternative: getrennte Dateien mit Verweis ueber die PR-Nummer,
verworfen, weil sie in jedem Folgeschritt eine Zusammenfuehrung
erzwingt, ohne einen Vorteil zu bieten.

Wirkung: 476 Zeilen, 20 MB. Nicht versioniert (data/interim/ ist per
.gitignore ausgeschlossen); Nachweis ueber das Manifest.
Status: festgelegt.
Bezug: FF1, Reproduzierbarkeit.

### 2026-08-21 D1 Ergaenzung: Reihenfolge bei Stufe 3

Das Budget von 50000 Zeichen je Pull Request wird in der Reihenfolge
verbraucht, in der die API die Dateien liefert. Die Datei, bei der das
Budget endet, wird abgeschnitten und markiert. Alle folgenden Dateien
behalten Name, status, additions und deletions, aber keinen Patch-Text.

Begruendung: Eine gleichmaessige Aufteilung ergibt bei 574 Dateien rund
87 Zeichen je Datei und damit keinen lesbaren Ausschnitt. Eine Auswahl
nach Dateigroesse setzt voraus, dass gross gleich wichtig ist; dafuer
gibt es keinen Beleg.

Einschraenkung, die in Kapitel 7 gehoert: Die Lieferreihenfolge der API
ist keine Rangfolge nach Bedeutung. Bei sehr grossen Pull Requests
entscheidet damit die Sortierung, welcher Code in die Extraktion geht.
Jede Kuerzung ist am Datensatz markiert und geht in die Belegstaerke
ein.
Status: festgelegt, ueberpruefbar in Paket E.
Bezug: FF1, Limitationen.

### 2026-08-21 D6 Unvollstaendige Pull Requests bleiben enthalten

Pull Requests ohne Beschreibungstext (56) und ohne Codeaenderung (5)
bleiben in data/interim/ und werden markiert: has_body,
has_code_changes, has_patch_text, counts_dataset. Eine Auswahl erfolgt
erst dort, wo die Modelleingabe erzeugt wird.

Begruendung: Der Korpus bleibt bei 476, sodass alle bisherigen
Prozentangaben ihre Grundgesamtheit behalten. Ein Pull Request ohne
Codeaenderung traegt Titel und moeglicherweise Kommentare; ein
abgelehnter Vorschlag kann eine bewusst nicht umgesetzte Anforderung
belegen. D1 und D2 folgen bereits dem Muster kuerzen und markieren
statt loeschen.

Zur Reinigung des Beschreibungstexts: Entfernt werden nur
vollstaendige HTML-Kommentarbloecke von "<!--" bis "-->". Ein Marker
ohne Abschluss bleibt stehen und wird markiert, damit keine echte
Beschreibung verloren geht. Auf Patch-Text und diff_hunk wird die
Reinigung nicht angewandt, weil ein Kommentarmarker Bestandteil einer
geaenderten Datei sein kann.

Messergebnis: Die Zahl der Pull Requests ohne Beschreibung bleibt bei
56. Kein Beschreibungstext bestand ausschliesslich aus Vorlagentext
(body_emptied_by_cleaning = 0). Kein unabgeschlossener Marker im
gesamten Korpus (0). Die Vermutung, die Reinigung koenne Beschreibungen
leeren, ist damit widerlegt.
Status: festgelegt.
Bezug: FF1, Nachvollziehbarkeit.

### 2026-08-21 D7 Bots bleiben in data/interim/ - Praezisierung von D2

D2 vom 16.08. haelt fest, der Ausschluss der Bot-Beitraege erfolge
"erst in der Aufbereitung". Das wird praezisiert: Der Ausschluss
erfolgt erst bei der Erzeugung der Modelleingabe, nicht bereits in
data/interim/. Dort bleiben die 31 Bot-Beitraege enthalten und tragen
author_is_bot = true.

Begruendung: Markieren ist umkehrbar, Loeschen nicht. Dependabot
erzeugt Pull Requests, die Programmbibliotheken aktualisieren; solche
Aktualisierungen erfolgen haeufig wegen bekannter Sicherheitsluecken
und koennten damit fuer FF4 einschlaegig sein. Ob das fuer Qrisp
zutrifft, ist NICHT geprueft und ausdruecklich eine Vermutung. Genau
deshalb werden die Daten behalten, bis eine Messung vorliegt.

Status: festgelegt. Die Auswahl fuer die Modelleingabe ist in Paket E
zu treffen und dort zu begruenden. Die Messung, ob die 28
Dependabot-Beitraege sicherheitsbezogene Angaben enthalten, steht aus.
Bezug: FF1, FF4, Datenminimierung.

### 2026-08-21 D8 Fuenfter Testbereich: die Kuerzungsstufen

D4 vom 16.08. nennt vier Testbereiche. Ergaenzt wird ein fuenfter:
tests/test_truncation.py prueft prepare_files mit zwoelf Tests.

Begruendung: Die Kuerzung veraendert den Datensatz am staerksten. 4580
von 8424 Dateien (54,4 Prozent) verlieren ihren Patch-Text, und 77,3
Prozent aller Zeichen entfallen. Ein Fehler waere still: entfernter
Quellcode oder ein ueberschrittenes Budget faellt bei laufendem
Programm nicht auf. Damit erfuellt der Bereich das Auswahlkriterium
aus D4.

Geprueft werden: Typausschluss einschliesslich Grossschreibung,
fehlendes patch-Feld der API, Obergrenze je Datei, Budget je Pull
Request, Erhalt des Diff-Anfangs beim Abschneiden, Erhalt aller
Dateieintraege trotz entferntem Patch-Text, getrennte Zaehlung von
Ursprungs- und Restgroesse.

Gegenprobe: Die gesamte Testsuite wurde gegen absichtlich
eingebrachte Fehler geprueft. Bei vertauschtem outcome und einer
Reinigung ohne Abschlussmarker schlugen sechs von 26 Tests fehl; bei
verworfenen Dateieintraegen und umgekehrter Kuerzungsrichtung vier von
zwoelf. Die Tests bestehen also nicht nur, sie schlagen auch an.

Nicht abgedeckt bleiben: die Netzschicht in github_api.py (im Betrieb
geprueft, nicht automatisiert), die Auswertungsskripte und die
Schemavalidierung der LLM-Ausgaben (Paket E). Diese Luecken stehen in
tests/README.md.
Status: festgelegt, 38 Tests aktiv.
Bezug: FF1, Reproduzierbarkeit.

## 2026-08-23 Paket C: Vorentscheidungen zur Formatauswahl

### 2026-08-23 C1 Rekonstruierte Anforderungen werden auf Englisch formuliert

Die Pipeline gibt Anforderungen auf Englisch aus. Die schriftliche
Arbeit bleibt deutsch. Beispiele erscheinen im Original mit
deutscher Erlaeuterung.

Begruendung: Erstens ist es die konsequente Fortsetzung der
Entscheidung vom 19.08.2026 zur Sprache der Programmausgaben. Eine
rekonstruierte Anforderung ist eine Ausgabe des Programms, und das
Qrisp-Team soll das Werkzeug benutzen koennen. Zweitens sind die
Quellen englisch; eine deutsche Ausgabe erzwaenge eine Uebersetzung
und damit eine zusaetzliche Fehlerquelle zwischen Anforderungssatz
und belegendem Quellausschnitt. Drittens sind RFC 2119, EARS und
ISO/IEC/IEEE 29148 ausschliesslich fuer Englisch formuliert; eine
deutsche Modalitaetskonvention waere eine eigene Erfindung ohne
Beleg. Viertens ist die Formatkonformitaet maschinell pruefbar, weil
die Schluesselwoerter shall, WHEN, WHILE, IF und WHERE ein
geschlossenes Vokabular bilden.

Alternative Deutsch: verworfen. Sie verlangte eine selbst
aufgestellte Konvention und erschwerte die Bewertung durch das
Qrisp-Team.

Folge: Der bisher offene Punkt "deutschsprachige
Modalitaetskonvention festlegen" entfaellt. Der Absatz in
thesis.tex, der eine solche Festlegung ankuendigt, wird bei der
Ausarbeitung des Abschnitts zur Formatauswahl ersetzt.
Status: festgelegt.
Bezug: FF2, FF1.

### 2026-08-23 C2 Bewertungsgrundlage der Entscheidungsmatrix

Die Matrix wird zweifach abgestuetzt. Die Kriterien und der
ueberwiegende Teil der Bewertungen stammen aus der gelesenen
Literatur. Ergaenzend wird eine Formulierungsprobe von Hand an einer
kleinen, nach vorher festgelegten Regeln gezogenen Stichprobe echter
Qrisp-Pull-Requests durchgefuehrt. Ein Sprachmodell ist daran nicht
beteiligt.

Begruendung: Eine rein konzeptionelle Bewertung waere von einer
Praeferenz nicht unterscheidbar. Eine rein empirische Bewertung mit
dem Sprachmodell scheidet aus, weil sie je Kandidatenformat einen
eigenen Prompt und ein Modell voraussetzt. Ein schlechtes Ergebnis
liesse sich dann nicht dem Format, dem Prompt oder dem Modell
zuordnen. Das vermengte FF2 mit FF1 und FF3 und bedrohte die
Konstruktvaliditaet. Ausserdem setzt Paket E die Formatentscheidung
bereits voraus.

Die Probe misst insbesondere, ob die Quelldaten die von einem Format
verlangten Bestandteile ueberhaupt hergeben, etwa eine Rolle bei
User Stories oder einen belegten Ausloeser bei EARS. Damit wird eine
bisher begruendete Vermutung zu einer Messung.

Einschraenkungen, die in Kapitel 7 gehoeren: Die Probe ist eine
Selbstbewertung des Verfassers. Die Ziehungs- und Bewertungsregeln
werden vor dem Blick auf die Stichprobe festgelegt und versioniert.
Alle Versuche werden protokolliert, auch misslungene. Die gezogenen
PR-Nummern werden notiert, damit die Evaluationsstichprobe in
Paket H moeglichst andere Pull Requests umfasst.
Status: festgelegt, Regeln und Stichprobengroesse noch zu bestimmen.
Bezug: FF2, Limitationen.

### 2026-09-04 C2a Praezisierung zu C2: Rolle des Sprachmodells bei den Noten

C2 haelt fest, dass an der Formulierungsprobe kein Sprachmodell
beteiligt ist. Fuer die Noten, die aus der Literatur stammen (K1 bis
K5, K7, K8 und K10), wird die Rolle des Modells hier praezisiert.

Das Sprachmodell darf zu jeder Zelle der Entscheidungsmatrix die
Belegstelle mit Abschnittsangabe, einen Notenvorschlag und eine
Begruendung liefern. Es nennt zusaetzlich das Gegenargument, das zu
einer anderen Note fuehren wuerde. Die Note selbst vergibt der
Verfasser, nachdem er die Belegstelle in der Quelle nachgelesen hat.
Ein Vorschlag wird uebernommen, geaendert oder verworfen; alle drei
Ausgaenge sind moeglich.

Fuer die Formulierungsprobe bleibt C2 unveraendert. Dort war und
bleibt kein Sprachmodell beteiligt. Die Einstufungen der zwoelf Pull
Requests stammen vollstaendig vom Verfasser.

Begruendung: Ohne diese Praezisierung widersprechen sich C2 und
docs/ki-protokoll.md, weil das Protokoll die Vorschlagstaetigkeit des
Modells ausweist.

Verworfene Alternative: die Belegstellen ohne Notenvorschlag vorlegen.
Das haette den Ankereffekt vermieden, aber den Aufwand verdoppelt.

Einschraenkung fuer Kapitel 7: Ein Notenvorschlag wirkt als Anker. Die
zuerst genannte Zahl kann das eigene Urteil beeinflussen. Diese
Bedrohung der Konstruktvaliditaet ist auszuweisen. Bei den gemessenen
Kriterien K6 und K9 besteht sie nicht, weil dort kein Modellvorschlag
vorlag.

Reichweite: Diese Praezisierung betrifft ausschliesslich die
Entscheidungsmatrix in Paket C. Fuer die uebrige Zusammenarbeit gilt
unveraendert der Hinweis zur Arbeitsteilung in docs/ki-protokoll.md
und der Abschnitt "Zusammenarbeit im Chat" in STATUS.md. Dort darf das
Modell Vorschlaege zu Vorgehen, Code, Text und Recherche machen; der
Verfasser prueft und entscheidet.

Status: festgelegt am 04.09.2026. Die Note fuer K1 war zu diesem
Zeitpunkt bereits vergeben. Der Nachtrag erfolgte danach, wie schon
bei R9 und R10 am 30.08.2026.
Bezug: FF2, Limitationen.

### 2026-08-23 C3 Eine Kombination mehrerer Ebenen gilt als ein Format

Die Projektanweisung verlangt zu pruefen, ob eine Kombination
mehrerer Ebenen geeigneter ist als ein einzelnes Format. Das Exposé
spricht von der Auswahl eines Anforderungsformats. Beides wird so in
Einklang gebracht: Faellt die Wahl auf eine Kombination, wird diese
als ein festgelegtes Zielformat definiert, benannt und vollstaendig
spezifiziert.
Status: festgelegt.
Bezug: FF2, formale Vorgaben.

### 2026-08-23 C4 Kriterienkatalog, Skala und Entscheidungsverfahren

Der vollstaendige Katalog steht in docs/formatauswahl.md. Hier nur
die Festlegungen mit Begruendung.

Zehn Kriterien. Acht ergeben sich aus der Zielsetzung der Arbeit und
aus FF2. Zwei kommen hinzu. K9 Deckung durch die Quelldaten misst,
ob die Pull Requests die Pflichtbestandteile eines Ansatzes
ueberhaupt hergeben. Ohne K9 bliebe der bekannte Schwachpunkt der
User Story, naemlich die geforderte Rolle, eine Vermutung statt
einer Messung. K10 Kombinierbarkeit liefert den Massstab dafuer, ob
mehrere Ebenen widerspruchsfrei verbunden werden koennen. Da die
vier Ebenen unterschiedliche Aspekte einer Anforderung regeln, ist
eine solche Verbindung moeglich und zu pruefen; ohne K10 waere sie
nicht bewertbar.

Dreistufige ordinale Skala mit den Werten 2, 1 und 0, ergaenzt um
n. a. fuer nicht anwendbar und ? fuer nicht entscheidbar.
Begruendung: Die Belege sind Textstellen aus Normen und Aufsaetzen.
Aus ihnen ist ablesbar, ob eine Regel vorhanden, unvollstaendig oder
abwesend ist. Feinere Stufen taeuschten eine Genauigkeit vor, die
die Quellen nicht hergeben. Der Wert ? verhindert, dass im Zweifel
eine Note geraten wird.

Keine Gesamtsumme und keine Gewichte. Begruendung: K2 formale
Struktur, K4 maschinelle Verarbeitbarkeit und K8 automatische
Validierbarkeit haengen voneinander ab. Eine strenge Satzstruktur
wuerde dreimal belohnt; eine Summe waere dann ein Rechenfehler und
kein Befund. Stattdessen wird jeder Ebene eine Rolle zugewiesen:
verpflichtend, optional oder nicht verwendet. Eine Kombination
entsteht dadurch als Ergebnis und nicht als Vorgabe.

Ausschlussregel E1: Eine Ebene erhaelt die Rolle verpflichtend
nicht, wenn K9 mit 0 bewertet ist; die Rolle optional bleibt
moeglich. Begruendung: Ein Pflichtbestandteil ohne Beleg in der
Quelle zwingt das Modell zum Erfinden oder erzeugt eine Leerstelle.
Die Pipeline erzeugte dann unbelegte Angaben durch Konstruktion und
widerspraeche der Belegstaerke-Systematik.

Alternative verworfen: gewichtete Punktsumme. Sie waere durch die
genannte Abhaengigkeit verzerrt, und die Gewichte selbst waeren
unbelegt.

Einschraenkung fuer Kapitel 7: Die Schwellen 80 und 40 Prozent bei
K9 sowie die Zuordnung der Kriterien zu den Ebenen sind Setzungen
des Verfassers. Regel R8 verlangt deshalb, den gemessenen Wert zu
berichten und zu pruefen, ob eine andere Schwelle die Entscheidung
aendern wuerde. K7 Verstaendlichkeit wird nur ersatzweise bewertet
und ist erst nach der Bewertung in Paket H belastbar.

Status: festgelegt vor jeder Bewertung.
Bezug: FF2, Limitationen.

## 2026-09-07 Paket C: Nachtrag zum Testumfang

### 2026-09-07 D4a Praezisierung zu D4: keine Tests fuer das Ziehungsskript

src/analyze/draw_sample.py erhaelt keine automatischen Tests. Die
Abweichung von D4 wird begruendet statt behoben.

Begruendung: D4 verlangt Tests dort, wo ein Fehler still Daten
verfaelscht. Der Bezugsfall sind Skripte, die wiederholt Daten
erzeugen. Das Ziehungsskript ist einmal gelaufen, am 25.08.2026. Sein
Ergebnis liegt fest und ist dokumentiert: die zwoelf gezogenen
Nummern, der Startwert 20260823 und die SHA-256-Pruefsumme der
Eingabedatei stehen in docs/sample_formulation_probe.md. Die Ziehung
ist deterministisch; dieselbe Eingabedatei und derselbe Startwert
erzeugen dieselbe Auswahl.

Was die Reproduzierbarkeit sichert: Das Skript liegt im Repository.
Die Eingabedatei ist ueber ihre Pruefsumme eindeutig bestimmt. Der
Startwert ist dokumentiert. Eine vorhandene Ausgabedatei wird nur mit
--overwrite ueberschrieben.

Wiederholungslauf am 07.09.2026: Das Skript wurde mit derselben
Eingabedatei und demselben Startwert erneut ausgefuehrt, mit --output
auf einen Pfad ausserhalb des Repositorys. Die zwoelf gezogenen
Zeilen sind mit docs/sample_formulation_probe.md identisch. Auch die
Kennzahlen des Laufs stimmen ueberein: 476 Datensaetze gelesen, 31
Bot-Beitraege und 50 offene Vorgaenge ausgeschlossen, 395 in der
Grundgesamtheit. Die Reproduzierbarkeit der Ziehung ist damit nicht
nur belegt, sondern gezeigt.

Alternative verworfen: vier automatische Tests mit erfundenen Daten.
Sie haetten die Abweichung von D4 formal beendet, am dokumentierten
Ergebnis aber nichts geaendert. Der Wiederholungslauf leistet den
Nachweis der Reproduzierbarkeit mit geringerem Aufwand.

Einschraenkung fuer Kapitel 7: Der Nachweis erfolgte von Hand und ist
nicht automatisiert. Er wiederholt sich nicht, wenn das Skript spaeter
geaendert wird.

Status: festgelegt.
Bezug: Reproduzierbarkeit.

## 2026-09-08 Paket C: Formatentscheidung

### 2026-09-08 C5 Rollenzuweisung der vier Ebenen und Zielformat

Grundlage ist die vollstaendige Entscheidungsmatrix in
docs/formatauswahl.md Abschnitt 10 sowie die Formulierungsprobe in
docs/formatprobe_protokoll.md. Das Entscheidungsverfahren steht in
docs/formatauswahl.md Abschnitt 5.

#### 1 Rollenzuweisung

Jeder der vier Ebenen wird eine Rolle zugewiesen: verpflichtend,
optional oder nicht verwendet. Es wird nicht addiert und nicht
gewichtet (Regel R5). Die Zuweisung erfolgt kriterienweise.

| Ebene | Rolle |
|---|---|
| (a) Darstellungsperspektive: User Story | nicht verwendet |
| (b) Satz- und Syntaxmuster: EARS | verpflichtend |
| (c) Normative Modalitaet | nicht verwendet |
| (d) Qualitaets-, Sprach- und Attributregeln | verpflichtend, im Ausschnitt nach Abschnitt 4 |

Ebene (b) EARS, verpflichtend. Ebene (b) ist die einzige Satzebene mit
einer K9-Note ueber 0, also die einzige, deren Pflichtbestandteile die
Pull Requests mehrheitlich hergeben (9 von 12). Sie erreicht zusaetzlich
bei K2 formale Struktur, K5 Eignung fuer Modellausgaben und K8
automatische Validierbarkeit jeweils die Note 2.

Ebene (a) User Story, nicht verwendet. Die Ebenen (a) und (b) schliessen
einander im Satz aus; nur eine von beiden kann die Satzform stellen
(Befund zu K10). Ebene (b) ist in keinem Kriterium schlechter und in
sechs Kriterien besser. Ausschlaggebend ist K9: die von Ebene (a)
verlangte Rolle ist in 4 von 12 Faellen belegt, davon zwei nur pauschal.

Ebene (c) Normative Modalitaet, nicht verwendet. Zweck dieser Ebene ist
die Unterscheidung mehrerer Verbindlichkeitsstufen; die Messung ergibt
0 von 12 belegten Stufen. Eine Abstufung waere daher in jedem Fall
erfunden, was Ausschlussregel E1 verhindern soll. Die Verwendung des
Wortes shall folgt aus Ebene (b) und ist keine Aussage ueber die
Verbindlichkeit in der Quelle; siehe Abschnitt 3.

Ebene (d) Qualitaets-, Sprach- und Attributregeln, verpflichtend. Diese
Ebene erreicht bei K10 Kombinierbarkeit als einzige die Note 2 und
kollidiert mit keiner anderen Ebene, weil sie einen fertigen Satz
beurteilt statt eine Satzform vorzuschreiben. Sie erreicht bei K3
Verifizierbarkeit als einzige die Note 2 und traegt damit die
Nachweisbarkeit, die weder Ebene (a) noch Ebene (b) erzwingt. Sie ist
durch E1 nicht ausgeschlossen, weil K9 dort nicht anwendbar ist und
nicht anwendbar nach Regel R3 nie wie 0 wirkt.

Anwendung von E2: E2 greift nur bei aehnlichem Profil und war hier
nicht erforderlich, weil Ebene (b) Ebene (a) in jedem Kriterium
mindestens erreicht. Zur Kontrolle angewandt fuehrt E2 zum selben
Ergebnis, da es zuerst K9 heranzieht.

Reihenfolge nach R7: Alle vier Ebenen waren am 08.09.2026 einzeln
bewertet. Die Kombination wurde erst danach geprueft.

#### 2 Wahl der Schluesselwortkonvention

Es gilt die Konvention nach ISO/IEC/IEEE 29148:2018 Abschn. 5.2.4.
Verbindliche Anforderungen verwenden shall. Von must wird abgesehen.
RFC 2119 wird nicht als Modalitaetskonvention uebernommen.

Begruendung: Ebene (b) EARS ist verpflichtend und verwendet
ausschliesslich shall; die Konvention nach 29148 ist damit
widerspruchsfrei, die nach RFC 2119 nicht, weil sie MUST und SHALL
gleichsetzt und fuenf Stufen kennt. RFC 2119 Abschn. 6 verlangt
ausserdem eine Abwaegung, welche Stufe angemessen ist; diese Abwaegung
ist aus Quelldaten ohne belegte Stufe nicht zu treffen.

Praezisiert am 09.09.2026: Die Formulierung "widerspruchsfrei, die nach
RFC 2119 nicht" ist zu stark. RFC 2119 verlangt weder die Verwendung
aller fuenf Stufen noch beider Ausdruecke und fordert in Abschn. 6
einen sparsamen Gebrauch; eine dokumentierte Beschraenkung auf SHALL
waere moeglich. Tragend ist deshalb nicht eine Unvereinbarkeit, sondern
dass die Konvention ohne einen einzigen belegten Fall ihren Zweck
verliert. Die Entscheidung selbst bleibt unveraendert.

Ergaenzender Grund: RFC 2119 haelt im Abstract fest, dass die Wirkung
seiner Schluesselwoerter von der Verbindlichkeitsstufe des Dokuments
abhaengt, in dem sie stehen. Ein rekonstruiertes Anforderungsdokument
ist kein verabschiedeter Standard. Dieser Vorbehalt entfaellt mit der
Wahl von 29148.

Folge fuer die Matrix: Der bei K10 fuer Ebene (c) vermerkte Konflikt
ist damit aufgeloest. Die Zelle behaelt die Note 1, weil sie die Ebene
als Ganzes bewertet und die Matrix auf dem Stand bleiben soll, auf dem
sie in diese Entscheidung eingegangen ist. Die Aufloesung ist als
datierter Nachtrag bei der Zelle und in docs/formatauswahl.md
Abschnitt 9 vermerkt.

#### 3 Die Verbindlichkeit wird gesetzt, nicht rekonstruiert

Alle rekonstruierten Anforderungen verwenden einheitlich shall. Diese
Einheitlichkeit ist eine dokumentierte Konvention dieser Arbeit und
keine aus der Quelle gewonnene Eigenschaft.

Begruendung: Die Formulierungsprobe hat in keinem der zwoelf Faelle
eine explizite Verbindlichkeitsstufe gefunden. Ohne Konvention muesste
die Pipeline je Anforderung eine Stufe waehlen und dabei erfinden. Mit
Konvention steht in der Ausgabe eine offengelegte Festlegung.

Das Wort shall ist ein Formbestandteil des EARS-Musters. Es darf weder
in der Ausgabe noch in der Arbeit als Beleg fuer eine in der Quelle
dokumentierte Verbindlichkeit gelesen werden. Dieselbe Festlegung gilt
bereits fuer die Formulierungsprobe, siehe
docs/formatprobe_protokoll.md, Abschnitt "Pflichtbestandteile je
Ebene".

Umsetzung: Das Ausgabeschema der Pipeline fuehrt ein Feld, das
festhaelt, dass die Verbindlichkeit gesetzt und nicht belegt ist. Die
genaue Form des Feldes wird in Paket E festgelegt.

#### 4 Ausschnitt der Ebene (d)

Ebene (d) umfasst in docs/formatauswahl.md Abschnitt 1 die
Normabschnitte 5.2.5 bis 5.2.8 sowie die acht Sprachprobleme aus Big
EARS und die 13 QUS-Kriterien. Verpflichtend gilt davon ein
begruendeter Ausschnitt.

Verpflichtend, geprueft an jedem einzelnen Anforderungssatz:

1. ISO/IEC/IEEE 29148 Abschn. 5.2.7 vollstaendig. Das umfasst den
   Grundsatz, dass eine Anforderung das Was und nicht das Wie
   beschreibt, sowie die neun Klassen unbestimmter oder mehrdeutiger
   Ausdruecke.
2. Fuenf der neun Merkmale aus Abschn. 5.2.5: eindeutig (Unambiguous),
   vollstaendig (Complete), einzelbezogen (Singular), nachweisbar
   (Verifiable), vorlagenkonform (Conforming).
3. Drei Attribute aus Abschn. 5.2.8.2 als Pflichtfelder neben dem Satz:
   Identification, Rationale, Type.

Nicht Teil des Zielformats, mit Begruendung:

| Ausgeschlossen | Begruendung |
|---|---|
| Necessary (5.2.5) | Der Standard verlangt zu beurteilen, ob ohne die Anforderung eine Luecke in Faehigkeit oder Eigenschaft entstuende. Das setzt Kenntnis des tatsaechlichen Bedarfs voraus. |
| Feasible (5.2.5) | Der Standard nennt Kosten, Termine und Technik als Massstab. Diese Angaben enthaelt die Pull-Request-Historie nicht. |
| Correct (5.2.5) | Der Standard verlangt eine zutreffende Wiedergabe des Bedarfs, aus dem die Anforderung hervorging. Der Bedarf ist nicht dokumentiert. Das verwandte Anliegen wird durch die Belegstaerke-Systematik erfasst. |
| Appropriate (5.2.5) | Der Standard meint damit zwei Dinge: die passende Abstraktionsebene und den Verzicht auf Entwurfsvorgaben. Nur das Zweite ist an einem Satz pruefbar, und es ist bereits durch Abschn. 5.2.7 abgedeckt. Eine Aufnahme ergaebe einen zweiten Namen fuer dieselbe Pruefung. |
| Abschn. 5.2.6, fuenf Merkmale der Anforderungsmenge | Diese Merkmale gelten fuer die Menge, nicht fuer den einzelnen Satz. Sie werden als Bewertungskriterien der Evaluation in Paket H herangezogen. |
| Fuenf weitere Attribute aus 5.2.8.2 | Version Number, Owner, Stakeholder Priority, Risk und Difficulty sind aus der Historie nicht belegbar. Owner waere zudem eine personenbezogene Angabe und widerspraeche der Datenminimierung. |
| 13 QUS-Kriterien | Sie sind auf User Stories definiert und setzen Bestandteile wie die Rolle voraus. Ebene (a) wird nicht verwendet. |
| Acht Sprachprobleme aus Big EARS | Sie sind ein Instrument zur Bewertung vorhandener Anforderungen, kein Regelwerk fuer deren Erzeugung. Sie sind Kandidaten fuer den Bewertungsbogen in Paket H. |

Die Zuordnung der neun Merkmale aus Abschn. 5.2.5 auf am Satz pruefbar
und nicht pruefbar ist eine Einordnung des Verfassers und steht so
nicht im Standard.

Anhang C.1 des Standards ist normativ und schliesst eine
Konformitaetsbehauptung bei Verwendung eines Ausschnitts aus. Die
Arbeit orientiert sich an dem Standard und behauptet keine
Konformitaet. Der Ausschnitt ist mit diesem Eintrag begruendet und
dokumentiert.

#### 5 Umgang mit der Rolleninformation

Wo die Quelle einen Nutzniesser oder eine Rolle nennt, wird diese
Angabe im Attribut Rationale nach Abschn. 5.2.8.2 festgehalten.

Begruendung: Der Standard beschreibt Rationale als die Begruendung,
warum die Anforderung gebraucht wird, mit Verweis auf die stuetzenden
Belege. Wer eine Anforderung braucht und wozu, ist genau diese
Begruendung. Ein eigenes Feld waere eine Setzung ohne Beleg in einer
Quelle.

Offen fuer Paket E: Ob zusaetzlich ein eigenes Feld gefuehrt wird, das
die Rolle getrennt auszaehlbar macht, wird beim Entwurf des
Ausgabeschemas entschieden. Dafuer spraeche, dass die Deckungsquote der
Rolle ein Messwert fuer FF1 ist. Die Frage betrifft ein Ausgabefeld und
keine Formatregel; sie kann ohne Aenderung dieser Entscheidung
beantwortet werden.

#### 6 Das Zielformat

Nach Entscheidung C3 gilt eine Kombination mehrerer Ebenen als ein
festgelegtes Zielformat und wird benannt und vollstaendig
spezifiziert.

Bezeichnung: EARS-Satzform mit Qualitaetsregeln nach ISO/IEC/IEEE
29148, kurz EARS+29148.

Sprache: Englisch (Entscheidung C1).

Satzform. Die generische Syntax besteht aus einer optionalen
Vorbedingung, einem optionalen Ausloeser, dem Systemnamen, dem Wort
shall und der Systemreaktion. Die Reihenfolge der Klauseln ist
verbindlich. Pflichtbestandteile sind Systemname, shall und
Systemreaktion.

| Muster | Schluesselwort | Aufbau |
|---|---|---|
| Ubiquitous | keines | The <System> shall <Systemreaktion>. |
| State-driven | While, Nebenform During | While <Zustand>, the <System> shall <Systemreaktion>. |
| Event-driven | When | When <Ausloeser>, the <System> shall <Systemreaktion>. |
| Unwanted behaviour | If ... then | If <unerwuenschte Bedingung>, then the <System> shall <Systemreaktion>. |
| Optional feature | Where | Where <Merkmal vorhanden>, the <System> shall <Systemreaktion>. |

Eine Kombination mehrerer Muster zu komplexen Anforderungen ist
zulaessig.

Systemname. Der Systemname wird der Quelle entnommen, sofern sie eine
Komponente benennt. Andernfalls wird Qrisp verwendet. Diese Regel ist
eine Festlegung dieser Arbeit und wird in Paket E an den Daten
ueberprueft.

Modalwort. Durchgehend shall, ohne Abstufung, als gesetzte Konvention
nach Abschnitt 3.

Qualitaetsregeln je Satz. Der Ausschnitt nach Abschnitt 4.

Pflichtfelder neben dem Satz. Identification, Rationale und Type nach
Abschn. 5.2.8.2. Diese drei Felder sind der formatbezogene Teil des
Ausgabeschemas. Das vollstaendige Ausgabeschema der Pipeline wird in
Paket E festgelegt und enthaelt weitere Felder, unter anderem
Quellreferenz, Quellausschnitt und Belegstaerke.

Nicht Bestandteil des Zielformats. Die User-Story-Satzform, die
Abstufung der Verbindlichkeit nach RFC 2119, die Merkmale der
Anforderungsmenge nach Abschn. 5.2.6, die 13 QUS-Kriterien und die
acht Sprachprobleme aus Big EARS.

Maschinell pruefbarer Teil. Ein Programm kann pruefen: das Vorliegen
eines der fuenf Muster anhand seines Schluesselworts, die
Klauselreihenfolge, das Vorhandensein von shall, das Fehlen anderer
Modalwoerter sowie die Wortklassen aus Abschn. 5.2.7. Nicht maschinell
pruefbar sind die inhaltlichen Merkmale aus Abschn. 5.2.5.

#### 7 Verworfene Alternativen

User Story als Satzform. Verworfen wegen K9: die verlangte Rolle ist in
4 von 12 Faellen belegt. Ein Pflichtbestandteil ohne Beleg zwingt das
Modell zum Erfinden.

RFC 2119 als Modalitaetskonvention. Verworfen wegen des Widerspruchs zu
EARS und wegen der nicht entscheidbaren Sparsamkeitsregel. Der Ansatz
bleibt in Kapitel 2 als Grundlage dargestellt und ist nicht widerlegt,
sondern fuer diesen Anwendungsfall nicht geeignet.

Mischform aus (a) und (b) je nach Deckung. Verworfen, weil die Ausgabe
dann zwei Satzformen enthielte. Das erschwert die automatische
Formatpruefung und widerspricht C3, das ein einheitliches Zielformat
verlangt.

Ebene (d) vollstaendig. Verworfen, weil vier der neun Merkmale aus
Abschn. 5.2.5 aus der Pull-Request-Historie nicht beurteilbar sind und
die QUS-Kriterien ohne Ebene (a) gegenstandslos waeren.

#### 8 Einschraenkungen fuer Kapitel 7

- Die Note fuer Ebene (b) bei K9 haengt an einem einzigen Fall. Bei
  einem zusaetzlich gedeckten Fall waere sie 2 statt 1. Bei Ebene (a)
  gilt dasselbe in umgekehrter Richtung.
- EARS ist nach seinen Urhebern fuer hochrangige
  Stakeholder-Anforderungen entwickelt und erprobt. Pull-Request-Inhalte
  liegen auf Implementierungsebene. Die Uebertragung ist begruendet,
  aber nicht durch eine Quelle belegt.
- Das durchgehende shall kann von einer lesenden Person als Aussage
  ueber die Verbindlichkeit missverstanden werden. Der Vermerk in der
  Arbeit und im Datensatz faengt dieses Risiko nicht vollstaendig auf.
- Die Rolle geht als eigenstaendiger Satzbestandteil verloren. Sie wird
  nur noch im Attribut Rationale gefuehrt.
- Die Rollenbezeichnungen in docs/formatauswahl.md Abschnitt 5 sind fuer
  Satzmuster formuliert. Fuer Ebene (d) bedeutet verpflichtend, dass
  jede Anforderung gegen die Regeln geprueft wird, nicht dass sie einem
  Satzmuster folgt.
- Fuer Ebene (c) fallen die Rollen optional und nicht verwendet
  zusammen, weil die Quelle den Bestandteil in keinem Fall hergibt. Das
  Entscheidungsverfahren unterscheidet an dieser Stelle nichts mehr.
- Die Verwendung eines Ausschnitts des Standards schliesst nach dessen
  Anhang C.1 eine Konformitaetsbehauptung aus.
- Die Zuordnung der neun Merkmale aus Abschn. 5.2.5 auf pruefbar und
  nicht pruefbar ist eine eigene Einordnung.

#### 9 Herkunft dieser Entscheidung

Die Rollenzuweisung und die Teilentscheidungen hat der Verfasser am
08.09.2026 getroffen. Grundlage sind die Noten der Entscheidungsmatrix,
die der Verfasser zwischen dem 04. und 08.09.2026 selbst vergeben hat,
sowie die Messungen zu K6 und K9, die er selbst durchgefuehrt hat.

Das Sprachmodell hat nach Entscheidung C2a je Ebene einen
Rollenvorschlag, eine Begruendung und ein Gegenargument vorgelegt. Drei
Punkte gingen ueber die vorliegende Matrix hinaus: die Rolle nicht
verwendet fuer Ebene (c), die gesetzte Verbindlichkeitskonvention und
die Wahl von 29148 gegenueber RFC 2119. Der Verfasser hat sie als
eigene Einschaetzung bestaetigt.

Das Modell hat ISO/IEC/IEEE 29148 Abschn. 5.2.4 bis 5.2.8 sowie
RFC 2119 und RFC 8174 im Volltext gelesen. Die Volltexte von Mavin et
al. 2009, Mavin und Wilkinson 2010 und Lucassen et al. 2016 lagen ihm
nicht vor. Die Angaben zu EARS und zu User Stories stammen insoweit aus
den Lesenotizen unter literatur/notizen/ und aus den Abschnitten 2.2.2
und 2.2.3 der Arbeit.

Ein Notenvorschlag und ein Rollenvorschlag wirken als Anker. Diese
Bedrohung der Konstruktvaliditaet ist bereits in C2a benannt und gilt
hier fort.

Status: festgelegt.
Bezug: FF2, FF1, Limitationen.

## 2026-09-09 Paket C: Umfang der Matrix in der Arbeit

### 2026-09-09 C6 Notentabelle in Kapitel 4, Einzelbegruendungen gekuerzt in Anhang A

Die Entscheidungsmatrix steht als Notentabelle in Abschnitt 4.1.3.
Die Einzelbegruendungen zu den vierzig Zellen stehen gekuerzt in
Anhang A. Die vollstaendige Fassung bleibt in docs/formatauswahl.md
Abschnitt 10 (Weg C).

Begruendung: Die Formatauswahl beantwortet FF2. Eine Notentabelle
ohne einsehbare Begruendung ist als Beleg schwach. Die
Arbeitsunterlage wird zwar mit dem Repository abgegeben, ist aber
nicht Teil des Dokuments; eine pruefende Person muesste sie
gesondert oeffnen. Die ungekuerzten Begruendungen wuerden als Anhang
wie Rohmaterial wirken.

Alternativen verworfen:
- Weg A, nur die Notentabelle und Fliesstext zu den ausschlaggebenden
  Kriterien: Die Einzelbegruendungen waeren im Dokument nicht
  nachvollziehbar.
- Weg B, alle Einzelbegruendungen ungekuerzt als Anhang: nach
  damaliger Schaetzung fuenfzehn bis zwanzig Seiten Rohmaterial.

Herkunft: Die Gegenueberstellung der drei Wege und die Empfehlung fuer
Weg C stammen aus einem Chat mit einem Sprachmodell. Entschieden hat
der Verfasser am 09.09.2026. Den Wortlaut der Gegenueberstellung hat
er am 10.09.2026 im Folgechat wiedergegeben.

Nachtrag 10.09.2026, Platzierung: Anhang A steht nach dem
Literaturverzeichnis. STATUS.md hatte die Platzierung davor
vorgesehen. Das Literaturverzeichnis beginnt in der Vorlage mit
\section* und bildet kein eigenes Kapitel. Nach einem \appendix
wuerde es deshalb zu einem Teil von Anhang A. Das zeigte eine
Testuebersetzung des Modells mit Ersatzpaketen fuer babel-german,
bibtopic und soul. Das PDF des Verfassers bestaetigte, dass das
Literaturverzeichnis schon jetzt ohne Seitenumbruch an das letzte
Kapitel anschliesst. Die Abweichung hat der Verfasser am 10.09.2026
entschieden. Die Vorlage bleibt unveraendert.

Nachtrag 10.09.2026, Form und Kuerzungsregeln (vom Verfasser
freigegeben):
- Je Kriterium ein \section mit Label sec:anhang-kN. Je Zelle ein
  Eintrag in einer description-Liste mit Beleg, Begruendung und
  Gegenargument samt der Note, zu der es fuehren wuerde.
- Vorbemerkungen tragen die Vorfrage zu K2 und die Vorbehalte zu K4
  und K5.
1. Noten und Fundstellen kommen unveraendert aus Abschnitt 10.
   Ergaenzungen nur mit Freigabe. Mit dem Entwurf uebernommen wurden
   zwei zusaetzliche Abschnittsangaben zu Mavin/Wilkinson 2010: bei
   K2 Ebene (b) ausdruecklich freigegeben, bei K5 Ebene (d).
2. Klammer-Erlaeuterungen im Beleg entfallen; noetiger Inhalt wandert
   in die Begruendung.
3. Begruendung ein Satz, hoechstens zwei.
4. Gegenargument ein Satz mit der Note, zu der es fuehren wuerde.
5. Hinweise zur Stufe 2 (R11) bleiben als ein Satz, wo Abschnitt 10
   sie fuehrt.
6. Es entfallen Befund-Absaetze, Vermerke zur Belegpruefung,
   Herkunftszeilen und Berichtigungsvermerke.
7. Keine internen Kuerzel wie R11, C5, "Paket E" oder Pfade zu
   Lesenotizen; stattdessen Verweise auf Abschnitte der Arbeit.
8. Messwerte erhalten einen Verweis auf Tabelle tab:deckung oder
   Abschnitt 4.1.2.
Eine Kuerzung aus Platzgruenden ist nicht vorgesehen (Verfasser,
10.09.2026). Der Vorspann enthaelt einen Satz zur Herkunft der Noten:
Das Sprachmodell hat Belegstellen, Notenvorschlaege und
Gegenargumente vorgelegt; die Noten hat der Verfasser zwischen dem
04. und 08.09.2026 nach Pruefung an den Originalquellen vergeben.

Status: festgelegt.
Bezug: FF2, Nachvollziehbarkeit, formale Fertigstellung.

Nachtrag vom 11.09.2026 (Durchgang 2, K6 bis K10): Der Verfasser hat
sieben Abweichungen vom Wortlaut in Abschnitt 10 freigegeben. Vier
sind Berichtigungen; sie stehen in der Aenderungshistorie von
docs/formatauswahl.md vom 11.09.2026 und sind dort in Abschnitt 10
nachgezogen. Drei sind Ergaenzungen, die es in Abschnitt 10 nicht
gibt: eine Vorbemerkung bei K6 und K9 zur Herkunft der gemessenen
Noten, die Tabelle A.1 mit den sechs Formulierungsversuchen sowie je
ein zusaetzliches Gegenargument bei K6 Ebene (b) und K9 Ebene (c).
Grund: Der Vorspann von Anhang A beschreibt das Verfahren nach C2a,
das fuer die beiden gemessenen Kriterien nicht gilt. Keine Note
aendert sich.

## 2026-09-15 Paket E: Datenmodell, Evaluationsform und Budget

### 2026-09-15 E1 Datenmodell der strukturierten Ausgabe

Die Ausgabe der Extraktion hat drei Ebenen. Die Lauf-Ebene mit Modell,
Version, Parametern, Prompt-Version, Datum und Umgebung wird als
Manifest gefuehrt, wie in Paket D. Die Vorgang-Ebene traegt je Pull
Request den Verarbeitungsstand. Die Anforderungs-Ebene traegt die
einzelnen rekonstruierten Anforderungen.

Das Schema steht als config/requirement_schema_v1.json im Repository.
Es ist in JSON Schema geschrieben, Entwurf 2020-12. Geprueft wird es
mit dem Paket jsonschema 4.26.0.

Verarbeitungsstand. Drei Werte: requirements_found,
no_requirements_found, input_unusable. Bei den letzten beiden ist eine
Begruendung Pflicht und die Liste muss leer sein. Grund: Ein Vorgang
ohne Anforderung ist ein gueltiges Ergebnis und muss von einem
gescheiterten Lauf unterscheidbar bleiben. Die Quote ist ein Messwert
fuer FF1.

Sechzehn Felder je Anforderung. Elf davon sind Pflicht. Herkunft:
elf Felder aus der Aufgabenstellung zu Punkt 4, drei Attribute aus
ISO/IEC/IEEE 29148 Abschn. 5.2.8.2 (Identification, Rationale, Type)
nach Entscheidung C5, dazu zwei Felder aus C5 selbst.

Wertemenge des Attributs Type. Sie wird aus 29148 Abschn. 5.2.8.3
uebernommen: functional_performance, interface, process,
quality_non_functional, usability_quality_in_use. Die Menge ist
geschlossen.

Sicherheitsbezug als eigenes Feld. Abschn. 5.2.8.3 fuehrt security als
eine Eigenschaft unter Quality (Non-Functional). Eine eigene Art gibt
es dort nicht. Fuer FF4 wird ein getrenntes Wahrheitsfeld
security_relevant gefuehrt. Damit kann eine Anforderung zugleich
funktional und sicherheitsrelevant sein. Die Trennung ist eine
Festlegung dieser Arbeit und keine Vorgabe des Standards.

Begruendung in einem Feld. Die in der Aufgabenstellung verlangte
Begruendung und das Attribut Rationale nach Abschn. 5.2.8.2 werden in
einem Feld gefuehrt. Der Standard beschreibt Rationale als den Grund,
warum die Anforderung gebraucht wird, mit Verweis auf die stuetzenden
Belege. Die Gleichsetzung ist eine Einordnung des Verfassers.

Nutzniesser als eigenes Feld, optional. C5 Abschnitt 5 hatte das offen
gelassen. Das Feld beneficiary wird gefuehrt, ist aber nicht Pflicht.
Grund: Die Deckungsquote der Rolle ist ein Messwert fuer FF1. Die
Rolleninformation bleibt zusaetzlich im Feld rationale, wie C5 es
verlangt.

Marker fuer die gesetzte Verbindlichkeit. Das Feld
modality_set_by_convention hat den festen Wert true und laesst sich
nicht abschalten. Es setzt C5 Abschnitt 3 um: Das Wort shall ist eine
Konvention dieser Arbeit und kein Beleg fuer eine dokumentierte
Verbindlichkeit.

Keine erfundenen Zusatzfelder. Das Schema weist jedes Feld zurueck,
das nicht vorgesehen ist. Eine vom Modell frei erzeugte Zahl, etwa
eine Konfidenz, wird damit abgelehnt statt stillschweigend
uebernommen.

Belegstaerke. Die Wertemenge lautet direct, indirect, insufficient.
Die Zuordnungsregeln sind noch offen und werden in E6 festgelegt.

Regel zum Quellausschnitt. Jeder Ausschnitt muss woertlich in der
benannten Quelle stehen. Bei einem Diff gilt das nach Entfernen der
Zeichen am Zeilenanfang. Zeilen, die die Aenderung entfernt hat,
zaehlen nicht als Quelle, weil sie nach der Aenderung nicht mehr im
Code stehen. Diese Praezisierung ergab sich aus einem fehlgeschlagenen
Probelauf am 15.09.2026; der erste Entwurf fand keinen einzigen
Ausschnitt wieder.

Pruefung. src/extract/validate_output.py prueft jede Ausgabe zweimal:
gegen das Schema und gegen die Quelle. Die Schemapruefung allein kann
ein erfundenes Zitat nicht erkennen. tests/test_schema_validation.py
enthaelt 34 Tests dazu.

Herkunft. Das Modell hat Schema, Pruefprogramm und Tests entworfen.
Der Verfasser hat sie gelesen, ausgefuehrt und freigegeben. Beim
ersten Testlauf fiel ein Test durch und deckte einen Fehler im Schema
auf: eine leere Begruendung bei no_requirements_found wurde
angenommen. Der Fehler ist behoben.

Status: festgelegt.
Bezug: FF1, FF2, Kapitel 4 Abschn. 4.1.4, Kapitel 5.

### 2026-09-15 E2 Form der Evaluation

Die Evaluation besteht aus einem Hauptteil und einem Nebenteil.

Hauptteil: Selbstbewertung durch den Verfasser an einer neuen
Stichprobe von rund zwanzig Pull Requests. Die Stichprobe wird mit
src/analyze/draw_sample.py gezogen, mit einem anderen Startwert und
unter Ausschluss der zwoelf Vorgaenge aus Paket C. Kriterien, Skala
und Entscheidungsregeln werden vor der ersten Bewertung schriftlich
festgelegt und danach nicht mehr geaendert.

Nebenteil: Vergleich mit der Formulierungsprobe aus Paket C. Verglichen
werden nicht Saetze, sondern Fundstellen. Fuer die zwoelf Vorgaenge
liegt je eine von Hand erstellte Kreuztabelle vor, die angibt, ob
Systemname und Systemreaktion belegt sind und wo. Geprueft wird, ob die
Pipeline dieselben Stellen findet.

Nicht verwendet wird Teil B der Formulierungsprobe. Die dortigen sechs
Saetze beruhen auf konstruierten Referenzinhalten aus 29148 und haben
keinen Bezug zu einem Pull Request.

Der Nebenteil bleibt Zusatzbefund. Die zwoelf Vorgaenge waren die
Grundlage der Formatentscheidung C5. Wer mit denselben Daten bewertet,
mit denen er das Verfahren gebaut hat, prueft nicht unabhaengig. Der
Hauptteil braucht daher eine ueberschneidungsfreie Stichprobe.

Bewertung durch das Qrisp-Team und den Betreuer findet nach der Abgabe
statt. Der Verfasser legt die Ergebnisse vor; der Betreuer entscheidet
ueber eine Weitergabe an das Qrisp-Team.

Abweichung vom Expose. Das Expose sieht die Bewertung durch Qrisp-Team
und Betreuer waehrend der Bearbeitungszeit vor, mit dem Meilenstein M5
in Woche 9. Diese Abweichung ist mit dem Betreuer abzustimmen. Stand
15.09.2026: Abstimmung steht aus.

Bedrohung der Validitaet. Der Verfasser bewertet eine Pipeline, die er
selbst entworfen hat. Das ist eine Bedrohung der internen Validitaet
und gehoert nach Kapitel 7. Gegenmassnahmen: vorab festgelegter
Bewertungsbogen, ueberschneidungsfreie Stichprobe, maschinell erhobene
Messwerte neben der Bewertung von Hand.

Status: festgelegt, Abstimmung mit dem Betreuer offen.
Bezug: FF1, FF2, Kapitel 6, Kapitel 7.

### 2026-09-15 E3 API-Budget

Fuer den Zugriff auf ein Modell ueber die Programmierschnittstelle
stehen hoechstens 150 Euro zur Verfuegung.

Folgen. Der Betrag begrenzt die Zahl der Laeufe, die Stichprobengroesse
und die Zahl der Wiederholungen fuer FF3. Vor dem ersten
kostenpflichtigen Lauf wird eine Kostenschaetzung erstellt und in
experiments/ festgehalten. Nach jedem Lauf werden die tatsaechlichen
Kosten nachgetragen.

Status: festgelegt.
Bezug: FF3, Kapitel 4 Modellwahl, Kapitel 5.

### 2026-09-15 E4 Auswahlregel fuer die Modelleingabe

Verarbeitet werden alle Pull Requests ausser zwei Gruppen.

Ausgeschlossen: Beitraege von Programmen (31) und Vorgaenge mit
outcome = open (50 nach Abzug der Bots). Es verbleiben 395 von 476.
Dieselbe Regel verwendet bereits src/analyze/draw_sample.py; der Lauf
vom 25.08.2026 nennt genau diese Zahlen. Grund fuer den Ausschluss
offener Vorgaenge: Ihr Inhalt kann sich noch aendern, eine daraus
rekonstruierte Anforderung waere nicht stabil.

Ausdruecklich nicht ausgeschlossen werden drei Gruppen, die zunaechst
dafuer in Betracht kamen:

Entwuerfe (43 der 395). Die Markierung als Entwurf sagt nichts ueber
den Inhalt; nahezu alle sind inzwischen abgeschlossen.

Vorgaenge ohne Beschreibung (56 der 395). Titel und Diff bleiben eine
Quelle. Nur 44 haben zusaetzlich keinen Kommentar, und nur 5 haben
weder Beschreibung noch Kommentar noch Diff-Text.

Vorgaenge ohne Codeaenderung (3 der 395).

Statt eines Ausschlusses vorab wird ein unbrauchbarer Vorgang
verarbeitet und im Datenmodell nach E1 mit processing_status =
input_unusable vermerkt. Damit ist die Quote ein Ergebnis und kein
blinder Fleck. Zaehlung am Datensatz vom 19.08.2026.

Dependabot gesondert. Die 28 Dependabot-Beitraege werden in Paket G
einmal getrennt auf sicherheitsbezogene Angaben gesichtet. Grund: Die
unter "Ungepruefte Beobachtungen" vermerkte Frage aus D7 ist fuer FF4
relevant. Das ist keine Aufnahme in den Hauptdurchlauf.

Umgesetzt in config/model_input.toml und
src/extract/build_prompt_input.py, geprueft durch sieben Tests in
tests/test_prompt_input.py.

Status: festgelegt.
Bezug: FF1, FF4 mittelbar, Kapitel 4 und 5.

### 2026-09-15 E5 Budget der Modelleingabe

Ausgangspunkt ist ein Befund vom 15.09.2026. Die Kuerzungsstufen nach
D1 gelten nur fuer den Diff einer Datei. Der Diff-Ausschnitt, den
GitHub an einen Review-Kommentar anhaengt (diff_hunk), ist davon nicht
erfasst. Gemessen ueber die 395 ausgewaehlten Vorgaenge umfasst er
6 937 611 Zeichen und damit mehr als der gesamte bereits gekuerzte
Diff mit 6 502 124 Zeichen. In Vorgang 403 entfallen 2 400 081 von
2 431 359 Zeichen allein darauf. Ohne diff_hunk ueberschreitet kein
Vorgang 50 000 Zeichen Text. Der Ausschnitt wiederholt ueberwiegend
Code, der bereits im Diff der Datei steht.

D1 wird nicht geaendert und der aufbereitete Datensatz nicht neu
erzeugt. Grund: Seine Pruefsumme ist in STATUS.md dokumentiert, die
Formulierungsprobe aus Paket C beruht auf genau dieser Datei, und
Paket D ist abgeschlossen. Die Aufbereitung haelt fest, was GitHub
geliefert hat. Das Budget der Modelleingabe ist ein eigener,
nachgelagerter Schritt.

Folge: Gekuerzt wird an zwei Stellen, in der Aufbereitung nach D1 und
beim Bau der Modelleingabe nach E5. Beide Stellen sind in Kapitel 5
getrennt darzustellen.

Regeln. Der Diff-Ausschnitt eines Review-Kommentars wird auf 500
Zeichen begrenzt. Ein Quellblock umfasst hoechstens 80 000 Zeichen.
Befuellt wird in der Reihenfolge Titel, Beschreibung, Kommentare,
Codeaenderungen; gekuerzt wird also zuerst der Code. Begruendung: Eine
Anforderung steht in der Regel in Worten, nicht in Quelltext; die
Belege aus Paket C stammen ueberwiegend aus Beschreibung und
Kommentaren. Jede Kuerzung hinterlaesst eine sichtbare Zeile im Block.

Wahl von 80 000. Bei 60 000 waeren 16 von 395 Vorgaengen betroffen,
bei 80 000 sechs, bei 120 000 drei. 80 000 Zeichen entsprechen grob
20 000 Token und passen bei aktuellen Modellen in einen Aufruf. Der
Wert ist nicht kostengetrieben; die Kostenschaetzung nach E3 folgt,
sobald das Modell feststeht.

Keine Anmeldenamen im Quellblock. Statt des Logins wird
author_association uebergeben. Der Name traegt zur Anforderung nichts
bei, die Rolle schon. Zugleich geht kein personenbezogenes Datum an
ein externes Modell. Ein Test sichert das ab.

Trennung von Anweisung und Quelldaten. Der Quellblock enthaelt
ausschliesslich Material aus dem Vorgang und keine Anweisung an das
Modell. Das ist die erste Massnahme gegen Prompt Injection nach
Kapitel 5.

Messung am Datensatz vom 19.08.2026: 395 Bloecke, Median 11 920
Zeichen, groesster Block 79 841 Zeichen, 79 Bloecke mit einer
Kuerzung, davon 60 nur beim Review-Kontext.

Herkunft. Das Modell hat Programm, Einstellungen und Tests entworfen.
Der Verfasser hat sie gelesen, ausgefuehrt und freigegeben. Beim
ersten Lauf ueberschritt ein Block das Budget um 141 Zeichen, weil die
Schlusszeile ueber das Weggelassene nicht eingerechnet war. Behoben
durch eine Ruecklage von 300 Zeichen, abgesichert durch zwei Tests.

Status: festgelegt.
Bezug: FF1, FF3 mittelbar, Kapitel 5.

### 2026-09-15 E6 Regeln der Belegstaerke

Die Belegstaerke wird nicht vom Modell gesetzt, sondern aus zwei
ueberpruefbaren Angaben berechnet. Neun Regeln legen das fest.

B1 Pflichtbestandteile. Sie richten sich nach dem EARS-Muster. Immer
verlangt sind Systemname und Systemreaktion. Zusaetzlich verlangt sind
die Vorbedingung bei state_driven und optional_feature, der Ausloeser
bei event_driven und unwanted_behaviour, beides bei complex. Die
Festlegung auf Systemname und Systemreaktion uebernimmt die Tabelle
der Pflichtbestandteile aus docs/formatprobe_protokoll.md.

B2 Die Deckung entscheidet zuerst. Fehlt ein Pflichtbestandteil in der
Quelle, lautet die Stufe insufficient. Die Aussageform wird dann nicht
mehr geprueft.

B3 Die Aussageform entscheidet zweitens. Fordert die Quelle etwas
(prescriptive), lautet die Stufe direct. Berichtet sie nur, was ist
oder getan wurde (descriptive), lautet sie indirect.

B4 Das Wort shall im erzeugten Satz belegt keine fordernde Quelle. Es
ist Formbestandteil des EARS-Musters. Das entspricht der Festlegung
aus Paket C, wonach shall nicht nachtraeglich als Beleg fuer eine
Verbindlichkeitsstufe der Quelle gewertet wird.

B5 Mehrere Belege duerfen sich ergaenzen, hoechstens drei je
Anforderung. Jeder Beleg nennt im Feld supports, welche Bestandteile
er traegt. Grund: Die Kreuztabellen aus Paket C zeigen, dass
Systemname und Systemreaktion haeufig an verschiedenen Stellen
belegt sind, etwa in Titel und Beschreibung bei PR 533.

B6 Jeder Beleg muss woertlich in der genannten Quelle stehen, bei
einem Diff nach Entfernen der Zeichen am Zeilenanfang. Die Regel
stammt aus E1 und gilt jetzt fuer jeden einzelnen Beleg.

B7 Die Belegstaerke wird aus B1 bis B3 berechnet. Weicht der vom
Modell gelieferte Wert vom berechneten ab, wird die Anforderung
abgelehnt. Damit ist die Einstufung extern definiert und
reproduzierbar und keine freie Modellausgabe.

B8 insufficient wird ausgegeben und nicht unterdrueckt. Die Quote ist
ein Messwert fuer FF1 und fuer die Unbelegtheitsrate in FF3.

B9 Eine Kuerzung des Quellblocks nach E5 senkt die Stufe nicht
automatisch. Sie wird vermerkt, weil der fehlende Teil einen Beleg
enthalten haben koennte. Gehoert nach Kapitel 7.

Aenderung am Datenmodell. E1 sah genau eine Quelle je Anforderung vor.
Das reicht nach B5 nicht aus. config/requirement_schema_v2.json
ersetzt die Felder source und source_excerpt durch eine Liste evidence
mit ein bis drei Eintraegen und fuehrt das Pflichtfeld source_form
ein. Fassung 1 bleibt im Repository und dokumentiert den Stand davor.

Grenze des Verfahrens. Etikettiert das Modell einen echten Ausschnitt
falsch, also behauptet es, ein Satz trage den Systemnamen, obwohl er
das nicht tut, faellt das maschinell nicht auf. Das ist ein Pruefpunkt
der Selbstbewertung nach E2 und gehoert nach Kapitel 7.

Pruefung. src/extract/validate_output.py prueft jede Ausgabe dreifach:
gegen das Schema, gegen die Regeln B1 bis B3 und gegen die Quelle.
tests/test_schema_validation.py enthaelt 54 Tests.

Herkunft. Das Modell hat Regeln, Schema und Tests entworfen. Der
Verfasser hat sie gelesen, ausgefuehrt und freigegeben. Bei der
Gegenprobe blieb ein absichtlich eingebauter Fehler zunaechst
unentdeckt: Die Konsistenzpruefung war richtig, wurde im Ablauf aber
nicht aufgerufen. Behoben durch die Funktion check_record und einen
zusaetzlichen Test.

Status: festgelegt.
Bezug: FF1, FF3 mittelbar, Kapitel 4 Abschn. 4.1.4, Kapitel 5 und 7.

### Nachtrag zu E2 (2026-09-15)

Die in E2 als offen vermerkte Abstimmung mit dem Betreuer liegt vor.
Der Betreuer hat der Abweichung vom Expose zugestimmt: Die Bewertung
durch das Qrisp-Team erfolgt nach der Abgabe, nicht waehrend der
Bearbeitungszeit. Der Meilenstein M5 des Exposes entfaellt in dieser
Form.
Der Satz "Stand 15.09.2026: Abstimmung steht aus" in E2 ist damit
ueberholt. Am uebrigen Inhalt von E2 aendert sich nichts: Der
Hauptteil bleibt die Selbstbewertung an einer ueberschneidungsfreien
Stichprobe, der Nebenteil der Fundstellenvergleich mit den zwoelf
Faellen aus Paket C. Die Bedrohung der internen Validitaet durch die
Selbstbewertung bleibt bestehen und gehoert unveraendert nach
Kapitel 7.

## 2026-09-17 Paket E: Prompt Version 1 und Nachtraege

### Nachtrag zu C5 (2026-09-17): Sprachregeln aus 29148 Abschn. 5.2.4

Der Ausschnitt der Ebene (d) nach C5 Abschnitt 4 wird um drei
sprachliche Vorgaben aus ISO/IEC/IEEE 29148:2018 Abschn. 5.2.4
ergaenzt: Aktiv statt Passiv, positive Formulierung statt "shall not"
und Verzicht auf "shall be able to".

Begruendung: Nach der Zuordnung vom 07.09.2026 gehoeren diese
Vorgaben zu Ebene (d). Der Ausschnitt in C5 Abschnitt 4 nannte sie
nicht, obwohl sie wie Abschn. 5.2.7 am einzelnen Satz pruefbar sind.
Alle drei lassen sich zudem an Wortformen erkennen und stuetzen damit
die automatische Validierbarkeit (K8). Die Norm fuehrt sie als Teil
eines gebraeuchlichen Vorgehens ("A common approach"), nicht als
Pflicht; die Arbeit uebernimmt sie als eigene Festlegung.

Abgrenzung: Eine Eigenschaft mit "shall be" und einem Adjektiv, etwa
"shall be immutable", gilt nicht als Passiv.

Umsetzung: prompts/extraction_system_v1.md, Abschnitt "Language rules
for every requirement sentence". Eine maschinelle Pruefung dieser
Regeln ist noch nicht umgesetzt.

Herkunft: Das Modell hat die Luecke gemeldet. Der Verfasser hat die
Aufnahme am 17.09.2026 freigegeben.

Status: festgelegt.
Bezug: FF2, Kapitel 4 Abschn. 4.1.

### Nachtrag zu E1 (2026-09-17): sechster Wert des Attributs Type

E1 gibt an, die Wertemenge des Attributs Type sei aus 29148
Abschn. 5.2.8.3 uebernommen. Der Abschnitt nennt jedoch sechs
Beispiele, nicht fuenf. Es fehlte "Human Factors Requirements". Der
Wert human_factors wird ergaenzt.

Praezisierung: Die Norm fuehrt die Werte ausdruecklich als Beispiele
("Important examples"). Die Schliessung der Menge ist eine Festlegung
dieser Arbeit und keine Vorgabe des Standards.

Einschraenkung fuer Kapitel 7: Die Norm grenzt Human Factors und
Usability/Quality-in-Use nicht trennscharf ab; beide nennen etwa die
Zufriedenheit. Der Prompt gibt deshalb eine Vorrangregel: Passen
beide, wird usability_quality_in_use gewaehlt und der Zweifel unter
uncertainties vermerkt.

Umsetzung: config/requirement_schema_v2.json, Wertemenge und
Beschreibung des Feldes type. Die Schemaversion bleibt 2. Grund: Zum
Zeitpunkt der Aenderung hatte noch kein Lauf das Schema verwendet. Die
Grenze zwischen beiden Fassungen ist der Commit dieser Aenderung.

Status: festgelegt.
Bezug: FF1, FF4 mittelbar, Kapitel 4 Abschn. 4.1.4.

### Nachtrag zu E6 (2026-09-17): Muster complex

B1 verlangt beim Muster complex Vorbedingung und Ausloeser. Damit
muss ein Satz dieses Musters mindestens ein Schluesselwort fuer eine
Vorbedingung (While, During, Where) und mindestens eines fuer einen
Ausloeser (When, If ... then) enthalten. Eine Kombination nur aus While
und Where waere sonst stets insufficient, obwohl die Quelle alles
belegt.

Eine feste Reihenfolge der Schluesselwoerter wird nicht vorgegeben.
Keine der vorliegenden Quellen legt sie fest.

Umsetzung: prompts/extraction_system_v1.md, Tabelle der Muster.
validate_output.py prueft die Schluesselwoerter im Satz noch nicht;
es prueft nur die Deckung. Moegliche Ergaenzung, noch offen.

Status: festgelegt.
Bezug: FF1, FF2.

### 2026-09-17 E7 Prompt Version 1

Die Anweisung an das Modell liegt in zwei Dateien vor:
prompts/extraction_system_v1.md (fester Teil, gleich fuer jeden Pull
Request) und prompts/extraction_user_v1.md (Vorlage mit den
Platzhaltern pull_number und source_block).
src/extract/prompt_files.py laedt beide, setzt den Quellblock ein und
bildet die Pruefsummen fuer das Lauf-Manifest.

Sprache: Englisch. Die Anforderungen sind englisch (C1), die
Programme geben Englisch aus.

Modellneutral: Version 1 verlangt reines JSON und nutzt keine
anbieterspezifische Schemapruefung. Das Modell steht erst nach A7
fest. Bei Bedarf folgt eine Version 1.1.

Keine vollstaendigen Beispiele: Die zwoelf Faelle aus Paket C sind
der Nebenteil der Evaluation nach E2 und scheiden aus. Der Prompt
enthaelt nur einzelne Formbeispiele, etwa zur Kennung. So bleibt die
Wirkung der Regeln messbar.

Aufbau: Aufgabe; Umgang mit dem Quellblock; Aufbau des Quellblocks;
Vorgehen in sieben Schritten; Zielformat EARS+29148; Sprachregeln;
Feldregeln; Belegregeln B1 bis B8; Verarbeitungsstand; Ausgabe. Das
Vorgehen folgt dem zweistufigen Verfahren aus Big EARS: Eine Aussage
wird zuerst als Anforderung, Information oder nicht anwendbar
eingestuft und erst danach formuliert. B7 steht nur als
Rechenvorschrift im Prompt; die Kontrolle liegt bei
validate_output.py. B9 erscheint als Hinweis unter
missing_information.

Trennung von Anweisung und Material: Der Quellblock steht zwischen
festen Begrenzungszeilen. Der Prompt erklaert ihn zu Material, dessen
Anweisungen nicht befolgt werden. Ein Block, der eine Begrenzungszeile
enthaelt, wird abgelehnt; ebenso ein Block, dessen Kopfnummer nicht
zur Nummer des Vorgangs passt. Alle 395 Bloecke vom 15.09.2026 haben
beide Pruefungen bestanden (Lauf in der Umgebung des Modells).

Was als Anforderung zaehlt: eine Faehigkeit, ein Verhalten, eine
Eigenschaft, eine Einschraenkung oder eine Qualitaet von Qrisp oder
einem Teil davon, die der Pull Request hinzufuegt, aendert, repariert,
fordert oder dokumentiert. Nicht dazu zaehlt reine Aufraeumarbeit ohne
Wirkung auf Verhalten oder Eigenschaften, etwa Tippfehler,
Umformatierung oder das Zusammenfuehren von Zweigen. Solche Vorgaenge
erhalten no_requirements_found mit Begruendung.
Begruendung: Trivialanforderungen wuerden die Zahl der rekonstruierten
Anforderungen aufblaehen, ohne etwas ueber die Anforderungen an Qrisp
zu sagen, und die Bewertung nach E2 verwaessern. Der Ausschluss bleibt
sichtbar, weil jeder solche Vorgang mit Begruendung gezaehlt wird;
wie bei E4 entsteht kein blinder Fleck. Die Abgrenzung ist eine
Festlegung dieser Arbeit. Grenzfaelle werden bei der Selbstbewertung
nach E2 geprueft.
Herkunft: Festlegung des Verfassers. Vorschlag des Modells vom
17.09.2026, vom Verfasser geprueft und uebernommen.

input_unusable: wenn der Block ausser Titel und Dateinamen nichts
enthaelt, also keine Beschreibung, keinen Kommentar und keinen
Diff-Text.

security_relevant, vorlaeufige Definition: wahr, wenn die Anforderung
den Schutz von Daten oder der Software vor Missbrauch, Manipulation,
unbefugtem Zugriff, Verlust oder Ausfall betrifft, den Umgang mit nicht
vertrauenswuerdigen Eingaben oder bekannte Schwachstellen, auch von
Abhaengigkeiten. Die Definition ist eine Festlegung dieser Arbeit und
wird in Paket G gegen das Sicherheitsraster geprueft.

html_url: Das Modell gibt stets null aus, weil der Quellblock keine
Links auf Kommentare enthaelt. Die Links werden nach dem Lauf aus dem
Datensatz nachgetragen (A8).

Namen: Ausserhalb des Feldes excerpt schreibt das Modell keinen Namen
und keinen Anmeldenamen. Im Ausschnitt ist das nicht zu verhindern,
weil er woertlich sein muss (B6). Offen vor A8: Die Beschreibungen und
Kommentare im Quellblock enthalten Erwaehnungen von Anmeldenamen. Die
Aussage in E5, es gehe kein personenbezogenes Datum an ein externes
Modell, gilt nur fuer die Kopfzeilen. Eine grobe Zaehlung des Modells
fand in rund 109 von 395 Bloecken Zeichenfolgen, die wie Erwaehnungen
aussehen; das Suchmuster erfasst auch Python-Dekoratoren, die Zahl ist
ungeprueft und nicht zitierfaehig.

Ausgang des Pull Requests: Der Quellblock enthaelt nicht, ob ein
Vorgang uebernommen oder verworfen wurde. Version 1 bleibt dabei. Der
Wert steht im Datensatz und wird bei der Auswertung ergaenzt. Gehoert
nach Kapitel 7.

Pruefung: tests/test_prompt_files.py mit 14 Tests. Sie pruefen vor
allem die Uebereinstimmung von Prompt und Schema. Gegenprobe in der
Umgebung des Modells: acht von neun eingebauten Fehlern wurden
erkannt; der neunte (safe_substitute statt substitute) aendert bei
korrekter Vorlage kein Verhalten.

Nicht geprueft: ob ein Modell den Prompt befolgt. Das zeigt erst A8.

Herkunft der Artefakte: Das Modell hat Prompt, Ladeprogramm und Tests
entworfen. Der Verfasser hat die Dateien uebernommen und die Tests auf
seinem Rechner ausgefuehrt (127 bestanden am 17.09.2026, vor den
Nachtraegen zu C5, E1 und E6).

Status: festgelegt.
Bezug: FF1, FF2, Kapitel 4, Kapitel 5, Kapitel 7.

## 2026-09-19 Paket E: Modellwahl und Ersetzung von Erwaehnungen

### 2026-09-19 E8 API-Modell, Aufrufweg und Kostenrahmen

Gewaehlt: gpt-5.6-terra von OpenAI als das API-basierte Modell fuer FF3.
Der Pilotlauf A8 laeuft im Normalbetrieb, der Volllauf ueber 395 Vorgaenge
im Stapelbetrieb ("Batch"), der Eingabe und Ausgabe halb so teuer macht und
die Antwort verzoegert. Die Verzoegerung stoert nicht, weil niemand auf das
Ergebnis wartet.

Preise, recherchiert am 19.09.2026, in US-Dollar je 1 Mio Token,
Eingabe/Ausgabe: gpt-5.6-sol 4/20, gpt-5.6-terra 2/12, gpt-5.6-luna
0,20/1,20; zum Vergleich claude-sonnet-5 2/10 und claude-haiku-4.5 1/5.
Kontextfenster von gpt-5.6: 1,05 Mio Token. Der laengste Quellblock hat
79 841 Zeichen, also rund 23 000 Token. Kein Vorgang scheitert an der
Groesse.

Begruendung:
1. Terra liegt preislich gleichauf mit claude-sonnet-5. Die Bevorzugung von
   OpenAI kostet nichts und ist damit keine Verzerrung zulasten der Kosten.
2. Sol kostet das Zweieinhalbfache. Dass es Anforderungen besser
   rekonstruiert, ist unbelegt und wird in dieser Arbeit nicht behauptet.
3. Luna ist zehnmal guenstiger. Da das Budget nach der Schaetzung nicht der
   Engpass ist, entscheidet die Ergebnisqualitaet, nicht der Preis.
4. Doppelrolle: Claude wird als Arbeitswerkzeug eingesetzt. Ein Modell
   derselben Familie als Messobjekt waere nach der Projektanweisung
   zulaessig, muesste aber in Kapitel 7 als Bedrohung der
   Konstruktvaliditaet behandelt werden. Mit OpenAI entfaellt das.

Vorbehalt zur Preisangabe: Der Sol-Preis von 4/20 ist ein Aktionspreis, den
OpenAI als mindestens bis zum 21.11.2026 gueltig angibt, ohne Enddatum und
ohne Nachfolgepreis. Mehrere Uebersichten fuehren weiterhin 5/30; diese
Angabe ist veraltet und stand auch im ersten Entwurf dieser Entscheidung.
Berichtigt am 19.09.2026 nach einem Hinweis des Verfassers und einer
zweiten Recherche. Folgenlos fuer die Wahl, weil Sol nicht genommen wird.
Jede Preisangabe in der Arbeit braucht ein Abrufdatum.

Kostenschaetzung nach E3: experiments/kostenschaetzung.md, Stand
19.09.2026. Ein Volllauf mit terra kostet im Stapelbetrieb
geschaetzt 9 bis 14 US-Dollar ohne Steuer. Die gesamte Planung bis zum Abschluss von Paket E und F
liegt bei 31 bis 37 US-Dollar mit einem Aufschlag von 19 Prozent. Das
Budget von 150 Euro wird damit zu rund einem Viertel ausgeschoepft.
Wechselkurs und Steuersatz sind nicht recherchiert; die Rechnung setzt
1 Euro gleich 1 US-Dollar und rechnet 19 Prozent auf, beides zugunsten des
Budgets.

Noch nicht entschieden, weil erst nach dem Pilotlauf beurteilbar: die
Einstellung des Denkaufwands ("reasoning effort") und die Frage, ob eine
anbieterseitige Schemapruefung genutzt wird. Version 1 des Prompts bleibt
nach E7 modellneutral.

Zu dokumentieren ist je Lauf: Modellname mit Version, Datum, Parameter,
Prompt-Version mit Pruefsumme, Eingabedatei mit Pruefsumme, Aufrufweg
(normal oder Stapel), verbrauchte Token und Kosten.

Herkunft: Festlegung des Verfassers. Recherche und Rechnung vom Modell am
19.09.2026, vom Verfasser geprueft.

Status: festgelegt.
Bezug: FF3, Kapitel 4 Abschn. 4.6, Kapitel 5, Kapitel 7.

### 2026-09-19 E9 Erwaehnungen von Anmeldenamen werden ersetzt

Erwaehnungen von GitHub-Anmeldenamen im Fliesstext werden durch feste
Platzhalter ersetzt, bevor ein Quellblock an ein externes Modell geht. Aus
einem Anmeldenamen wird @person_01, @person_02 und so weiter. Derselbe
Anmeldename erhaelt immer denselben Platzhalter.

Anlass: E5 hielt fest, es gehe kein personenbezogenes Datum an ein externes
Modell. Das galt nur fuer die Kopfzeilen der Kommentare, in denen statt des
Anmeldenamens nur die Zuordnung (CONTRIBUTOR, COLLABORATOR, NONE) steht. In
den Texten selbst standen weiterhin Erwaehnungen. E7 hielt diesen Punkt als
offen fest; E9 schliesst ihn.

Begruendung: Der Anmeldename traegt zu keiner rekonstruierten Anforderung
bei. Das Feld beneficiary verlangt eine Rolle, keine Person. Die
Datenminimierung nach Art. 5 DSGVO spricht dafuer, ihn wegzulassen. Die
Daten sind zwar oeffentlich einsehbar, was die Weiterverarbeitung aber
nicht ohne Weiteres rechtfertigt. Nach der Dokumentation von OpenAI werden
Daten aus der Programmierschnittstelle nicht fuer das Training verwendet;
Protokolle zur Missbrauchserkennung werden jedoch bis zu 30 Tage
aufbewahrt und koennen Anfragen und Antworten enthalten.

Umfang, gemessen am Datensatz vom 19.09.2026:
- 34 Anmeldenamen ersetzt.
- Vor der Ersetzung: 98 von 395 Bloecken mit mindestens einer Erwaehnung im
  Fliesstext, 279 Treffer. Diese Zahlen hat der Verfasser nachgezaehlt.
- Nach der Ersetzung: keine unersetzte Erwaehnung im Fliesstext. Die 30
  verbleibenden Zeichenfolgen mit Klammeraffen stehen in Diffs oder in
  Codeschrift und bezeichnen Programmteile, etwa property, staticmethod,
  qjit, passX.

Regeln der Ersetzung:
1. Ersetzt wird nur in Prosa: Titel, Beschreibung, Kommentartext,
   Review-Kommentartext.
2. Nicht ersetzt wird im Diff und im Codeausschnitt eines
   Review-Kommentars. Diese Texte gehen unveraendert an das Modell.
3. In Codebloecken, eingerueckten Zeilen und Codeschrift wird nur ersetzt,
   was bereits aus der Prosa als Anmeldename bekannt ist. Ein Dekorator wie
   @property geraet nie in die Zuordnung und bleibt stehen.
4. Eine eingerueckte Zeile gilt nur dann als Code, wenn sie nicht mit einem
   Listenzeichen beginnt. Verschachtelte Aufzaehlungen in Markdown sind
   Prosa.
5. Eine Ausnahmeliste in config/model_input.toml haelt Fachbegriffe frei,
   die in Prosa wie eine Erwaehnung aussehen: jaspify, jax, pytest, rus.
   Kriterium fuer die Aufnahme: Die Zeichenfolge kommt auch im Programmcode
   vor. RUS steht fuer Repeat-Until-Success.
6. Die Nummerierung folgt der alphabetischen Reihenfolge der
   Anmeldenamen, damit ein zweiter Lauf dieselben Platzhalter vergibt.

Zwei Fehler der ersten Fassung, beide durch Tests und Nachzaehlung des
Verfassers gefunden und behoben:
- Ein Anmeldename in einer verschachtelten Aufzaehlung blieb stehen, weil
  die Einrueckung als Code gewertet wurde. Regel 4 behebt das.
- Der Fachbegriff RUS wurde als Person behandelt. Regel 5 behebt das.

Ablage: Die Zuordnung von Anmeldename zu Platzhalter liegt in
data/interim/mention_map.json und damit ausserhalb des Repositorys, weil
sie die Ersetzung rueckgaengig macht. Sie ist durch .gitignore Zeile 9
ausgeschlossen. Das Manifest der Modelleingabe enthaelt nur die Anzahl der
ersetzten Anmeldenamen, keinen Namen.

Umsetzung: src/extract/pseudonymise.py, Aenderungen in
build_prompt_input.py und validate_output.py, Abschnitt
[pseudonymisation] in config/model_input.toml,
tests/test_pseudonymise.py mit 28 Tests. Die Belegpruefung nach B6
vergleicht gegen denselben ersetzten Text; dafuer nimmt
validate_output.py den Schalter --mentions-map. Ohne diesen Schalter wird
ein Zitat aus ersetztem Text abgelehnt.

Gueltige Eingabedatei ab sofort: data/processed/model_input_2026-09-19.jsonl
mit Manifest im selben Ordner. Sie ersetzt model_input_2026-09-15.jsonl aus
E7. Die aeltere Datei bleibt liegen, wird aber nicht mehr verwendet.

Grenzen, fuer Kapitel 7:
- Erfasst werden nur Erwaehnungen mit Klammeraffen. Ein Klarname im Fliess-
  text, etwa in einer Anrede, bleibt stehen.
- Diffs werden nicht bearbeitet. Steht ein Name in einer geaenderten Datei,
  etwa in einer Danksagung, geht er mit.
- Die Ersetzung ist eine Pseudonymisierung, keine Anonymisierung. Mit der
  Zuordnungstabelle laesst sie sich umkehren.
- Ab dem ersten kostenpflichtigen Lauf darf die Zuordnung nicht mehr neu
  vergeben werden, sonst bezeichnet derselbe Platzhalter verschiedene
  Personen.

Herkunft: Festlegung des Verfassers. Entwurf von Regeln, Programm und
Tests durch das Modell am 19.09.2026; der Verfasser hat die Zahlen
nachgezaehlt und die Ergebnisse geprueft.

Status: festgelegt.
Bezug: FF3, FF1 mittelbar, Kapitel 5, Kapitel 7.


## 2026-09-21 Paket E: Rahmen des Pilotlaufs A8

### 2026-09-21 E10 Rahmen des Pilotlaufs

Der Pilotlauf A8 schickt 20 Quellbloecke an gpt-5.6-terra, bevor alle
395 gesendet werden. Er prueft das Aufrufprogramm und die Befolgung des
Prompts und ersetzt die Annahmen der Kostenschaetzung durch Messwerte.
Er ist keine Bewertung der Ergebnisqualitaet; diese erfolgt nach E2 an
einer eigenen Stichprobe. Die folgenden Festlegungen gelten vor dem
ersten kostenpflichtigen Aufruf.

a) Stichprobe. src/analyze/draw_sample.py erhaelt zwei Schalter:
--sizes legt die Zahl je Schicht fest, --exclude nennt Nummern, die
nicht gezogen werden duerfen. Ohne beide Schalter verhaelt sich das
Skript wie bisher. Nachweis: Der Aufruf mit Startwert 20260823 muss
wieder die zwoelf Nummern vom 25.08.2026 ergeben.
Groessen fuer den Pilot, zusammen 20:
S6 1 · S5 4 · S4 3 · S3 3 · S2 4 · S1 5.
S5 (grosser, gekuerzter Diff) ist staerker besetzt, weil lange Bloecke
das Aufrufprogramm am staerksten fordern. S6 bleibt bei 1, weil es nur
fuenf Vorgaenge ohne Codeaenderung gibt und einer davon (408) bereits
in der Formulierungsprobe liegt.
Startwert: 20260921. Ausgeschlossen: 48, 75, 191, 371, 408, 413, 464,
533, 577, 622, 692, 711 (Formulierungsprobe, Paket C).
Die Stichprobe fuer die Evaluation nach E2 schliesst spaeter diese
zwoelf und die 20 Pilotvorgaenge aus. Begruendung: Am Pilot wird der
Prompt weiterentwickelt. Wer an denselben Vorgaengen bewertet, prueft
das Verfahren an den Daten, an denen es angepasst wurde.
Tests: nur fuer die beiden neuen Schalter, weil ein wirkungsloser
Ausschluss still falsche Daten erzeugt (Kriterium aus D4). Praezisiert
D4a; fuer das uebrige Skript bleibt D4a bestehen.

b) Aufrufweg. Das Aufrufprogramm nutzt das vorhandene Paket requests,
keine zusaetzliche Programmbibliothek. Der Schluessel steht als
OPENAI_API_KEY in .env und wird mit load_token aus github_api.py
gelesen. Die Wiederholungslogik wird neu geschrieben, weil
request_with_retry nur Abrufe kennt und HTTP 403 als Ratenbegrenzung
deutet; bei OpenAI bedeutet 403 fehlende Berechtigung.

c) Ablage. Die Ergebnisse liegen flach in data/processed/:
extraction_<Datum>_pilot.jsonl (Modellantworten),
extraction_<Datum>_pilot.raw.jsonl (vollstaendige Antworten der
Schnittstelle) und extraction_<Datum>_pilot.manifest.json. Nach
.gitignore bleiben die ersten beiden lokal, das Manifest wird
versioniert. Ein Unterordner scheidet aus: Git nimmt keine Datei aus
einem ausgeschlossenen Ordner wieder auf.

d) Denkaufwand. Der Pilot laeuft mit der Voreinstellung des Anbieters.
Entscheidungsregel fuer die endgueltige Einstellung (E11), festgelegt
vor dem Lauf: Die Voreinstellung bleibt, wenn hoechstens eine der 20
Antworten abgeschnitten oder kein gueltiges JSON ist und die Kosten des
Pilots 2,10 US-Dollar nicht uebersteigen. Sonst wird genau eine andere
Stufe an denselben 20 Vorgaengen erprobt. Entschieden wird nur nach
maschinell messbaren Werten. Ein Qualitaetsurteil an 20 Faellen ohne
festgelegten Bewertungsbogen waere nicht belastbar.
Die Schwellen sind eine Festlegung dieser Arbeit, keine Quellenangabe.
2,10 US-Dollar entsprechen 20 Bloecken nahe der Hoechstgroesse von
80 000 Zeichen und je 4 000 Ausgabe-Token, zu den Preisen
vom 19.09.2026 (rechnerisch 2,06 US-Dollar).

e) Keine anbieterseitige Schemapruefung im Pilot. Gemessen wird, wie
oft das Modell das Format ohne Hilfe einhaelt; das ist ein Messwert
fuer die Formatkonformitaet (FF2). Ob die Pruefung des Anbieters die
Bedingungen des Schemas v2 abbilden kann, ist ungeprueft. Fuer FF3 muesste
das lokale Modell eine vergleichbare Hilfe erhalten, sonst ist der
Vergleich verzerrt.

Herkunft: Festlegung des Verfassers am 21.09.2026. Vorschlaege des
Modells, vom Verfasser uebernommen.

Status: festgelegt.
Bezug: FF1, FF2, FF3, Kapitel 4, Kapitel 5, Kapitel 6, Kapitel 7.

### Nachtrag zu E2 (2026-09-21): Kriterienliste vor dem Pilot

Vor dem ersten kostenpflichtigen Aufruf werden die Namen der
Bewertungskriterien mit je einer Satzdefinition in
eval/instrument/kriterien_v0.md festgehalten. Skala und
Entscheidungsregeln folgen wie in E2 vorgesehen vor der ersten
Bewertung.
Begruendung: Im Pilot sieht der Verfasser erstmals Modellausgaben. Wer
danach die Kriterien festlegt, kann sie unbewusst an die Ausgaben
anpassen. Die Liste schuetzt den Gegenstand der Bewertung; dass Skala
und Regeln nach dem Pilot entstehen, gehoert nach Kapitel 7.
Abweichung: STATUS.md verlangte den Bogen, bevor die erste Anforderung
gelesen wird. Massgeblich ist der Wortlaut von E2.

### Nachtrag zu E9 (2026-09-21): Freigabe und Platzhalter in der Arbeit

Freigabe: Der Betreuer hat die Uebertragung der pseudonymisierten
Quellbloecke an die Schnittstelle von OpenAI als fuer die Arbeit
unbedenklich bestaetigt. Mitgeteilt vom Verfasser am 21.09.2026; eine
schriftliche Fassung liegt nicht vor. Damit ist der offene Punkt
"Datenschutzrechtliche Bewertung der Pseudonymisierung" erledigt.
Die Grenzen aus E9 fuer Kapitel 7 bleiben bestehen.

Platzhalter in der Arbeit: Nennt die Arbeit eine Person, verwendet sie
die Platzhalter aus E9 (person_NN). Die Kennungen A01 ff. aus dem
Eintrag vom 12.08.2026 werden nicht eingefuehrt; docs/pseudonyme.csv
entfaellt. So bezeichnet ein Zitat aus einer Modellausgabe dieselbe
Person wie der Text der Arbeit. Fuer eine Person, die nicht in der
Zuordnung steht, ist eine Regel festzulegen, sobald der Fall eintritt.

### Nachtrag zu E10 (2026-09-22): Recherche, Aufrufparameter, Berichtigung

Recherche am 21.09.2026 in der Dokumentation von OpenAI. Befunde und
Folgen fuer config/api_run.toml:

- Modell: Denkaufwand in sechs Stufen (none bis max), Voreinstellung
  medium. Kontextfenster 1 050 000 Token, hoechstens 128 000
  Ausgabe-Token. Preise 2,00 / 12,00 US-Dollar je Mio Token, wie in der
  Kostenschaetzung. Die kostenlose Stufe ist nicht zugelassen.
  Folge: reasoning_effort = "medium" wird ausdruecklich gesendet.
  Quelle: https://developers.openai.com/api/docs/models/gpt-5.6-terra
- Kein Snapshot: Die Modellseite fuehrt nur den Alias gpt-5.6-terra.
  Folge: Das Manifest speichert je Antwort den zurueckgemeldeten
  Modellnamen. Fuer Kapitel 7 eine Bedrohung der Reproduzierbarkeit.
- Speicherung: Kein Training ohne Zustimmung; Missbrauchsprotokolle bis
  30 Tage. Zusaetzlich speichert die Responses-Schnittstelle Antworten
  standardmaessig mindestens 30 Tage, ausser mit store = false. Ohne
  Zero Data Retention gilt ein erweiterter Zwischenspeicher fuer
  wiederholte Anfangsteile, hoechstens 24 Stunden.
  Folge: store = false, geprueft beim Laden der Konfiguration.
  Quelle: https://developers.openai.com/api/docs/guides/your-data
- Abgeschnittene Antworten: Denk-Token zaehlen zur Ausgabe. Beim
  Erreichen der Obergrenze kommt der Status incomplete, auch ohne
  sichtbaren Text, aber mit Kosten. Empfohlen: mindestens 25 000 Token.
  Folge: max_output_tokens = 25000; incomplete wird im Manifest gezaehlt
  und fuer die Regel aus E10 d verwendet.
  Quelle: https://developers.openai.com/api/docs/guides/reasoning
- Ausgabenlimit: Beim Erreichen antwortet die Schnittstelle mit HTTP 429
  und einem eigenen Code; die Sperre greift verzoegert.
  Folge: Nur 429 mit rate_limit_exceeded wird wiederholt, jede andere 429
  haelt den Lauf sofort an.
  Quelle: https://developers.openai.com/api/docs/guides/spend-limits
- Lizenz von Qrisp: Eclipse Public License 2.0, zweitrangig GPL 2.0 mit
  Classpath-Ausnahme, laut Projektseite der Eclipse Foundation,
  abgerufen am 23.09.2026. Die Auswertung ist keine Weitergabe des
  Codes; kein Lizenzhindernis erkennbar (Einschaetzung, keine
  Rechtsauskunft).
  Quelle: https://projects.eclipse.org/projects/technology.qrisp
- Ungeprueft: Einstellbarkeit der Temperatur, Mindestbetrag fuer das
  Guthaben, Zaehlung des Zuschlags fuer das Schreiben in den
  Zwischenspeicher. Temperatur und Modus werden nicht gesendet; die
  Kosten im Manifest sind eine Obergrenze, verbindlich ist die
  Abrechnung.

Konto, eingerichtet am 21.09.2026: Projekt qrisp-re-thesis, Guthaben
10 US-Dollar, hartes Monatslimit 10 US-Dollar, Hinweise bei 5 und 10
US-Dollar, Datenfreigabe an OpenAI ueberall deaktiviert.

Berichtigung zu a): Von den fuenf Vorgaengen ohne Codeaenderung sind nur
drei auswaehlbar; die uebrigen stammen von Bots oder sind offen. Nach
Ausschluss von 408 blieben zwei, der Pilot zog einen (169). Fuer die
Evaluation bleibt einer. Die Begruendung von a) gilt unveraendert.

Ergebnis der Ziehung: docs/sample_pilot_a8.md, Commit c2a98e0. Die
Wiederholung mit Startwert 20260823 ergab die zwoelf Nummern vom
25.08.2026; eine zweite Ziehung mit 20260921 ergab dieselben 20.

### Nachtrag zu E2 (2026-09-22): vorgesehene Art der Bewertung

Der Verfasser waehlt fuer die Bewertung von Hand den folgenden Weg,
statt sie einem Sprachmodell zu uebertragen: Maschinell pruefbare
Kriterien (B8 Schema, B9, B10, Teile von B3) werden maschinell geprueft;
die uebrigen bewertet der Verfasser an einer vorab festgelegten
Zufallsauswahl von Anforderungen mit einem Bewertungswerkzeug und einer
dreistufigen Skala. Begruendung: Eine Bewertung von Modellausgaben
allein durch ein Modell haette keinen unabhaengigen Massstab. Umfang
der Auswahl, Skala und Regeln legt Fassung v1 der Kriterienliste fest.

## 2026-09-23 Paket E: Begruendung des Bot-Ausschlusses

### Nachtrag zu E4 (2026-09-23): Begruendung fuer den Ausschluss der Bot-Beitraege

E4 schloss die 31 Bot-Beitraege aus, ohne einen Grund zu nennen; D7
verlangt ihn fuer Paket E. Er wird hier nachgetragen. Die Auswahl
selbst aendert sich nicht.

Befund vom 23.09.2026, gezaehlt am Datensatz vom 19.08.2026: 28 der 31
Bot-Beitraege sind abgeschlossen. 25 stammen von Dependabot, davon 19
ohne Uebernahme geschlossen und 6 uebernommen. Alle 28
Dependabot-Titel lauten "Bump ... from ... to ..." oder "Update ...
requirement from ... to ...". 3 stammen von Copilot, alle ohne
Uebernahme geschlossen, zwei davon ohne Codeaenderung (332, 578).

Begruendung:
1. Dependabot-Beitraege heben die Version einer fremden
   Programmbibliothek an. Sie beschreiben keine Faehigkeit und keine
   Eigenschaft von Qrisp und liefern damit keinen Stoff fuer FF1. Ihr
   moeglicher Wert fuer FF4 wird in Paket G gesondert gesichtet (E4,
   D7).
2. Copilot-Beitraege sind maschinell verfasst. Ob ihr Text eine
   Absicht des Qrisp-Teams wiedergibt, ist nicht feststellbar. Keiner
   wurde uebernommen.
3. Zusaetzlich: Eine Aufnahme haette die Zuordnung der Platzhalter
   nach E9 beruehrt. In den abgeschlossenen Bot-Beitraegen stehen 7
   Zeichenfolgen mit Klammeraffen, die nicht in der Zuordnung stehen.
   Seit dem Pilotlauf darf die Zuordnung nicht mehr neu vergeben
   werden.

Einschraenkung fuer Kapitel 7: Die Einstufung beruht auf Titel,
Konto und Ausgang, nicht auf einer Durchsicht der Beschreibungen. Bei
den drei Copilot-Beitraegen ist der Ausschluss am wenigsten zwingend,
weil sie Entwicklungsversuche an Qrisp selbst waren.

Herkunft: Festlegung des Verfassers; Zaehlung durch den Verfasser,
Entwurf durch das Modell.

Status: festgelegt.
Bezug: FF1, FF4, Kapitel 5 und 7.

## 2026-09-24 Paket E: Ursache der Ablehnungen im Pilot

### Nachtrag zu E10 (2026-09-24): Regel fuer die Ursache der Ablehnungen

Anlass: validate_output.py lehnte im Lauf 2026-09-22_pilot 5 von 20
Datensaetzen ab, mit zusammen 6 Fundstellen (PR 71, 86, 166, 299 zweimal,
316). Alle scheiterten an der Zitatpruefung, alle bei Zitaten aus einem
Diff. Die folgende Regel ist festgelegt, bevor ein Diagnoseskript die
Ursachen bestimmt. So kann die Regel nicht nach dem Ergebnis gewaehlt
werden.

Massstab ist der Prompt Version 1, prompts/extraction_system_v1.md,
Abschnitt zum Feld excerpt mit den Regeln fuer ein Zitat aus einem Diff.
Diese Regeln verbieten unter anderem entfernte Zeilen, @@-Zeilen,
Auslassungen mit Punkten und das Stehenlassen des ersten Zeichens einer
Diffzeile.

1. Haelt ein Zitat alle Zitatregeln des Prompts ein und wird trotzdem
   abgelehnt, liegt ein Fehler des Pruefprogramms vor.
   validate_output.py wird korrigiert und getestet, der Lauf wird neu
   geprueft. Die Schnittstelle wird dafuer nicht erneut aufgerufen.
2. Verstoesst ein Zitat gegen eine Regel des Prompts, ist das ein Befund
   ueber das Modell. Die Ablehnung bleibt und wird in Kapitel 6 gezaehlt.
3. Passt keine vorab definierte Ursache, sieht der Verfasser die Stelle
   lokal ein und ordnet sie nach Punkt 1 oder 2 zu. Der Inhalt der Stelle
   geht nicht in den Chat.
4. Haben Befunde nach Punkt 2 in mindestens zwei verschiedenen Pull
   Requests dieselbe Ursache, entsteht Prompt Version 2. Sie wird an
   denselben 20 Vorgaengen unter neuer Kennung erprobt; die Ergebnisse
   von Version 1 bleiben erhalten. Fuer Version 2 gilt die Regel aus
   E10 d erneut. Sonst bleibt Version 1 fuer den Volllauf.
   Begruendung: Ein einzelner Fehler zeigt keine Schwaeche der Anweisung.
   Derselbe Fehler in mehreren Vorgaengen kann an einer unklaren
   Formulierung liegen und laesst sich dann gezielt beheben. Zulaessig
   nach E10 a, weil am Pilot der Prompt weiterentwickelt wird und die
   Evaluation nach E2 eine eigene Stichprobe nutzt.
5. Zusaetzlich zaehlt das Diagnoseskript bei den angenommenen Zitaten,
   ohne deren Inhalt auszugeben, wo validate_output.py nachsichtiger ist
   als der Prompt: Zitate ueber eine entfernte Zeile oder eine @@-Zeile
   hinweg, Zitate aus dem Code-Ausschnitt eines Review-Kommentars und
   Zitate aus einer Datei, die nicht im Quellblock stand. Ob das
   Pruefprogramm verschaerft wird, wird nach dieser Zaehlung entschieden.

Herkunft: Vorschlag des Modells im Chat vom 24.09.2026, vom Verfasser
festgelegt.

Status: festgelegt.
Bezug: FF1, FF2, Kapitel 5, 6 und 7.

### Nachtrag zu E10 (2026-09-24): Ergebnis der Ursachensuche, Prompt Version 2 und Regel fuer ihre Uebernahme

Ergebnis. Grundlage ist das Suchprogramm src/extract/diagnose_excerpts.py,
Stand Commit 1cb8849, angewandt auf den Lauf 2026-09-22_pilot mit dem
verschaerften Pruefprogramm (Commit ec360b3). 8 Zitate sind abgelehnt.

- Regel 1: keines. Das Pruefprogramm hat die urspruenglich 6
  Ablehnungen richtig begruendet.
- Regel 2, maschinell zugeordnet: hunk_header in PR 71, 86 und 166
  (Text einer @@-Zeile zitiert); spans_removed_line in PR 64 und 615
  (Zeilen ueber eine entfernte Zeile hinweg verbunden); inner_whitespace
  zweimal in PR 299 (Leerzeichen oder Zeilenumbrueche veraendert).
- Regel 3: PR 316. Der Verfasser hat die Stelle lokal eingesehen. Das
  Modell gab einen doppelten Backslash der Quelle als einfachen wieder.
  Zuordnung nach Regel 2. Das Suchprogramm hatte den Fall als
  wahrscheinlich umformuliert eingestuft; ein einzelnes veraendertes
  Zeichen erkennt es nicht als eigene Ursache (Grenze fuer Kapitel 7).

Punkt 5. Die Zaehlung ergab 2 angenommene Zitate ueber eine entfernte
Zeile hinweg und keine weiteren nachsichtigen Faelle. Entschieden: Das
Pruefprogramm prueft seit Commit ec360b3 nach den Zitatregeln des
Prompts. Entfernte Zeilen und @@-Zeilen trennen die Zeilen davor und
danach, bei einem Review-Kommentar zaehlt nur der Kommentartext, und eine
hinzugefuegte Zeile, die mit ++ beginnt, wird nicht mehr verworfen.
Die 2 Zitate sind seitdem abgelehnt, daher 8 statt 6. Begruendung: B9
misst am Prompt; ein nachsichtigeres Pruefprogramm wuerde die
Quellentreue zu guenstig darstellen.
Nebenbefund: Nach diesem Umbau ordnete das Suchprogramm PR 86 zunaechst
falsch ein, weil das Zitat zwei Regeln zugleich verletzt. Berichtigt in
Commit 1cb8849.

Punkt 4. Erfuellt fuer hunk_header (3 Pull Requests) und
spans_removed_line (2 Pull Requests). Prompt Version 2
(prompts/extraction_system_v2.md) fasst genau diese beiden Regeln
deutlicher. Alle anderen Zeilen und die Nutzervorlage bleiben gleich;
ein Test in tests/test_prompt_files.py sichert das. Die Leerzeichen-
Faelle (ein Pull Request) und PR 316 loesen keine Aenderung aus.

Regel fuer die Uebernahme von Version 2, festgelegt vor ihrem Lauf:
Version 2 wird am Pilot unter der Kennung 2026-09-24_pilot_v2 erprobt.
Sie wird fuer den Volllauf uebernommen, wenn alle drei Bedingungen
gelten:

a) Die Regel aus E10 d ist erfuellt.
b) hunk_header und spans_removed_line treten zusammen in weniger Pull
   Requests auf als bei Version 1 (dort 5).
c) Der Anteil abgelehnter Zitate an allen Zitaten ist nicht hoeher als
   bei Version 1 (dort 8 von 145).

Sonst bleibt Version 1. Bedingung c misst einen Anteil und keine
Anzahl. So schneidet eine Version nicht allein dadurch besser ab, dass
sie weniger zitiert. Beide Laeufe werden mit demselben Pruefprogramm
und demselben Suchprogramm geprueft.
Einschraenkung fuer Kapitel 7: Je Version gibt es einen Lauf an 20
Vorgaengen. Das Modell antwortet bei gleicher Eingabe nicht immer
gleich. Ein Unterschied kann daher auch zufaellig sein.

Herkunft: Vorschlag des Modells im Chat vom 24.09.2026, vom Verfasser
festgelegt.

Status: festgelegt.
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

## 2026-09-24 Paket E: Abschluss des Pilots A8

### 2026-09-24 E11 Denkaufwand, Schemapruefung beim Anbieter und Prompt-Version fuer den Volllauf

a) Denkaufwand bleibt medium. Grundlage ist die vorab festgelegte Regel
aus E10 d. In beiden Pilotlaeufen war keine Antwort abgeschnitten, alle
20 waren gueltiges JSON, und die Kostenobergrenze lag mit 1,3665 und
1,2942 US-Dollar unter 2,10 US-Dollar.

b) Keine Schemapruefung beim Anbieter, aus dem Grund von E10 e: Gemessen
wird, wie oft das Modell das Format ohne Hilfe einhaelt (FF2), und der
Vergleich mit dem lokalen Modell in Paket F bleibt fair (FF3). Mit Prompt
v1 erfuellten 20 von 20 Antworten das Schema, mit Prompt v2 19 von 20
(PR 86: leere Liste unter supports). validate_output.py erkennt solche
Faelle; sie werden als Messwert gezaehlt.

c) Prompt v2 fuer den Volllauf. Die Uebernahmeregel aus dem Nachtrag zu
E10 vom 24.09.2026 ist erfuellt: E10 d eingehalten; hunk_header und
spans_removed_line zusammen in 4 statt 5 Pull Requests; Anteil
abgelehnter Zitate 7 von 152 statt 8 von 145. Die Unterschiede sind
klein und beruhen auf je einem Lauf. Die @@-Regel hat offenbar gewirkt
(1 statt 3 Pull Requests), die Regel zu entfernten Zeilen nicht (3
statt 2). Auf Ebene der Datensaetze lehnte das Pruefprogramm 8 statt 7
ab, wegen des Schemafehlers aus b.

d) Keine Version 3. Punkt 4 des Nachtrags zu E10 gilt nur fuer den
Schritt von Version 1 zu Version 2. spans_removed_line trat mit v2 in 3
Pull Requests auf, obwohl der Prompt die Regel ausdruecklich nennt. Eine
weitere Umformulierung verspricht wenig, und validate_output.py lehnt
solche Zitate ab. Eine weitere Ursachensuche findet nur statt, wenn es
dafuer einen neuen, schriftlich begruendeten Anlass gibt.

e) Ursachen im Lauf 2026-09-24_pilot_v2 (Suchprogramm, Commit 8cdaaca),
7 abgelehnte Zitate: hunk_header in PR 71; spans_removed_line in PR 214,
442 und 615; diff_markers_kept in PR 307; inner_whitespace in PR 299;
likely_rephrased in PR 294. Regel 1: keines. PR 294 hat der Verfasser
lokal eingesehen: Das Modell setzte vor \ket zwei Backslashes, die
Quelle hat einen. Zuordnung nach Regel 2. Zusammen mit PR 316 aus dem
ersten Lauf (dort ein Backslash zu wenig) ergibt sich eine Beobachtung
an zwei Faellen: Bei LaTeX-Ausdruecken in Python-Kommentarbloecken gibt
das Modell die Zahl der Backslashes nicht verlaesslich wieder. Das
Suchprogramm erkennt diese Faelle nicht als eigene Ursache. Beides
gehoert nach Kapitel 6 und 7.

Herkunft: Regel und Messwerte wie angegeben; Vorschlag des Modells im
Chat vom 24.09.2026, vom Verfasser festgelegt.

Status: festgelegt.
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

### Nachtrag zu E10 (2026-09-24): Laufdatum und Antwort zu PR 64 im Lauf 2026-09-22_pilot

Die Kennung 2026-09-22_pilot bleibt. Laut Manifest wurde PR 64 am
22.09.2026 gesendet, die uebrigen 19 Vorgaenge am 23.09.2026 zwischen
05:49 und 06:02 UTC. In der Arbeit wird das Datum aus dem Manifest
genannt.

Die Antwort zu PR 64 stammt aus dem Probeaufruf vom 22.09.2026, also vor
der Korrektur der Kostenrechnung (Aufschlag fuer das Schreiben in den
Zwischenspeicher). Die Korrektur betrifft nur die Nachberechnung der
Kosten, nicht die Anfrage an das Modell. Die Antwort ist deshalb
gleichwertig und bleibt Teil des Laufs.

Status: festgelegt.
Bezug: Kapitel 5 und 7, Nachvollziehbarkeit.

### Nachtrag zu E8 (2026-09-24): Volllauf im Normalbetrieb statt im Stapelbetrieb

Entscheidung des Verfassers: Der Volllauf ueber 395 Vorgaenge laeuft im
Normalbetrieb, wie die beiden Pilotlaeufe. Er nutzt dasselbe
Aufrufprogramm src/extract/run_extraction.py und dieselbe Konfiguration
config/api_run.toml mit Prompt v2. Der in E8 vorgesehene Stapelbetrieb
("Batch") entfaellt. Alle uebrigen Festlegungen von E8 gelten weiter.

Anlass: E8 begruendete den Stapelbetrieb damit, dass niemand auf das
Ergebnis wartet. Seit dem vorgezogenen Abgabetermin 15.10.2026 warten
Paket F (FF3) und Paket G (FF4) auf den Volllauf (STATUS.md, Roter
Faden). Recherche vom 24.09.2026 in der Dokumentation von OpenAI:

- Stapelbetrieb: halber Preis, Frist nur 24 Stunden. Danach werden
  unfertige Anfragen abgebrochen, fertige werden berechnet.
  Quelle: https://developers.openai.com/api/docs/guides/batch
- Warteschlange: Fuer gpt-5.6-terra duerfen in Nutzungsstufe 1
  hoechstens 1 500 000 Eingabe-Token gleichzeitig warten. Das Konto ist
  in Stufe 1 (abgelesen vom Verfasser am 24.09.2026). Der Volllauf hat
  rund 3,96 Mio Eingabe-Token (experiments/kostenschaetzung.md,
  Abschnitt 6.2). Er braeuchte also mindestens drei Stapel
  nacheinander, jeder mit bis zu 24 Stunden Frist.
  Quelle: https://developers.openai.com/api/docs/models/gpt-5.6-terra
- Datenhaltung: Fuer /v1/batches und /v1/files nennt OpenAI als
  Speicherdauer "bis zur Loeschung"; die Ausgabedatei eines Stapels wird
  30 Tage nach dessen Ende geloescht. Im Normalbetrieb mit store = false
  bleibt kein solcher Anwendungszustand, nur das Missbrauchsprotokoll
  bis 30 Tage.
  Quelle: https://developers.openai.com/api/docs/guides/your-data
- Nicht belegt: ob der Zwischenspeicher fuer gpt-5.6-terra im
  Stapelbetrieb wirkt und was eine harte Ausgabengrenze mit einem
  laufenden Stapel macht. Den Stapelpreis fuer terra (1,00 / 6,00
  US-Dollar je Mio Token) nennt nur eine Sekundaerquelle.

Begruendung:
1. Zeit. Es braucht keinen neuen Code. Das Aufrufprogramm hat 26 Tests
   und lief zweimal echt. Geschaetzte Laufzeit 4,8 Stunden, weil der
   Lauf 2026-09-24_pilot_v2 fuer 20 Vorgaenge 878 Sekunden brauchte.
   Der Stapelbetrieb braeuchte wenige Stunden bis etwa vier Tage,
   dazu die Programmierung.
2. Vergleichbarkeit. Pilot und Volllauf nutzen denselben Aufrufweg. Ein
   Unterschied zwischen ihnen kann deshalb nicht am Aufrufweg liegen.
3. Datenkontrolle (FF3). Die Quellbloecke liegen nicht als Datei beim
   Anbieter.
4. Kosten. Obergrenze rund 25,86 statt 12,93 US-Dollar ohne Steuer:
   3,96 Mio Eingabe-Token zu 2,00 mit Aufschlag 1,25 und 1,33 Mio
   Ausgabe-Token zu 12,00 je Mio. Mit dem bisherigen Verbrauch von 2,40
   US-Dollar und 19 Prozent Aufschlag sind das rund 34 US-Dollar. Das
   Budget aus E3 von 150 Euro bleibt weit unterschritten.

Konto am 24.09.2026, abgelesen vom Verfasser: Verbrauch im September
2,40 US-Dollar, Guthaben nach Aufladung 42,60 US-Dollar, hartes
Monatslimit 35 US-Dollar. Das Limit von 10 US-Dollar aus dem Nachtrag
zu E10 vom 22.09.2026 ist damit abgeloest.

Folge fuer die Arbeit: In Kapitel 5 und bei FF3 (Kosten) gilt der
Normalpreis. Der Stapelbetrieb wird nur als rechnerische Moeglichkeit
genannt, nicht als gemessener Wert.

Herkunft: Entscheidung des Verfassers am 24.09.2026. Recherche,
Rechnung und Formulierung von Claude im Chat vom 24.09.2026, vom
Verfasser geprueft.

Status: festgelegt.
Bezug: FF1, FF2, FF3, Kapitel 4 Abschn. 4.6, Kapitel 5, Kapitel 7.

## 2026-09-27 Paket E: Pruefung des Volllaufs 2026-09-25_full_v2

### Nachtrag zu E10 (2026-09-27): Regel 1 im Volllauf, Teil 1: Anlass und Zuordnungsregel

Teil 1 ist festgelegt, bevor gezaehlt wird. So kann die Regel nicht nach
dem Ergebnis gewaehlt werden. Teil 2 mit dem Ergebnis folgt darunter.

Anlass: Das Suchprogramm src/extract/diagnose_excerpts.py ordnete in der
Pruefung des Volllaufs vom 26.09.2026 (Commit laut STATUS.md, Abschnitt
Aktuell) 8 abgelehnte Zitate der Ursache edge_whitespace zu, also Regel 1
(Pruefprogramm schuld). Es prueft edge_whitespace vor diff_markers_kept.
Laesst ein Zitat bei einer Kontextzeile (Diffzeile, die mit einem
Leerzeichen beginnt) dieses Leerzeichen stehen, verstoesst es gegen Prompt
v2, Feld excerpt: "Leave out the first character of each copied line".
Das Suchprogramm zaehlt es trotzdem unter edge_whitespace. Gezeigt am
27.09.2026 mit erfundenen Daten in der Umgebung von Claude. Wie viele der
8 Zitate betroffen sind, ist offen. Das ist der neue, schriftlich
begruendete Anlass nach E11 d.

Geltung: Die Regeln 1 bis 3 des Nachtrags zu E10 vom 24.09.2026 gelten
auch fuer den Volllauf 2026-09-25_full_v2. Bisher stand das nur in
STATUS.md.

Regel:

1. Neue Ursache context_marker_kept, zugeordnet nach Regel 2. Sie trifft
   zu, wenn alle drei Bedingungen gelten:
   a) Das Zitat stammt aus einem Diff (location diff).
   b) Seine erste Zeile beginnt mit einem Leerzeichen und enthaelt nicht
      nur Leerraum.
   c) In der genannten Datei steht nach einer @@-Zeile eine Kontextzeile,
      die mitsamt ihrem Leerzeichen mit dieser ersten Zeile beginnt.
      Leerraum am Ende der ersten Zeile zaehlt dabei nicht mit.
   Das Suchprogramm prueft context_marker_kept vor edge_whitespace. Diese
   Aenderung gilt unabhaengig vom Ergebnis der Zaehlung.
2. Die uebrigen Zitate unter edge_whitespace bleiben bei Regel 1.
3. Faellt mindestens ein Zitat unter Regel 1, wird validate_output.py
   korrigiert. Ein Zitat gilt dann auch als gefunden, wenn alle drei
   Bedingungen gelten: Es kommt ohne Leerraum am Anfang und am Ende an
   der genannten Stelle vor; dieser Rest ist mindestens 10 Zeichen lang,
   die Untergrenze des Prompts; es faellt nicht unter context_marker_kept.
   Faellt kein Zitat unter Regel 1, bleibt validate_output.py
   unveraendert.
4. Nach jeder Codeaenderung folgen Tests, ein Test gegen absichtlich
   eingebaute Fehler und die neue Pruefung des Volllaufs mit beiden
   Programmen. Die Schnittstelle wird nicht erneut aufgerufen. Die Laeufe
   2026-09-22_pilot und 2026-09-24_pilot_v2 werden ebenfalls neu
   geprueft. Erwartet sind dort unveraenderte Zahlen, weil in beiden
   Laeufen kein Zitat unter edge_whitespace fiel (Nachtrag zu E10 vom
   24.09.2026, Ergebnis der Ursachensuche, und E11 e). Weicht eine Zahl
   ab, wird das in Teil 2 festgehalten.

Grenze fuer Kapitel 7: Steht in derselben Datei zufaellig eine
Kontextzeile, die so beginnt wie eine hinzugefuegte Zeile mit einem
zusaetzlichen Leerzeichen davor, zaehlt die Regel das Zitat faelschlich
unter context_marker_kept.

Herkunft: Befund und Regelvorschlag von Claude im Chat vom 27.09.2026.
Der Verfasser hat unter drei Wegen gewaehlt: erst aufteilen, dann
korrigieren. Verworfen: nicht korrigieren, weil das Regel 1 widerspricht;
ohne Aufteilung korrigieren, weil das Pruefprogramm dann nachsichtiger
waere als der Prompt (Nachtrag zu E10 vom 24.09.2026, Punkt 5).

Status: festgelegt (Teil 1).
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

### Nachtrag zu E10 (2026-09-27): Regel 1 im Volllauf, Teil 2: Ergebnis

Alle Zahlen stammen aus Laeufen des Verfassers am 27.09.2026. Es gab
keinen neuen Aufruf der Schnittstelle.

1. Zaehlung nach Punkt 1 (Suchprogramm, Commit 6b379dc): Kein Zitat
   faellt unter context_marker_kept. Keine andere Ursache hat Faelle
   abgegeben. Alle 8 Zitate bleiben bei Regel 1. Sie stammen alle aus
   Diffs: 2 aus PR 141, 5 aus PR 270, 1 aus PR 453.
2. Folge nach Punkt 3: validate_output.py wurde korrigiert (Commit
   b3cf18d). Beide Programme nutzen seitdem dieselbe Funktion
   excerpt_found. Dafuer ist context_marker_kept unveraendert in das
   Pruefprogramm umgezogen. Testsuite: 285 Tests bestanden. Der Test
   gegen absichtlich eingebaute Fehler (13 Fehler) lief in der Umgebung
   von Claude; jeder Fehler wurde von mindestens einem Test erkannt.
3. Volllauf vor und nach der Korrektur:

   | Groesse | vorher | nachher |
   |---|---|---|
   | abgelehnte Datensaetze (von 395) | 126 | 124 |
   | Anforderungen in angenommenen Datensaetzen | 922 | 932 |
   | abgelehnte Zitate (von 2 711) | 214 | 208 |
   | davon Regel 1 | 8 | 2 |
   | davon Regel 2 | 178 | 178 |
   | davon Regel 3 | 28 | 28 |
   | Anteil abgelehnter Zitate | 7,9 % | 7,7 % |

   Die 2 711 Zitate sind alle Zitate, die das Suchprogramm prueft:
   angenommene und abgelehnte zusammen. Zaehler und Nenner des Anteils
   stammen damit aus derselben Grundmenge.
4. Pilotlaeufe nach Punkt 4: unveraendert, wie vorhergesagt.
   Suchprogramm: 8 bzw. 7 abgelehnte Zitate mit denselben Ursachen.
   Pruefprogramm: 7 bzw. 8 von 20 Datensaetzen abgelehnt, 41 bzw. 39
   Anforderungen in angenommenen Datensaetzen. Die Vergleichswerte des
   Pruefprogramms wurden vor der Korrektur unter 6b379dc gemessen.
5. Abweichung von der Erwartung: 2 Zitate bleiben abgelehnt,
   QR-0270-04 und QR-0270-05, jeweils Beleg 1, aus einem Diff. Grund,
   aus dem Code abgeleitet und nicht einzeln eingesehen: Ohne Leerraum
   am Rand bleiben weniger als 10 Zeichen. Das Suchprogramm fuehrt sie
   unter edge_whitespace, also Regel 1.
   Entscheidung des Verfassers: Die Mindestlaenge aus Punkt 3 bleibt.
   Die 2 Zitate bleiben abgelehnt. In Kapitel 6 werden sie als Regel 1
   gezaehlt, nach der vorab festgelegten Mindestlaenge nicht
   korrigiert. Begruendung: Die Mindestlaenge nachtraeglich zu
   streichen, waere eine Regelaenderung nach Kenntnis des Ergebnisses.
   Wirkung auf Datensatzebene, aus den Zahlen abgeleitet: Die beiden
   Datensaetze, die nicht mehr abgelehnt werden, sind die zu PR 141 und
   PR 453. Der Datensatz zu PR 270 bleibt abgelehnt; er enthaelt
   mindestens 8 Anforderungen. Ob er nur wegen dieser 2 Zitate
   abgelehnt wird, ist nicht geprueft.
   Grenze fuer Kapitel 7: Der Prompt regelt Leerraum am Rand nicht. Ein
   Zitat aus Leerraum und einem kurzen Wort haelt womoeglich seinen
   Wortlaut ein. Das Pruefprogramm ist hier bewusst strenger.

Regel 1 ist fuer den Volllauf damit abgeschlossen. Als Naechstes folgt
Regel 3: 28 Zitate, die der Verfasser lokal einsieht.

Herkunft: Laeufe und Ablesung durch den Verfasser, Einordnung und
Formulierung von Claude im Chat vom 27.09.2026, vom Verfasser
geprueft. Die Wahl zu Punkt 5 traf der Verfasser.

Status: festgelegt (Teil 2).
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

## 2026-09-28 Paket E: Regel 3 im Volllauf

### Nachtrag zu E10 (2026-09-28): Regel 3 im Volllauf, Teil 3: Zuordnungsregel

Teil 3 ist festgelegt, bevor der Verfasser die Zitate einsieht. So kann
die Zuordnung nicht nach dem Inhalt der Stellen gewaehlt werden. Das
Ergebnis folgt als Teil 4.

Gegenstand: die 28 abgelehnten Zitate des Volllaufs 2026-09-25_full_v2,
die das Suchprogramm src/extract/diagnose_excerpts.py nach Teil 2 der
Regel 3 zuordnet. 21 stehen unter likely_rephrased (mindestens 80
Prozent der Woerter stehen in der genannten Quelle, der Wortlaut
nicht), 7 unter no_match (keine vorab definierte Ursache passt). Es
gelten die Programme im Stand des Commits, der diesen Nachtrag
enthaelt.

Massstab: Prompt v2, prompts/extraction_system_v2.md, Feld excerpt. Ein
Zitat muss woertlich aus dem Quellblock stammen, den das Modell gesehen
hat, bei einem Diff ohne das erste Zeichen jeder Zeile. Leerraum am
Rand und die Mindestlaenge von 10 Zeichen gelten wie in Teil 1,
Punkt 3.

Hilfsmittel: src/extract/inspect_excerpts.py. Es waehlt mit denselben
Pruefungen dieselben Zitate aus wie das Suchprogramm und zeigt sie nur
im Terminal des Verfassers. Je Zitat zeigt es das Zitat, die
naechstliegende Stelle der genannten Quelle, die Unterschiede zwischen
beiden und den Hinweis H1: ob das Zitat ohne Rand-Leerraum im
Quellblock des Modells vorkommt und in welchem Abschnitt. H1 ist ein
Hinweis, keine Entscheidung. Inhalte der Stellen gehen nicht in den
Chat.

Regel:

1. Der Verfasser prueft jedes Zitat an der genannten Stelle (location
   und locator) und vergibt genau eine Unterart. Er prueft in dieser
   Reihenfolge, die erste zutreffende gilt:
   a) pruefprogramm, Regel 1: Das Zitat steht Zeichen fuer Zeichen an
      der genannten Stelle des Quellblocks und haelt alle Zitatregeln
      des Prompts ein. Das Pruefprogramm vergleicht dann mit einem
      Text, der vom Quellblock abweicht.
   b) zusammengesetzt, Regel 2: Das Zitat verbindet Teile, zwischen
      denen in der Quelle mindestens ein ganzer Satz oder eine ganze
      Zeile liegt.
   c) umformuliert, Regel 2: Das Zitat entspricht einer
      zusammenhaengenden Stelle, aber mindestens ein Wort ist ersetzt,
      ergaenzt, weggelassen oder umgestellt.
   d) zeichen, Regel 2: Alle Woerter stimmen in derselben Reihenfolge
      mit einer zusammenhaengenden Stelle ueberein. Abweichend sind nur
      einzelne Zeichen, etwa ein Backslash, ein Anfuehrungszeichen, ein
      Bindestrich, ein Satzzeichen oder Gross- und Kleinschreibung.
   e) ohne_gegenstueck, Regel 2: Der Verfasser findet in der Quelle
      keine Stelle, die dem Zitat entspricht.
2. Regel 1 gilt nur bei einem positiven Befund nach 1 a. Kann der
   Verfasser ihn nicht feststellen, gilt Regel 2. Begruendung: Der
   Prompt verlangt eine woertliche Kopie. Ein Fehler des
   Pruefprogramms liegt nur vor, wenn es eine solche Kopie gibt.
3. Steht H1 auf nein und findet der Verfasser trotzdem eine woertliche
   Stelle nach 1 a, gilt 1 a. Der Fehler von H1 wird in Teil 4
   festgehalten.
4. Zwei Zusatzangaben je Zitat, jeweils ja oder nein:
   Andere Stelle: ja, wenn das Gegenstueck nicht an der genannten,
   sondern an einer anderen Stelle desselben Pull Requests steht. Die
   Unterart richtet sich dann nach dieser Stelle. 1 a verlangt nein.
   Zweifel: ja, wenn der Verfasser zwischen zwei Unterarten schwankt.
5. Aufzeichnung: docs/regel3_volllauf.md, erzeugt von
   inspect_excerpts.py mit --template. Die Tabelle enthaelt nur
   Kennungen und die Zuordnung, keine Inhalte. Ausgezaehlt wird mit
   --tally, das jede Zeile gegen die Auswahl und die Wertemengen
   prueft.

Folgen:

a) Faellt mindestens ein Zitat unter 1 a, wird die Ursache im
   Pruefprogramm gesucht, benannt und korrigiert. Es folgen Tests, ein
   Test gegen absichtlich eingebaute Fehler und die neue Pruefung des
   Volllaufs und beider Pilotlaeufe, wie in Teil 1, Punkt 4. Die
   Schnittstelle wird nicht erneut aufgerufen.
b) Faellt kein Zitat unter 1 a, bleiben beide Programme unveraendert.
c) Es entsteht keine neue Prompt-Version (E11 d) und keine neue
   Ursache im Suchprogramm. Die Unterarten beschreiben die Fehler des
   Modells fuer Kapitel 6.
d) ohne_gegenstueck wird in Kapitel 6 gesondert ausgewiesen. Ein Beleg
   ohne Gegenstueck ist Material fuer die Unbelegtheitsrate (FF3);
   wie sie gemessen wird, legt Paket F fest.

Grenzen fuer Kapitel 7: Eine Person ordnet zu, ohne zweite
unabhaengige Einschaetzung. Die Grenze zwischen zusammengesetzt,
umformuliert und zeichen ist Ermessen; die Zuordnung zu Regel 1 oder 2
haengt davon nicht ab. H1 sucht im ganzen Quellblock und kann eine
Stelle in einem anderen Abschnitt finden als dem genannten.

Herkunft: Regelvorschlag und Anzeigeskript von Claude im Chat vom
28.09.2026, vom Verfasser vor der Einsicht festgelegt.

Status: festgelegt (Teil 3).
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

### Nachtrag zu E10 (2026-09-28): Regel 3 im Volllauf, Teil 3a: Auslegung von 1 b bis 1 d

Teil 3a ist festgelegt, bevor der Verfasser die Tabelle
docs/regel3_volllauf.md ausfuellt. Anlass: Die Regel aus Teil 3 liess
zwei Fragen zur Unterart offen.

Offenlegung: Claude hatte zu diesem Zeitpunkt die Inhalte aller 28
Zitate gesehen, weil die Ausgabe des Anzeigeskripts in den Chat kopiert
wurde. Die Auslegung ist danach formuliert. Sie betrifft nur die
Unterart innerhalb von Regel 2. Die Zuordnung zu Regel 1 oder 2 aendert
sie nicht. Einzelheiten folgen in Teil 4.

1. Zu 1 b: In einem Diff zaehlt eine entfernte Zeile oder eine @@-Zeile
   als ganze Zeile der Quelle. Verbindet ein Zitat Zeilen ueber eine
   solche Zeile hinweg, ist es zusammengesetzt. Grund: Genau das
   verbietet der Prompt im Feld excerpt, Regeln fuer ein Zitat aus
   einem Diff.
2. Zu 1 c und 1 d: Ein Wort, das sich nur in einzelnen Zeichen
   unterscheidet, gilt als gleich. Einzelne Zeichen sind etwa ein
   Backslash, ein Satz- oder Formatzeichen, ein Leerzeichen oder Gross-
   und Kleinschreibung. Ein solches Zitat faellt unter 1 d. 1 c gilt
   erst, wenn mindestens ein ganzes Wort ersetzt, ergaenzt, weggelassen
   oder umgestellt ist.

Herkunft: Vorschlag von Claude im Chat vom 28.09.2026, vom Verfasser
vor dem Ausfuellen der Tabelle festgelegt.

Status: festgelegt (Teil 3a).
Bezug: FF1, FF2, FF3, Kapitel 6 und 7.

### Nachtrag zu E10 (2026-09-28): Regel 3 im Volllauf, Teil 4: Ergebnis und Abschluss der Pruefung

Stand 29.09.2026. Zuordnung nach Teil 3 und Teil 3a, aufgezeichnet in
docs/regel3_volllauf.md, ausgezaehlt mit inspect_excerpts.py --tally.
Die Auszaehlung meldete keine fehlerhafte Zeile.
Alle Zeilen hat der Verfasser nach dem Commit von Teil 3a
(8543bb9, 29.09.2026, 08:13 Uhr) ausgefuellt.

Ergebnis der Regel 3:

- Regel 1 (Pruefprogramm): 0. Regel 2 (Modell): 28 von 28, aus
  20 Pull Requests.
- Unterarten: zeichen 18, umformuliert 6,
  zusammengesetzt 4, ohne_gegenstueck 0.
- Andere Stelle: 0. Zweifel: 5.
- Beide Ursachen des Suchprogramms gehen vollstaendig in Regel 2 auf:
  likely_rephrased 21, no_match 7.
- Der Hinweis H1 stand laut Anzeigeskript bei allen 28 Zitaten auf
  nein. Punkt 3 aus Teil 3 kam nicht zur Anwendung.

Folge nach Teil 3, Folge b: validate_output.py und diagnose_excerpts.py
bleiben unveraendert. Eine Korrekturrunde entfaellt.

Endgueltige Pruefzahlen des Volllaufs 2026-09-25_full_v2, ausgezaehlt
mit src/extract/breakdown_rejections.py (Commit 167f49b):

- 124 von 395 Datensaetzen abgelehnt. Nach der ersten verletzten
  Pruefung: Schema 3, Belegstaerke nach E6 6, Zitat 115.
- Schema: fehlendes Feld requirements 1 (PR 796), mehr Belege als
  erlaubt 1, zu kurzes Zitat 1.
- E6: 8 Anforderungen in den 6 Datensaetzen. Das Modell gab die
  Belegstaerke jedes Mal hoeher an, als die Regeln ergeben: 7-mal
  indirect statt insufficient, 1-mal direct statt insufficient.
- In 3 der 9 wegen Schema oder E6 abgelehnten Datensaetze schlaegt
  auch die Zitatpruefung fehl. 118 Datensaetze enthalten mindestens
  ein nicht gefundenes Zitat.
- 547 Anforderungen stehen in abgelehnten Datensaetzen: 12 nach
  Schema, 34 nach E6, 501 nach Zitat.
- 208 von 2 711 Zitaten abgelehnt: Regel 1 2 (Teil 2), Regel 2 206.
- PR 270 wird nur wegen QR-0270-04 und QR-0270-05 abgelehnt. Schema
  und E6 besteht er.

Teilschritt 10 von A8 (Links): Variante B, Wahl des Verfassers vom
28.09.2026. Titel, Beschreibung und Diff erhalten den Link des Pull
Requests, Kommentare den Link, den GitHub je Kommentar geliefert hat.
Das Programm src/extract/add_links.py setzt keinen Link selbst
zusammen. In den Rohdateien hat jeder der 639 Kommentare und der
1 713 Review-Kommentare einen solchen Link. Ergebnis: 2 711 Belege,
2 606 mit Link auf den Pull Request, 105 auf einen Kommentar, keiner
ohne Link. Datei lokal:
data/processed/extraction_2026-09-25_full_v2.links.jsonl,
2 711 Zeilen, SHA-256 e5ba8c6c9d09c1da70638ce1f7d9e5d01ac77cc6bb9614bdb1b5f0a43a06a187.
Die Modellausgabe bleibt unveraendert (E7).

Kosten und Laufzeit des Volllaufs: experiments/kostenschaetzung.md,
Abschnitt 6.3, erzeugt mit src/extract/cost_report.py. Zwischen den
beiden Kontoablesungen lief nach Angabe des Verfassers kein anderer
Aufruf.

Abweichung von Teil 3: Teil 3 sah vor, dass Inhalte der Stellen nicht
in den Chat gehen. Der Verfasser hat am 28.09.2026 die Ausgabe des
Anzeigeskripts zu allen 28 Zitaten in den Chat kopiert. Claude hat
daraufhin keine Zuordnung und keine Einschaetzung zu einzelnen
Zitaten gegeben. Die Beispiele in seinen Erklaerungen stammen aus den
erfundenen Testdaten. Die Auslegung in Teil 3a hat Claude nach Sicht
der Inhalte formuliert; sie betrifft nur die Unterarten. Die Inhalte
sind oeffentlich, Erwaehnungen waren nach E9 ersetzt.

Grenzen fuer Kapitel 7, zusaetzlich zu Teil 3:
- Eine Person ordnet zu. Eine Gegenpruefung durch Claude wurde
  angeboten, aber bisher nicht angefordert.
- 5 von 28 Zuordnungen tragen den Vermerk Zweifel.
- Bei niedriger Aehnlichkeit zeigte das Anzeigeskript oft eine
  unpassende Stelle. Fuer diese Faelle standen zwei Befehle bereit,
  die die ganze genannte Quelle und den ganzen Quellblock zeigen.

Herkunft: Zuordnung, Wahl der Linkvariante und alle Laeufe durch den
Verfasser; Programme, Auszaehlung und Formulierung von Claude im Chat
vom 28. und 29.09.2026, vom Verfasser geprueft.

Status: festgelegt (Teil 4). Die Pruefung des Volllaufs ist
abgeschlossen.
Bezug: FF1, FF2, FF3, Kapitel 5, 6 und 7.

## 2026-09-29 Paket F: Kontrollpunkt und lokales Modell

### 2026-09-29 F1 Umfang von FF3 nach dem Kontrollpunkt

Festgelegt vor dem Pilotfall, damit der Umfang von FF3 nicht nach dem
Ergebnis gewaehlt wird (STATUS.md, Zeitplan, Risiko 1). Vorher lag nur
ein Probeaufruf ohne Daten dieser Arbeit am 29.09.2026 um 23:46 Uhr
(Serverprotokoll). Er pruefte, ob die Laufzeitumgebung die Felder des
Aufrufprogramms annimmt. Eine erste Fassung mit der Frist Di 29.09.2026,
22:00 Uhr, wurde nicht committet, weil die Frist vor dem Commit
verstrichen war.

Pilotfall: PR 64 aus docs/sample_pilot_a8.md, gesendet mit
src/extract/run_extraction.py, config/local_run.toml und --limit 1. Er
gilt als gelungen, wenn die Antwort vollstaendig ist und als
JSON-Objekt in der Extraktionsdatei steht. Ob validate_output.py sie
annimmt, zaehlt dafuer nicht, weil eine Ablehnung selbst ein Messwert
ist.

Frist fuer den Pilotfall: Mi 30.09.2026, 12:00 Uhr.

Einstellungen in allen Stufen wie beim API-Modell: Prompt v2,
Modelleingabe data/processed/model_input_2026-09-19.jsonl,
Denkaufwand medium, max_output_tokens 25000, keine Formathilfe der
Laufzeitumgebung (E10 e, E11 b).

a) Pilotfall innerhalb der Frist gelungen: zwei Durchgaenge mit
   gleichen Einstellungen ueber alle 20 Vorgaenge der Pilotstichprobe,
   wie beim API-Modell. Vor dem Rest des ersten Durchgangs ein
   Probelauf mit --limit 5.
b) Wie a, aber die Hochrechnung aus dem Probelauf liegt ueber 16
   Stunden fuer beide Durchgaenge. Hochrechnung: mittlere Dauer je
   Vorgang aus Pilotfall und Probelauf mal 40. Dann laeuft der erste
   Durchgang ueber alle 20, der zweite nur ueber 12 Vorgaenge. Die 12
   sind je Schicht die ersten, aufgerundet halb so viele, in der
   Reihenfolge von docs/sample_pilot_a8.md: 64, 71, 86, 136, 169, 171,
   187, 294, 299, 316, 442, 448. Die Konsistenz beider Modelle wird
   dann an diesen 12 verglichen.
c) Pilotfall nicht gelungen: ein zweiter Versuch bis Mi 30.09.2026,
   20:00 Uhr, mit einer anderen Laufzeitumgebung oder einem anderen
   Modell, gewaehlt nach der Fehlerursache. Gelingt er, laufen beide
   Durchgaenge ueber die 12 Vorgaenge aus b.
d) Auch c misslingt: FF3 wird ohne Qualitaetsmessung eines lokalen
   Modells beantwortet. Die lokale Seite besteht dann aus dem
   dokumentierten Einrichtungsversuch, dem Einrichtungsaufwand und der
   Datenkontrolle. Das weicht vom Expose ab, das einen praktischen
   Vergleich auch der Ergebnisqualitaet vorsieht. Die Abweichung ist
   eine Entscheidung des Verfassers; die Begruendung steht im Nachtrag
   zu F1, Teil 2, Punkt 5, und in Abschnitt 6.1 der Arbeit.

Begruendung der Schwelle von 16 Stunden: Paket G beginnt laut Zeitplan
am Do 01.10.2026. Beide Durchgaenge muessen bis dahin fertig sein; 16
Stunden entsprechen einer Nacht und einem Arbeitstag. Die Schwelle ist
eine Festlegung dieser Arbeit, keine Quellenangabe.

Herkunft: Vorschlag von Claude im Chat vom 29.09.2026, vom Verfasser
vor dem Pilotfall festgelegt.

Status: festgelegt.
Bezug: FF3, Kapitel 4, Kapitel 5, Kapitel 7.

### 2026-09-29 F2 Laufzeitumgebung und lokales Modell

Gewaehlt: Ollama 0.34.4, stabile Fassung aus Homebrew, als
Laufzeitumgebung und gpt-oss:20b von OpenAI als lokales Modell fuer
FF3. Daraus abgeleitet das Modell gpt-oss-20b-ctx64k nach
config/ollama/gpt-oss-20b-ctx64k.Modelfile mit einem Kontextfenster von
65 536 Token. Aufgerufen wird es ueber dieselbe Schnittstelle
/v1/responses und dasselbe Programm run_extraction.py wie das
API-Modell, mit config/local_run.toml. Versionsnummer, Pruefsumme des
Modells und Kontextfenster schreibt das Programm in jedes Manifest.

Begruendung:
1. Aufrufweg. Ollama unterstuetzt /v1/responses
   (https://docs.ollama.com/api/openai-compatibility, abgerufen am
   29.09.2026, geprueft am 30.09.2026). Die Dokumentation nennt model,
   max_output_tokens und reasoning.effort als unterstuetzt; das Feld
   store nennt sie nicht. Der Probeaufruf vom 29.09.2026 kam mit status
   completed und store false zurueck. Programm, Prompt und Eingabe
   bleiben damit fuer beide Seiten gleich.
2. Speicher. Modell und Kontextfenster belegen laut Serverprotokoll
   13 838 von 28 753 MiB Grafikspeicher; ollama ps meldet 100% GPU.
3. Denkaufwand. gpt-oss kennt die Stufen low, medium und high, Standard
   medium (ollama show). Die Einstellung aus E10 d bleibt erhalten.
4. Lizenz Apache 2.0 (ollama show). Kein Schluessel, kein Konto, keine
   Daten verlassen den Rechner: Cloud-Funktionen abgeschaltet
   (Serverprotokoll: Ollama cloud disabled: true), Server nur auf
   127.0.0.1. Das Programm lehnt eine Konfiguration ohne Schluessel ab,
   deren Adresse nicht auf diesem Rechner liegt.

Verworfen: qwen3.6:35b, weil 23 GB nah an der Grenze des
Grafikspeichers liegen; qwen3.6:27b, weil es als dichtes Modell nach
eigener Rechnung aus der Speicherbandbreite zu langsam fuer den
Zeitplan ist. qwen3.6:27b bleibt der Ersatz fuer F1 c.

Gegenargumente, fuer Kapitel 7:
- gpt-oss stammt vom selben Anbieter wie gpt-5.6-terra. Der Vergleich
  trennt API und lokal, sagt aber nichts ueber andere Anbieter.
- Jedes auf diesem Rechner lauffaehige Modell ist viel kleiner als das
  API-Modell. Lokal und klein fallen zusammen.
- Prompt v2 wurde am API-Modell erprobt, nicht am lokalen.
- Offen sind die Gewichte (Apache 2.0), nicht die Trainingsdaten. Der
  Begriff Open-Source aus dem Expose ist in Kapitel 2 zu schaerfen.

Befunde aus Einrichtung und Probeaufruf, fuer Kapitel 5:
- Ohne Modelfile haette der Server ein Kontextfenster von 32 768 Token
  gewaehlt (Serverprotokoll: vram-based default context). Das reicht
  nicht fuer die laengste Eingabe der Pilotstichprobe plus 25 000
  Ausgabe-Token.
- Ollama meldete reasoning_tokens als 0, obwohl die Antwort einen
  Denkteil enthielt. Die Zahl der Denk-Token ist lokal nicht gemessen;
  das Manifest vermerkt, ob die Laufzeitumgebung sie meldet.
- Das Serverprotokoll nennt fuer die Auswahl der Token top_k 40 und
  top_p 0,9, die Antwort meldet top_p 1. Welche Werte wirken, ist
  ungeprueft. Das Serverprotokoll jedes Laufs wird deshalb lokal
  ausserhalb des Repositorys aufbewahrt; es zeigt je Anfrage auch, ob
  gekuerzt wurde.
- Ollama 0.34.4 fuehrt gpt-oss mit llama-server aus (Serverprotokoll).
- Die Hinweise von Homebrew zu OLLAMA_FLASH_ATTENTION und
  OLLAMA_KV_CACHE_TYPE=q8_0 werden nicht umgesetzt. q8_0 speichert
  Zwischenwerte ungenauer (Ollama-FAQ), und der Speicher reicht ohne.

Umgebung: brew install ollama hat am 29.09.2026 als Abhaengigkeit
python@3.14 von 3.14.6 auf 3.14.7 angehoben und mlx sowie mlx-c
installiert. Die Laeufe von Paket E liefen laut Manifest unter 3.14.6,
die Laeufe von Paket F laufen unter 3.14.7. Fuer den Aufruf ist das
ohne erkennbare Wirkung, weil Python nur die Anfrage sendet; es wird
dennoch in Kapitel 5 genannt.

Herkunft: Recherche und Vorschlag von Claude im Chat vom 29.09.2026,
Einrichtung und Probeaufruf durch den Verfasser, Wahl durch den
Verfasser vor dem Pilotfall.

Status: festgelegt.
Bezug: FF3, Kapitel 2, Kapitel 4 Abschn. 4.6, Kapitel 5, Kapitel 7.

### Nachtrag zu F1 (2026-09-30): Ergebnis des Pilotfalls und Regel fuer den zweiten Versuch

Pilotfall am 30.09.2026: PR 64 mit gpt-oss-20b-ctx64k, Lauf
2026-09-30_local_pilot_v2_r1. Messwerte im Manifest
data/processed/extraction_2026-09-30_local_pilot_v2_r1.manifest.json.

1. Ergebnis nach F1: nicht gelungen. Die Antwort ist laut
   Laufzeitumgebung vollstaendig (status completed), steht aber nicht als
   JSON-Objekt in der Extraktionsdatei.
2. Lesart von F1: Der Pilotfall ist ein einziger Versuch. Ein weiterer
   Versuch mit demselben Modell an PR 64 zaehlt nicht, weil F1 genau
   einen Aufruf mit --limit 1 nennt und ein Wiederholen bis zum Erfolg
   eine Auswahl nach dem Ergebnis waere. Gewaehlt vom Verfasser am
   30.09.2026, vor der Ursachensuche. Es gilt F1 c.
3. Formpruefung der Antwort, ohne Inhalte und ohne Reparatur: Der
   Antworttext beginnt mit einer oeffnenden geschweiften Klammer, endet
   aber mitten im Objekt; das JSON-Modul meldet am Textende ein fehlendes
   Komma. Keine Codeblock-Umrahmung. Die Antwort enthaelt einen Denkteil
   und eine Nachricht. Das Kontextfenster wurde nicht erreicht, das
   Serverprotokoll meldet truncated = 0.
4. Moegliche Ursachen: (a) Das Modell beendet seine Nachricht mit einem
   Endzeichen, bevor das Objekt geschlossen ist. (b) Die
   Laufzeitumgebung beendet die Ausgabe vorzeitig und meldet trotzdem
   completed. Aus den Zahlen allein ist das nicht entscheidbar.
5. Zuordnungsregel, festgelegt vor der Einsicht in die Stoppmeldungen
   des Serverprotokolls. Gesucht wird im Serverprotokoll des Laufs nach
   Zeilen mit stopped, cancel, n_decoded oder n_predict.
   - Ende durch ein Endzeichen des Modells (etwa stopped by EOS, oder
     stopped by word mit einem Harmony-Endzeichen): Ursache (a). Zweiter
     Versuch mit qwen3.6:27b in derselben Laufzeitumgebung, dem Ersatz
     aus F2.
   - Abbruch durch eine Grenze oder durch Ollama (etwa stopped by limit
     oder cancel): Ursache (b). Zweiter Versuch mit gpt-oss:20b in einer
     anderen Laufzeitumgebung, gewaehlt nach Recherche.
   - Kein Stoppgrund im Protokoll: nicht entscheidbar. Zweiter Versuch
     mit qwen3.6:27b in derselben Laufzeitumgebung, weil F2 dieses Modell
     als Ersatz nennt und Programm und Aufrufweg gleich bleiben. Endet
     auch diese Antwort mitten im Objekt, spricht das fuer Ursache (b);
     das wird in Kapitel 7 berichtet, und es gilt F1 d.
6. Die Antwort von gpt-oss zu PR 64 bleibt als Messwert erhalten: ein
   Formatfehler bei einem Vorgang. Rohdatei lokal, Manifest versioniert.
   Der Lauf 2026-09-30_local_pilot_v2_r1 wird nicht fortgesetzt.

Herkunft: Formpruefung durch den Verfasser mit einem Diagnoseprogramm
aus dem Chat vom 30.09.2026; Lesart durch den Verfasser; Zuordnungsregel
von Claude vorgeschlagen, vom Verfasser vor der Einsicht festgelegt.

Status: festgelegt (Teil 1). Teil 2 folgt mit dem Ergebnis der
Zuordnung.
Bezug: FF2, FF3, Kapitel 5, 6 und 7.

### Nachtrag zu F1 (2026-09-30), Teil 2: Zuordnung, zweiter Versuch und Umfang von FF3

1. Zuordnung nach Teil 1, Punkt 5: Im Serverprotokoll des Laufs fand
   die Suche nach stopped, cancel, n_decoded und n_predict keine Zeile.
   Die Ursache beim ersten Versuch ist damit nicht entscheidbar. Nach
   der Regel folgte der zweite Versuch mit qwen3.6:27b in derselben
   Laufzeitumgebung, mit config/local_run_qwen.toml, committet vor dem
   Lauf.
2. Zweiter Versuch am 30.09.2026: PR 64 mit qwen3.6-27b-ctx64k, Lauf
   2026-09-30_local_qwen_pilot_v2_r1, Messwerte im Manifest
   data/processed/extraction_2026-09-30_local_qwen_pilot_v2_r1.manifest.json.
   Die Antwort ist laut Laufzeitumgebung vollstaendig, steht aber nicht
   als JSON-Objekt in der Extraktionsdatei: Das Modell hat den
   Antworttext in einen Markdown-Codeblock gesetzt, obwohl der Prompt
   ein Objekt ohne Umrahmung verlangt. Nach F1 c nicht gelungen.
3. Formpruefung, nur zur Diagnose und ohne Wertung (E10 e): Vor und
   nach dem Codeblock steht kein weiterer Text, innerhalb steht ein
   vollstaendiges JSON-Objekt. Die Antwort endet also nicht mitten im
   Objekt. Nach Teil 1, Punkt 5 spricht der zweite Versuch damit nicht
   fuer die Laufzeitumgebung als gemeinsame Ursache. Die Ursache beim
   ersten Versuch bleibt offen.
4. Folge: Es gilt F1 d. FF3 wird ohne Qualitaetsmessung eines lokalen
   Modells beantwortet. Die lokale Seite umfasst den dokumentierten
   Einrichtungsversuch, den Einrichtungsaufwand, Laufzeit und
   Speicherbedarf der beiden Pilotfaelle und die Datenkontrolle. Die
   Formatfehler beider Modelle werden als explorativer Befund mit einem
   Vorgang je Modell berichtet.
5. Entscheidung des Verfassers am 30.09.2026: F1 d wird woertlich
   angewandt, ohne zusaetzliche Messung. Verworfen wurde ein einzelner,
   als explorativ gekennzeichneter Lauf von gpt-oss:20b ueber die 12
   Vorgaenge aus F1 b. Begruendung:
   a) Die Regel stand vor beiden Versuchen fest. Eine Zusatzmessung
      waere nach dem Ergebnis beschlossen und wuerde die vorab
      festgelegte Stufe d aufweichen.
   b) Auch mit 12 Vorgaengen eines Modells bliebe der Befund explorativ.
      Belastbar vergleichen liesse sich damit weder die Qualitaet noch
      die Konsistenz ueber Wiederholungen.
   c) Bis zur internen Abgabe am 13.10.2026 stehen die Pakete G und H
      und der groesste Teil des Schreibens aus. Die Zeit geht dorthin.
   d) FF3 bleibt beantwortbar: Kosten, Aufwand und Datenkontrolle sind
      fuer beide Seiten gemessen oder belegt, zur Qualitaet liegt der
      Formatbefund vor.
6. Fuer Kapitel 7 festgehalten: ein Vorgang je lokales Modell; die
   Erfolgsbedingung von F1 verbindet technisches Gelingen mit
   Formattreue, obwohl ein Formatfehler nach E10 e selbst ein Messwert
   ist; der Prompt wurde nur am API-Modell erprobt; die lokalen Modelle
   sind viel kleiner als das API-Modell; gpt-oss stammt vom selben
   Anbieter wie das API-Modell; qwen kennt beim Denken nur an oder aus,
   gesendet wurde medium; die Auswahlwerte der Modelle weichen
   voneinander ab und wurden nicht gesendet (E10 e); die
   Laufzeitumgebung meldet keine Denk-Token; Python 3.14.7 statt 3.14.6
   in Paket E.

Herkunft: Suche im Serverprotokoll und Formpruefung durch den
Verfasser mit Befehlen aus dem Chat vom 30.09.2026; Zuordnung nach der
vorab committeten Regel; Entscheidung und Begruendung durch den
Verfasser, Formulierung durch Claude.

Status: festgelegt. F1 ist damit abgeschlossen.
Bezug: FF2, FF3, Kapitel 4, 6 und 7.

### 2026-09-30 F3 Messgroessen fuer FF3

Anlass: Die Projektanweisung erlaubt fuer den Modellvergleich hoechstens
sechs Messgroessen mit Zahlenwerten. Die uebrigen Vergleichsdimensionen
werden in Worten beschrieben. Nach F1 d liegt keine gueltige Ausgabe
eines lokalen Modells vor; die Messgroessen sind darauf zugeschnitten.

Kuerzel: M1 bis M6 sind die Nummern der sechs Messgroessen dieser
Entscheidung. M1 Formatkonformitaet, M2 Unbelegtheitsrate, M3
Konsistenz ueber Wiederholungen, M4 Laufzeit je Vorgang, M5 Kosten je
Vorgang, M6 Speicherbedarf. Ein Vorgang ist ein Pull Request mit
seinem Quellblock aus der Modelleingabe.

Einschraenkung, fuer Kapitel 7: Fuer M1, M4, M5 und M6 lagen die
Zahlen des API-Modells und der beiden lokalen Pilotfaelle vor dieser
Festlegung schon vor. Ein strenges "vorab" ist dort nicht mehr
moeglich. Die Definitionen folgen deshalb nur aus aelteren, bereits
committeten Regeln und Dateien: dem Pruefprogramm validate_output.py,
den Manifesten, den Regeln B1 bis B8 aus E6 und den Regeln 1 bis 3 aus
den Nachtraegen zu E10. Damit bleibt kein Spielraum, eine Definition
passend zum Ergebnis zu waehlen. M2 und M3 sind noch nicht gezaehlt;
ihre Regeln stehen mit diesem Commit fest.

Messgroessen mit Zahlenwerten:

M1 Formatkonformitaet. Oberkategorie Ergebnisqualitaet; FF2, FF3.
   Kennzahl: Anteil der Antworten, die (a) als JSON-Objekt in der
   Extraktionsdatei stehen (Manifest, valid_json_object) und (b) die
   Schemapruefung von validate_output.py bestehen.
   Daten: API-Modell im Volllauf 2026-09-25_full_v2 (395 Vorgaenge)
   und im Pilotlauf 2026-09-24_pilot_v2 (20 Vorgaenge); lokale Modelle
   je ein Vorgang, PR 64, Laeufe 2026-09-30_local_pilot_v2_r1 und
   2026-09-30_local_qwen_pilot_v2_r1.
   Stand: Volllauf (a) 395 von 395, (b) 3 Datensaetze mit Schemafehler
   laut Nachtrag zu E10, Teil 4, also 392 von 395. Zu bestaetigen beim
   Zaehlen: Das Pruefprogramm prueft das Schema zuerst, sodass die 3
   alle Schemafehler sind. Pilotlauf: (a) 20 von 20, (b) noch zu
   zaehlen. Lokal: (a) 0 von 1 je Modell, damit M1 0 von 1.

M2 Unbelegtheitsrate. Oberkategorie Ergebnisqualitaet; FF1, FF3.
   Einheit: die einzelne Anforderung, also ein Eintrag im Feld
   requirements eines Datensatzes.
   Grundmenge (Nenner): alle Anforderungen in den Datensaetzen des
   Volllaufs 2026-09-25_full_v2, die die Schemapruefung bestehen.
   Datensaetze mit Schemafehler gehen nur in M1 ein, damit kein Fehler
   doppelt zaehlt.
   Eine Anforderung gilt als unbelegt, wenn mindestens eine der zwei
   Bedingungen zutrifft:
   (1) Kein Beleg gefunden. Keiner ihrer hoechstens drei Belege steht
       woertlich in der genannten Quelle (B6). Als gefunden gilt ein
       Beleg, den das Pruefprogramm annimmt, und ein Beleg, dessen
       Ablehnung nach Regel 1 dem Pruefprogramm zugeordnet ist. Nicht
       gefunden ist ein Beleg, dessen Ablehnung nach Regel 2 dem Modell
       zugeordnet ist, einschliesslich der 28 Faelle, die nach Regel 3
       von Hand der Regel 2 zugeordnet wurden.
   (2) Belegstaerke insufficient. Die nach B1 bis B3 berechnete
       Belegstaerke lautet insufficient: Mindestens ein
       Pflichtbestandteil der Anforderung fehlt in der Quelle.
       Massgeblich ist der vom Pruefprogramm berechnete Wert, nicht der
       vom Modell angegebene.
   Kennzahl: Zahl der unbelegten Anforderungen geteilt durch die
   Grundmenge.
   Begruendung fuer (2): B8 in E6 legt fest, dass die Quote von
   insufficient ein Messwert fuer die Unbelegtheitsrate ist. Eine
   Anforderung, deren Pflichtbestandteil in der Quelle fehlt, ist nicht
   belegt, auch wenn das Modell das offen angibt.
   Gesondert berichtet, ohne eigene Messgroesse: (i) bei wie vielen
   unbelegten Anforderungen das Modell selbst insufficient angab und
   bei wie vielen eine hoehere Stufe (darunter die 8 Ablehnungen nach
   E6); (ii) Anforderungen mit teils gefundenen, teils nicht gefundenen
   Belegen; (iii) auf Ebene der Zitate: 206 von 2 711 nach Regel 2
   abgelehnt.
   Zu pruefen beim Zaehlen: ob validate_output.py bei der Berechnung
   nach B1 bis B3 auch nicht gefundene Belege mitzaehlt. Der Befund
   wird berichtet, die Regel bleibt.
   Lokal: entfaellt, weil keine gueltige Ausgabe vorliegt.
   Stand: noch nicht gezaehlt. Zaehlung in Paket H mit einem kleinen
   Zaehlprogramm, das die Belegpruefung und die Berechnung der
   Belegstaerke aus validate_output.py und die Zuordnung nach den
   Regeln 1 bis 3 nutzt und keine eigenen Pruefregeln enthaelt.

M3 Konsistenz ueber Wiederholungen. Oberkategorie Ergebnisqualitaet;
   FF1, FF3.
   Daten: die 20 Vorgaenge der Pilotstichprobe (docs/sample_pilot_a8.md)
   in zwei Durchgaengen, 2026-09-24_pilot_v2 und dieselben 20 Vorgaenge
   im Volllauf 2026-09-25_full_v2. Konfiguration und Promptdateien
   haben laut beiden Manifesten dieselben Pruefsummen; der Codestand
   ist verschieden.
   Quellstelle: das Paar aus location und locator eines Belegs.
   Je Vorgang und Durchgang: die Menge der Quellstellen aller Belege
   aller Anforderungen. Jaccard-Uebereinstimmung: Zahl der
   Quellstellen, die in beiden Mengen stehen, geteilt durch die Zahl
   der Quellstellen, die in mindestens einer Menge stehen. Sind beide
   Mengen leer, ist der Wert 1.
   Kennzahl: Mittelwert ueber die 20 Vorgaenge. Gesondert berichtet:
   kleinster Wert und Zahl der Anforderungen je Durchgang.
   Gezaehlt werden alle Belege, auch abgelehnte, weil M3 das Verhalten
   des Modells misst und nicht das Ergebnis der Pruefung.
   Lokal: entfaellt. Stand: noch nicht gezaehlt, Paket H.
   Grenze: Zwei Durchgaenge an 20 Vorgaengen ergeben keine belastbare
   Streuung; der Wert ist explorativ.

M4 Laufzeit je Vorgang. Oberkategorie Kosten und Aufwand; FF3.
   Kennzahl: duration_seconds im Manifest. Das Programm
   run_extraction.py misst die Zeit auf dem Rechner des Verfassers mit
   time.monotonic um den Aufruf. Verglichen wird an PR 64, dem einzigen
   Vorgang mit Werten aller Modelle. Fuer das API-Modell zusaetzlich
   Median, kleinster und groesster Wert ueber die 395 Vorgaenge des
   Volllaufs.
   Stand: bekannt, aus den Manifesten. Grenze: Beim API-Modell enthaelt
   die Zeit die Uebertragung ueber das Netz; je lokales Modell liegt
   ein Wert vor.

M5 Kosten je Vorgang. Oberkategorie Kosten und Aufwand; FF3.
   Kennzahl: Abrechnung im Konto geteilt durch die Zahl der Vorgaenge
   des Laufs. API-Modell: Volllauf, Abrechnung laut
   experiments/kostenschaetzung.md, Abschnitt 6.3. Lokal: keine
   Gebuehren. Strom und Anschaffung des Rechners sind nicht erhoben und
   werden beschrieben.
   Stand: bekannt. Grenze: Die Abrechnung ist die Differenz zweier
   Ablesungen; ob sie Umsatzsteuer enthaelt, ist ungeprueft (6.3).

M6 Speicherbedarf. Oberkategorie Kosten und Aufwand; FF3.
   Kennzahl: vom Server eingeplanter Grafikspeicher in MiB, Zeile
   "projected to use ... MiB of device memory" im Serverprotokoll,
   belegt in docs/ollama_protokollauszug.md. Gesondert berichtet: die
   Dateigroesse der Gewichte und bei qwen3.6:27b der Bildteil, der in
   der Projektion nicht enthalten ist.
   API-Modell: nicht anwendbar. Stand: bekannt.

In Worten beschrieben, ohne Zahlenwert:
- Einrichtungsaufwand: Arbeitsschritte und aufgetretene Probleme der
  lokalen Ausfuehrung. Stunden wurden nicht erfasst.
- Datenkontrolle und Verbleib der Daten: API-Modell mit store false und
  Missbrauchsprotokoll des Anbieters bis zu 30 Tage
  (config/api_run.toml); lokal nur auf diesem Rechner,
  Cloud-Funktionen abgeschaltet (F2).
- Reproduzierbarkeit: API-Modell ueber einen Namen ohne festen Stand;
  lokal Pruefsumme der Gewichte und Version der Laufzeitumgebung im
  Manifest. Alle Modelle mit Temperatur 1.
- Eindeutigkeit, Verifizierbarkeit, Vollstaendigkeit: in Paket H fuer
  FF1 am API-Modell bewertet. Fuer FF3 keine Vergleichsgroesse, weil
  keine lokale Ausgabe vorliegt.

Weitere Festlegungen vom 30.09.2026:
- Die Gegenpruefung der Zuordnung nach Regel 3 durch Claude entfaellt,
  weil sie die Inhalte der 28 Zitate im Chat voraussetzen wuerde. Fuer
  Kapitel 7: Die Zuordnung nach Regel 3 stammt von einer Person.
- Das Serverprotokoll vom 30.09.2026 bleibt ausserhalb des
  Repositorys. Die belegenden technischen Zeilen stehen mit
  Zeilennummer und SHA-256 der Protokolldatei in
  docs/ollama_protokollauszug.md. Ein Protokoll des Probeaufrufs vom
  29.09.2026 liegt nicht vor. Die in F2 genannten Werte 13 838 MiB,
  28 753 MiB und 32 768 Token stehen gleichlautend im Protokoll vom
  30.09.2026.
- Laut Zugriffsliste des Servers gingen am 30.09.2026 genau zwei
  Anfragen an /v1/responses, die beiden gezaehlten Versuche. Die
  Anfragen an /api/generate um 09:03:52 und 09:05:21 nutzen einen
  Endpunkt, den run_extraction.py nicht verwendet.
- Die Abweichung von F1 d vom Expose ist eine Entscheidung des
  Verfassers. Eine Abstimmung mit dem Betreuer ist nicht vorgesehen.

Herkunft: Vorschlag von Claude im Chat vom 30.09.2026. Auswahl der
sechs Messgroessen, Ebene der Anforderung fuer M2 und Einschraenkung
vom Verfasser bestaetigt; Bedingung (2) von M2 nach B8 aus E6 vom
Verfasser bestaetigt.

Status: festgelegt.
Bezug: FF1, FF2, FF3, Kapitel 4, 6 und 7.

## 2026-10-01 Paket G: Belegbegriff fuer FF4

### 2026-10-01 G1 Belegbegriff fuer die Gap-Analyse

Festgelegt vor jeder Zaehlung in Paket G, damit die Regel nicht nach
dem Ergebnis gewaehlt wird. Bekannt waren nur die Zahlen der Pruefung
aus Paket E (Nachtraege zu E10 vom 27.09. und 28.09.2026). Wie viele
Anforderungen sicherheitsrelevant sind und welchen Typ sie haben, war
nicht gezaehlt.

Anlass: Befund am Code vom 01.10.2026. Die Funktion
derive_evidence_strength in src/extract/validate_output.py berechnet
die Belegstaerke aus der Angabe supports aller Belege einer
Anforderung, auch aus Belegen, die nicht woertlich in der Quelle
stehen. Das beantwortet den zweiten Pruefpunkt aus F3, M2, am Code;
die Zaehlung zeigt, wie viele Anforderungen das betrifft. Nach F3
bleibt die Regel fuer M2 unveraendert. Fuer FF4 hiesse das aber: Eine
Anforderung, deren Systemreaktion nur ein nicht gefundenes Zitat
traegt, gaelte als mit Beleg rekonstruierbar.

Entscheidung:
1. Grundmenge wie bei M2: alle Anforderungen in den Datensaetzen des
   Volllaufs 2026-09-25_full_v2, die die Schemapruefung bestehen.
2. Gefunden ist ein Beleg wie bei M2, Bedingung (1): validate_output.py
   nimmt ihn an (Funktion excerpt_found), oder diagnose_excerpts.py
   ordnet seine Ablehnung einer Ursache der Regel 1 zu (Funktion
   classify). Belege mit einer Ursache der Regel 2 oder 3 gelten als
   nicht gefunden. Alle Faelle der Regel 3 hat der Verfasser der
   Regel 2 zugeordnet (Nachtrag zu E10 vom 28.09.2026, Teil 4).
3. Belegstaerke fuer FF4: berechnet nach B1 bis B3 aus E6 mit derselben
   Funktion derive_evidence_strength, aber nur aus den gefundenen
   Belegen. Ohne gefundenen Beleg lautet sie insufficient.
4. Fuer FF4 belegt ist eine Anforderung, deren Belegstaerke fuer FF4
   direct oder indirect lautet.
5. M2 und alle uebrigen Festlegungen von F3 bleiben unveraendert.

Folge: Jede fuer FF4 belegte Anforderung ist auch nach M2 belegt, aber
nicht umgekehrt. Sie hat mindestens einen gefundenen Beleg, und was die
gefundenen Belege an Pflichtbestandteilen tragen, tragen auch alle
Belege zusammen.

Begruendung:
- Aussagen zur Sicherheit duerfen nicht ueber die Belege hinausgehen.
  Ein Pflichtbestandteil, den nur ein nicht vorhandenes Zitat traegt,
  ist nicht belegt.
- Die Rechenregel bleibt die aus E6. Beschraenkt wird nur ihre Eingabe
  auf gefundene Belege. Eine neue Pruefregel entsteht nicht.
- M2 bleibt so, wie F3 es festgelegt hat. Die Zahlen fuer FF3 aendern
  sich dadurch nicht.

Alternativen:
- Weg A, M2 unveraendert fuer FF4 uebernehmen. Verworfen wegen des
  Anlasses.
- Nur Anforderungen aus Datensaetzen, die validate_output.py annimmt.
  Verworfen: Das Pruefprogramm lehnt ganze Datensaetze ab. Ein falsches
  Zitat wuerde alle Anforderungen eines Pull Requests entfernen, auch
  gut belegte.

Nicht Teil dieser Entscheidung: wie die Stufen direct und indirect den
Kategorien der Gap-Analyse zugeordnet werden. Das legt die Entscheidung
zur Gap-Analyse fest.

Grenze fuer Kapitel 7: Wie in E6 faellt ein echter Ausschnitt mit
falsch angegebenem supports maschinell nicht auf. G1 aendert daran
nichts.

Umsetzung: Zaehlprogramm in Paket G. Es importiert die genannten
Funktionen und enthaelt keine eigenen Pruefregeln.

Herkunft: Befund und Vorschlag von Claude im Chat vom 01.10.2026. Der
Verfasser hat Weg B gewaehlt.

Status: festgelegt.
Bezug: FF4, FF1, Kapitel 4, 6 und 7.

## 2026-10-01 Paket G: Grundzahlen des Volllaufs

### Nachtrag zu F3 (2026-10-01): M2 gezaehlt, beide Pruefpunkte beantwortet

Gezaehlt am 01.10.2026 in Paket G statt in Paket H, mit
src/analyze/count_requirements.py (Commit af23216). Die Regeln von F3
und G1 standen vorher fest und sind unveraendert. Das Programm nutzt
die Pruefungen aus validate_output.py und diagnose_excerpts.py und
enthaelt keine eigenen Pruefregeln. Alle Zahlen stehen in
experiments/requirement_counts_2026-09-25_full_v2.json und werden hier
nicht wiederholt.

1. Erster Pruefpunkt: validate_output.py prueft das Schema zuerst
   (Funktion check_record). Die Zaehlung findet so viele Datensaetze
   mit Schemafehler wie die Ablehnungen "Schema" im Nachtrag zu E10 vom
   28.09.2026, Teil 4. Teil b von M1 im Volllauf ist damit bestaetigt.
2. Zweiter Pruefpunkt: derive_evidence_strength zaehlt auch nicht
   gefundene Belege mit (Befund am Code, siehe G1). Die Regel fuer M2
   bleibt. Wie viele Anforderungen das betrifft, zeigt der Wert
   strength_changed_by_g1 in der Ergebnisdatei.
3. Abgleich mit Paket E: Zahl der Zitate, Zahl der abgelehnten Zitate
   und ihre Verteilung auf die Regeln 1 bis 3 stimmen mit dem Nachtrag
   zu E10 vom 27.09.2026, Teil 2, ueberein. Die im Chat vorab genannte
   Erwartung fuer stated_differs_from_all_evidence ist eingetroffen.
4. Offen fuer Paket H: Angabe (i) aus M2, also bei wie vielen
   unbelegten Anforderungen das Modell selbst insufficient angab. Das
   Programm zaehlt sie noch nicht.

Herkunft: Lauf und Ablesung durch den Verfasser, Programm und
Einordnung von Claude im Chat vom 01.10.2026.

Status: festgelegt.
Bezug: FF1, FF3, FF4, Kapitel 6.

## 2026-10-02 Paket G: Kategorien der Gap-Analyse

### 2026-10-02 G3 Kategorie "nachweislich fehlende Sicherheitsfunktion" gestrichen

Pflichtentscheidung nach der Projektanweisung (Methodik Punkt 7),
Schritt 3 des Arbeitsplans von Paket G. Festgelegt vor jeder
Zuordnung rekonstruierter Anforderungen zum Raster.

Entscheidung: Die Gap-Analyse verwendet die vier Kategorien der
Projektanweisung: (1) Sicherheitsanforderung mit Beleg in der
untersuchten Historie rekonstruierbar; (2) Hinweise auf eine
Umsetzung oder ein sicherheitsbezogenes Verhalten, aber keine
explizite Anforderung; (3) anhand der untersuchten Historie nicht
entscheidbar; (4) fuer Qrisp oder den Untersuchungsrahmen nicht
relevant. Die Kategorie "nachweislich fehlende Sicherheitsfunktion"
wird gestrichen.

Begruendung:
1. Die Projektanweisung erlaubt die Kategorie nur, wenn eine
   zusaetzliche Code-, Test- oder Systempruefung im
   Untersuchungsumfang eindeutige Belege liefert. Der Arbeitsplan von
   Paket G enthaelt keine solche Pruefung, und bis zur Abgabe ist
   keine vorgesehen.
2. Es fehlt ein Massstab. Nach CC:2022 Teil 3 Abschn. 3.28 ist eine
   Schwachstelle eine Schwaeche, mit der sich die
   Sicherheitsfunktionen (SFR) verletzen lassen. Sicherheitsfunktionen
   dienen Sicherheitszielen aus einem Schutzprofil oder einer
   Sicherheitsvorgabe (Teil 2, Einleitung). Qrisp hat kein solches
   Dokument. Ob eine Funktion "fehlt", laesst sich ohne festgelegte
   Ziele nicht entscheiden (Einordnung von Claude).
3. TR-03185 Abschn. 2.2.3 bestimmt keine Rolle, die ein
   Open-Source-Projekt konform machen muss, und nennt mehrere
   moegliche Umsetzende. Ein fehlender Eintrag in der Historie ist
   damit kein Versaeumnis einer bestimmten Stelle.
4. Abgrenzung der Arbeit: keine Zertifizierung, und keine Aussage, dass
   Qrisp eine Sicherheitsanforderung nicht erfuellt, wenn nur kein
   Beleg gefunden wurde.

Schreibauftrag (Wunsch des Verfassers vom 02.10.2026): Abschnitt 4.2
und Kapitel 7 erklaeren ausfuehrlich, warum die Kategorie fuer Qrisp
nicht tragfaehig ist (Punkte 1 bis 4). Dazu beschreibt die Arbeit aus
den Quellen, was eine Software fuer eine Sicherheitspruefung mindestens
braucht. Fundstellen, von Claude am 02.10.2026 gelesen, vom Verfasser
noch nicht:
a) CC:2022 Teil 3 Abschn. 7.4.2 (APE_SPD.1): Sicherheitsproblem-
   definition mit Bedrohungen (Angreifer, Schutzgut, schaedliche
   Handlung), organisatorischen Sicherheitsregeln und Annahmen ueber
   die Einsatzumgebung. Die Entsprechung fuer die Sicherheitsvorgabe,
   ASE_SPD.1 in Abschn. 9.4.2, ist am Text noch zu pruefen.
b) Teil 3 Abschn. 7.5 (APE_OBJ): Sicherheitsziele, die das Problem
   abdecken und zwischen Produkt und Einsatzumgebung aufteilen.
c) Teil 3 Abschn. 7.7 (APE_REQ): Sicherheitsfunktionen und
   Anforderungen an die Vertrauenswuerdigkeit als klare, eindeutige
   Beschreibung.
d) Teil 3 Abschn. 7.2.2 (APE_INT.1): Beschreibung des
   Evaluationsgegenstands mit Typ und Fremdbestandteilen.
e) Teil 3 Abschn. 5.3.4 und 5.3.5: Vertrauen entsteht durch Evaluation
   des Produkts; Liste der Pruefverfahren, etwa Tests,
   Schwachstellenanalyse und Penetrationstests.
f) Teil 3 Abschn. 12.1: Nachweise entstehen regelmaessig waehrend
   Entwicklung, Herstellung, Auslieferung und Wartung.
g) TR-03185 Abschn. 2.3: die 20 Mindestanforderungen an ein
   Open-Source-Projekt (SR10 bis SR29 im Entwurf G2).
h) Zum Vergleich TR-03185 Teil 1, Tabelle 14, PROD.PM.A.2: Bei
   proprietaerer Software muessen alle Anforderungen an die
   Informationssicherheit zu Projektbeginn erfasst und dokumentiert
   sein; Abschn. 1.2.1 setzt voraus, dass sie vorliegen. Fuer Qrisp
   liegt kein solches Dokument vor; das ist der Anlass von FF4.
i) 29148 Abschn. 9.6.18 c als Inhaltsblock einer Spezifikation
   (Abschnitt 2.1.7 der Arbeit).

Folge: Die Tabellen der Gap-Analyse haben vier Kategorien. Kapitel 7
nennt die Streichung als Grenze: Die Arbeit kann Dokumentationsluecken
zeigen, aber keine fehlenden Funktionen.

Herkunft: Vorschlag von Claude im Chat vom 02.10.2026. Der Verfasser
hat das Streichen gewaehlt und den Schreibauftrag erteilt.

Status: festgelegt.
Bezug: FF4, Kapitel 2, 4 und 7.

## Offene Entscheidungen

- Anforderungsformat (FF2), Paket C: entschieden am 08.09.2026, siehe C5
- API-Modell und lokales Modell (FF3), Paket E und F: entschieden
  am 19.09.2026 und 29.09.2026, siehe E8 und F2
- Messgroessen fuer FF3, Paket F: entschieden am 30.09.2026, siehe F3
- Ausschnitt des Sicherheitsrasters (FF4), Paket G: Option C
  gewaehlt am 02.10.2026, Entwurf G2 in STATUS.md, Freigabe offen
- Kategorie "nachweislich fehlende Sicherheitsfunktion" (FF4), Paket
  G: entschieden am 02.10.2026, siehe G3
- Auswahlregel fuer die Modelleingabe (FF1), Paket E: entschieden
  am 15.09.2026, siehe E4
- Budget der Modelleingabe (FF1), Paket E: entschieden am
  15.09.2026, siehe E5
- Regeln der Belegstaerke (FF1), Paket E: entschieden am
  15.09.2026, siehe E6
- Umfang gegenueber dem Qrisp-Team: Was gehoert zur Arbeit, was ist
  Weiterentwicklung? Mit Professor zu klaeren.

