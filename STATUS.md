# Bearbeitungsstand

Letzte Aktualisierung: 31.07.2026
Abgabetermin: 01.11.2026

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, 515 GB frei
macOS 26.5.2 (25F84) · Python 3.14.6 (Homebrew) · pip 26.1.2 · Git 2.50.1
Repository: /Users/omar/Developer/qrisp-re-thesis

## Abgeschlossen

Arbeitspaket A (Setup) vollstaendig:
- A0 Repository initialisiert (Zweig main), .gitignore, README.md, STATUS.md
- A1 Ordnerstruktur mit Erklaerungsdateien; SSH-Schluessel eingerichtet
  (Fingerabdruck gegen GitHub-Doku geprueft); privates Repository
  github.com/os759/qrisp-re-thesis angelegt und verbunden; erster push
- A2 Virtuelle Umgebung .venv, requests 2.34.2, requirements.txt

Belegt: .gitignore greift bis zum Server (data/raw, data/interim,
eval/responses erscheinen nicht auf GitHub).
Belegt: Fuer Python 3.14 existieren vorkompilierte Pakete (cp314-Wheels).
Gilt nur fuer requests, nicht fuer lokale Inferenz.

## Aktuell

Arbeitspaket A abgeschlossen. Naechstes Paket nach Zeitplan:
B (Literatur und Grundlagen) oder D (GitHub-Extraktion).

## Getroffene Entscheidungen

- Evaluation reduziert: Bewertung durch den Betreuer, ergaenzt um eine
  dokumentierte Selbstbewertung. Abweichung vom Exposé, mit dem Professor
  abgestimmt, schriftliche Bestaetigung ausstehend. In den Limitationen
  auszuweisen. Folge: kein Uebereinstimmungsmass in der Evaluation;
  stattdessen Abgleich LLM-Klassifikation gegen manuelle Klassifikation
  in Schritt 6.
- FF3: API-Modell darf von OpenAI oder Anthropic stammen (freie Wahl).
  Zu beachten: Wird dasselbe Modell als Arbeitswerkzeug und als
  Evaluationsgegenstand verwendet, ist das eine Bedrohung der
  Konstruktvaliditaet und muss dokumentiert werden.
- Repository privat. Begruendung: Veroeffentlichung der Arbeit laut
  Vorlage auf Nein; PR-Daten enthalten Klarnamen Dritter.
- KI-Einsatz durch den Professor erlaubt (Textgenerierung, Literatursuche,
  Code). Konkrete Formulierung fuer vorspann.tex noch einzutragen.

## Zugangsdaten

- GitHub-Token `qrisp-thesis-readonly`, fein granuliert, nur oeffentliche
  Repositories, keine zusaetzlichen Berechtigungen, mit Ablaufdatum.
  Liegt im Passwortmanager. Noch nicht praktisch erprobt.
- SSH-Schluessel ed25519 fuer Zugriff auf das eigene Repository.
- Git-Identitaet: Omar Assad Salem, GitHub-Noreply-Adresse.

## Offene Punkte

- Schriftliche Bestaetigung des Professors zur reduzierten Evaluation
- API-Budget fuer FF3, zu klaeren bis Woche 4
- Lokale Inferenz mit Python 3.14: ungeprueft, Kontrollpunkt Woche 5
- preamble.tex laedt longtable, booktabs, array nicht
- vorspann.tex bindet figures/hsrmlogo.pdf ein,
  vorhanden ist hsrmlogo_bunt.pdf
- Rote KI-Hinweisbox in vorspann.tex vor Abgabe ersetzen
- Formulierung zur KI-Nutzung mit Professor abstimmen:
  Kennzeichnungspflicht im Anhang? Prompts beilegen?

## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> show --stat -> status -> push
- Kein git add . verwenden

## Zeitplan

W1 03.-09.08. Setup, Literaturstart
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf
W3 17.-23.08. Extraktion, Formatauswahl
W4 24.-30.08. LLM-Extraktion mit API-Modell
W5 31.08.-06.09. Prompt-Iteration, lokales Modell
W6 07.-13.09. Modellvergleich (Kontrollpunkt lokales Modell)
W7 14.-20.09. Klassifikation, Sicherheitsraster
W8 21.-27.09. Gap-Analyse, Evaluationsmaterial versenden
W9 28.09.-04.10. Kapitel Implementierung
W10 05.-11.10. Auswertung, Kapitel Evaluation
W11 12.-18.10. Diskussion, Fazit
W12 19.-25.10. Korrekturschleife
W13 26.-30.10. Endkontrolle, Abgabe
