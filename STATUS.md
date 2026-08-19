# Bearbeitungsstand

Letzte Aktualisierung: 19.08.2026
Abgabetermin: 01.11.2026 (Sonntag; intern geplant auf Fr 30.10.2026)

## Zusammenarbeit im Chat

Diese Regeln gelten fuer jeden Chat und gehen Annahmen vor.

- Claude hat kein Gedaechtnis ueber Chats hinweg. Nur was in dieser
  Datei oder im Projektwissen steht, gilt als bekannt.
- Projektwissen enthaelt ausschliesslich Unveraenderliches:
  exposee.tex und 29148-2018.pdf. Arbeitsdateien werden pro Chat
  hochgeladen, nie im Projektwissen abgelegt - dort veralten sie
  unbemerkt.
- Wenn Claude den Inhalt einer Datei braucht, muss er sie ausdruecklich
  anfordern und dabei den vollstaendigen Pfad nennen. Claude arbeitet
  nie mit einer aus dem Gedaechtnis rekonstruierten Fassung.
- Dasselbe gilt fuer Befehlsausgaben: Claude erklaert einen Commit,
  eine Installation, eine Kompilierung oder einen Test erst dann fuer
  erfolgreich, wenn die tatsaechliche Ausgabe im Chat steht.
- Claude erfindet keine Bearbeitungsstaende, Trefferzahlen,
  Bewertungen oder Dateiinhalte. Bei Unklarheit fragt er nach.
- Stopp-Punkte in Anleitungen sind verbindlich. Sie stehen dort, wo
  etwas unwiederbringlich ueberschrieben werden kann.
- Claude testet groessere Skripte vor der Uebergabe in seiner eigenen
  Umgebung mit erfundenen Testdaten und sagt das dazu. Bewaehrt: hat in
  Paket D Teil 2 jeden Fehler vor dem echten Lauf gefunden.

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS 26.5.2 (25F84) - Python 3.14.6 (Homebrew) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)

## Repository-Struktur

config/ · data/{raw,interim,processed,manifests} · docs/ ·
eval/{instrument,sample,responses} · experiments/ ·
literatur/{notizen,volltexte,pdf} · prompts/ ·
src/{collect,prepare,extract,classify,analyze} · tests/ · thesis/

src/ enthaelt eine README.md, die alle Unterordner beschreibt. Die
Unterordner selbst haben keine README.md - bewusst so entschieden.

Per .gitignore ausgeschlossen: .env, config/config.yaml, *.key, *.token,
data/raw/, data/interim/, eval/responses/, docs/pseudonyme.csv,
models/, literatur/pdf/, literatur/volltexte/, .venv/, __pycache__/,
LaTeX-Hilfsdateien in thesis/, .DS_Store, .vscode/, .idea/
Nicht ausgeschlossen und damit versioniert: data/manifests/

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

Dazu je eine .progress.jsonl fuer Kommentare und Dateien, ebenfalls
lokal. Alle Manifeste unter data/manifests/ sind versioniert.

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

## Ungepruefte Beobachtungen

- Ob die 321 Nummernluecken alle Issues sind: plausibel, nicht gemessen.
- Zu PR 344: vermutet ein Review im Zustand pending, nur seinem
  Verfasser sichtbar. Nicht pruefbar.
- PR 674 und 676 sind fast gleich gross (574/575 Dateien) - vermutlich
  zwei Anlaeufe derselben Umbauaktion. Nicht geprueft.
- Warum author_association nie OWNER oder MEMBER annimmt: unbekannt.

## Aktuell

Paket D, Teil 2: alle vier Abrufe abgeschlossen und committet.
Naechster Schritt: Reduktion nach data/interim/, danach die vier Tests.

Paket C (Entscheidungsmatrix zur Formatauswahl) ist nicht blockiert und
braucht keine weitere Lesearbeit. Vorgesehen als eigener Chat nach
Paket D.

## Getroffene Entscheidungen

Vollstaendig in docs/entscheidungen.md. Kurzfassung:

- Repository privat. Nach Abgabe umstellbar.
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
- D2 Bots markieren (author_is_bot), nicht loeschen. Regel: user.type
  gleich "Bot" ODER Login endet auf "[bot]".
- D3 eine Rohdatei je Endpunkt, Zusammenfuehrung erst in data/interim/.
  Jedes Manifest traegt source_dataset mit Pruefsumme.
- D4 pytest, vier Tests: Wiederaufnahme, outcome, Normalisierung,
  JSONL-Ein- und Ausgabe. Kein Nachbau der API.
- Sprache: Programme unter src/ geben Meldungen und Berichte auf
  Englisch aus, einschliesslich der Berichtsdateinamen. docs/ und
  literatur/ bleiben deutsch.
- Erst Quelltext committen, dann abrufen.

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
tab:ears-muster · tab:qus-kriterien · tab:aqusa

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
- (d) Qualitaets- und Sprachregeln: 29148 Abschn. 5.2.5-5.2.7,
  ergaenzt um die acht NL-Probleme aus Big EARS und die 13
  QUS-Kriterien

Zur Norm:
- 29148 Abschn. 5.2.5 neun Merkmale einzelner Anforderungen, 5.2.6 fuenf
  Merkmale von Anforderungsmengen, 5.2.7 sprachliche Kriterien.
- Abschn. 5.2.7 laesst sich in maschinell pruefbare Regeln ueberfuehren.
- Abschn. 5.2.4 (NOTE 2) schliesst User Stories nicht aus.
- 29148 sieht shall vor und raet von must ab; RFC 2119 behandelt MUST und
  SHALL als gleichbedeutend. In der Matrix zu entscheiden.
- Schluesselwortkonvention nur fuer Englisch formuliert. Fuer
  deutschsprachige Anforderungen eigene Festlegung noetig - OFFEN.
- Abschn. 8.4 und 8.5 noch nicht gelesen.

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
- Deutschsprachige Modalitaetskonvention festlegen (FF2)
- Entscheidungsmatrix aufstellen (Paket C)
- Phase 2 der systematischen Literatursuche (S1, S2, S4)
- INVEST: Lucassen loest das S als Scalable auf. Gegen Wake 2003 pruefen.
- Titelvariante Mavin 2009 vereinheitlichen.

Paket D, noch zu erledigen:
- Reduktion nach data/interim/: Feldauswahl, outcome, author_is_bot,
  Normalisierung der Zeilenenden, Entfernen des Vorlagentexts,
  Umsetzung der drei Kuerzungsstufen aus D1, Zusammenfuehrung der
  vier Rohdateien, Manifest
- Vier Tests unter tests/ mit pytest. pytest ist noch NICHT
  installiert; requirements.txt enthaelt bisher nur requests.
- docs/ki-protokoll.md fuer Paket D Teil 2 nachtragen

Technisch und redaktionell:
- github_api.py: doppelte Leerzeile vor fetch_paginated, kein
  Zeilenumbruch am Dateiende. Rein kosmetisch, Aufraum-Commit.
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Woche 5
- Platzhalter in thesis.tex: Z. 20 Abgabedatum · Z. 23 Korreferent ·
  Z. 29 Abstract · Z. 39 Einleitung · Z. 299 SATZ UEBERARBEITEN ·
  Z. 364 Verweis auf die Entscheidungsmatrix ·
  Z. 759 Femmer et al. - Primaerquelle beschaffen oder Satz streichen ·
  Z. 766, 771, 777, 785, 793, 800, 807, 815 noch leere Kapitel
- Demo-Dateien der Vorlage in thesis/figures/ vor Abgabe entfernen
- Overfull hboxen, Behebung in Woche 12: vorspann.tex Z. 4-16 (86,6pt) ·
  thesis.tex Z. 263-269 (12,7pt) · Z. 288-295 (12,9pt) ·
  Z. 300-301 (14,5pt) · Z. 768 (1,4pt)
- Rote KI-Hinweisbox in vorspann.tex vor Abgabe ersetzen
- fancyhdr-Warnungen stammen aus der Vorlage und sind harmlos

## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Skripte immer aus der Projektwurzel starten
  (python src/collect/<n>.py), sonst wird github_api nicht gefunden
- Erst Quelltext committen, dann abrufen. Dann stimmt collector_commit
  im Manifest exakt.
- Vor dem vollen Lauf immer ein Probelauf mit --limit 5
- Nach Abbruch: denselben Befehl erneut ausfuehren. Die Skripte lesen
  ihren Fortschritt aus der bereits geschriebenen Datei.
- --day <Datum> mitgeben, wenn in eine bestehende Datei
  weitergeschrieben werden soll
- Kompilieren: cd thesis && pdflatex thesis.tex && bibtex thesis1 &&
  bibtex thesis2 && pdflatex thesis.tex && pdflatex thesis.tex
  (nicht make all - braucht LibreOffice und ImageMagick)
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> log -1 -> status -> push
- Kein git add . und kein git add ordner/
- Commit-Praefixe: lit:, bib:, tex:, code:, chore:
- Bereits gepushte Commits werden nicht nachtraeglich geaendert.
- BibTeX-Felder mit Umlauten oder Backslashes in {...} setzen.
- Eigennamen im BibTeX-Titel in {...} setzen.
- requirements.txt nie von Hand bearbeiten: pip freeze > requirements.txt

## Konfiguration (config/collect.toml)

[source] owner eclipse-qrisp, repo Qrisp, repo_id 632066325
[api] base_url https://api.github.com, version 2022-11-28,
      per_page 100, state all
[fetch] timeout_seconds 30, pause_seconds 0.2, max_retries 5

## Commits Paket D Teil 2

fe95a1a Detailabruf mit Wiederaufnahme
d26c682 Auswertung der Detaildaten, Befund, Entscheidungen D1-D4
c4f0dee Kommentarabruf fuer beide Endpunkte
a8d649b Manifeste des Kommentarabrufs und Befund zu den Abweichungen
44c669f Abruf der geaenderten Dateien und Diffs
336422d Dateiabruf ausgewertet, D1 endgueltig, Berichte auf Englisch

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   erledigt
W3 17.-23.08. Extraktion, Formatauswahl                Abrufe erledigt
                                                       19.08.
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

Paket B wurde eine Woche frueher fertig. Alle vier Abrufe aus Paket D
Teil 2 liefen am dritten Tag von W3. Reduktion und Tests koennen in W3
abgeschlossen werden, danach Paket C.