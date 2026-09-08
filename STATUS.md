# Bearbeitungsstand

Letzte Aktualisierung: 08.09.2026
Abgabetermin: 01.11.2026 (Sonntag; intern geplant auf Fr 30.10.2026)

## Zusammenarbeit im Chat

Diese Regeln gelten fuer jeden Chat und gehen Annahmen vor.

- Projektwissen enthaelt ausschliesslich Unveraenderliches:
  exposee.tex und 29148-2018.pdf. Arbeitsdateien werden pro Chat
  hochgeladen, nie im Projektwissen abgelegt - dort veralten sie
  unbemerkt.
- Wenn Claude den Inhalt einer Datei braucht, muss er sie ausdruecklich
  anfordern und dabei den vollstaendigen Pfad nennen. Claude arbeitet
  nie mit einer aus dem Gedaechtnis rekonstruierten Fassung. Bewaehrt:
  in Paket D Teil 3 hat Claude von sich aus gemeldet, dass ihm zwei
  Dateien nicht mehr vorliegen, statt sie nachzubauen.
- Commit-Nachrichten werden erst nach dem git diff formuliert, nie
  vorab. In Paket D Teil 3 hat eine vorformulierte Nachricht eine
  Aenderung behauptet, die der Commit nicht enthielt (1d83472).
- Stopp-Punkte in Anleitungen sind verbindlich. Sie stehen dort, wo
  etwas unwiederbringlich ueberschrieben werden kann.
- Claude testet groessere Skripte vor der Uebergabe in seiner eigenen
  Umgebung mit erfundenen Testdaten und sagt das dazu. Bewaehrt: hat in
  Paket D Teil 2 jeden Fehler vor dem echten Lauf gefunden.
- Ab Paket D Teil 3: Claude prueft eine Testsuite zusaetzlich gegen
  absichtlich eingebrachte Fehler und zeigt, welche Tests dabei
  anschlagen. Nur so ist belegt, dass ein bestandener Test etwas misst.
- Es gelten unveraendert der Zweckbindungs-Block und die technische
  Schritt-fuer-Schritt-Regel der Projektanweisung. Keine Kurzfassung.
- Eine Messung, die die Arbeit selbst ausmacht, trifft der Verfasser.
  Das Modell darf erklaeren, gegenpruefen und formulieren. Wer eine
  Bewertung ausgefuellt hat, gehoert ins Protokoll.
- Claude darf Pull-Request-Seiten selbst oeffnen, um Bewertungen
  gegenzupruefen. Es sagt dann ausdruecklich, welche Seiten es
  geoeffnet hat und welche nicht.
- Soll eine Zeile hinzukommen, sagt Claude ausdruecklich "anhaengen,
  nichts ersetzen", und nennt die Zeile darueber als Anker. In Paket C
  Schritt 4b hat eine Ersetzungsanweisung zweimal eine Tabellenzeile
  geloescht (02.09.2026).
- Kommt ein Wortlaut in einer Datei mehrfach vor, warnt Claude vorher
  und nennt die gemeinte Stelle mit Zeilennummer. In Paket C Schritt 4b
  blieb "Zuletzt geaendert" an der zweiten Stelle stehen.
- Ein Pruefbefehl darf nicht nach Formulierungen suchen, die auch im
  neuen Text vorkommen. Sonst meldet er neu geschriebenen Text als
  Rest.

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS 26.5.2 (25F84) - Python 3.14.6 (Homebrew) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)
Pakete laut requirements.txt: requests 2.34.2, pytest 9.1.1 sowie
certifi, charset-normalizer, idna, iniconfig, packaging, pluggy,
Pygments, urllib3

## Repository-Struktur

config/ · data/{raw,interim,processed,manifests} · docs/ ·
eval/{instrument,sample,responses} · experiments/ ·
literatur/{notizen,volltexte,pdf} · prompts/ ·
src/{collect,prepare,extract,classify,analyze} · tests/ · thesis/

src/ enthaelt eine README.md, die alle Unterordner beschreibt. Die
Unterordner selbst haben keine README.md - bewusst so entschieden.
tests/ hat eine eigene README.md, die die Testbereiche und die
bewusst offenen Luecken benennt.

Per .gitignore ausgeschlossen: .env, config/config.yaml, *.key, *.token,
data/raw/, data/interim/, eval/responses/, docs/pseudonyme.csv,
models/, literatur/pdf/, literatur/volltexte/, .venv/, __pycache__/,
LaTeX-Hilfsdateien in thesis/, .DS_Store, .vscode/, .idea/
Nicht ausgeschlossen und damit versioniert: data/manifests/
Geprueft am 21.08.2026: __pycache__/ und .pytest_cache/ erscheinen
nicht in git status.

## Abgeschlossen

Arbeitspaket A (Setup) vollstaendig:
- Repository, .gitignore, README.md, STATUS.md, Ordnerstruktur
- SSH-Schluessel (Fingerabdruck gegen GitHub-Doku geprueft)
- Virtuelle Umgebung .venv, requests 2.34.2, requirements.txt
- GitHub-Token qrisp-thesis-readonly (fein granuliert, nur oeffentliche
  Repositories, im Passwortmanager)

Arbeitspaket B (Literatur und Grundlagen) inhaltlich abgeschlossen:
- literatur/suchprotokoll.md und literaturmatrix.md fortgeschrieben
  (16 Quellen erfasst, davon 7 gelesen und eingearbeitet:
  L05, L06, L07, L11, L14, L15, L16)
- Sechs Lesenotizen unter literatur/notizen/
- LaTeX-Vorlage nach thesis/ uebernommen, kompiliert fehlerfrei
- Abschnitte 2.1, 2.2.1, 2.2.2, 2.2.3 ausformuliert

Arbeitspaket D, Teil 1 (Pilotabruf) abgeschlossen:
- .env mit GITHUB_TOKEN, config/collect.toml
- src/collect/: github_api.py, api_test.py, explore_fields.py,
  compare_objects.py, fetch_pull_list.py
- Erhebung 12.08.2026: 476 Pull Requests

Arbeitspaket D, Teil 2 - alle vier Abrufe abgeschlossen:
- src/collect/fetch_pull_details.py, fetch_pull_comments.py,
  fetch_pull_files.py, analyze_pull_details.py, analyze_pull_files.py
- github_api.py um sha256_of, current_commit, read_jsonl, append_jsonl,
  retry_delay_seconds, request_with_retry, fetch_paginated ergaenzt.
  fetch_pull_list.py importiert die ersten beiden von dort.
- config/collect.toml um pause_seconds = 0.2 und max_retries = 5
  ergaenzt
- docs/findings_pull_details.md und findings_pull_files.md erzeugt
- Entscheidungen D1 bis D4 in docs/entscheidungen.md festgeschrieben

Arbeitspaket D, Teil 3 (Aufbereitung und Tests) abgeschlossen:
- config/collect.toml um den Abschnitt [prepare] ergaenzt
- src/prepare/build_interim.py: fuehrt die vier Rohdateien zu einem
  Datensatz je Pull Request zusammen, reduziert die Felder,
  normalisiert Zeilenenden, entfernt Vorlagenkommentare und setzt die
  drei Kuerzungsstufen aus D1 um
- Lauf vom 19.08.2026 ueber alle 476 Pull Requests, Manifest versioniert
- tests/: conftest.py und fuenf Testdateien mit 38 Tests, alle bestanden
- tests/README.md neu gefasst
- Entscheidungen D5 bis D8 in docs/entscheidungen.md
- docs/ki-protokoll.md fuer Teil 2 und Teil 3 nachgetragen

Arbeitspaket C (Formatauswahl), Schritte 1 bis 3 sowie 4a und 4b
erledigt (4a = Gegenpruefung und Auswertung Teil A, 4b = Messung
fuer K6):
- Vorentscheidungen C1 bis C4 in docs/entscheidungen.md
- docs/formatauswahl.md: zehn Kriterien K1 bis K10, dreistufige ordinale Skala, zehn Bewertungsregeln R1 bis R10
  (R9 und R10 ergaenzt am 30.08.2026),
  Entscheidungsverfahren ueber Rollen je Ebene, Schwellen fuer K6/K9
- Abschnitt 2.1.7 in thesis/thesis.tex zu ISO/IEC/IEEE 29148 Abschn.
  9.6, mit Tabelle 2.1 zu den Inhaltsbloecken
- src/analyze/draw_sample.py und docs/sample_formulation_probe.md:
  zwoelf Pull Requests geschichtet und reproduzierbar gezogen
- docs/formatprobe_protokoll.md ausgefuellt (Arbeitsentwurf)
- Regeln R9 (pauschale Rollenangabe) und R10 (Bezugspunkt der
  Modalitaet) am 30.08.2026 ergaenzt, vor der Gegenpruefung
- Schwellen aus Abschnitt 6 auf zwoelf Faelle umgerechnet:
  Note 2 ab 10, Note 1 ab 5, sonst Note 0
- Alle zwoelf Faelle der Formulierungsprobe unabhaengig
  gegengeprueft. Fuenf Aenderungen, alle bei Ebene (c):
  PR 371 (27.08.), PR 408, 533, 577, 622 (30.08.)
- Auswertung Teil A abgeschlossen
- Schritt 4b: K6 fuer die Ebenen (c) und (d) als nicht anwendbar
  festgelegt (31.08.2026); Rahmen und drei Referenzinhalte aus 29148
  Abschn. 9.6.12 a, 9.6.14 und 9.6.18 c 5 festgelegt (02.09.2026),
  jeweils vor der Messung
- Teil B des Protokolls neu gefasst: sechs Formulierungsversuche,
  alle gelungen. K6: Ebene (a) 3 von 3 (Note 2), Ebene (b) 3 von 3
  (Note 2), Ebenen (c) und (d) n. a.
- docs/ki-protokoll.md um die Zeilen fuer den 30.08.2026 und den
  02.-03.09.2026 ergaenzt

## Datensaetze (alle lokal, nicht im Repository)

data/raw/pulls_2026-08-12.jsonl - 476 PRs
  SHA-256 88a6652c1de9c2f2a1d2e60dbe9bef7291c8e1f3fada14418f4bf5bc387bead1
data/raw/pull_details_2026-08-14.jsonl - 476 Detailobjekte
  SHA-256 19bc97ad11d3e097e873eb72cc84df283d20c9fffb61d8a1f7013151dfa03bd9
data/raw/issue_comments_2026-08-19.jsonl - 639 Kommentare
  SHA-256 7d9918c628bd51bc2c9245fcbc2a678c20ec963c3d92481809fbdd724c760459
data/raw/review_comments_2026-08-19.jsonl - 1713 Kommentare
  SHA-256 d1c0dd08487402bf6020c2fd43b0243903c010d761c75e98cda8a86c7c12c7a4
data/raw/pull_files_2026-08-19.jsonl - 8424 Dateisaetze
  SHA-256 7315f5254a914278618c85c23422d7f2a04d1460ee8d8c6c6733f4e91533bbdc
data/interim/pulls_prepared_2026-08-19.jsonl - 476 aufbereitete PRs, 20 MB
  SHA-256 138e60ce47c1e6508d14ea6cec113c11e72772407fef2232870e2b1b981a4683

Dazu je eine .progress.jsonl fuer Kommentare und Dateien, ebenfalls
lokal. Alle Manifeste unter data/manifests/ sind versioniert:
manifest_pulls_2026-08-12.json, manifest_pull_details_2026-08-14.json,
manifest_issue_comments_2026-08-19.json,
manifest_review_comments_2026-08-19.json,
manifest_pull_files_2026-08-19.json,
manifest_prepared_2026-08-19.json

## Belegte Fakten aus Paket D (Stand 19.08.2026)

Erhebung
- Token: Kontingent 5000/Stunde, Ablauf 2027-05-31.
- Repository eclipse-qrisp/Qrisp, oeffentlich, ID 632066325.
- 476 Pull Requests, Nummern 5 bis 797, keine Duplikate. Die Luecken
  entstehen durch den gemeinsamen Zaehler von Issues und Pull Requests.
  Jede Verarbeitung muss die Nummern aus der Datei lesen.
- Listenendpunkt 36 Felder, Detailendpunkt 48.
- state kennt nur open und closed; merged_at unterscheidet
  zusammengefuehrt von verworfen.

Struktur des Korpus
- outcome: merged 314 (66,0 %), closed_unmerged 109 (22,9 %),
  open 53 (11,1 %).
- 61 Autoren; die drei aktivsten schrieben 236 der 476 PRs (49,6 %),
  die zehn aktivsten rund 79 Prozent.
- Bots: 31 PRs (6,5 %), dependabot[bot] 28 und Copilot 3. Copilot endet
  nicht auf "[bot]" und wird nur ueber user.type erkannt.
- 222 PRs (46,6 %) ohne jeden Kommentar; nur 113 (23,7 %) mit
  Review-Kommentaren.
- 56 PRs (11,8 %) ohne Beschreibungstext.
- Vorlagentext "<!--" in 124 von 420 Beschreibungen (29,5 %),
  CRLF-Zeilenenden in 259 (61,7 %).
- labels nur bei 36 PRs (7,6 %) - keine Klassifikationsgrundlage.
- locked konstant False. draft 66-mal True (13,9 %).
- author_association nur CONTRIBUTOR (435) und NONE (41).
- Durchgehend leer: requested_teams, auto_merge, active_lock_reason.
- Fuenf PRs ohne jede Codeaenderung: 169, 332, 407, 408, 578.

Groessen
- additions + deletions je PR: Median 162, p90 2424, p99 18474,
  Maximum 30166, Summe 583821.
- 8424 Dateisaetze, 32557763 Zeichen Aenderungstext, entspricht bei rund
  3,5 Zeichen je Token grob 9 Millionen Token.
- Zeichen je Datei: Median 1397, p90 9534, Maximum 99478.
- Zeichen je PR: Median 9627, p90 112459, Maximum 2761999.
- .py haelt 81,0 Prozent des Aenderungstextes; src und tests zusammen
  80,7 Prozent. Die groessten PRs sind handgeschriebener Python-Code.
- GitHub liefert bei 331 von 8424 Dateien (3,9 %) kein patch-Feld.

Abweichungen
- PR 639: erwartet 1, geholt 4 allgemeine Kommentare. Geklaert, drei
  Kommentare vom 18.08.
- PR 470: erwartet 7, geholt 14 Dateien. Geklaert, updated_at von
  13.06. auf 17.08. gewandert, Commits 16 -> 22.
- PR 331, 344, 767: je ein Review-Kommentar weniger als gezaehlt. Nicht
  aufloesbar, reproduzierbar. 3 von 1716, 0,17 Prozent.
- Alle fuenf Abweichungen erscheinen unveraendert im Manifest der
  Aufbereitung. Keine neue Abweichung.

## Belegte Fakten aus der Aufbereitung (Lauf 19.08.2026)

Quelle: manifest_prepared_2026-08-19.json, erzeugt von
src/prepare/build_interim.py.

Vollstaendigkeit
- 476 Pull Requests, 639 allgemeine und 1713 Review-Kommentare, 8424
  Dateien uebernommen. Kein Datensatz verloren.
- 31 Bot-Beitraege enthalten und markiert (D7).
- 5 Pull Requests ohne Codeaenderung, 222 ohne Kommentar, 56 ohne
  Beschreibung - alle enthalten und markiert (D6).

Reinigung
- Zeilenenden bei 259 Beschreibungen vereinheitlicht.
- Vorlagentext bei 124 Beschreibungen entfernt.
- 0 Beschreibungen wurden durch die Reinigung leer. Die Zahl 56 bleibt
  unveraendert. Widerlegt die Vorabvermutung, sie koenne steigen.
- 0 unabgeschlossene Kommentarmarker im gesamten Korpus.
- Zeichenzahl 32555716 statt 32557763 im Rohabruf. Die Differenz von
  2047 Zeichen entfaellt auf CRLF-Zeilenenden, die zu LF werden. Kein
  Inhaltsverlust.

Wirkung der Kuerzung nach D1
- Stufe 1: 497 Dateien ohne Patch-Text (Dateityp oder kein patch-Feld).
- Stufe 2: 258 Dateien auf 10000 Zeichen gekuerzt.
- Stufe 3: 61 Dateien gekuerzt, 4580 Dateien ohne Patch-Text wegen
  erschoepftem Budget. Das sind 54,4 Prozent aller Dateien.
- 32555716 Zeichen werden zu 7396580, also 22,7 Prozent. Bei rund
  3,5 Zeichen je Token grob 2,1 statt 9,3 Millionen Token.
- 183 von 476 Pull Requests (38,4 %) sind irgendwie gekuerzt.
- Ergebnisdatei 476 Zeilen, 20 MB.

Diese Wirkung ist die groesste Einzelentscheidung der Datenaufbereitung
und gehoert nach Kapitel 5 und Kapitel 7. Der Budgetwert steht in
config/collect.toml und ist in Paket E ohne Codeaenderung anpassbar;
der Lauf ist dann zu wiederholen.

## Struktur eines aufbereiteten Datensatzes

Eine Zeile je Pull Request. Felder:
number, title, body, has_body, body_had_crlf, body_had_template,
body_template_unterminated, state, outcome, draft, author,
author_is_bot, author_association, created_at, updated_at, closed_at,
merged_at, html_url, labels, base_ref, base_sha, head_sha,
counts_api, counts_dataset, has_code_changes, has_patch_text,
truncation, issue_comments, review_comments, files

- counts_api enthaelt die Zaehlfelder von GitHub, counts_dataset die
  tatsaechlich vorliegenden Anzahlen. Beide bleiben getrennt, damit die
  bekannten Abweichungen sichtbar bleiben.
- truncation zaehlt je Pull Request: stage1_dropped, stage2_truncated,
  stage3_truncated, stage3_dropped, chars_original, chars_kept.
- Je Datei: filename, status, additions, deletions, changes, patch,
  patch_kept, patch_drop_reason, patch_truncated, patch_chars_original,
  patch_chars_kept. Gruende: no_patch_from_api, excluded_file_type,
  pull_budget_exhausted.
- Je Review-Kommentar zusaetzlich: path, line, side, commit_id,
  review_id, diff_hunk. Der diff_hunk gibt die Codezeilen, auf die sich
  der Kommentar bezieht - wertvoll fuer die Rueckverfolgbarkeit.
- Kommentare sind nach created_at sortiert, Dateien in der
  Lieferreihenfolge der API.

## Testsuite

38 Tests, ausfuehren aus der Projektwurzel:
python -m pytest tests/ -v
Zuletzt gruen am 21.08.2026 unter Python 3.14.6.

tests/conftest.py setzt den Importpfad auf src/collect und src/prepare.
Ohne diese Datei finden die Tests die Module nicht.

Bereiche: test_resume.py (Wiederaufnahme), test_outcome.py,
test_normalisation.py, test_jsonl_io.py, test_truncation.py.
Nicht abgedeckt: Netzschicht in github_api.py, Auswertungsskripte,
Schemavalidierung der LLM-Ausgaben (Paket E).

## Ungepruefte Beobachtungen

- Ob die 321 Nummernluecken alle Issues sind: plausibel, nicht gemessen.
- Zu PR 344: vermutet ein Review im Zustand pending, nur seinem
  Verfasser sichtbar. Nicht pruefbar.
- PR 674 und 676 sind fast gleich gross (574/575 Dateien) - vermutlich
  zwei Anlaeufe derselben Umbauaktion. Nicht geprueft.
- Warum author_association nie OWNER oder MEMBER annimmt: unbekannt.
- Ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben enthalten:
  Vermutung aus D7, nicht gemessen. Relevant fuer FF4.
- Ob 50000 Zeichen je Pull Request ausreichen: haengt vom Modell ab,
  Entscheidung in Paket E.
- PR 408 hat auf GitHub einen Commit, gilt im Datensatz aber als
  Pull Request ohne Codeaenderung. Der Head-Branch wurde geloescht.
  Ob das zusammenhaengt: ungeprueft. Falls ja, betrifft es die
  Vollstaendigkeit der Erhebung und gehoert nach Kapitel 7.
- Im Diff von PR 533 stehen Soll-Saetze, die Inhalt der neuen
  Dokumentation sind (etwa: jede oeffentliche Funktionalitaet
  sollte durch mindestens einen Test abgedeckt sein). Sie wurden
  nicht als Fundstelle gewertet. Fuer Paket E interessant: Solche
  Saetze sind selbst rekonstruierbare Anforderungen.

## Aktuell

Paket C, Schritt 4c abgeschlossen am 08.09.2026. Die
Entscheidungsmatrix in docs/formatauswahl.md Abschnitt 10 ist
vollstaendig: alle zehn Kriterien sind je Ebene vergeben, jede Zelle
mit Belegstelle, Begruendung und Gegenargument. Damit ist E2
anwendbar. Offen sind die Schritte 5 und 6.

Seit dem 07.09.2026 gilt zusaetzlich R11: Die Skalenstufe 2 bemisst
sich am Vorhandensein und an der Reichweite einer ausdruecklichen
Regel, nicht an einem empirischen Wirksamkeitsnachweis. Berichtete
Restprobleme einer Erprobung fuehren fuer sich genommen nicht zu
Note 1. Alle vier K1-Noten wurden daraufhin geprueft, keine aendert
sich.

Ebenfalls seit dem 07.09.2026: ISO/IEC/IEEE 29148 Abschn. 5.2.4 ist
auf drei Ebenen aufgeteilt. Aufbausatz und Figure 1 gehoeren zu
Ebene (b), die Schluesselwoerter zu Ebene (c), die sprachlichen
Vorgaben zu Ebene (d). Ebene (c) wird ausschliesslich an den
Schluesselwoertern gemessen. Ebene (b) stuetzt sich damit auf zwei
Quellen; bewertet wird EARS als die spezifischere. Die
Pflichtbestandteile aendern sich nicht, die K9-Messung bleibt
gueltig.

Verfahren seit 04.09.2026 (C2a): Das Modell legt je Zelle die
Belegstelle, einen Notenvorschlag und das Gegenargument vor. Der
Verfasser liest die Belegstelle in der Quelle nach und vergibt die
Note. Vorgegangen wird kriterienweise ueber alle vier Ebenen.

Volltexte, die dem Modell am 04.09.2026 vorlagen und die es selbst
gelesen hat: Mavin 2009, Mavin/Wilkinson 2010, Wilkinson/Mavin 2018,
Lucassen 2016, RFC 2119, RFC 8174, ISO/IEC/IEEE 29148 Abschn. 5.2.4
bis 5.2.7.

Am 07. und 08.09.2026 lagen die Volltexte von RFC 2119 und RFC 8174
nicht vor. Die Vorschlaege zu Ebene (c) in den Runden K2 bis K5, K7,
K8 und K10 stuetzen sich insoweit auf
literatur/notizen/bradner_1997_rfc2119.md. Das ist in
docs/formatauswahl.md Abschnitt 10 in jedem Block vermerkt. Wer die
Zellen der Ebene (c) gegenpruefen will, sollte die beiden
RFC-Volltexte beilegen.

Messergebnis K9, Stand 30.08.2026:
- Ebene (a) User Story: 4 von 12 gedeckt (33,3 %), Note 0.
  Zwei davon stuetzen sich auf eine pauschale Rolle (PR 371, 622).
  Ohne diese: 2 von 12 (16,7 %), Note bleibt 0.
- Ebene (b) EARS: 9 von 12 gedeckt (75,0 %), Note 1.
- Ebene (c) Modalitaet: 0 von 12 gedeckt, Note 0.
- Ebene (d) Qualitaetsregeln: K9 nicht anwendbar.

Die Noten von (a) und (b) haengen an je einem einzigen Fall. Die
Note von (c) nicht: dafuer fehlen fuenf Faelle.

Messergebnis K6, Stand 02.09.2026:
- Ebene (a) User Story: 3 von 3 gelungen, Note 2.
- Ebene (b) EARS: 3 von 3 gelungen, Note 2.
- Ebenen (c) und (d): K6 nicht anwendbar.
- K6 unterscheidet die Ebenen (a) und (b) nicht. Beide beziehen je
  einen Pflichtbestandteil aus dem Rahmen: (a) die Rolle, (b) den
  Systemnamen. Wuerde die Rahmenrolle nicht anerkannt, faellt (a)
  auf 0 von 3. Beides gehoert nach Kapitel 7.

Naechste Schritte in dieser Reihenfolge:
1. Schritt 5: Rollenzuweisung je Ebene und Formatentscheidung, als
   C5 in docs/entscheidungen.md. Dabei den Konflikt shall gegen
   must entscheiden. Nach E1 duerfen die Ebenen (a) und (c) nicht
   "verpflichtend" werden, weil beide bei K9 die Note 0 haben.
   Ebene (d) ist nicht betroffen: K9 ist dort n. a., und nach R3
   wird n. a. nie wie 0 behandelt. Fuer "verpflichtend" bleiben
   damit nur die Ebenen (b) und (d).
2. Schritt 6: Abschnitt zur Formatauswahl in thesis/thesis.tex,
   Kapitel 4. Dabei Z. 127-132 ersetzen und den Platzhalter zum
   Verweis auf die Entscheidungsmatrix fuellen.
Danach Paket E.

## Getroffene Entscheidungen

Vollstaendig in docs/entscheidungen.md. Kurzfassung:

- Repository privat. Nach Abgabe umstellbar.
- R11 (07.09.2026): Skalenstufe 2 bemisst sich am Vorhandensein und
  an der Reichweite einer Regel, nicht an einem Wirksamkeitsnachweis.
- Zuordnung von 29148 Abschn. 5.2.4 auf drei Ebenen (07.09.2026);
  Ebene (c) wird nur an den Schluesselwoertern gemessen.
- D4a (07.09.2026): keine automatischen Tests fuer draw_sample.py.
  Stattdessen Wiederholungslauf am 08.09.2026, Ergebnis identisch.
- Evaluation nach Exposé-Variante, ergaenzt um Selbstbewertung.
  Werkzeug bis Ende Woche 8 bewertbar, Git-Tag thesis-v1.0.
- FF3: API-Modell von OpenAI oder Anthropic. Dasselbe Modell als
  Werkzeug und Evaluationsgegenstand ist eine Bedrohung der
  Konstruktvaliditaet und muss dokumentiert werden.
- Kapitel nicht in Einzeldateien. Alles in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard.
- API-Version 2022-11-28, explizit, in config/collect.toml.
- Speicherformat JSONL. Keine Datensaetze im Repository, Nachweis ueber
  SHA-256 im Manifest.
- Datenminimierung: vom user-Objekt nur login. Pseudonyme A01 ff. in
  der Arbeit, Zuordnung in docs/pseudonyme.csv, lokal.
- D1 dreistufige Kuerzung, erst in der Aufbereitung:
  Stufe 1 Typausschluss .ipynb, .drawio, .bkp, .svg und Dateien ohne
  patch-Feld; Dateiname, status, additions, deletions bleiben.
  Stufe 2 hoechstens 10000 Zeichen je Datei.
  Stufe 3 Budget 50000 Zeichen je Pull Request, unter Vorbehalt Paket E.
  Alle Werte in die Konfiguration, jede Kuerzung wird markiert.
  Ergaenzung 21.08.: Das Budget wird in der Lieferreihenfolge der API
  verbraucht. Die Schwaeche dieser Regel steht in Kapitel 7.
- D2 Bots markieren (author_is_bot), nicht loeschen. Regel: user.type
  gleich "Bot" ODER Login endet auf "[bot]".
- D3 eine Rohdatei je Endpunkt, Zusammenfuehrung erst in data/interim/.
  Jedes Manifest traegt source_dataset mit Pruefsumme.
- D4 pytest, Tests dort, wo ein Fehler still Daten verfaelscht:
  Wiederaufnahme, outcome, Normalisierung, JSONL-Ein- und Ausgabe.
  Kein Nachbau der API.
- D5 ein Datensatz je Pull Request, Kommentare und Dateien eingebettet.
- D6 Pull Requests ohne Beschreibung und ohne Codeaenderung bleiben
  enthalten und werden markiert. Reinigung entfernt nur vollstaendige
  Kommentarbloecke und wird nie auf Patch-Text angewandt.
- D7 praezisiert D2: Bots bleiben in data/interim/. Der Ausschluss
  erfolgt erst bei der Erzeugung der Modelleingabe, weil
  Dependabot-Beitraege fuer FF4 einschlaegig sein koennten.
- D8 ergaenzt D4 um einen fuenften Testbereich: die Kuerzungsstufen.
- Sprache: Programme unter src/ geben Meldungen und Berichte auf
  Englisch aus, einschliesslich der Berichtsdateinamen. docs/ und
  literatur/ bleiben deutsch.
- C1 Rekonstruierte Anforderungen werden auf Englisch formuliert. Die
  Arbeit bleibt deutsch. Damit entfaellt die deutsche
  Modalitaetskonvention.
- C2 Die Entscheidungsmatrix stuetzt sich auf Literatur plus eine
  Formulierungsprobe von Hand an zwoelf echten Pull Requests. Kein
  Sprachmodell trifft die Bewertung.
- C2a (04.09.2026) praezisiert C2: Bei den Literaturnoten darf das
  Modell Belegstellen und Notenvorschlaege liefern. Die Note vergibt
  der Verfasser nach Pruefung an der Quelle. An der Formulierungsprobe
  bleibt kein Sprachmodell beteiligt. Die Praezisierung gilt nur fuer
  Paket C; sonst gilt der Abschnitt "Zusammenarbeit im Chat".
- C3 Faellt die Wahl auf eine Kombination mehrerer Ebenen, gilt sie als
  ein festgelegtes Zielformat und wird vollstaendig spezifiziert.
- C4 Zehn Kriterien K1 bis K10, dreistufige ordinale Skala mit n. a.
  und ?, keine Gesamtsumme und keine Gewichte. Entscheidung ueber
  Rollen je Ebene mit Ausschlussregel E1.
- Quelltext und Arbeitsunterlagen werden mit abgegeben. docs/ und
  literatur/ muessen daher ohne Kenntnis der Projektanweisung
  verstaendlich sein.
- Erst Quelltext committen, dann abrufen oder aufbereiten.

## LaTeX-Konventionen

Zitierschluessel in thesis.bib: iso29148, mavin2009ears, mavin2010bigears,
wilkinson2018mitigation, lucassen2016qus.
Zitierschluessel in online.bib: rfc2119, rfc8174.

Labels in thesis.tex (Stand 10.08.2026, vollstaendig):
cha:einleitung · cha:grundlagen · cha:verwandte-arbeiten · cha:konzeption ·
cha:implementierung · cha:evaluation · cha:diskussion · cha:fazit
sec:anforderungsqualitaet · sec:anforderungsformate · sec:llm-grundlagen ·
sec:cc-bsi · sec:ears (ist eine subsection, Praefix historisch)
subsec:re-begriffe · subsec:anforderungsaufbau · subsec:merkmale-einzeln ·
subsec:merkmale-menge · subsec:sprachkriterien ·
subsec:anforderungsattribute · subsec:rfc2119 · subsec:userstories
subsec:srs-inhalte (neu 23.08.2026)
tab:29148-srs-inhalte (Tabelle 2.1) · tab:ears-muster (2.2) ·
tab:qus-kriterien (2.3) · tab:aqusa (2.4)

Tabellenspalten in Markdown-Dateien:
suchprotokoll.md: | Datum | Portal | Suchstring | Filter | Treffer |
gescreent | aufgenommen | Bemerkung |
ki-protokoll.md: | Datum | Werkzeug | Modell | Zweck | Eingegebene Daten |
Wesentliche Ausgabe | Meine Pruefung | Uebernommen |
literaturmatrix.md: | ID | Kurzangabe | Jahr | Typ | FF | Kernaussage |
Nutzen | Einschraenkungen | Status |
Status-Werte: offen -> zu beschaffen -> beschafft -> ueberflogen ->
gelesen -> eingearbeitet

## Fachliche Zwischenergebnisse (FF2)

Vier-Ebenen-Modell, Stand nach sieben gelesenen Quellen:
- (a) Darstellungsperspektive: User Story (Lucassen et al. 2016)
- (b) Satz- und Syntaxmuster: EARS (Mavin et al. 2009, 2010)
- (c) Modalitaet: shall nach EARS und 29148; RFC 2119/8174 als
  Modalitaetskonvention, nicht als Alternative dazu
- (d) Qualitaets- und Sprachregeln: 29148 Abschn. 5.2.5-5.2.8,
  ergaenzt um die acht NL-Probleme aus Big EARS und die 13
  QUS-Kriterien

Ergebnis der vollstaendigen Entscheidungsmatrix, Stand 08.09.2026.
Die Noten je Zelle stehen in docs/formatauswahl.md Abschnitt 10 und
werden hier nicht wiederholt. Die Befunde in Kurzform:
- Ebene (d) erreicht bei K3, K7 und K10 die Note 2 und steht mit
  keiner anderen Ebene im Widerspruch. Sie ist ein Querschnitt, kein
  Konkurrent.
- Die Ebenen (a) und (b) schliessen einander im Satz aus. Nur eine
  von beiden kann die Satzform stellen.
- Ebene (c) erreicht bei K8 die Note 2. Ihre Zelle bei K10 haengt an
  der noch offenen Wahl zwischen RFC 2119 und den Schluesselwoertern
  aus 29148 Abschn. 5.2.4.
- K4 und K6 unterscheiden die Ebenen (a) und (b) nicht.
- K5 und K9 sind nicht unabhaengig, ebenso wenig K6 und K9. Alles
  drei ist in Abschnitt 7 der formatauswahl.md vermerkt.

Zur Norm:
- 29148 Abschn. 5.2.5 neun Merkmale einzelner Anforderungen, 5.2.6 fuenf
  Merkmale von Anforderungsmengen, 5.2.7 sprachliche Kriterien.
- Abschn. 5.2.7 laesst sich in maschinell pruefbare Regeln ueberfuehren.
- Abschn. 5.2.4 (NOTE 2) schliesst User Stories nicht aus.
- 29148 sieht shall vor und raet von must ab; RFC 2119 behandelt MUST und
  SHALL als gleichbedeutend. In der Matrix zu entscheiden.
- Schluesselwortkonvention nur fuer Englisch formuliert. Durch C1
  erledigt: die Anforderungen werden englisch formuliert.
- Abschn. 8.4 und 8.5 gelesen: Gliederungsvorlagen auf Dokumentebene,
  kein Satzmuster. 8.5 verweist fuer den Inhalt auf 9.6.
- Abschn. 9.6 gelesen und in Abschn. 2.1.7 eingearbeitet. 9.6.10
  Vorgaben je Anforderung, 9.6.11-9.6.18 Inhaltsbloecke, 9.6.18 c
  sechs Beispiele fuer Sicherheitsanforderungen, 9.6.19 Verifikation.
- Anhang C.1 gelesen: Anpassung schliesst volle Konformitaet aus.
- 9.6.3 bis 9.5 nicht gelesen, kein Bedarf erkennbar.

Zu RFC 2119 / 8174:
- Fuenf Verbindlichkeitsstufen; Abschn. 6 fordert sparsamen Gebrauch.
- RFC 8174: besondere Bedeutung nur bei durchgaengiger Grossschreibung.
- Risiko: Ein Sprachmodell wird dazu neigen, alles als MUST zu
  formulieren. Im Prompt-Entwurf zu adressieren, im Modellvergleich zu
  messen.

Zu EARS:
- Fuenf Muster: Ubiquitous, State-driven (WHILE), Event-driven (WHEN),
  Unwanted behaviour (IF-THEN), Optional feature (WHERE).
- EARS verwendet ausschliesslich shall, kennt keine Modalitaetsstufen.
- Zweistufiges Verfahren aus Big EARS ist Vorbild fuer das
  Prompt-Design in Kapitel 4.
- Schluesselwoerter und feste Klauselfolge erlauben regelbasierte
  Formatpruefung -> Vergleichsmass fuer FF3.
- Slotstruktur auf JSON-Schema abbildbar.
- Grenze: fuer hochrangige Stakeholder-Anforderungen entwickelt.
- Evidenz: Fallstudien in einem Unternehmen, Selbstbewertung der
  Autoren. Die 99-Prozent-Angabe darf nicht als Wirksamkeitsnachweis
  zitiert werden.

Zu User Stories:
- Vier Bestandteile im Begriffsmodell, drei Bestandteile des Konzepts.
  Ueber 80 syntaktische Varianten.
- QUS: 13 Kriterien, getrennt nach Einzelstory und Menge.
- AQUSA erreicht mikro-gemittelt 93,8 Prozent Trefferquote bei 72,2
  Prozent Genauigkeit an 1023 Stories aus 18 Datensaetzen.
- Perfect Recall Condition: belegter Grundsatz fuer die Arbeitsteilung
  Mensch/Werkzeug.
- Kernproblem: Well-formed verlangt eine Rolle. PR-Daten sind
  entwicklerzentriert und nennen den Nutzniesser meist nicht.
  Durch die Erhebung gestuetzt: die Daten sind entwicklerzentriert.

Nicht belegbare Merkmale aus 29148: Notwendigkeit, Umsetzbarkeit und
Korrektheit. Eindeutigkeit, Einzelbezug, Nachweisbarkeit und
Vorlagenkonformitaet sind am Text pruefbar.

Aus der Erhebung fuer die Matrix nutzbar:
- labels traegt nichts bei (nur 7,6 %). Die Klassifikation muss aus
  Text und Code kommen.
- author_association unterscheidet nur CONTRIBUTOR und NONE. Keine
  Rollenzuordnung fuer User Stories ableitbar.
- 46,6 Prozent der Pull Requests haben keinen Kommentar. Die
  Begruendung einer Anforderung stammt bei ihnen allein aus Titel,
  Beschreibung und Diff.

Aus der Formulierungsprobe (Stand 30.08.2026, Commit ecf4a40):
- Eine explizite Verbindlichkeitsstufe fuer die jeweils
  rekonstruierte Anforderung kommt in keinem der zwoelf Faelle vor.
  Modalaussagen gibt es, sie betreffen aber das Vorgehen im Pull
  Request, eine andere Anforderung oder ein benachbartes Bauteil.
  Fuer FF2 heisst das: Die Modalitaet ist aus dieser Historie nicht
  belegbar und muesste beim Rekonstruieren gesetzt werden.
- Nach Regel E1 darf Ebene (c) damit nicht die Rolle
  "verpflichtend" erhalten. "optional" bleibt moeglich. Das ist in
  Schritt 5 zu entscheiden.
- Ohne R10 stuende Ebene (c) bei 4 von 12 und erhielte ebenfalls
  Note 0. Die Regel veraendert die Zahl, nicht die Entscheidung.
- Rollen sind seltener belegt als Systemverhalten. Ebene (a)
  scheitert meist am Rollenbestandteil.
- Das EARS-Muster Ubiquitous passt fuer die meisten Faelle; WHEN
  bei PR 622, WHILE bei PR 577.

Aus Teil B der Formulierungsprobe (Stand 02.09.2026, Commit a56bb5e):
- Beide bewerteten Ebenen koennen alle drei Anforderungsarten
  ausdruecken: funktional, leistungsbezogen, sicherheitsbezogen.
  Eine typabhaengige Schwaeche zeigt sich bei keiner von beiden.
- K6 ist fuer die Ebenen (c) und (d) nicht anwendbar. Beide geben
  keine Satzbestandteile vor: (c) regelt nur die Verbindlichkeit,
  (d) beurteilt eine bereits fertige Formulierung.
- Die User-Story-Saetze nennen das System nicht, weil sie im Passiv
  stehen. Die EARS-Saetze nennen es jedes Mal. Dieser Unterschied
  gehoert zu K1 und ist bei der Formatentscheidung zu beachten.

Folge fuer Schritt 5, aus E1 und den Messwerten:
- Ebene (a) und Ebene (c) haben bei K9 die Note 0. Nach E1 kann
  keine von beiden die Rolle "verpflichtend" erhalten; "optional"
  bleibt fuer beide moeglich.
- Ebene (d) ist nicht ausgeschlossen, weil K9 dort n. a. ist und
  n. a. nach R3 nie wie 0 wirkt.
- Fuer "verpflichtend" kommen damit nur die Ebenen (b) und (d) in
  Frage. Das steht vor Schritt 5 fest und ist keine Vorwegnahme der
  Entscheidung, sondern deren Rahmen.

## Zugangsdaten

- GitHub-Token qrisp-thesis-readonly, im Passwortmanager und in
  .env im Projektwurzelverzeichnis. Ablauf 2027-05-31.
- SSH-Schluessel ed25519 fuer das eigene Repository.
- Git-Identitaet: Omar Assad Salem, GitHub-Noreply-Adresse.

## Offene Punkte

Extern, mit Vorlauf:
- Umfangsfrage gegenueber dem Qrisp-Team. Stand Ende Woche 8 als
  Git-Tag thesis-v1.0 einfrieren; alles Weitere in den Ausblick.
- Bewertungsbogen und Anweisungen fuer die Bewertenden bis Woche 8.
- Datenschutzrechtliche Bewertung der Pseudonymisierung mit dem
  Betreuer klaeren.
- KI-Formulierung fuer vorspann.tex mit Professor abstimmen.
- Korreferent in thesis.tex eintragen (Platzhalter Zeile 23)
- API-Budget fuer FF3, zu klaeren bis Woche 4

Inhaltlich offen:
- Paket C Schritt 5: Rollenzuweisung und Formatentscheidung. Dabei
  faellt die Wahl der Modalitaetskonvention; danach kann die Zelle
  K10 fuer Ebene (c) mit Datum berichtigt werden.
- Paket C Schritt 6: Abschnitt zur Formatauswahl in Kapitel 4;
  dabei Z. 127-132 in thesis.tex ersetzen (kuendigt eine deutsche
  Konvention an, widerspricht C1)
- Phase 2 der systematischen Literatursuche (S1, S2, S4), nach
  Schritt 4 von Paket C
- INVEST: Lucassen loest das S als Scalable auf. Gegen Wake 2003 pruefen.
- Titelvariante Mavin 2009 vereinheitlichen.
- docs/entscheidungen.md Z. 142 und 658 verweisen auf die
  Projektanweisung. Da das Repository mit abgegeben wird, durch eine
  inhaltliche Begruendung ersetzen - als datierte Praezisierung, nicht
  durch Aendern der gepushten Commits.
- Pruefen, ob in docs/findings_pull_details.md und
  findings_pull_files.md GitHub-Anmeldenamen stehen. Die Suche nach "@"
  fand nur docs/entscheidungen.md (zwei Bot-Namen, unproblematisch);
  ein Name ohne "@" wuerde so nicht gefunden.
- Wegweiser in README.md ergaenzen: welche Datei erklaert was und in
  welcher Reihenfolge sie zu lesen ist (Paket I).
- src/analyze/draw_sample.py hat keine Tests. Weicht von D4 ab.
  Entweder Tests ergaenzen oder die Ausnahme begruenden.
- PR 711: Rolle und Systemreaktion sind die einzigen zwei Felder der
  Stichprobe, die nicht unabhaengig gegengeprueft wurden. Die
  Diff-Ansicht war dem gegenpruefenden Modell nicht zugaenglich.
  Steht im Protokoll unter "Methodischer Status".
- Vier Datumsangaben in der Aenderungshistorie von
  docs/formatauswahl.md sind auf den 26.08.2026 geschaetzt
  (Pflichtbestandteile, K9 bei Ebene (d), Erhebungsform Teil A).
  Belegt ist nur "Begonnen: 26.08.2026" im Protokoll.

Aus Paket D in spaetere Pakete uebernommen:
- Budget der Stufe 3 in Paket E bestaetigen oder anpassen. Bei
  Aenderung ist build_interim.py erneut auszufuehren.
- Auswahlregel fuer die Modelleingabe festlegen und begruenden:
  Bots, Pull Requests ohne Beschreibung, ohne Codeaenderung (Paket E).
- Messen, ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben
  enthalten (Paket G, FF4).
- Schemavalidierung der LLM-Ausgaben testen (Paket E).

Technisch und redaktionell:
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Woche 5
- Platzhalter in thesis.tex: Z. 20 Abgabedatum · Z. 23 Korreferent ·
  Z. 29 Abstract · Z. 39 Einleitung · Z. 443 SATZ UEBERARBEITEN ·
  Z. 508 Verweis auf die Entscheidungsmatrix ·
  Z. 903 Femmer et al. - Primaerquelle beschaffen oder Satz streichen ·
  Z. 910, 915, 921, 929, 937, 944, 951, 959 noch leere Kapitel
  Achtung: Diese Nummern sind aus dem Versatz +144 errechnet, nicht
  einzeln geprueft. Vor dem Bearbeiten nachsehen.
- Overfull hboxen, Behebung in Woche 12: vorspann.tex Z. 4-16 (86,6pt) ·
  thesis.tex Z. 263-269 (12,7pt) · Z. 288-295 (12,9pt) ·
  Z. 444-445 (14,5pt) · Z. 912 (1,4pt)
  Neu: Underfull hbox Z. 355 (badness 1546), Beschriftung Tabelle 2.1
- Demo-Dateien der Vorlage in thesis/figures/ vor Abgabe entfernen


## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Skripte immer aus der Projektwurzel starten
  (python src/collect/<n>.py bzw. python src/prepare/<n>.py), sonst
  wird github_api nicht gefunden
- Tests: python -m pytest tests/ -v aus der Projektwurzel
- Erst Quelltext committen, dann abrufen oder aufbereiten. Dann stimmt
  collector_commit bzw. builder_commit im Manifest exakt.
- Vor dem vollen Lauf immer ein Probelauf mit --limit 5
- Probelaeufe erzeugen ein Manifest. Vor dem Commit loeschen, sonst
  landet ein Probelauf in der Historie.
- Nach Abbruch: denselben Befehl erneut ausfuehren. Die Abrufskripte
  lesen ihren Fortschritt aus der bereits geschriebenen Datei.
- --day <Datum> mitgeben, wenn in eine bestehende Datei
  weitergeschrieben werden soll
- build_interim.py schreibt nie in eine vorhandene Datei. Zum Neubau
  --overwrite mitgeben.
- Kompilieren: cd thesis && pdflatex thesis.tex && bibtex thesis1 &&
  bibtex thesis2 && pdflatex thesis.tex && pdflatex thesis.tex
  (nicht make all - braucht LibreOffice und ImageMagick)
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> log -1 -> status -> push
- Kein git add . und kein git add ordner/
- Commit-Praefixe: lit:, bib:, tex:, code:, test:, docs:, chore:
- Bereits gepushte Commits werden nicht nachtraeglich geaendert.
- BibTeX-Felder mit Umlauten oder Backslashes in {...} setzen.
- Eigennamen im BibTeX-Titel in {...} setzen.
- requirements.txt nie von Hand bearbeiten: pip freeze > requirements.txt

## Konfiguration (config/collect.toml)

[source] owner eclipse-qrisp, repo Qrisp, repo_id 632066325
[api] base_url https://api.github.com, version 2022-11-28,
      per_page 100, state all
[fetch] timeout_seconds 30, pause_seconds 0.2, max_retries 5
[prepare] skip_patch_extensions .ipynb .drawio .bkp .svg,
      max_patch_chars_per_file 10000, max_patch_chars_per_pull 50000,
      truncation_marker "\n[... truncated ...]\n"

## Aufruf des Aufbereitungsskripts

python src/prepare/build_interim.py \
  --details data/raw/pull_details_2026-08-14.jsonl \
  --issue-comments data/raw/issue_comments_2026-08-19.jsonl \
  --review-comments data/raw/review_comments_2026-08-19.jsonl \
  --files data/raw/pull_files_2026-08-19.jsonl

Optional: --limit N (Probelauf), --day JJJJ-MM-TT, --overwrite

## Commits Paket D Teil 2

fe95a1a Detailabruf mit Wiederaufnahme
d26c682 Auswertung der Detaildaten, Befund, Entscheidungen D1-D4
c4f0dee Kommentarabruf fuer beide Endpunkte
a8d649b Manifeste des Kommentarabrufs und Befund zu den Abweichungen
44c669f Abruf der geaenderten Dateien und Diffs
336422d Dateiabruf ausgewertet, D1 endgueltig, Berichte auf Englisch

## Commits Paket D Teil 3

1c47a39 Kuerzungsparameter aus D1 in die Konfiguration
f7f8c52 build_interim.py und Testsuite (26 Tests)
d56feec Manifest des aufbereiteten Datensatzes vom 19.08.2026
c63f700 Kuerzungsstufen aus D1 getestet (12 weitere Tests)
acacebb KI-Protokoll fuer Paket D Teil 3
ea16a7c Entscheidungen D5 bis D8
1d83472 Zeilenumbruch am Dateiende in github_api.py,
        docs/ki-protokoll.md und tests/README.md. Achtung: Die
        Commit-Nachricht kuendigt zusaetzlich das Entfernen einer
        Leerzeile in github_api.py an. Das ist in diesem Commit nicht
        geschehen und wurde nachgeholt.
95175fb Leerzeile in github_api.py entfernt, Richtigstellung zu 1d83472

## Commits Paket C

9eb9052 Vorentscheidungen C1 bis C3 zur Formatauswahl
e78f491 29148 Abschn. 9.6 und Anhang C.1 in Notiz und Matrix
0a72cdf Abschnitt 2.1.7 Inhalte einer Software-Anforderungsspezifikation
9147cc0 Kriterienkatalog, Skala und Entscheidungsverfahren
6be91a8 Ziehungsskript und Stichprobe fuer die Formulierungsprobe
076c396 Regeln R9 und R10, Formulierungsprobe aufgenommen
ecf4a40 Gegenpruefung der Formulierungsprobe abgeschlossen
7ba386e Stand nach Abschluss von Paket C Schritt 4a
ecd907c K6 fuer die Ebenen (c) und (d) nicht anwendbar, Schritt 4c ergaenzt
bf3f137 Rahmen und drei Referenzinhalte fuer K6 festgelegt
98c3ca4 Datum der K6-Referenzinhalte auf 02.09.2026 korrigiert
a56bb5e Teil B neu aufgesetzt, K6 mit Note 2 fuer die Ebenen (a) und (b)
2951149 KI-Protokoll um Paket C Schritt 4a und 4b ergaenzt
cfe44ca Entscheidungen vor K2: R11, Zuordnung 29148 Abschn. 5.2.4, D4a
c062d92 Entscheidungsmatrix K2 vergeben, K6 und K9 uebertragen
c8b48b5 Entscheidungsmatrix K3 und K4 vergeben, Vorbehalt zu K4 in Abschnitt 7
b3367ae Quattrocchi 2026 und Paiva 2026 geprueft und aufgenommen
a2f3e48 Entscheidungsmatrix K5 vergeben, Vorbehalt zu K5 in Abschnitt 7
cb856ca Entscheidungsmatrix K7, K8 und K10 vergeben, Schritt 4c abgeschlossen

## Aufruf des Ziehungsskripts

python src/analyze/draw_sample.py \
  --input data/interim/pulls_prepared_2026-08-19.jsonl

Optional: --output, --seed (Standard 20260823), --overwrite.
Das Skript importiert nichts aus github_api.py und laeuft aus der
Projektwurzel. Ausgeschlossen werden Bot-Beitraege und Vorgaenge mit
outcome = open. Sechs Schichten S6 bis S1, von der seltensten zur
haeufigsten zugeordnet, jeder Datensatz nur einmal.

Lauf vom 25.08.2026: 476 gelesen, 31 Bots, 50 offen, 395 verbleibend.
Gezogen: 48, 75, 191, 371, 408, 413, 464, 533, 577, 622, 692, 711.

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   erledigt
W3 17.-23.08. Extraktion, Formatauswahl                Paket D
                                                       erledigt 21.08.
W4 24.-30.08. LLM-Extraktion mit API-Modell
W5 31.08.-06.09. Prompt-Iteration, lokales Modell
W6 07.-13.09. Modellvergleich (Kontrollpunkt lokales Modell)
W7 14.-20.09. Klassifikation, Sicherheitsraster
W8 21.-27.09. Gap-Analyse, Git-Tag thesis-v1.0, Evaluation starten
W9 28.09.-04.10. Kapitel Implementierung
W10 05.-11.10. Auswertung, Kapitel Evaluation
W11 12.-18.10. Diskussion, Fazit
W12 19.-25.10. Korrekturschleife
W13 26.-30.10. Endkontrolle, Abgabe

Stand 03.09.2026, W5. Paket D war drei Tage vor Plan fertig.
Paket C laeuft seit 23.08.; die Schritte 4a und 4b sind
abgeschlossen, es fehlen Schritt 4c, Schritt 5 und Schritt 6.
Paket E hat noch nicht begonnen und liegt hinter dem Plan fuer W4.
Bis zur Abgabe am 01.11.2026 verbleiben rund acht Wochen.