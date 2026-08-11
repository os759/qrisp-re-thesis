# Bearbeitungsstand

Letzte Aktualisierung: 10.08.2026
Abgabetermin: 01.11.2026 (Sonntag; intern geplant auf Fr 30.10.2026)

## Zusammenarbeit im Chat

Diese Regeln gelten fuer jeden Chat und gehen Annahmen vor.

- Claude hat kein Gedaechtnis ueber Chats hinweg. Nur was in dieser
  Datei oder im Projektwissen steht, gilt als bekannt.
- Projektwissen enthaelt ausschliesslich Unveraenderliches:
  exposee.tex und 29148-2018.pdf. Arbeitsdateien werden pro Chat
  hochgeladen, nie im Projektwissen abgelegt - dort veralten sie
  unbemerkt. Die Vorlagenkopien (thesis.tex, thesis.bib, online.bib,
  preamble.tex, hyphenations.tex, Makefile) wurden am 10.08.2026
  entfernt; sie enthielten Demo-Daten der Hochschulvorlage.
- Wenn Claude den Inhalt einer Datei braucht, muss er sie ausdruecklich
  anfordern und dabei den vollstaendigen Pfad nennen. Claude arbeitet
  nie mit einer aus dem Gedaechtnis oder aus dem Projektwissen
  rekonstruierten Fassung einer Arbeitsdatei.
- Dasselbe gilt fuer Befehlsausgaben: Claude erklaert einen Commit,
  eine Installation, eine Kompilierung oder einen Test erst dann fuer
  erfolgreich, wenn die tatsaechliche Ausgabe im Chat steht.
- Claude erfindet keine Bearbeitungsstaende, Trefferzahlen,
  Bewertungen oder Dateiinhalte. Bei Unklarheit fragt er nach.

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS 26.5.2 (25F84) - Python 3.14.6 (Homebrew) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)

## Repository-Struktur

config/ · data/{raw,interim,processed} · docs/ · eval/{instrument,sample,
responses} · experiments/ · literatur/{notizen,volltexte,pdf} · prompts/ ·
src/{collect,prepare,extract,classify,analyze} · tests/ · thesis/
Jeder Ordner enthaelt eine README.md.

literatur/volltexte/ und literatur/pdf/ sind per .gitignore ausgeschlossen.
Im Repository stehen nur Metadaten, BibTeX und eigene Notizen.

## Abgeschlossen

Arbeitspaket A (Setup) vollstaendig:
- Repository, .gitignore, README.md, STATUS.md, Ordnerstruktur
- SSH-Schluessel (Fingerabdruck gegen GitHub-Doku geprueft)
- Virtuelle Umgebung .venv, requests 2.34.2, requirements.txt
- GitHub-Token qrisp-thesis-readonly (fein granuliert, nur oeffentliche
  Repositories, mit Ablaufdatum, im Passwortmanager)

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
- Abschnitt 2.2.2: EARS (Mavin et al. 2009, Mavin/Wilkinson 2010,
  Wilkinson/Mavin 2018), mit Tabelle der fuenf Muster
- Abschnitt 2.2.3: User Stories (Lucassen et al. 2016), mit Tabelle der
  13 QUS-Kriterien und Tabelle der Kennzahlen zur Formatpruefung
- preamble.tex um booktabs und array ergaenzt, konfliktfrei geladen

Belegt (Kompilierlauf 10.08.2026): 28 Seiten, keine undefinierten
Referenzen, keine Overfull-Box aus den drei neuen Tabellen.
Belegt: .gitignore greift bis zum Server.
Belegt: Fuer Python 3.14 existieren vorkompilierte Pakete (cp314).
Gilt nur fuer requests, nicht fuer lokale Inferenz.
Belegt: Zugang zu ACM, IEEE (IEL) und Springer ueber die HLB.
Belegt: ISO/IEC/IEEE 29148 ueber IEEE Xplore beziehbar - kein Kauf noetig.
Belegt: Lucassen et al. 2016 ist Open Access (CC BY 4.0).

## Aktuell

Paket B ist bis auf Phase 2 der systematischen Suche abgeschlossen.
Naechster Schritt laut Zeitplan: Paket D (GitHub-Extraktion).
Paket C (Entscheidungsmatrix) ist ohne weitere Lesearbeit moeglich und
kann parallel laufen.

## Getroffene Entscheidungen

- Repository privat. Veroeffentlichung laut Vorlage auf Nein;
  PR-Daten enthalten Klarnamen Dritter. Nach Abgabe umstellbar.
- Evaluation nach Exposé-Variante: Das Qrisp-Team wird durch den
  Professor informiert und bewertet, sobald das Werkzeug fertig ist.
  Ergaenzt um eine dokumentierte Selbstbewertung. Bei mehreren
  Bewertenden wird ein Uebereinstimmungsmass moeglich; die
  Selbstbewertung ist Ergaenzung, nicht Ersatz.
  Terminabhaengigkeit: Werkzeug bis Ende Woche 8 bewertbar,
  Git-Tag thesis-v1.0.
- FF3: API-Modell darf von OpenAI oder Anthropic stammen.
  Wird dasselbe Modell als Arbeitswerkzeug und als Evaluationsgegenstand
  verwendet, ist das eine Bedrohung der Konstruktvaliditaet und muss
  dokumentiert werden.
- Kapitel nicht in Einzeldateien: Vorlage raet bei 30-50 Seiten davon ab.
  Alles steht in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard: Stil plain kennt standard nicht.
- Lizenzpflichtige Volltexte in literatur/volltexte/, frei lizenzierte in
  literatur/pdf/. Beide per .gitignore ausgeschlossen. Bewusst so
  belassen: schuetzt zusaetzlich vor versehentlichem Commit.
- preamble.tex um booktabs und array ergaenzt (10.08.2026). longtable
  bewusst nicht - kein aktueller Bedarf. Wird noetig, sobald eine
  Tabelle ueber einen Seitenumbruch laeuft.
- Given-When-Then (Gherkin) wird nicht als eigener Grundlagenabschnitt
  aufgearbeitet. Begruendung: Testspezifikation, kein Anforderungsformat;
  deckt keine der vier Ebenen zusaetzlich ab. Ausschluss wird in der
  Entscheidungsmatrix begruendet.
- Wilkinson/Mavin 2018 nachrangig: behandelt safety, nicht security.
  Fuer FF4 nicht tragfaehig, nur methodisches Vorbild fuer die
  Gap-Analyse.
- Lesenotizen: Ab 06.08.2026 gilt die Neun-Abschnitte-Vorlage
  (literatur/notizen/_vorlage.md). Die beiden aelteren Notizen
  (bradner, iso) folgen einer frueheren Struktur und werden nicht
  umgeschrieben - sie sind inhaltlich vollstaendig.

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
  ergaenzt um die acht operationalisierten NL-Probleme aus Big EARS
  und die 13 QUS-Kriterien

Zur Norm:
- 29148 Abschn. 5.2.5 neun Merkmale einzelner Anforderungen, 5.2.6 fuenf
  Merkmale von Anforderungsmengen, 5.2.7 sprachliche Kriterien.
- Abschn. 5.2.7 laesst sich in maschinell pruefbare Regeln ueberfuehren.
- Abschn. 5.2.4 (NOTE 2) schliesst User Stories nicht aus
  (Verweis auf ISO/IEC/IEEE 12207:2017, Annex H).
- 29148 sieht shall vor und raet von must ab; RFC 2119 behandelt MUST und
  SHALL als gleichbedeutend. In der Matrix zu entscheiden.
- Schluesselwortkonvention nur fuer Englisch formuliert. Fuer
  deutschsprachige Anforderungen eigene Festlegung noetig - OFFEN.
- Abschn. 8.4 und 8.5 (Gliederungsvorlagen) noch nicht gelesen;
  relevant fuer die Struktur der Ergebnisdokumente.

Zu RFC 2119 / 8174:
- Fuenf Verbindlichkeitsstufen; Abschn. 6 fordert sparsamen Gebrauch.
- RFC 8174: besondere Bedeutung nur bei durchgaengiger Grossschreibung.
- Risiko fuer die Pipeline: Ein Sprachmodell wird dazu neigen, alles als
  MUST zu formulieren. Widerspricht der Sparsamkeitsregel. Im
  Prompt-Entwurf zu adressieren, im Modellvergleich zu messen.

Zu EARS:
- Fuenf Muster: Ubiquitous (kein Schluesselwort), State-driven (WHILE,
  alternativ During), Event-driven (WHEN), Unwanted behaviour (IF-THEN),
  Optional feature (WHERE); kombinierbar zu komplexen Mustern.
- EARS verwendet ausschliesslich shall, kennt keine Modalitaetsstufen.
  Steht damit auf der Seite von 29148, nicht von RFC 2119.
- Zweistufiges Verfahren aus Big EARS (erst einstufen, ob eine Aussage
  Anforderung ist, dann umformulieren) ist das Vorbild fuer das
  Prompt-Design in Kapitel 4.
- Schluesselwoerter und feste Klauselfolge erlauben regelbasierte
  Formatpruefung -> Vergleichsmass fuer FF3.
- Slotstruktur auf JSON-Schema abbildbar -> Modell fuellt Felder, Satz
  wird programmatisch erzeugt.
- Grenze: fuer hochrangige Stakeholder-Anforderungen entwickelt und
  validiert, nicht fuer Implementierungsebene. Die Autoren nennen die
  Erweiterung auf Softwareanforderungen als offene Richtung.
- Evidenz: Fallstudien in einem Unternehmen, Selbstbewertung der Autoren.
  Kein kontrolliertes Experiment. Die 99-Prozent-Angabe aus Big EARS darf
  nicht als Wirksamkeitsnachweis zitiert werden.

Zu User Stories:
- Vier Bestandteile im Begriffsmodell: Rolle, Means, null oder mehr Ends,
  Format. Drei Bestandteile des Konzepts: Text, Gespraeche,
  Akzeptanzkriterien. Ueber 80 syntaktische Varianten existieren.
- QUS: 13 Kriterien in den Kategorien syntaktisch, semantisch,
  pragmatisch; getrennt nach Einzelstory und Menge - dieselbe Systematik
  wie 29148 Abschn. 5.2.5 gegenueber 5.2.6.
- Automatische Pruefung (AQUSA) erreicht mikro-gemittelt 93,8 Prozent
  Trefferquote bei 72,2 Prozent Genauigkeit an 1023 Stories aus 18
  Datensaetzen. Je Kriterium stark unterschiedlich: Unique 100/100,
  Well-formed 95,7/42,3. Semantische Kriterien nicht automatisiert.
- Perfect Recall Condition: Werkzeug uebernimmt die maschinell
  entscheidbaren Pruefungen, urteilsabhaengige verbleiben beim Menschen.
  Belegter Grundsatz fuer die Arbeitsteilung in dieser Arbeit.
- Kernproblem fuer diese Arbeit: Das Kriterium Well-formed verlangt
  zwingend eine Rolle. PR-Daten sind entwicklerzentriert und nennen den
  Nutzniesser meist nicht. Die Rolle muesste erfunden werden, was der
  Belegstaerke-Systematik widerspricht.
- Aus PR-Daten ist nur ein Teil der drei Bestandteile gewinnbar;
  Akzeptanzkriterien im agilen Sinn fehlen.

Nicht belegbare Merkmale aus 29148: Notwendigkeit, Umsetzbarkeit und
Korrektheit setzen Wissen ueber den tatsaechlichen Bedarf voraus und sind
aus der PR-Historie nur begrenzt zugaenglich. Eindeutigkeit, Einzelbezug,
Nachweisbarkeit und Vorlagenkonformitaet sind am Text pruefbar.

## Zugangsdaten

- GitHub-Token qrisp-thesis-readonly, im Passwortmanager,
  noch nie praktisch erprobt.
- SSH-Schluessel ed25519 fuer das eigene Repository.
- Git-Identitaet: Omar Assad Salem, GitHub-Noreply-Adresse.

## Offene Punkte

Extern, mit Vorlauf:
- Umfangsfrage: Was gehoert zur Arbeit, was ist Weiterentwicklung?
  Das Team will das Werkzeug aktiv nutzen. Stand Ende Woche 8 als
  Git-Tag thesis-v1.0 einfrieren; alles Weitere in den Ausblick.
  Wunschliste in docs/entscheidungen.md.
- Bewertungsbogen und Anweisungen fuer die Bewertenden bis Woche 8.
  Grundlage: 29148 Abschn. 5.2.5-5.2.7, die acht NL-Probleme aus
  Big EARS, die 13 QUS-Kriterien.
- KI-Formulierung fuer vorspann.tex mit Professor abstimmen:
  Kennzeichnungspflicht im Anhang? Prompts beilegen?
- Korreferent in thesis.tex eintragen (Platzhalter Zeile 23)
- API-Budget fuer FF3, zu klaeren bis Woche 4

Inhaltlich offen:
- Deutschsprachige Modalitaetskonvention festlegen (FF2)
- Entscheidungsmatrix aufstellen (Paket C) - keine Lesearbeit mehr noetig
- Phase 2 der systematischen Literatursuche (S1, S2, S4; S3 nur noch fuer
  Anwendungsarbeiten Dritter)
- INVEST: Lucassen loest das S als Scalable auf, gebraeuchlich ist Small.
  Gegen Wake 2003 pruefen, falls INVEST verwendet wird.
- Titelvariante Mavin 2009: Papierkopf und Datenbank weichen ab.
  Einheitlichkeit sicherstellen.

Technisch und redaktionell:
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Woche 5
- Platzhalter in thesis.tex, die sich beim Weiterschreiben aufloesen:
  Z. 20 Abgabedatum · Z. 23 Korreferent · Z. 29 Abstract ·
  Z. 39 Einleitung · Z. 299 kuendigt User Stories und EARS an, obwohl
  beides geschrieben ist - SATZ UEBERARBEITEN ·
  Z. 364 Verweis auf die Entscheidungsmatrix (loest sich, sobald
  Kapitel 4 einen Abschnitts-Label hat) ·
  Z. 759 Femmer et al. (requirements smells gegen 29148) -
  Primaerquelle beschaffen oder Satz streichen ·
  Z. 766, 771, 777, 785, 793, 800, 807, 815 noch leere Kapitel
- Demo-Dateien der Vorlage in thesis/figures/ vor Abgabe entfernen
  (gnu.png, automata.pdf, zeichnung*, templateprozess*).
  blindtext.sty entfaellt erst, wenn preamble.tex geaendert wird.
- Overfull hboxen lokalisiert, Behebung in Woche 12:
  vorspann.tex Z. 4-16 (86,6pt, Titelseite) · thesis.tex Z. 263-269
  (12,7pt) · Z. 288-295 (12,9pt) · Z. 300-301 (14,5pt, loest sich mit dem
  Platzhalter auf) · Z. 768 (1,4pt, Ueberschrift)
- Rote KI-Hinweisbox in vorspann.tex vor Abgabe ersetzen
- fancyhdr-Warnungen stammen aus der Vorlage und sind harmlos

## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Kompilieren: cd thesis && pdflatex thesis.tex && bibtex thesis1 &&
  bibtex thesis2 && pdflatex thesis.tex && pdflatex thesis.tex
  (nicht make all - braucht LibreOffice und ImageMagick)
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> log -1 -> status -> push
- Kein git add . und kein git add ordner/
- Commit-Praefixe: lit:, bib:, tex:, chore:
- Bereits gepushte Commits werden nicht nachtraeglich geaendert.
  Korrekturen kommen als eigener Folge-Commit.
- BibTeX-Felder mit Umlauten oder Backslashes in {...} setzen,
  nicht in "..." - sonst bricht der Eintrag ab.
- Eigennamen im BibTeX-Titel in {...} setzen, damit plain die
  Grossschreibung nicht entfernt.
- requirements.txt wird nie von Hand bearbeitet, sondern nach jeder
  Installation neu erzeugt: pip freeze > requirements.txt

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   <- aktuell
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

Paket B wurde eine Woche frueher fertig als geplant. Paket C
(Formatauswahl, urspruenglich W3) ist ohne weitere Lesearbeit moeglich
und kann in W2 vorgezogen werden.