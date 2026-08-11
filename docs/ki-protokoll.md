# Protokoll des KI-Einsatzes

Grundlage: Der Professor hat den Einsatz generativer KI erlaubt
(Textgenerierung, Literatursuche, Code). Die konkrete Formulierung
fuer vorspann.tex ist noch abzustimmen.

Auf den oeffentlichen KI-Seiten der HLB wurde keine verbindliche
Vorgabe zu Protokollpflicht, Prompt-Abgabe oder Einzelkennzeichnung
gefunden (geprueft am 05.08.2026). Dieses Protokoll wird dennoch
gefuehrt, um Nachweispflichten erfuellen zu koennen.

| Datum | Werkzeug | Modell | Zweck | Eingegebene Daten | Wesentliche Ausgabe | Meine Pruefung       | Uebernommen |
|---|---|---|---|---|---|----------------------|---|
| 31.07.2026 | Claude | Opus | Projektplanung, Kompetenz- und Zeitplan | Projektanweisung, Exposé | Zeitplan 13 Wochen, Repository-Struktur | Plausibilitaet gegen Exposé geprueft | Struktur und Zeitplan uebernommen |
| 31.07.2026 | Claude | Opus | Einrichtung Git, SSH, Python-Umgebung | Terminal-Ausgaben | Schrittanleitungen | Jeden Befehl selbst ausgefuehrt und Ausgabe geprueft | ja |
| 05.08.2026 | Claude | Opus | Pruefung der Literaturliste des Exposés | Exposé, Webrecherche | Bestaetigung der Quellenangaben, drei Zusatzfunde | Fundstellen stichprobenartig geprueft | Ergaenzungen in Literaturmatrix |
| 05.08.2026 | Claude | Opus | ISO/IEC/IEEE 29148 Abschn. 5.2.5-5.2.7 aufbereiten | Norm-Volltext | Deutsche Erlaeuterung, LaTeX-Abschnitt | Abschnitt selbst gelesen, ueberarbeitet und um 5.2.4, 5.2.8 sowie die Definitionen erweitert | Abschnitt 2.1 in thesis.tex |
| 05.08.2026 | Claude | Opus | Uebernahme der HSRM-Vorlage, Kapitelgeruest | Vorlagendateien, Exposé | thesis.tex mit Metadaten und Kapitelstruktur | Selbst kompiliert, Ausgabe geprueft | ja |
| 06.08.2026 | Claude | Opus | Gegenpruefung meiner Belege in Abschnitt 2.1 | ueberarbeitete thesis.tex, Norm-Volltext | Alle acht Abschnittsangaben als korrekt bestaetigt | Ergebnis nachvollzogen | Beleg am ersten Absatz ergaenzt |
| 06.08.2026 | Claude | Opus | RFC 2119 und RFC 8174 aufbereiten | Volltexte beider RFCs | Deutsche Erlaeuterung, LaTeX-Abschnitt, BibTeX | gelesen und geprueft | Abschnitt 2.2.1 in thesis.tex |
| 06.08.2026 | Claude | Opus | EARS aufarbeiten (Mavin 2009, Mavin/Wilkinson 2010, Wilkinson/Mavin 2018) | Volltexte der drei Papiere, STATUS.md | Deutsche Erlaeuterung, Feingliederung, LaTeX-Abschnitt 2.2.2 mit Tabelle, drei BibTeX-Eintraege, Lesenotizen, Matrixeintraege | gegen Volltexte geprueft | Abschnitt 2.2.2 in thesis.tex, Eintraege in thesis.bib |
| 10.08.2026 | Claude | Opus | User Stories aufarbeiten (Lucassen et al. 2016) | Volltext des Artikels, STATUS.md | Deutsche Erlaeuterung, Einordnung, Feingliederung, LaTeX-Abschnitt 2.2.3 mit zwei Tabellen, Lesenotiz, Matrixeintrag, BibTeX | gegen Volltexte geprueft | Abschnitt 2.2.3 in thesis.tex, Eintrag in thesis.bib |


## Hinweis zur Arbeitsteilung

Kapitelentwuerfe entstehen mit KI-Unterstuetzung: Das Modell liest die
Quelle, erlaeutert sie auf Deutsch und liefert einen Entwurf mit
Belegen. Ich lese den Entwurf, pruefe die Belege gegen die Quelle und
ueberarbeite ihn, bevor er uebernommen wird. Abschnitt 2.1 wurde von
mir inhaltlich erweitert.
