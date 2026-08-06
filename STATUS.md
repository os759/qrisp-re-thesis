# Bearbeitungsstand

Letzte Aktualisierung: 06.08.2026
Abgabetermin: 01.11.2026 (Sonntag; intern geplant auf Fr 30.10.2026)

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS 26.5.2 (25F84) - Python 3.14.6 (Homebrew) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)

## Abgeschlossen

Arbeitspaket A (Setup) vollstaendig:
- Repository, .gitignore, README.md, STATUS.md, Ordnerstruktur
- SSH-Schluessel (Fingerabdruck gegen GitHub-Doku geprueft)
- Virtuelle Umgebung .venv, requests 2.34.2, requirements.txt
- GitHub-Token qrisp-thesis-readonly (fein granuliert, nur oeffentliche
  Repositories, mit Ablaufdatum, im Passwortmanager)

Arbeitspaket B (Literatur), teilweise:
- literatur/suchprotokoll.md und literaturmatrix.md angelegt und
  fortgeschrieben (13 Quellen erfasst)
- docs/ki-protokoll.md und entscheidungen.md angelegt und fortgeschrieben
- LaTeX-Vorlage nach thesis/ uebernommen, kompiliert fehlerfrei
- ISO/IEC/IEEE 29148:2018 Abschn. 3.1, 5.2.4-5.2.8 gelesen und als
  Abschnitt 2.1 ausformuliert (von mir ueberarbeitet und erweitert;
  alle acht Abschnittsangaben gegen den Normtext geprueft)
- RFC 2119 und RFC 8174 gelesen und als Abschnitt 2.2.1 ausformuliert

Belegt: .gitignore greift bis zum Server.
Belegt: Fuer Python 3.14 existieren vorkompilierte Pakete (cp314).
Gilt nur fuer requests, nicht fuer lokale Inferenz.
Belegt: Zugang zu ACM, IEEE (IEL) und Springer ueber die HLB.
Belegt: ISO/IEC/IEEE 29148 ueber IEEE Xplore beziehbar - kein Kauf noetig.

## Aktuell

Arbeitspaket B laeuft. Naechster Baustein: EARS (Mavin et al. 2009) und
User Stories, danach Entscheidungsmatrix (Paket C).

## Getroffene Entscheidungen

- Repository privat. Veroeffentlichung laut Vorlage auf Nein;
  PR-Daten enthalten Klarnamen Dritter. Nach Abgabe umstellbar.
- Evaluation nach Exposé-Variante: Das Qrisp-Team wird durch den
  Professor informiert und bewertet, sobald das Werkzeug fertig ist.
  Ergaenzt um eine dokumentierte Selbstbewertung.
  Damit entfaellt die zuvor geplante Reduktion. Folge: Bei mehreren
  Bewertenden wird ein Uebereinstimmungsmass moeglich; die
  Selbstbewertung ist Ergaenzung, nicht Ersatz.
  Terminabhaengigkeit: Das Werkzeug muss bis Ende Woche 8 in einem
  bewertbaren Zustand sein, sonst faellt die Auswertung aus dem
  Zeitplan. Deshalb Git-Tag thesis-v1.0 Ende Woche 8.
- FF3: API-Modell darf von OpenAI oder Anthropic stammen.
  Zu beachten: Wird dasselbe Modell als Arbeitswerkzeug und als
  Evaluationsgegenstand verwendet, ist das eine Bedrohung der
  Konstruktvaliditaet und muss dokumentiert werden.
- Kapitel nicht in Einzeldateien: Die Vorlage raet bei 30-50 Seiten
  ausdruecklich davon ab. Alles steht in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard: Stil plain kennt standard
  nicht. Getestet.
- Lizenzpflichtige Volltexte in literatur/volltexte/, per .gitignore
  ausgeschlossen.

## Fachliche Zwischenergebnisse (FF2)

- ISO/IEC/IEEE 29148 Abschn. 5.2.5 nennt neun Merkmale einzelner
  Anforderungen, 5.2.6 fuenf Merkmale von Anforderungsmengen,
  5.2.7 sprachliche Kriterien und unzulaessige Formulierungsklassen.
  Diese Kriterien bilden die normative Grundlage der
  Entscheidungsmatrix, statt selbst erfundener Kriterien.
- Abschn. 5.2.7 laesst sich in maschinell pruefbare Regeln ueberfuehren.
  Daraus koennen eine automatische Formatvalidierung und ein
  quantitatives Vergleichsmass fuer FF3 entstehen.
- 29148 Abschn. 5.2.4 (NOTE 2) haelt fest, dass im agilen Umfeld
  alternative Formulierungen wie User Stories verwendet werden koennen
  (Verweis auf ISO/IEC/IEEE 12207:2017, Annex H). Der Standard
  schliesst User Stories also nicht aus.
- Konflikt, der in der Matrix zu entscheiden ist: 29148 sieht shall vor
  und raet von must ab; RFC 2119 behandelt MUST und SHALL als
  gleichbedeutend. Beide Konventionen sind nicht gleichzeitig anwendbar.
- 29148 formuliert die Schluesselwortkonvention fuer Englisch. Fuer
  deutschsprachige Anforderungen ist eine eigene Festlegung noetig.
- RFC 2119 ist eine Modalitaetskonvention, kein Satzmuster; es ist mit
  EARS oder User Stories kombinierbar, nicht deren Alternative.
- RFC 8174 (2017) aktualisiert RFC 2119: besondere Bedeutung nur bei
  Grossschreibung. Beide bilden BCP 14 und sind gemeinsam zu zitieren.
- Nicht belegte Merkmale: Notwendigkeit, Umsetzbarkeit und Korrektheit
  setzen Wissen ueber den tatsaechlichen Bedarf voraus und sind aus der
  PR-Historie nur begrenzt zugaenglich. Eindeutigkeit, Einzelbezug,
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
  Wunschliste in docs/entscheidungen.md fuehren.
- Bewertungsbogen und Anweisungen fuer die Bewertenden bis Woche 8
  fertigstellen
- KI-Formulierung fuer vorspann.tex mit Professor abstimmen:
  Kennzeichnungspflicht im Anhang? Prompts beilegen?
- Korreferent in thesis.tex eintragen (Platzhalter)
- API-Budget fuer FF3, zu klaeren bis Woche 4

Technisch und redaktionell:
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Woche 5
- preamble.tex laedt longtable, booktabs und array nicht.
  Ergaenzung noetig, bevor die erste Tabelle gesetzt wird.
- Demo-Dateien der Vorlage in thesis/figures/ vor Abgabe entfernen
  (gnu.png, automata.pdf, zeichnung*, templateprozess*).
  blindtext.sty entfaellt erst, wenn preamble.tex geaendert wird.
- Overfull hbox von ca. 32pt in thesis.tex noch nicht lokalisiert
- Rote KI-Hinweisbox in vorspann.tex vor Abgabe ersetzen
- Abstract und Abgabedatum noch offen
- Lesenotizen unter literatur/notizen/ noch nicht angelegt
  (bradner_1997_rfc2119.md, iso_2018_29148.md)
- Systematische Literatursuche (Phase 2 im Suchprotokoll) noch offen

## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Kompilieren: cd thesis && pdflatex thesis.tex && bibtex thesis1 &&
  bibtex thesis2 && pdflatex thesis.tex && pdflatex thesis.tex
  (nicht make all - braucht LibreOffice und ImageMagick)
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> log -1 -> status -> push
- Kein git add . und kein git add ordner/
- Commit-Praefixe: lit:, bib:, tex:, chore:
- BibTeX-Felder mit Umlauten oder Backslashes in {...} setzen,
  nicht in "..." - sonst bricht der Eintrag ab.
- requirements.txt wird nie von Hand bearbeitet, sondern nach jeder
  Installation neu erzeugt: pip freeze > requirements.txt

## Zeitplan

W1 03.-09.08. Setup, Literaturstart          <- aktuell
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf
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