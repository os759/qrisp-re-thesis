# Bearbeitungsstand

Letzte Aktualisierung: 29.09.2026
Abgabetermin: 15.10.2026 (Donnerstag; intern geplant auf Di 13.10.2026)

## Roter Faden

Stand 29.09.2026. Dieser Abschnitt erzaehlt ohne Kuerzel, wie die
Arbeit bis heute gelaufen ist und warum. Einzelheiten stehen weiter
unten und in docs/entscheidungen.md.

Worum es geht: Die Arbeit baut ein Programm, das aus alten
Aenderungsvorschlaegen (Pull Requests) des Projekts Qrisp
Softwareanforderungen herausschreibt. Ein Sprachmodell formuliert die
Anforderungen, das Programm prueft jede davon gegen ihre Quelle.

1. Literatur (Paket B, vor Paket D abgeschlossen): Vier Ansaetze,
   Anforderungen zu schreiben, wurden gelesen und in Kapitel 2
   beschrieben: die Norm ISO/IEC/IEEE 29148, die Schluesselwoerter aus
   RFC 2119, die Satzschablone EARS und User Stories. Das war noetig,
   weil die spaetere Formatwahl sonst nicht mit Quellen belegbar waere.

2. Daten (Paket D, 12.08. bis 21.08.2026): Alle 476 Pull Requests von
   Qrisp wurden bei GitHub abgerufen und zu einem Datensatz je Pull
   Request zusammengefuehrt. Sehr grosse Code-Aenderungen werden in
   drei Stufen gekuerzt (Entscheidung D1), weil einzelne Pull Requests
   ueber zwei Millionen Zeichen haben. Jede Kuerzung ist markiert.

3. Format (Paket C, 23.08. bis 11.09.2026): Eine Tabelle mit zehn
   Kriterien hat die vier Ansaetze verglichen, gestuetzt auf Literatur
   und auf eine Probe von Hand an zwoelf echten Pull Requests.
   Ergebnis ist das Zielformat EARS+29148: englische EARS-Saetze mit
   shall, geprueft nach Sprachregeln der Norm (Entscheidung C5).
   User Stories fielen weg, weil nur 4 der 12 Pull Requests eine Rolle
   nennen, zwei davon nur pauschal. Verbindlichkeitsstufen wie in
   RFC 2119 fielen weg, weil keiner der 12 Faelle eine solche Stufe
   belegt.

4. Vorbereitung der Extraktion (Paket E, ab 15.09.2026): Festgelegt
   wurden das Ausgabeformat (E1), die Evaluation (E2), das Budget von
   hoechstens 150 Euro (E3), die Auswahl der Pull Requests (E4) und
   die Regeln der Belegstaerke (E6). Das Modell bekommt 395 von 476
   Pull Requests. Noch offene Vorgaenge fehlen, weil sich ihr Inhalt
   noch aendern kann. Beitraege von Programmen fehlen, weil sie fast
   nur Versionen fremder Bibliotheken anheben oder nie uebernommen
   wurden (Nachtrag zu E4); fuer FF4 werden die Dependabot-Beitraege
   in Paket G gesondert gesichtet. Die Belegstaerke wird vom Programm berechnet,
   weil sie so reproduzierbar ist und keine freie Modellausgabe.
   Bewertet wird an einer neuen Stichprobe, weil die zwoelf Faelle aus
   Paket C schon die Formatwahl getragen haben. Was sich maschinell
   pruefen laesst, prueft ein Programm; den Rest bewertet der
   Verfasser von Hand, weil eine Bewertung allein durch ein Modell
   keinen unabhaengigen Massstab haette. Die Liste der
   Bewertungskriterien steht seit dem 21.09.2026 fest, vor dem ersten
   bezahlten Lauf. Das Qrisp-Team bewertet erst nach der Abgabe; der
   Betreuer hat zugestimmt. Danach entstand die Anweisung an das
   Modell (Prompt, E7).

5. Modell (19.09.2026): Gewaehlt ist gpt-5.6-terra von OpenAI (E8),
   weil es preislich gleichauf mit dem vergleichbaren Claude-Modell
   liegt und eine Doppelrolle vermeidet: Claude ist Arbeitswerkzeug und
   waere sonst zugleich Messgegenstand. Anmeldenamen in den Texten
   werden vorher durch person_NN ersetzt (E9), weil sie zu keiner
   Anforderung beitragen und nicht an einen fremden Anbieter gehen
   sollen.

6. Pilotlauf (Aufgabe A8, 21. und 22.09.2026): 20 Pull Requests gingen
   an das Modell, bevor alle 395 gesendet werden (E10). So werden
   Programm, Prompt und Kosten an wenigen Faellen geprueft. Alle 20
   Antworten waren gueltig. Das Pruefprogramm lehnte 5 ab, weil ein
   Zitat aus einem Code-Ausschnitt nicht woertlich in der Quelle
   stand. Ob das am Pruefprogramm oder am Modell liegt, ist offen.

7. Ursachen und zweiter Probelauf (24.09.2026): Alle abgelehnten
   Zitate gehen auf das Modell zurueck, keines auf das Pruefprogramm.
   Das Modell hat aus Kopfzeilen eines Diffs zitiert, entfernte Zeilen
   uebersprungen oder einzelne Zeichen veraendert. Die Regel fuer die
   Zuordnung stand vor der Suche fest, weil sie sonst nach dem Ergebnis
   haette gewaehlt werden koennen. Das Pruefprogramm prueft seitdem
   genau so streng wie der Prompt, weil es sonst verbotene Zitate als
   korrekt zaehlen wuerde. Eine zweite Fassung des Prompts formuliert
   die zwei verletzten Zitatregeln deutlicher. Sie wurde an denselben
   20 Pull Requests erprobt und nach einer vorab festgelegten Regel fuer
   den Volllauf uebernommen, weil sie etwas seltener falsch zitiert.
   Der Vorsprung ist klein. Eine dritte Fassung gibt es nicht, weil eine
   weitere Umformulierung wenig verspricht und das Pruefprogramm die
   verbleibenden Fehler abfaengt.

8. Volllauf (25. und 26.09.2026): Alle 395 Pull Requests gingen mit
   Prompt v2 an gpt-5.6-terra. Sie liefen im Normalbetrieb, also eine
   Anfrage nach der anderen, nicht im geplanten Stapelbetrieb. Das hat
   der Verfasser entschieden, weil der Stapelbetrieb im Konto der
   Nutzungsstufe 1 mehrere Tage und neuen Code gebraucht haette
   (Nachtrag zu E8). Alle 395 Antworten kamen vollstaendig und als
   gueltiges JSON zurueck. Das Pruefprogramm lehnte 126 Datensaetze
   ab, meist wegen Zitaten, die ueber eine entfernte Diffzeile
   hinweg verbinden. 8 abgelehnte Zitate gehen nach der vorab
   festgelegten Regel auf das Pruefprogramm zurueck, 28 muss der
   Verfasser selbst ansehen.

9. Pruefung nach Regel 1 (27. und 28.09.2026): Vor der Zaehlung fiel
   ein Fehler in der Reihenfolge des Suchprogramms auf. Ein Zitat, das
   bei einer unveraenderten Diffzeile das fuehrende Leerzeichen
   mitkopiert, verstoesst gegen den Prompt. Das Suchprogramm lastete
   es trotzdem dem Pruefprogramm an. Deshalb wurde zuerst eine Regel
   zur Trennung festgeschrieben und committet, erst dann gezaehlt.
   Ergebnis: Keines der 8 Zitate hatte das Leerzeichen mitkopiert. Das
   Pruefprogramm duldet seitdem Leerraum am Anfang und Ende eines
   Zitats, weil der Prompt genaue Leerzeichen nur im Inneren verlangt.
   6 der 8 Zitate gelten nun als gefunden. 2 bleiben abgelehnt, weil
   ohne den Rand weniger als 10 Zeichen uebrig bleiben. Die
   Mindestlaenge stand vorher fest und wird nicht nachtraeglich
   gestrichen, weil das eine Regelaenderung nach dem Ergebnis waere.

10. Pruefung nach Regel 3 und Abschluss von Paket E (28. und
    29.09.2026): Die 28 Zitate ohne vorab festgelegte Ursache hat der
    Verfasser selbst angesehen. Die Regel dafuer stand vorher fest und
    war committet, weil die Einordnung sonst nach dem Ergebnis haette
    gewaehlt werden koennen. Alle 28 gehen auf das Modell zurueck,
    keines auf das Pruefprogramm; die Programme bleiben deshalb
    unveraendert. Meist hat das Modell einzelne Zeichen veraendert
    (18), seltener Woerter (6) oder Stuecke ueber
    eine entfernte Zeile hinweg verbunden (4). Die
    Inhalte der Zitate sind dabei in den Chat gelangt; das ist
    offengelegt. Die Zahlen des Volllaufs sind jetzt endgueltig: 124
    von 395 Datensaetzen abgelehnt, 3 wegen des Formats, 6 wegen einer
    zu hoch angegebenen Belegstaerke, 115 wegen eines Zitats. Jeder
    Beleg hat einen Link auf seine Quelle, weil die Rueckverfolgbarkeit
    ein Bewertungskriterium ist. Kosten und Laufzeit stehen in der
    Kostenschaetzung.

Warum der naechste Schritt jetzt kommt: Paket E ist abgeschlossen,
die Pruefzahlen des Volllaufs stehen fest. Der Stand ist als Git-Tag
thesis-v1.0 eingefroren, weil spaetere Aenderungen sonst nicht von dem
Stand zu trennen waeren, mit dem die Arbeit gemessen hat. Als
Naechstes kommt das lokale Modell (Paket F), nach Paket E und nicht
parallel. Es wird an denselben Faellen mit denselben Programmen
geprueft; deshalb brauchte es diese endgueltigen Zahlen. Der
Kontrollpunkt ist Di 29.09.: Laeuft das lokale Modell dann nicht an
einem Pilotfall, wird am selben Tag entschieden, wie FF3 mit
kleinerem Umfang beantwortet wird.

Geschrieben sind Teile von Kapitel 2, Abschnitt 4.1 und Anhang A.
Abgabe am 15.10.2026, intern am 13.10.2026. Der Plan hat keine
Reserve. Groesstes Risiko ist das lokale Modell, Kontrollpunkt 29.09.


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
- Umfangsangaben fuer LaTeX-Text nennt Claude erst nach einer
  Testuebersetzung. In Paket C Anhang A lag die Schaetzung vorab
  deutlich zu niedrig (10.09.2026).
- Git-Befehle mit Pfaden wie thesis/thesis.tex setzen den
  Repository-Stamm als Arbeitsverzeichnis voraus. Wer im Ordner
  thesis/ steht, schreibt thesis.tex (11.09.2026). 
- Nach jeder Einfuegung in thesis.tex prueft vor dem Commit ein grep
  mit Suchtext ohne Umlaute die Einfuegestelle. Eine abweichende
  Zeilenzahl im git diff --stat ist ein Stoppsignal. In Paket C
  Anhang A fehlte dadurch eine Zeile im Vorspann (11.09.2026).
- Commits werden gebuendelt: ein Commit je abgeschlossenem
  Teilergebnis, nicht je Einzelschritt (Wunsch des Verfassers,
  28.09.2026). Ausnahme: Eine Regel, die vor einer Zaehlung feststehen
  muss, wird vorher einzeln committet, weil nur so ihr Zeitpunkt
  belegt ist. Qualitaet und Verstaendlichkeit gehen vor Tempo.
- Codeaenderungen liefert Claude als Patchdatei mit SHA-256-Summe. Der
  Verfasser prueft die Summe und fuehrt git apply --check vor git apply
  aus, weil so beim Kopieren kein Zeichen verloren geht. Bewaehrt am
  27.09.2026.
- Vor jedem Pruefungslauf nennt Claude die erwarteten Zahlen und sagt,
  was daran unsicher ist, weil eine Abweichung sonst unbemerkt bliebe.
  Eine Abweichung wird gemeldet und erklaert, nicht nachtraeglich
  passend gemacht (27.09.2026: 2 Zitate mehr als erwartet, Grund war
  die vorab festgelegte Mindestlaenge).
- Aendert ein Schritt mehr als drei Stellen in bestehenden Dateien,
  darf Claude die Ersetzungen als Python-Skript liefern: mit altem und
  neuem Wortlaut, Abbruch vor dem Schreiben, wenn ein alter Wortlaut
  nicht genau einmal vorkommt, Werte aus der Quelle statt abgetippt,
  SHA-256-Summe. Das Skript liegt ausserhalb des Repositorys. Grund:
  Handanweisungen fuer viele Stellen sind fehleranfaellig. Steht so in
  der Projektanweisung (Ersetzungen per Skript), hier seit 29.09.2026.
- Ausgaben, die Inhalte von Pull Requests zeigen (etwa --only des
  Anzeigeskripts), gehen nicht in den Chat; zurueckgemeldet werden nur
  Zahlen. Am 28.09.2026 sind die Inhalte aller 28 Zitate der Regel 3
  trotzdem in den Chat gelangt (Nachtrag zu E10 vom 28.09.2026,
  Teil 4). Claude hat daraufhin keine Zuordnung vorgeschlagen.

## Kuerzel

Doppelt belegte Kuerzel - immer mit Klartext verwenden:
- E1, E2, E3 bezeichnen zwei verschiedene Dinge.
  (1) Die drei Verfahrensregeln der Formatauswahl in
      docs/formatauswahl.md Abschnitt 5 (Z. 299 bis 316):
      Ausschlussregel E1: Eine Ebene erhaelt die Rolle verpflichtend
      nicht, wenn K9 mit 0 bewertet ist; die Rolle optional bleibt
      moeglich. Auch in C4, entscheidungen.md Z. 742.
      Vorrangregel E2: Bei aehnlichem Profil entscheidet zuerst K9,
      dann K3, dann K8. Angewandt in C5, entscheidungen.md Z. 855.
      Dokumentationsregel E3: Jede Rollenzuweisung wird mit
      hoechstens drei Saetzen begruendet.
  (2) Die Entscheidungen aus Paket E in docs/entscheidungen.md:
      E1 Datenmodell, E2 Form der Evaluation, E3 API-Budget, alle
      vom 15.09.2026.
- B-Nummern bezeichnen zwei verschiedene Dinge.
  (1) B1 bis B9 = Regeln der Belegstaerke aus E6,
      docs/entscheidungen.md ab Z. 1435.
  (2) B1 bis B10, B11a und B11b = Bewertungskriterien in
      eval/instrument/kriterien_v0.md vom 21.09.2026, etwa
      B8 Formatkonformitaet, B9 Quellennachvollziehbarkeit,
      B10 Sprachliche Kriterien. Der Nachtrag zu E2 vom 22.09.2026
      meint diese Kriterien.
- Weg A: In C6 (entscheidungen.md Z. 1125) eine verworfene Form von
  Anhang A, nur mit Notentabelle. Im Zeitplan W10 und im Commit
  d858275 dagegen die Art der Bewertung aus dem Nachtrag zu E2 vom
  22.09.2026 (entscheidungen.md Z. 2010): Die Bewertungskriterien
  B8 (Schema), B9, B10 und Teile von B3 prueft ein Programm, die
  uebrigen bewertet der Verfasser von Hand. Dort steht der Name
  "Weg A" nicht.

Weitere Kuerzel:
Paket A bis I = Arbeitspakete (je ein Chat). A1 bis A8 = Aufgaben in
Paket E; A8 = Pilotlauf mit 20 Pull Requests, Teilschritte 1 bis 12.
C, D, E mit Nummer = Entscheidungen der Pakete C, D, E in
docs/entscheidungen.md, ausser den oben genannten Regeln E1 bis E3.
K1 bis K10 = Kriterien der Formatauswahl, docs/formatauswahl.md
Abschnitt 2. R1 bis R11 = Regeln fuer die Noten, dort Abschnitt 4.
Ebenen (a) bis (d) = die vier Ebenen einer Anforderung: (a) Sicht,
User Story; (b) Satzmuster, EARS; (c) Verbindlichkeit, RFC 2119;
(d) Qualitaetsregeln, 29148.
S1 bis S6 = Schichten der Stichprobenziehung in draw_sample.py.
L01 ff. = Quellen-IDs in literatur/literaturmatrix.md.
W1 bis W11 = Wochen des Zeitplans.
person_NN = Platzhalter fuer Personen (E9, gilt auch in der Arbeit).
Die Kennungen A01 ff. werden nicht verwendet (Nachtrag zu E9 vom
21.09.2026).
Ursachennamen wie hunk_header oder spans_removed_line = Kategorien
des Suchprogramms src/extract/diagnose_excerpts.py fuer abgelehnte
Zitate; Liste und Bedeutung im Kopf des Programms.
Regel 1 bis 3 = Zuordnung einer Ablehnung: 1 Pruefprogramm schuld,
2 Modell schuld, 3 der Verfasser sieht nach (Nachtrag zu E10 vom
24.09.2026).
v1, v2 = Fassungen des Prompts unter prompts/.
H1 = Hinweis des Anzeigeskripts src/extract/inspect_excerpts.py, ob ein
Zitat ohne Rand-Leerraum im Quellblock des Modells vorkommt (Nachtrag
zu E10 vom 28.09.2026, Teil 3).
Unterarten pruefprogramm, zusammengesetzt, umformuliert, zeichen,
ohne_gegenstueck = Art der Abweichung eines Zitats nach Regel 3,
festgelegt in Teil 3 und Teil 3a desselben Nachtrags.
Neue Kuerzel duerfen keinen dieser Namen wiederverwenden.

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS-27.0-arm64 (laut Manifest, berichtigt 24.09.2026) - Python 3.14.6 (Homebrew) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)
Pakete laut requirements.txt: requests 2.34.2, pytest 9.1.1, jsonschema 4.26.0 sowie 
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

Arbeitspaket C (Formatauswahl) vollstaendig abgeschlossen am
11.09.2026, siehe Abschnitt "Aktuell". Darin Schritte 1 bis 3 sowie 4a und 4b
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

Arbeitspaket E (Prompt und API-Modell) abgeschlossen am 29.09.2026:
- Entscheidungen E1 bis E11 mit Nachtraegen in docs/entscheidungen.md
- Prompt v2, Aufrufprogramm run_extraction.py, Pruefprogramm
  validate_output.py und Suchprogramm diagnose_excerpts.py mit Tests
- Pilotlaeufe 2026-09-22_pilot und 2026-09-24_pilot_v2 sowie Volllauf
  2026-09-25_full_v2 mit 395 Vorgaengen, Manifeste committet
- Pruefung des Volllaufs nach Regel 1 und Regel 3 abgeschlossen
  (Nachtrag zu E10 vom 27.09.2026 und vom 28.09.2026, Teil 1 bis 4)
- Links je Beleg (Teilschritt 10 von A8) und Messwerte des Volllaufs
  in experiments/kostenschaetzung.md, Abschnitt 6.3
- Stand am Ende von Paket E als Git-Tag thesis-v1.0 eingefroren

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
data/processed/model_input_2026-09-19.jsonl - 395 Quellbloecke, 8,5 MB
  Manifest versioniert unter demselben Namen mit .manifest.json
  Ersetzt model_input_2026-09-15.jsonl, siehe E9.
data/interim/mention_map.json - Zuordnung der 34 Anmeldenamen,
  lokal, durch .gitignore ausgeschlossen
data/processed/extraction_2026-09-22_pilot.raw.jsonl - 20 vollstaendige
  Antworten der Schnittstelle, lokal
  SHA-256 5209e484ed6ec2fd88277b4832469afd3104ac5b9df5593b0bce72dbb663ac0b
data/processed/extraction_2026-09-22_pilot.jsonl - 20 Modellausgaben,
  lokal
  SHA-256 6bfda3cfae8c1d38f7f7a243d5dd91cc38f5736268e130e0bc1fca6bbd871602
  Manifest versioniert unter demselben Namen mit .manifest.json.

data/processed/extraction_2026-09-25_full_v2.raw.jsonl - 395 vollstaendige
  Antworten der Schnittstelle, lokal
  SHA-256 319b909fe07119184986794e31224ae79870587fdf204bfef07f07366d7456da
data/processed/extraction_2026-09-25_full_v2.jsonl - 395 Modellausgaben,
  lokal
  SHA-256 3dbc74b24438cac24feba080eca69ef66a4b495b4f7fd677de0f22d7d91e569d
  Manifest versioniert unter demselben Namen mit .manifest.json.

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

373 Tests, ausfuehren aus der Projektwurzel:
python -m pytest tests/ -v
Zuletzt gruen am 29.09.2026 (373 passed) unter Python 3.14.6,
abgelesen vom Aktualisierungsskript.

tests/conftest.py setzt den Importpfad auf src/collect, src/prepare
und src/extract. Ohne diese Datei finden die Tests die Module nicht.

Bereiche: test_resume.py (Wiederaufnahme), test_outcome.py,
test_normalisation.py, test_jsonl_io.py, test_truncation.py,
test_schema_validation.py (70 Tests, Schema, Belegstaerke und
Zitatregeln des Prompts, seit 27.09.2026 auch Leerraum am Rand),
test_prompt_input.py (21 Tests, Auswahl und Budget),
test_prompt_files.py (30 Tests, Prompt v1 und v2 gegen Schema; v2
darf nur die Regeln fuer Zitate aus Diffs aendern),
test_pseudonymise.py (28 Tests, Ersetzung von Erwaehnungen),
test_draw_sample.py (15 Tests, Schalter --sizes und --exclude, E10 a),
test_run_extraction.py (26 Tests, Aufrufprogramm ohne Netz, mit
erfundenen Antworten), test_diagnose_excerpts.py (51 Tests,
Ursachensuche fuer abgelehnte Zitate), test_inspect_excerpts.py
(35 Tests, Anzeige und Auszaehlung fuer Regel 3),
test_breakdown_rejections.py (17 Tests, Ablehnungen nach
Art), test_cost_report.py (18 Tests, Abschnitt 6.3 aus dem
Manifest), test_add_links.py (18 Tests, Links je Beleg). Die
beiden neuen Dateien vom 21. und 22.09.2026, test_diagnose_excerpts.py
und die vier Dateien vom 28.09.2026 setzen ihren Importpfad selbst.
Die vier Dateien vom 28.09.2026 wurden in der Umgebung von Claude
gegen 34 absichtlich eingebaute Fehler geprueft: 33 erkannt, einer
ohne Wirkung, weil eine zweite Pruefung denselben Fall abfaengt.
Nicht abgedeckt: Netzschicht in github_api.py, Auswertungsskripte,
draw_sample.py ausserhalb der neuen Schalter (siehe D4a).

## Ungepruefte Beobachtungen

- Ob die 321 Nummernluecken alle Issues sind: plausibel, nicht gemessen.
- Zu PR 344: vermutet ein Review im Zustand pending, nur seinem
  Verfasser sichtbar. Nicht pruefbar.
- PR 674 und 676 sind fast gleich gross (574/575 Dateien) - vermutlich
  zwei Anlaeufe derselben Umbauaktion. Nicht geprueft.
- Warum author_association nie OWNER oder MEMBER annimmt: unbekannt.
- Ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben enthalten:
  Vermutung aus D7, nicht gemessen. Relevant fuer FF4.
- Erledigt durch E5: Quellblock hoechstens 80 000 Zeichen, kein
  Vorgang scheitert an der Kontextgroesse des Modells (E8).
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

Paket C, Schritt 5 abgeschlossen am 08.09.2026, Schritt 6 am
09.09.2026. Die Rollenzuweisung und die Formatentscheidung stehen als C5 in
docs/entscheidungen.md, der Abschnitt 4.1 steht in
thesis/thesis.tex. Ergebnis: die Ebenen (b) EARS und (d)
Qualitaetsregeln sind verpflichtend, die Ebenen (a) und (c) werden
nicht verwendet. Das Zielformat heisst EARS+29148.

Paket C ist am 11.09.2026 abgeschlossen. Anhang A enthaelt die
gekuerzten Einzelbegruendungen zu allen zehn Kriterien, K1 bis K5 aus
Durchgang 1 und K6 bis K10 aus Durchgang 2. Er steht nach dem
Literaturverzeichnis; Abschnitt 4.1.3 verweist mit dem Label
cha:anhang-einzelbegruendungen darauf. Die Uebersetzung laeuft ohne
Fehler und ohne undefinierte Verweise, das Dokument hat 54 Seiten,
Anhang A die Seiten 39 bis 50. Der Verfasser hat den Entwurf gelesen
und geprueft.

Anhang A enthaelt keine Note, die nicht schon in Abschnitt 10 von
docs/formatauswahl.md oder im Formulierungsprotokoll steht. Bei K6
und K9 geht er in drei Punkten ueber Abschnitt 10 hinaus, weil dort
keine Einzelbegruendungen stehen: eine Vorbemerkung zur Herkunft der
gemessenen Noten, die Tabelle A.1 mit den sechs
Formulierungsversuchen sowie je ein zusaetzliches Gegenargument bei
K6 Ebene (b) und K9 Ebene (c). Festgehalten im Nachtrag zu C6.

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

Erledigt am 08.09.2026: Die Zellen der Ebene (c) wurden an den
Volltexten von RFC 2119 und RFC 8174 gegengeprueft. Die Lesenotiz
literatur/notizen/bradner_1997_rfc2119.md enthielt keinen Fehler.
Vier Ungenauigkeiten entstanden erst beim Verkuerzen in die Zellen
und sind berichtigt; keine Note aendert sich. Am 09.09.2026 wurden
zusaetzlich Mavin et al. 2009 und Lucassen et al. 2016 im Volltext
geprueft. Damit sind alle Belegstellen der Matrix und des
Abschnitts 4.1 an den Quellen kontrolliert. Am 10.09.2026 kam
Mavin/Wilkinson 2010 hinzu; dabei wurde ein falscher
Abschnittsverweis in Abschnitt 4.1 berichtigt. Damit liegt zu jeder
in Kapitel 2 und Abschnitt 4.1 zitierten Quelle der Volltext vor
und ist geprueft.

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

Paket E begonnen am 15.09.2026, abgeschlossen am 29.09.2026. Elf
Entscheidungen sind gefallen.
E11 Denkaufwand, Schemapruefung beim Anbieter und Prompt-Version fuer
den Volllauf (24.09.2026) und E10 Rahmen des Pilotlaufs kommen zu den
folgenden neun hinzu:
E1 Datenmodell, E2 Evaluationsform, E3 API-Budget, E4 Auswahlregel,
E5 Budget der Modelleingabe, E6 Belegstaerke, E7 Prompt Version 1,
E8 Modellwahl, E9 Ersetzung von Erwaehnungen. Dazu Nachtraege zu C5,
E1 und E6.

Stand der Aufgaben in Paket E:
- A1 bis A5 fertig und committet.
- A6 Prompt Version 1 abgeschlossen am 17.09.2026. Dateien:
  prompts/extraction_system_v1.md, prompts/extraction_user_v1.md,
  src/extract/prompt_files.py, tests/test_prompt_files.py.
- A7 Modellwahl und Kostenschaetzung abgeschlossen am 19.09.2026.
- A8 Pilotlauf abgeschlossen am 24.09.2026. Teilschritt 10 (Links)
  am 28.09.2026 fuer den Volllauf nachgeholt, Variante B (Nachtrag zu
  E10 vom 28.09.2026, Teil 4). Datei lokal:
  data/processed/extraction_2026-09-25_full_v2.links.jsonl,
  2 711 Zeilen, SHA-256 e5ba8c6c9d09c1da70638ce1f7d9e5d01ac77cc6bb9614bdb1b5f0a43a06a187.
  Fuer die Pilotlaeufe nicht erzeugt; bei Bedarf mit demselben
  Programm. Stand der Teilschritte 1 bis 8 vom 22.09.2026:
  Festgelegt in E10 mit Nachtraegen zu
  E2, E9 und E10. Kriterienliste eval/instrument/kriterien_v0.md vor
  dem ersten bezahlten Aufruf committet. Pilotstichprobe
  docs/sample_pilot_a8.md, 20 Vorgaenge, Startwert 20260921, ohne die
  zwoelf Faelle aus Paket C. Aufrufprogramm
  src/extract/run_extraction.py mit config/api_run.toml.
  Lauf 2026-09-22_pilot: 20 von 20 beantwortet, keine abgeschnitten,
  alle 20 gueltiges JSON, store bei allen 20 von der Schnittstelle als
  false bestaetigt. Messwerte (Token, Dauer, Kosten) nur im Manifest
  data/processed/extraction_2026-09-22_pilot.manifest.json.
  validate_output.py: 5 von 20 Datensaetzen abgelehnt, alle an der
  Zitatpruefung, alle bei Zitaten aus Diffs (PR 71, 86, 166, 299, 316).
  Schema- und Belegstaerkepruefung bestanden alle 20. Ursache der
  Ablehnungen ungeklaert: Werkzeug oder Modell.
  Ausnahme von der Regel "neue Kennung nach Programmaenderung": Die
  Antwort zu PR 64 stammt aus dem Probeaufruf vor der Korrektur der
  Kostenrechnung. Die Korrektur betrifft nur die Nachberechnung aus
  der Rohdatei, nicht die Anfrage. Festgehalten im Nachtrag zu E10 vom
  24.09.2026, zusammen mit dem Laufdatum laut Manifest (PR 64 am 22.09.,
  die uebrigen 19 am 23.09.).
  Teilschritt 9, Ursachen: Das Suchprogramm
  src/extract/diagnose_excerpts.py ordnet jedes abgelehnte Zitat einer
  Ursache zu und gibt keine Inhalte aus. Die Regel dazu stand vor der
  Suche fest (Nachtrag zu E10 vom 24.09.2026). Ergebnis: alle
  Ablehnungen nach Regel 2 (Modell), keine nach Regel 1.
  validate_output.py prueft seit dem 24.09.2026 nach den Zitatregeln
  des Prompts (Sperre an entfernten Zeilen und @@-Zeilen, bei
  Review-Kommentaren nur der Text), weil es sonst verbotene Zitate als
  korrekt zaehlte. Dadurch lehnt es im Lauf v1 mehr ab als am 22.09.
  Prompt v2 (prompts/extraction_system_v2.md, Vorlage
  extraction_user_v2.md unveraendert) fasst die Regeln zu @@-Zeilen
  und entfernten Zeilen deutlicher. Lauf 2026-09-24_pilot_v2, Manifest
  committet. Nach der vorab festgelegten Uebernahmeregel gilt v2 fuer
  den Volllauf (E11 c); config/api_run.toml steht auf v2. Keine
  Version 3 (E11 d). Eine weitere Ursachensuche gibt es nur mit einem
  neuen, schriftlich begruendeten Anlass.
  Teilschritt 11: Messwerte beider Laeufe und Hochrechnung fuer den
  Volllauf in experiments/kostenschaetzung.md, Abschnitt 6. Laufzeit:
  Summe von duration_seconds in den Manifesten. Alle Zahlen zu
  Ablehnungen und Ursachen stehen in E11 und im Nachtrag zu E10 vom
  24.09.2026, nicht hier.
  Beobachtung fuer Kapitel 6 und 7: Das Modell gibt Backslashes in
  LaTeX-Ausdruecken aus Python-Kommentarbloecken nicht verlaesslich
  wieder (PR 316 und PR 294, E11 e).

Am 19.09.2026 wurde die Modelleingabe neu gebaut, weil Erwaehnungen
von Anmeldenamen ersetzt werden (E9). Gueltig ist
data/processed/model_input_2026-09-19.jsonl mit 395 Quellbloecken und
8 533 169 Zeichen. 34 Anmeldenamen wurden ersetzt; im Fliesstext
steht keine unersetzte Erwaehnung mehr. Nachgezaehlt vom Verfasser.

OpenAI-Zugang eingerichtet am 21.09.2026: Projekt qrisp-re-thesis,
Schluessel als OPENAI_API_KEY in .env, hartes Limit und Datenfreigabe
wie im Nachtrag zu E10. Seit dem Nachtrag zu E8 liegt das harte
Limit fuer Organisation und Projekt bei 35 US-Dollar. Das Schema
person_NN aus E9 gilt auch fuer den Text der Arbeit (Nachtrag zu E9
vom 21.09.2026).

Volllauf 2026-09-25_full_v2, Paket E: Kein Stapelbetrieb, sondern
Normalbetrieb, Entscheidung des Verfassers (Nachtrag zu E8), weil
der Stapelbetrieb in Stufe 1 mindestens drei Stapel mit je bis zu 24
Stunden Frist und neuen Code gebraucht haette. Liste aller 395
Vorgaenge: docs/sample_full_run_e.md, erzeugt mit draw_sample.py und
vollen Schichten, ohne Codeaenderung. Probelauf mit 5 Vorgaengen am
25.09., die uebrigen 390 am 26.09.2026 nach vorab festgelegten
Bedingungen. Ergebnis laut Programm: 395 von 395 beantwortet, keine
abgeschnitten, 395 gueltige JSON-Objekte, kein Aufruf wiederholt.
Konfiguration und Systemanweisung haben dieselben Pruefsummen wie im
Lauf 2026-09-24_pilot_v2; fuer diese 20 Vorgaenge liegen damit zwei
Durchgaenge mit gleichen Einstellungen vor (Material fuer FF3,
Konsistenz). Token und Kostenobergrenze stehen im Manifest.
Abrechnung laut Konto, abgelesen am 26.09.2026: Gesamtverbrauch
23,80 US-Dollar, davon vor dem Volllauf 2,40. Pruefung mit
validate_output.py und diagnose_excerpts.py, beide Stand f9eef00:
126 von 395 Datensaetzen abgelehnt, darunter PR 796 wegen des
fehlenden Feldes requirements (Formatfehler des Modells). 214
abgelehnte Zitate: Regel 1 (Pruefprogramm) 8, Regel 2 (Modell) 178,
Regel 3 (Verfasser sieht ein) 28. Stand nach Regel 1 am 27.09.2026
(Nachtrag zu E10, Rahmen des Pilotlaufs, vom 27.09.2026, Teil 1 und
2; dort alle Zahlen und Commits): 124 von 395 Datensaetzen
abgelehnt, 208 von 2 711 Zitaten, davon Regel 1: 2, Regel 2: 178,
Regel 3: 28.
validate_output.py duldet seitdem Leerraum am Rand eines Zitats;
beide Programme nutzen dieselbe Pruefung. Nach Regel 3 am 28. und
29.09.2026 gehen alle 28 auf das Modell zurueck. Endgueltig: Regel 1
2, Regel 2 206 von 208 abgelehnten Zitaten. Ablehnungen nach der
ersten verletzten Pruefung: Schema 3, E6 6, Zitat 115 (Nachtrag zu
E10 vom 28.09.2026, Teil 4; dort alle Zahlen).

Naechste Schritte in dieser Reihenfolge:
1. Paket F (lokales Modell), nach Paket E und nicht parallel
   (Entscheidung des Verfassers vom 28.09.2026). Zu Beginn den
   Kontrollpunkt vom Di 29.09. pruefen: Laeuft das lokale Modell nicht
   an einem Pilotfall, am selben Tag entscheiden, wie FF3 mit
   kleinerem Umfang beantwortet wird (Zeitplan, Risiko 1).
2. Modellvergleich FF3: die sechs Messgroessen in Paket F vorab
   festlegen. Material fuer die Unbelegtheitsrate: die Zitatablehnungen
   nach Regel 2 mit Ursachen und Unterarten und die Anforderungen mit
   zu hoch angegebener Belegstaerke nach E6 (Zahlen im Nachtrag zu E10
   vom 28.09.2026, Teil 4). Berichtigt am 29.09.2026: Die fruehere
   Fassung nannte nur die Unterart ohne_gegenstueck, die im Volllauf
   nicht vorkommt. Welche Ablehnungen als unbelegt zaehlen, legt die
   Definition der Messgroesse in Paket F fest.
3. Phase 2 der Literatursuche fuer Kapitel 3, verkleinert.
4. Erledigt am 29.09.2026: Abschlusscommit von Paket E und Tag
   thesis-v1.0 in der Commit-Liste von Paket E nachgetragen.
5. Nicht blockierend, aus Paket C uebernommen: zehn Overfull hboxen
   in Anhang A (Korrekturdurchgang 12.10.) und der Platzhalter zum
   Datenmodell in 4.1.4. Der Platzhalter kann jetzt gefuellt werden;
   das Datenmodell steht als E1, E6 und der Nachtrag zu E1 fest.

## Getroffene Entscheidungen

Vollstaendig in docs/entscheidungen.md. Kurzfassung:

- Repository privat. Nach Abgabe umstellbar.
- R11 (07.09.2026): Skalenstufe 2 bemisst sich am Vorhandensein und
  an der Reichweite einer Regel, nicht an einem Wirksamkeitsnachweis.
- Zuordnung von 29148 Abschn. 5.2.4 auf drei Ebenen (07.09.2026);
  Ebene (c) wird nur an den Schluesselwoertern gemessen.
- D4a (07.09.2026): keine automatischen Tests fuer draw_sample.py.
  Stattdessen Wiederholungslauf am 08.09.2026, Ergebnis identisch.
- E2 (15.09.2026, mit dem Betreuer abgestimmt): Evaluation als
  Selbstbewertung des Verfassers an einer neuen, ueberschneidungs-
  freien Stichprobe, ergaenzt um einen Fundstellenvergleich mit den
  zwoelf Faellen aus Paket C. Bewertung durch Qrisp-Team und
  Betreuer erst nach der Abgabe. Die Abweichung vom Expose
  (Meilenstein M5 in Woche 9) ist abgestimmt, siehe Nachtrag zu E2.
- FF3: Dasselbe Modell als Werkzeug und Evaluationsgegenstand waere
  eine Bedrohung der Konstruktvaliditaet. Mit E8 (Modell von OpenAI)
  entfaellt sie, weil Claude nur Werkzeug ist.
- E1 (15.09.2026): Datenmodell der Ausgabe in drei Ebenen. Schema in
  config/requirement_schema_v1.json, abgeloest durch v2.
- E3 (15.09.2026): API-Budget hoechstens 150 Euro.
- E4 (15.09.2026): Modelleingabe ohne Programme und ohne offene
  Vorgaenge, 395 von 476. Entwuerfe, fehlende Beschreibung und
  fehlende Codeaenderung schliessen nicht aus, weil Titel und Diff
  auch dann eine Quelle bleiben.
  Programme ausgeschlossen, weil sie fast nur Versionen anheben oder
  nie uebernommen wurden (Nachtrag zu E4 vom 23.09.2026).
- E5 (15.09.2026): Budget der Modelleingabe. Diff-Ausschnitt je
  Review-Kommentar hoechstens 500 Zeichen, Quellblock hoechstens
  80 000 Zeichen, weil der Diff-Ausschnitt ueberwiegend Code
  wiederholt, der schon im Diff der Datei steht. D1 bleibt
  unveraendert. Keine Anmeldenamen im Block, nur author_association.
  Durch E9 praezisiert: das galt nur fuer die Kopfzeilen, im Text
  standen weiterhin Erwaehnungen.
- E6 (15.09.2026): Belegstaerke wird aus Deckung und Aussageform
  berechnet, Regeln B1 bis B9. Schema Version 2 laesst bis zu drei
  Belege je Anforderung zu.
- E7 (17.09.2026): Prompt Version 1 in zwei Dateien unter prompts/,
  englisch, modellneutral, ohne vollstaendiges Beispiel. Quellblock
  zwischen festen Begrenzungszeilen.
- E8 (19.09.2026): API-Modell ist gpt-5.6-terra. Pilot im
  Normalbetrieb, Volllauf im Stapelbetrieb. Kostenschaetzung in
  experiments/kostenschaetzung.md. Der Volllauf ist geaendert, siehe
  Nachtrag zu E8.
- E9 (19.09.2026): Erwaehnungen von Anmeldenamen werden im Fliesstext
  durch @person_NN ersetzt, nie im Diff. Ausnahmeliste jaspify, jax,
  pytest, rus. Zuordnung lokal in data/interim/mention_map.json.
- E10 (21.09.2026): Rahmen des Pilotlaufs A8. 20 Vorgaenge,
  Startwert 20260921, ohne die zwoelf Faelle aus Paket C. Die Regel
  fuer E11 (Denkaufwand) stand vor dem Lauf fest und nutzt nur
  maschinell messbare Werte, weil ein Qualitaetsurteil an 20 Faellen
  ohne Bewertungsbogen nicht belastbar waere.
- Nachtrag zu E10 (24.09.2026): Die Regel fuer die Ursache einer
  Ablehnung stand vor der Suche fest, weil sie sonst nach dem Ergebnis
  gewaehlt werden koennte. Massstab ist der Prompt. Das Pruefprogramm
  prueft seither genau nach den Zitatregeln des Prompts, weil es sonst
  nachsichtiger mass, als der Prompt verlangt.
- E11 (24.09.2026): Denkaufwand bleibt medium, keine Schemapruefung
  beim Anbieter, Prompt v2 fuer den Volllauf, keine Version 3. Weil die
  vorab festgelegten Regeln erfuellt sind und eine Hilfe beim Format den
  Messwert fuer die Formatkonformitaet (FF2) verfaelschen wuerde.
- Nachtrag zu E8 (24.09.2026): Volllauf im Normalbetrieb statt im
  Stapelbetrieb, Entscheidung des Verfassers. Weil der Stapelbetrieb
  in Nutzungsstufe 1 mindestens drei Stapel mit je bis zu 24 Stunden
  Frist und neuen Code gebraucht haette, und weil Pilot und Volllauf
  so denselben Aufrufweg nutzen. Hartes Limit 35 US-Dollar.
- Nachtrag zu C5 (17.09.2026): drei Sprachregeln aus 29148
  Abschn. 5.2.4 kommen zur Ebene (d) hinzu.
- Nachtrag zu E1 (17.09.2026): sechster Typwert human_factors.
- Nachtrag zu E6 (17.09.2026): complex braucht Vorbedingung und
  Ausloeser.
- Kapitel nicht in Einzeldateien. Alles in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard.
- API-Version 2022-11-28, explizit, in config/collect.toml.
- Speicherformat JSONL. Keine Datensaetze im Repository, Nachweis ueber
  SHA-256 im Manifest.
- Datenminimierung: vom user-Objekt nur login, weil nur er die
  Rueckverfolgbarkeit sichert. Personen erscheinen in der Arbeit als
  person_NN aus E9; A01 ff. und docs/pseudonyme.csv entfallen
  (Nachtrag zu E9 vom 21.09.2026).
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
- C5 (08.09.2026): Rollenzuweisung und Zielformat EARS+29148.
  Ebenen (b) und (d) verpflichtend, (a) und (c) nicht verwendet.
  Schluesselwortkonvention nach 29148 Abschn. 5.2.4; RFC 2119
  nicht uebernommen. Die Verbindlichkeit wird als Konvention
  gesetzt und nicht rekonstruiert. Ausschnitt der Ebene (d):
  5.2.7 vollstaendig, fuenf der neun Merkmale aus 5.2.5, drei
  Attribute aus 5.2.8.2. Rolleninformation ins Attribut Rationale.
- Weg C (09.09.2026, C6): Die Notentabelle steht in Kapitel 4, die
  Einzelbegruendungen kommen gekuerzt in Anhang A. Anhang A steht
  nach dem Literaturverzeichnis (10.09.2026). Kuerzungsregeln und
  Form eines Eintrags stehen in C6.
- K10 fuer Ebene (c) bleibt bei Note 1 (08.09.2026). Die Matrix
  soll nicht vom Ergebnis der Entscheidung abhaengen, die sie
  stuetzt. Der Vorbehalt ist durch einen datierten Nachtrag ersetzt.

## LaTeX-Konventionen

Zitierschluessel in thesis.bib: iso29148, mavin2009ears, mavin2010bigears,
wilkinson2018mitigation, lucassen2016qus.
Zitierschluessel in online.bib: rfc2119, rfc8174.

Labels in thesis.tex (Stand 11.09.2026, vollstaendig):
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
Abschnitt 4.1 (seit 09.09.2026): sec:formatauswahl ·
subsec:auswahlverfahren · subsec:formulierungsprobe ·
subsec:bewertungsergebnis · subsec:rollenzuweisung ·
subsec:formatauswahl-grenzen · tab:kriterienkatalog ·
tab:schichtung · tab:deckung · tab:referenzinhalte ·
tab:entscheidungsmatrix
Anhang A (seit 11.09.2026): cha:anhang-einzelbegruendungen ·
sec:anhang-k1 bis sec:anhang-k5; Durchgang 2 fuegt sec:anhang-k6
bis sec:anhang-k10 an.

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
Formatentscheidung, Stand 09.09.2026 (Einzelheiten in C5):
- (a) nicht verwendet, (b) verpflichtend, (c) nicht verwendet,
  (d) verpflichtend im Ausschnitt.
- Zielformat EARS+29148: englischsprachiger EARS-Satz mit
  durchgehendem shall, geprueft gegen 29148 Abschn. 5.2.7 und
  fuenf Merkmale aus 5.2.5, mit den Pflichtfeldern Identification,
  Rationale und Type.
- Maschinell pruefbar sind Muster, Klauselreihenfolge, shall, das
  Fehlen anderer Modalverben und die Wortklassen aus 5.2.7. Die
  inhaltlichen Merkmale aus 5.2.5 sind es nicht.
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
  Note 0. Der frueher hier stehende Zusatz, die Regel veraendere nur
  die Zahl und nicht die Entscheidung, ist am 11.09.2026 berichtigt
  worden. Er zaehlt nur die vier Faelle nach der schriftlichen
  Festlegung von R10; PR 371 wurde schon am 27.08.2026 nach demselben
  Grundsatz geaendert. Ohne diesen Grundsatz insgesamt waeren 5 von
  12 gedeckt, die Note laege bei 1, und E1 wuerde Ebene (c) nicht
  mehr sperren. Die Regel bleibt unveraendert; die Empfindlichkeit
  gehoert nach Kapitel 7.
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
- Umfangsfrage gegenueber dem Qrisp-Team. Stand am Ende von Paket E
  als Git-Tag thesis-v1.0 eingefroren (29.09.2026 statt wie geplant
  27.09.); alles Weitere in den Ausblick.
- Kriterienliste v1 (Skala, Regeln, Umfang der Auswahl) vor der
  ersten Bewertung, laut Zeitplan in W9 (Nachtrag zu E2 vom
  21.09.2026).
- Erledigt am 28.09.2026: Links fuer Teilschritt 10. GitHub hat je
  Kommentar einen eigenen Link geliefert; Variante B (Nachtrag zu E10
  vom 28.09.2026, Teil 4).
- Gegenpruefung der Zuordnung nach Regel 3 durch Claude: angeboten
  am 28.09.2026, bisher nicht angefordert. Sonst bleibt fuer
  Kapitel 7: eine Person ordnet zu.
- Commit d09a1df steht nicht in der Commit-Liste von Paket E; bei der
  Uebergabe am 24.09.2026 mit git log nachgetragen.
- Ab dem ersten Lauf darf die Zuordnung der Platzhalter nicht mehr
  neu vergeben werden (E9).
- Platzhalter fuer Personen in der Arbeit: person_NN aus E9, siehe
  Nachtrag zu E9 vom 21.09.2026. Offen ist nur die Regel fuer eine
  Person, die nicht in der Zuordnung steht.
- KI-Formulierung fuer vorspann.tex mit Professor abstimmen.
- Korreferent in thesis.tex eintragen (Platzhalter Zeile 23)
- Phase 2 der Literatursuche nachholen, verkleinert, bis Ende W9.
  Kapitel 3 hat sonst keine Materialgrundlage.
- Namenskonflikt: Schicht S5 in draw_sample.py spricht von "per pull
  request budget" und meint D1. Seit E5 gibt es ein zweites Budget
  mit demselben Wort. In Kapitel 5 trennen.

Inhaltlich offen:
- Ein Platzhalter in Abschnitt 4.1: Verweis auf den Abschnitt zum
  Datenmodell (4.1.4, faellt in Paket E). Der Verweis auf Anhang A
  in 4.1.3 ist am 11.09.2026 gesetzt.
- K9 Ebene (c) ist empfindlicher als bisher dokumentiert: ohne den
  Grundsatz von R10 waeren 5 von 12 Faellen gedeckt und die Note
  laege bei 1. Gehoert nach Kapitel 7, zusammen mit dem Umstand,
  dass die Noten der Ebenen (a) und (b) an je einem Fall haengen.
- Abschnitt 4.1.5 spricht von einem "Ausschnitt der Inhaltsvorgaben"
  von 29148. Der gewaehlte Ausschnitt stammt aber aus Abschn. 5.2,
  nicht aus den Inhaltsvorgaben in Abschn. 9. Formulierung pruefen.
- Abschn. 2.2.3 und Lesenotiz zu Mavin/Wilkinson 2010: Die Aussage,
  Bewertende und Umformulierende seien dieselbe Personengruppe,
  steht so nicht im Volltext. Belegt sind nur die Festlegung der
  Komplexitaetsschwelle durch die Autoren (Fussnote 3) und die
  Umformulierung durch eine fachuebergreifende Ingenieursgruppe
  (Abschnitt Method). Pruefen und gegebenenfalls abschwaechen.
- Platzhalter in thesis.tex Abschn. 2.2 veraltet: er kuendigt User
  Stories und EARS an, die inzwischen als 2.2.2 und 2.2.3
  geschrieben sind. Nur die Spezifikationsvorlagen aus 29148
  fehlen dort noch.
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
- src/analyze/draw_sample.py: Tests nur fuer --sizes und --exclude
  (E10 a). Fuer das uebrige Skript die Ausnahme von D4 in Kapitel 5
  begruenden.
- PR 711: Rolle und Systemreaktion sind die einzigen zwei Felder der
  Stichprobe, die nicht unabhaengig gegengeprueft wurden. Die
  Diff-Ansicht war dem gegenpruefenden Modell nicht zugaenglich.
  Steht im Protokoll unter "Methodischer Status".
- Vier Datumsangaben in der Aenderungshistorie von
  docs/formatauswahl.md sind auf den 26.08.2026 geschaetzt
  (Pflichtbestandteile, K9 bei Ebene (d), Erhebungsform Teil A).
  Belegt ist nur "Begonnen: 26.08.2026" im Protokoll.

Aus Paket D in spaetere Pakete uebernommen:
- Erledigt: Budget der Stufe 3 bleibt (E5, D1 unveraendert).
  Auswahlregel festgelegt (E4).
- Messen, ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben
  enthalten (Paket G, FF4).
- Erledigt: Schemavalidierung mit 54 Tests (E6).

Technisch und redaktionell:
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Di 29.09.2026
- Platzhalter in thesis.tex: Z. 20 Abgabedatum · Z. 23 Korreferent ·
  Z. 29 Abstract · Z. 39 Einleitung · Z. 443 SATZ UEBERARBEITEN ·
  Z. 508 Verweis auf die Entscheidungsmatrix ·
  Z. 903 Femmer et al. - Primaerquelle beschaffen oder Satz streichen ·
  Z. 910, 915, 921, 929, 937, 944, 951, 959 noch leere Kapitel
  Achtung: Diese Nummern sind aus dem Versatz +144 errechnet, nicht
  einzeln geprueft. Vor dem Bearbeiten nachsehen.
- Overfull hboxen, Behebung am 12.10.: vorspann.tex Z. 4-16 (86,6pt) ·
  thesis.tex Z. 263-269 (12,7pt) · Z. 288-295 (12,9pt) ·
  Z. 444-445 (14,5pt) · Z. 912 (1,4pt)
    Neu 11.09.2026: zehn Overfull hboxen in Anhang A, alle in
  Beleg-Zeilen mit mehreren Zitaten. Stand nach dem Lauf vom
  11.09.2026 mit allen Aenderungen des Tages:
  thesis.tex Z. 1626-1636 (9,76654pt) ·
  Z. 1688-1695 (9,05933pt) ·
  Z. 1697-1708 (12,99223pt) ·
  Z. 1754-1764 (9,21904pt) ·
  Z. 1878-1888 (15,40123pt) ·
  Z. 1971-1978 (9,05933pt) ·
  Z. 1980-1987 (15,40123pt) ·
  Z. 2043-2053 (9,21904pt) ·
  Z. 2101-2110 (9,21904pt) ·
  Z. 2167-2176 (15,40123pt)
  Achtung: Die Zeilenangaben der aelteren Eintraege oben stimmen mit
  dem Log vom 11.09.2026 nicht mehr ueberein. Am 12.10. neu erheben.
- Literaturverzeichnis beginnt ohne Seitenumbruch unter dem Fazit und
  fehlt im Inhaltsverzeichnis (Befund 10.09.2026). Eine Behebung
  aendert die Vorlagenstruktur und braucht Abstimmung; Paket I.
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
d63c549 Paket C Schritt 5, Formatentscheidung C5
20d4761 Abschnitt 4.1 Auswahl des Anforderungsformats
e2187b8 29148 Abschn. 5.2.7 bei K2 und K3 auf neun Aufzaehlungspunkte berichtigt
7db9ae1 Anhang A, Einzelbegruendungen K1 bis K5 (Durchgang 1)
7861f29 Anhang A, fehlende Zeile im Vorspann ergaenzt
a5a9339 Uebergabe Anhang A Durchgang 1, Entscheidung C6, KI-Protokoll
c73f63e Anhang A, Einzelbegruendungen K6 bis K10 (Durchgang 2)
9db8601 Verweis auf Anhang A in 4.1.3, zwei Berichtigungen zu EARS
feb68c6 Stand nach Abschluss von Paket C

## Commits Paket E

e0d3f66 Schema und Pruefung der strukturierten LLM-Ausgabe
d22b83b  Auswahl und Budget der Modelleingabe
cee3b7e Commit-Kuerzel aus Paket C in STATUS.md nachgetragen
b261e6f Belegstaerke wird berechnet statt behauptet
e091d7f Prompt Version 1 mit Ladeprogramm, Schema um human_factors ergaenzt
c1d53a4 14 Tests fuer die Prompt-Dateien
1a80c14 Entscheidung E7, Nachtraege zu C5, E1 und E6, KI-Protokoll
2df90fd Herkunftsangaben in E7 berichtigt
595f79f Erwaehnungen werden vor der Modelleingabe ersetzt
224dcda Manifest der Modelleingabe vom 19.09.2026
b8b9307 Entscheidungen E8 Modellwahl und E9 Ersetzung von Erwaehnungen
15cdcf1 Kostenschaetzung fuer die API-Laeufe nach E3
78122e6 Stand nach Abschluss von A6 und A7
fc31b3d STATUS.md berichtigt, Commit-Kuerzel aus Paket E nachgetragen
2ddc434 Entscheidung E10 Rahmen des Pilotlaufs, Nachtraege zu E2 und E9
b977a4f Bewertungskriterien v0 vor dem Pilotlauf festgelegt
1fa9dcf draw_sample.py um --sizes, --exclude und --title erweitert (E10)
b4b8407 Tests fuer --sizes und --exclude von draw_sample.py
c2a98e0 Pilotstichprobe A8 gezogen, Startwert 20260921
fb16642 Aufrufprogramm run_extraction.py mit Konfiguration api_run.toml (E10)
d858275 Nachtrag zu E10 (Recherche, Konto, Berichtigung) und zu E2 (Weg A)
c01f3ab Kosten mit Zuschlag fuer Cache-Schreibungen, angewandte Einstellungen im Manifest
f80a30a Kostenrechnung am echten Aufruf von Pull Request 64 geprueft
Hinweis: d858275 enthaelt zusaetzlich tests/test_run_extraction.py.
ababa14 docs: STATUS.md und KI-Protokoll nach Pilotlauf A8, Zeitplan fuer Abgabe 15.10., Lizenz-Fundstelle
9225339 docs: Manifest des Pilotlaufs 2026-09-22_pilot
d09a1df docs: Roter Faden, Kuerzel und Begruendung des Bot-Ausschlusses
5bd1499 docs: Nachtrag zu E10, Regel fuer die Ursache der Ablehnungen im Pilot
bb57a5c code: Diagnoseskript fuer abgelehnte Zitate mit 31 Tests (Nachtrag zu E10)
ec360b3 code: Pruefprogramm prueft Zitate nach den Regeln des Prompts, Diagnose angepasst (Nachtrag zu E10, Punkt 5)
1cb8849 code: Diagnose ordnet Zitate mit zwei Verstoessen der ersten verletzten Regel zu
863d045 docs: Nachtrag zu E10, Ergebnis der Ursachensuche und Regel fuer die Uebernahme von Prompt v2
8cdaaca code: Prompt Version 2 mit deutlicheren Regeln fuer Zitate aus Diffs, Konfiguration auf v2
ea9f0a4 docs: Manifest des Laufs 2026-09-24_pilot_v2 (Prompt v2)
0443533 docs: E11, Messwerte beider Pilotlaeufe und Hochrechnung fuer den Volllauf
7df8cda docs: STATUS.md und KI-Protokoll nach Abschluss von A8
da88bb6 docs: Nachtrag zu E8, Volllauf im Normalbetrieb statt im Stapelbetrieb
38dc3bb docs: Abrechnung des Laufs v2 berichtigt, Kontosumme 2,40 US-Dollar
f9eef00 docs: Liste aller 395 Vorgaenge fuer den Volllauf, volle Schichten aus draw_sample.py
8ee96a1 docs: Manifest des Volllaufs 2026-09-25_full_v2, 395 Vorgaenge
1ef4e7e docs: STATUS.md und KI-Protokoll nach Volllauf 2026-09-25_full_v2
a9eed1f docs: Nachtrag zu E10 Teil 1, Zuordnungsregel fuer edge_whitespace im Volllauf
6b379dc code: Ursache context_marker_kept im Suchprogramm, 13 Tests (Nachtrag zu E10 Teil 1)
b3cf18d code: Pruefprogramm duldet Rand-Leerraum ausser Kennzeichenrest, Tests (Nachtrag zu E10 Teil 1, Punkt 3)
8e277a6 docs: Nachtrag zu E10 Teil 2, Ergebnis Regel 1 im Volllauf
7c83268 docs: STATUS.md und KI-Protokoll nach Regel 1 im Volllauf
167f49b code: Anzeigeskript fuer Regel 3 und Aufschluesselung der Ablehnungen nach Art, 52 Tests
4742be8 docs: Nachtrag zu E10 Teil 3, Zuordnungsregel fuer Regel 3 im Volllauf
92a6803 code: Abschnitt 6.3 aus dem Manifest und Links je Beleg (Teilschritt 10), 36 Tests
8543bb9 docs: Nachtrag zu E10 Teil 3a, Auslegung von 1 b bis 1 d vor dem Ausfuellen
44c1162 docs: Abschluss Paket E, Nachtrag zu E10 Teil 4 (Regel 3), Zuordnungstabelle, Abschnitt 6.3, STATUS, KI-Protokoll, tests/README.md auf 373 Tests
Tag thesis-v1.0 auf 44c1162

## Aufruf des Ziehungsskripts

python src/analyze/draw_sample.py \
  --input data/interim/pulls_prepared_2026-08-19.jsonl

Optional: --output, --seed (Standard 20260823), --overwrite, seit E10
zusaetzlich --sizes, --exclude und --title. Ohne die drei neuen
Schalter unveraendertes Verhalten, am 22.09.2026 durch Wiederholung
der Ziehung vom 25.08.2026 geprueft.
Das Skript importiert nichts aus github_api.py und laeuft aus der
Projektwurzel. Ausgeschlossen werden Bot-Beitraege und Vorgaenge mit
outcome = open. Sechs Schichten S6 bis S1, von der seltensten zur
haeufigsten zugeordnet, jeder Datensatz nur einmal.

Lauf vom 25.08.2026: 476 gelesen, 31 Bots, 50 offen, 395 verbleibend.
Gezogen: 48, 75, 191, 371, 408, 413, 464, 533, 577, 622, 692, 711.
Lauf vom 22.09.2026 fuer den Pilot A8:
python src/analyze/draw_sample.py \
  --input data/interim/pulls_prepared_2026-08-19.jsonl \
  --output docs/sample_pilot_a8.md --seed 20260921 \
  --sizes S6=1,S5=4,S4=3,S3=3,S2=4,S1=5 \
  --exclude 48,75,191,371,408,413,464,533,577,622,692,711 \
  --title "Pilot sample for step A8 (FF1)"
Gezogen: siehe docs/sample_pilot_a8.md. Die Evaluationsstichprobe nach
E2 schliesst diese 20 und die zwoelf aus Paket C aus.

## Aufruf des Extraktionsprogramms

python src/extract/run_extraction.py --sample docs/sample_pilot_a8.md \
  --run-id 2026-09-22_pilot [--dry-run] [--limit N]

Aus der Projektwurzel. Einstellungen in config/api_run.toml, Schluessel
OPENAI_API_KEY in .env. --dry-run sendet nichts und schreibt nichts.
--limit 0 berechnet Extraktionsdatei und Manifest nur aus der Rohdatei
neu. Ein erneuter Aufruf mit derselben Kennung setzt fort und sendet
nichts doppelt. Der echte Lauf verweigert sich bei nicht committeten
Aenderungen unter src/, config/ und prompts/. Bei langen Laeufen
caffeinate -i davorsetzen; den Deckel nicht schliessen.

Pruefung der Ausgabe:
python src/extract/validate_output.py \
  --input data/processed/extraction_<Kennung>.jsonl \
  --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
  --mentions-map data/interim/mention_map.json \
  --allowlist "jaspify,jax,pytest,rus"
Ohne --allowlist werden Zitate mit @jax und Aehnlichem faelschlich
abgelehnt.

Die Prompt-Version kommt aus config/api_run.toml, seit dem 24.09.2026
v2. Laeufe bisher: 2026-09-22_pilot (v1), 2026-09-24_pilot_v2 (v2),
2026-09-25_full_v2 (v2, Volllauf, Liste docs/sample_full_run_e.md).

Ursachensuche fuer abgelehnte Zitate, gibt keine Inhalte aus:
python src/extract/diagnose_excerpts.py \
  --input data/processed/extraction_<Kennung>.jsonl \
  --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
  --model-input data/processed/model_input_2026-09-19.jsonl \
  --mentions-map data/interim/mention_map.json \
  --allowlist "jaspify,jax,pytest,rus"

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   erledigt
W3 17.-23.08. Extraktion, Formatauswahl                Paket D
                                                       erledigt 21.08.
W4 24.-30.08. LLM-Extraktion mit API-Modell
W5 31.08.-06.09. Prompt-Iteration, lokales Modell
W6 07.-13.09. Modellvergleich (Kontrollpunkt lokales Modell)
              tatsaechlich: Paket C abgeschlossen am 11.09.
              Kontrollpunkt und Modellvergleich verschoben
W7 14.-20.09. Paket E: Entscheidungen E1 bis E6 am 15.09. erledigt.
              Rest der Woche: Prompt v1, API-Budget, Modellrecherche
Plan ab 23.09.2026, neu aufgestellt wegen des Abgabetermins 15.10.2026.
Er ersetzt den Plan vom 15.09.2026 ab W8. Geschrieben wird ab sofort
parallel, nicht am Ende.

W8 21.-27.09. Paket E: A8 abgeschlossen Do 24.09., ausser den Links
              (Teilschritt 10, nach dem Volllauf).
              Fr 25.09. Stapelbetrieb umsetzen, danach Volllauf.
              tatsaechlich: kein Stapelbetrieb (Nachtrag zu E8),
              Volllauf am 25. und 26.09. erledigt.
              Paket F: lokales Modell einrichten ab Fr 25.09.
              (verschoben von Do 24.09., weil A8 den Tag brauchte)
              tatsaechlich: Paket F nach Paket E, ab Di 29.09.
              Git-Tag thesis-v1.0 am So 27.09.
              tatsaechlich: am Di 29.09., am Ende von Paket E.
              Schreiben: Kapitel 4 Rest (4.1.4 Datenmodell)
              tatsaechlich: So 27. und Mo 28.09. Pruefung nach
              Regel 1 abgeschlossen (Nachtrag zu E10 vom 27.09.).
W9 28.09.-04.10. Paket F: Laeufe des lokalen Modells an derselben
              Stichprobe, Modellvergleich FF3 bis Mi 30.09.
              Paket G: Klassifikation, Sicherheitsraster,
              Gap-Analyse FF4 von Do 01.10. bis So 04.10.
              Kriterienliste v1, Evaluationsstichprobe ziehen.
              Literatursuche Phase 2, verkleinert.
              Schreiben: Kapitel 5 Implementierung
W10 05.-11.10. Paket H: Bewertung nach Weg A Mo 05. und Di 06.10.,
              Auswertung Mi 07.10.
              Schreiben: Kapitel 6, Kapitel 3, Kapitel 7, 8 und 1
W11 12.-15.10. Mo 12.10. Korrekturdurchgang
              Di 13.10. Endkontrolle, interne Abgabe
              Mi 14.10. Puffer
              Do 15.10. Abgabe

Ueberholt am 23.09.2026, nur zur Planungsgeschichte:
Stand 11.09.2026, W6. Paket D war drei Tage vor Plan fertig. Paket C
lief vom 23.08. bis zum 11.09.2026 und ist abgeschlossen: Schritte 1
bis 6, Anhang A mit beiden Durchgaengen, der Verweis in 4.1.3 und
die Ueberschrift von Abschnitt 10 in docs/formatauswahl.md. Paket E
hat noch nicht begonnen und liegt rund zwei Wochen hinter dem Plan
fuer W4. Der Kontrollpunkt fuer das lokale Modell in W6 ist nicht zu
halten. Bis zur internen Abgabe am 30.10.2026 verbleiben sieben
Wochen; verbindlicher Abgabetermin ist der 01.11.2026.

Stand 23.09.2026, W8. A8 bis einschliesslich Pilotlauf erledigt. Offen
in Paket E: Teilschritte 9 bis 12, danach Volllauf. Der Abgabetermin
ist auf den 15.10.2026 vorgezogen. Bis zur internen Abgabe am
13.10.2026 verbleiben 20 Tage, bis zur Abgabe 22 Tage. Der Plan hat
keine Reserve ausser dem 14.10.; jede Verzoegerung verschiebt das
Schreiben.

Stand 29.09.2026, W9. Paket E abgeschlossen, die Pruefung des
Volllaufs ist endgueltig. Paket F beginnt heute, nach Paket E statt
parallel. Der Modellvergleich war bis Mi 30.09. geplant und ist damit
knapp. Bis zur internen Abgabe am 13.10.2026 verbleiben 14 Tage, bis
zur Abgabe 16 Tage.

Stand 26.09.2026, W8. Volllauf erledigt, Manifest committet. Offen in
Paket E: Regel 1 und Regel 3 der Ursachensuche, Aufschluesselung der
Ablehnungen, Abschnitt 6.3 der Kostenschaetzung, Links. Bis zur
internen Abgabe am 13.10.2026 verbleiben 17 Tage, bis zur Abgabe 19
Tage.

Stand 24.09.2026, W8. A8 abgeschlossen bis auf die Links. Paket F
beginnt einen Tag spaeter als geplant; der Kontrollpunkt Di 29.09.
bleibt. Bis zur internen Abgabe am 13.10.2026 verbleiben 19 Tage, bis
zur Abgabe 21 Tage.

Drei Risiken, in dieser Reihenfolge:
1. Lokales Modell (Paket F). Der Verfasser hat damit keine Erfahrung,
   Python 3.14 ist sehr neu. Kontrollpunkt: Bis Di 29.09. laeuft das
   lokale Modell an einem Pilotfall. Sonst am selben Tag entscheiden,
   wie FF3 mit kleinerem Umfang beantwortet wird.
2. Umfang. Pakete F, G und H liegen in zweieinhalb Wochen. Jede
   Kuerzung muss alle vier FF beantwortbar lassen und wird mit dem
   Betreuer abgestimmt. Kapitel 3 und Phase 2 der Literatursuche
   laufen verkleinert.
3. Bewertungsbogen fuer E2. Kriterienliste v0 steht seit dem
   21.09.2026, vor dem Pilot. Skala, Regeln und Umfang der Auswahl
   (Fassung v1) muessen vor der ersten Bewertung fertig sein
   (Nachtrag zu E2 vom 21.09.2026).