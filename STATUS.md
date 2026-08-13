# Bearbeitungsstand

Letzte Aktualisierung: 12.08.2026
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
- Sechs Lesenotizen unter literatur/notizen/ angelegt:
  bradner_1997_rfc2119.md · iso_2018_29148.md · mavin_2009_ears.md ·
  mavin_2010_big_ears.md · wilkinson_2018_mitigation.md ·
  lucassen_2016_qus.md
- docs/ki-protokoll.md und entscheidungen.md fortgeschrieben
- LaTeX-Vorlage nach thesis/ uebernommen, kompiliert fehlerfrei
- Abschnitt 2.1: ISO/IEC/IEEE 29148:2018, Abschn. 3.1 und 5.2.4-5.2.8
- Abschnitt 2.2.1: RFC 2119 und RFC 8174
- Abschnitt 2.2.2: EARS, mit Tabelle der fuenf Muster
- Abschnitt 2.2.3: User Stories, mit zwei Tabellen
- preamble.tex um booktabs und array ergaenzt, konfliktfrei geladen

Arbeitspaket D, Teil 1 (Pilotabruf) abgeschlossen:
- .env mit GITHUB_TOKEN angelegt, per .gitignore ausgeschlossen
- config/collect.toml haelt alle Erhebungsparameter
- src/collect/github_api.py: gemeinsames Modul (Konfiguration, Token,
  HTTP-Kopfzeilen)
- src/collect/api_test.py: Verbindungstest
- src/collect/explore_fields.py: Feldstruktur eines PR-Objekts
- src/collect/compare_objects.py: Liste gegen Detail
- src/collect/fetch_pull_list.py: Listenabruf mit Paginierung,
  Duplikatpruefung, JSONL-Ausgabe und Manifest
- Erhebung 12.08.2026: 476 Pull Requests in
  data/raw/pulls_2026-08-12.jsonl (lokal, nicht im Repository)
- data/manifests/manifest_pulls_2026-08-12.json (versioniert)

## Belegte Fakten aus Paket D (Stand 12.08.2026)

- Token funktioniert: Statuscode 200, Kontingent 5000/Stunde,
  Ablaufdatum 2027-05-31, also nach dem Abgabetermin.
- Repository eclipse-qrisp/Qrisp ist oeffentlich, ID 632066325.
- 476 Pull Requests, Nummern 5 bis 797, keine Duplikate.
  Zweifach belegt: Link-Header mit per_page=1 und vollstaendiger Abruf.
- Die Nummernluecken (476 Datensaetze bei Spanne 793) entstehen durch
  den gemeinsamen Zaehler von Issues und Pull Requests. Jede
  Verarbeitung muss die vorhandenen Nummern aus der Datei lesen und darf
  nicht von 1 bis 797 durchzaehlen.
- Listenendpunkt liefert 36 Felder, Detailendpunkt 48. Keine Felder nur
  in der Liste. Nur im Detailabruf: additions, deletions, changed_files,
  comments, commits, review_comments, merged, merged_by,
  maintainer_can_modify, mergeable, mergeable_state, rebaseable.
- state kennt nur open und closed und unterscheidet nicht zwischen
  zusammengefuehrt und verworfen. Dafuer ist merged_at zustaendig.
- PR-Beschreibungen verwenden CRLF-Zeilenenden. Normalisierung in der
  Aufbereitung noetig.
- PR-Beschreibungen enthalten Vorlagentext des Projekts als
  HTML-Kommentar ("## Description <!-- What does this PR do? ...").
  Kein Autorentext, keine Anforderungsquelle.
- Ein Listenabruf kostet 5 Anfragen, ein Detailabruf 1 Anfrage je PR.
- SHA-256 des Datensatzes vom 12.08.2026:
  88a6652c1de9c2f2a1d2e60dbe9bef7291c8e1f3fada14418f4bf5bc387bead1

## Ungepruefte Beobachtungen

- Ob die 321 Nummernluecken alle Issues sind: plausibel, nicht gemessen.
- assignees, milestone, requested_reviewers, requested_teams,
  auto_merge und locked waren in PR #797 leer. Ein Datenpunkt, kein
  Befund. Der Detailabruf soll ihre Belegung zaehlen.
- Verbreitung des Vorlagentexts in den Beschreibungen: unbekannt.

## Aktuell

Paket D, Teil 1 abgeschlossen. Naechster Schritt: Detailabruf der 476
Pull Requests, dann Kommentare und Diffs, dann Reduktion nach
data/interim/.

Paket C (Entscheidungsmatrix zur Formatauswahl) ist nicht blockiert -
es braucht keine weitere Lesearbeit. Vorgesehen als eigener Chat nach
Paket D Teil 2. Begruendung: Die Formatentscheidung profitiert davon,
dass die echten PR-Daten bereits gesichtet sind (z. B. das
Rollen-Problem bei User Stories).

## Getroffene Entscheidungen

Vollstaendig in docs/entscheidungen.md. Kurzfassung der fuer die
Zusammenarbeit wichtigsten:

- Repository privat. Nach Abgabe umstellbar.
- Evaluation nach Exposé-Variante: Das Qrisp-Team wird durch den
  Professor informiert und bewertet, sobald das Werkzeug fertig ist.
  Ergaenzt um eine dokumentierte Selbstbewertung. Bei mehreren
  Bewertenden wird ein Uebereinstimmungsmass moeglich. Der aeltere
  Eintrag "Evaluation reduziert" vom 31.07. ist ueberholt.
  Terminabhaengigkeit: Werkzeug bis Ende Woche 8 bewertbar,
  Git-Tag thesis-v1.0.
- FF3: API-Modell darf von OpenAI oder Anthropic stammen. Dasselbe
  Modell als Werkzeug und als Evaluationsgegenstand ist eine Bedrohung
  der Konstruktvaliditaet und muss dokumentiert werden.
- Kapitel nicht in Einzeldateien. Alles in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard.
- Given-When-Then wird nicht als eigener Grundlagenabschnitt
  aufgearbeitet; Ausschluss in der Entscheidungsmatrix begruenden.
- Wilkinson/Mavin 2018 nachrangig (safety, nicht security).
- Lesenotizen ab 06.08.2026 nach Neun-Abschnitte-Vorlage.
- API-Version 2022-11-28, explizit in jeder Anfrage, Wert in
  config/collect.toml. Wechsel auf 2026-03-10 geprueft und verworfen.
- Codesprache im Quelltext: Englisch, Bezeichner und Kommentare.
  Deutschsprachige Erlaeuterung in Kapitel 5.
- Commit-Praefix code: fuer Quelltext, zusaetzlich zu lit:, bib:, tex:,
  chore:.
- Keine README.md in Unterordnern von src/.
- Speicherformat JSONL (fortsetzbar nach Abbruch).
- Keine Datensaetze im Repository. Nachweis der Datensatzversion ueber
  SHA-256-Pruefsumme im Manifest unter data/manifests/.
- Manifest je Erhebung: Zeitpunkt in UTC, Repository und ID,
  API-Version, Parameter, Anzahl, Dateiname, Pruefsumme,
  erhebender Git-Commit.
- Feldauswahl inklusive abgeleitetem Feld outcome
  (merged / closed_unmerged / open).
- Ausschluss volatiler Felder: mergeable, mergeable_state, rebaseable,
  merge_commit_sha.
- Datenminimierung: vom user-Objekt nur login, die uebrigen 18 Felder
  werden verworfen.
- Pseudonyme A01 ff. in der schriftlichen Arbeit; Zuordnungstabelle
  docs/pseudonyme.csv bleibt lokal.

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

Nicht belegbare Merkmale aus 29148: Notwendigkeit, Umsetzbarkeit und
Korrektheit. Eindeutigkeit, Einzelbezug, Nachweisbarkeit und
Vorlagenkonformitaet sind am Text pruefbar.

## Zugangsdaten

- GitHub-Token qrisp-thesis-readonly, im Passwortmanager und in
  .env im Projektwurzelverzeichnis. Erprobt am 12.08.2026,
  Ablauf 2027-05-31.
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
- Detailabruf je Pull Request (476 Anfragen)
- Review-Kommentare und allgemeine PR-Kommentare
- Geaenderte Dateien und Diffs; Umgang mit sehr grossen Diffs
- Reduktion nach data/interim/ mit Feldauswahl, outcome und
  Datenminimierung
- Normalisierung der Zeilenenden, Entfernen des Vorlagentexts
- Wiederaufnahme abgebrochener Abrufe, Caching
- Belegung der scheinbar leeren Felder zaehlen
- Tests unter tests/

Technisch und redaktionell:
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
  (python src/collect/<name>.py), sonst wird github_api nicht gefunden
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

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   Pilotabruf
                                                       erledigt 12.08.
W3 17.-23.08. Extraktion, Formatauswahl
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

Paket B wurde eine Woche frueher fertig. Der Pilotabruf lief am dritten
Tag von W2. Detailabruf und Aufbereitung koennen in W2 vorgezogen
werden. Paket C folgt danach als eigener Chat.