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

## Offene Entscheidungen

- Anforderungsformat (FF2), Paket C
- API-Modell und lokales Modell (FF3), Paket E und F
- Ausschnitt des Sicherheitsrasters (FF4), Paket G
- Umfang gegenueber dem Qrisp-Team: Was gehoert zur Arbeit, was ist
  Weiterentwicklung? Mit Professor zu klaeren.

