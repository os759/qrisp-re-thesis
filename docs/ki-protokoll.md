# Protokoll des KI-Einsatzes

Grundlage: Der Professor hat den Einsatz generativer KI erlaubt
(Textgenerierung, Literatursuche, Code). Die konkrete Formulierung
fuer vorspann.tex ist noch abzustimmen.

Auf den oeffentlichen KI-Seiten der HLB wurde keine verbindliche
Vorgabe zu Protokollpflicht, Prompt-Abgabe oder Einzelkennzeichnung
gefunden (geprueft am 05.08.2026). Dieses Protokoll wird dennoch
gefuehrt, um Nachweispflichten erfuellen zu koennen.

| Datum | Werkzeug | Modell | Zweck | Eingegebene Daten | Wesentliche Ausgabe | Meine Pruefung       | Uebernommen |
|---|---|--------|---|---|---|----------------------|---|
| 31.07.2026 | Claude | Opus   | Projektplanung, Kompetenz- und Zeitplan | Projektanweisung, Exposé | Zeitplan 13 Wochen, Repository-Struktur | Plausibilitaet gegen Exposé geprueft | Struktur und Zeitplan uebernommen |
| 31.07.2026 | Claude | Opus   | Einrichtung Git, SSH, Python-Umgebung | Terminal-Ausgaben | Schrittanleitungen | Jeden Befehl selbst ausgefuehrt und Ausgabe geprueft | ja |
| 05.08.2026 | Claude | Opus   | Pruefung der Literaturliste des Exposés | Exposé, Webrecherche | Bestaetigung der Quellenangaben, drei Zusatzfunde | Fundstellen stichprobenartig geprueft | Ergaenzungen in Literaturmatrix |
| 05.08.2026 | Claude | Opus   | ISO/IEC/IEEE 29148 Abschn. 5.2.5-5.2.7 aufbereiten | Norm-Volltext | Deutsche Erlaeuterung, LaTeX-Abschnitt | Abschnitt selbst gelesen, ueberarbeitet und um 5.2.4, 5.2.8 sowie die Definitionen erweitert | Abschnitt 2.1 in thesis.tex |
| 05.08.2026 | Claude | Opus   | Uebernahme der HSRM-Vorlage, Kapitelgeruest | Vorlagendateien, Exposé | thesis.tex mit Metadaten und Kapitelstruktur | Selbst kompiliert, Ausgabe geprueft | ja |
| 06.08.2026 | Claude | Opus   | Gegenpruefung meiner Belege in Abschnitt 2.1 | ueberarbeitete thesis.tex, Norm-Volltext | Alle acht Abschnittsangaben als korrekt bestaetigt | Ergebnis nachvollzogen | Beleg am ersten Absatz ergaenzt |
| 06.08.2026 | Claude | Opus   | RFC 2119 und RFC 8174 aufbereiten | Volltexte beider RFCs | Deutsche Erlaeuterung, LaTeX-Abschnitt, BibTeX | gelesen und geprueft | Abschnitt 2.2.1 in thesis.tex |
| 06.08.2026 | Claude | Opus   | EARS aufarbeiten (Mavin 2009, Mavin/Wilkinson 2010, Wilkinson/Mavin 2018) | Volltexte der drei Papiere, STATUS.md | Deutsche Erlaeuterung, Feingliederung, LaTeX-Abschnitt 2.2.2 mit Tabelle, drei BibTeX-Eintraege, Lesenotizen, Matrixeintraege | gegen Volltexte geprueft | Abschnitt 2.2.2 in thesis.tex, Eintraege in thesis.bib |
| 10.08.2026 | Claude | Opus   | User Stories aufarbeiten (Lucassen et al. 2016) | Volltext des Artikels, STATUS.md | Deutsche Erlaeuterung, Einordnung, Feingliederung, LaTeX-Abschnitt 2.2.3 mit zwei Tabellen, Lesenotiz, Matrixeintrag, BibTeX | gegen Volltexte geprueft | Abschnitt 2.2.3 in thesis.tex, Eintrag in thesis.bib |
| 12.08.2026 | Claude | Opus   | Paket D Teil 1: Anleitung zum GitHub-API-Zugriff, Entwurf von fuenf Python-Skripten, Entscheidungsvorlage zur Datenhaltung | STATUS.md, Projektanweisung, Repository-Name eclipse-qrisp/Qrisp, Ausgaben von curl und Python, Inhalt von .gitignore und entscheidungen.md. Kein Token, keine Rohdaten. | github_api.py, api_test.py, explore_fields.py, compare_objects.py, fetch_pull_list.py; 13 Entscheidungseintraege; Recherche zu Rate Limits, Paginierung und API-Versionen mit Fundstellen | Jeden Befehl selbst ausgefuehrt und jede Ausgabe zurueckgemeldet. Zwei Fehler des Modells korrigiert: der Vorschlag, data/interim/ zu versionieren, wurde verworfen (bestehende .gitignore war strenger); ein angegebener Pruefwert war falsch. | Skripte und Entscheidungen uebernommen, Vorschlag zu data/interim/ nicht |
| 14.-19.08.2026 | Claude | Opus   | Paket D Teil 2: Entwurf von drei Abrufskripten und zwei Auswertungsskripten, Erweiterung von github_api.py, Entscheidungsvorlagen D1 bis D4, Analyse von vier Datenabweichungen | STATUS.md, entscheidungen.md, ki-protokoll.md, github_api.py, collect.toml, fetch_pull_list.py, Manifeste, erzeugte Befundberichte, Terminalausgaben. Keine PR-Rohdaten, kein Token. Autorennamen nur in Terminalausgaben, nicht in versionierten Dateien. | fetch_pull_details.py, fetch_pull_comments.py, fetch_pull_files.py, analyze_pull_details.py, analyze_pull_files.py; Entscheidungen D1 bis D4; Recherche zur GitHub-Doku (Dateigrenze je Pull Request) mit Fundstelle | Jedes Skript vor dem vollen Lauf mit --limit 5 selbst getestet und die Ausgabe zurueckgemeldet. Alle Zahlen stammen aus eigenen Laeufen, keine aus dem Modell. Drei Fehler des Modells korrigiert bzw. festgestellt: falsches Datum (13.08. statt 14.08.); deutsche Programmausgaben entgegen der eigenen Sprachentscheidung, von mir bemerkt; ein Pruefbefehl klammerte den Zeitstempel nicht aus und meldete falschen Alarm. Zwei Modellvermutungen wurden durch Messung widerlegt (geloeschte Kommentare bei PR 331/344/767; erzeugte Dateien in den groessten Diffs). | Skripte, Entscheidungen und Befundtexte nach eigener Pruefung uebernommen |
| 19.-21.08.2026 | Claude | Opus   | Paket D Teil 3: Entwurf des Aufbereitungsskripts und der Testsuite, Klaerung von vier offenen Entscheidungen | STATUS.md, entscheidungen.md, ki-protokoll.md, github_api.py, collect.toml, die drei Abrufskripte, ein Manifest, Feldnamen und Datentypen der Rohdateien, Terminalausgaben. Keine PR-Rohdaten, kein Token, keine Autorennamen. | build_interim.py; conftest.py und fuenf Testdateien mit 38 Tests; Kuerzungsparameter fuer collect.toml; Entscheidungen D5 bis D8; Neufassung von tests/README.md | Jeden Befehl selbst ausgefuehrt und jede Ausgabe zurueckgemeldet. Der volle Lauf bestaetigte neun vom Modell vorhergesagte Kennzahlen exakt (476 Pull Requests, 31 Bots, 5 ohne Codeaenderung, 222 ohne Kommentar, 259 CRLF, 124 Vorlagentext, 639/1713 Kommentare, 8424 Dateien, 56 ohne Beschreibung). Zwei Fehler des Modells festgestellt: eine zu niedrige Groessenschaetzung der Ausgabedatei (10-15 MB statt 20 MB) und ein Testaufruf, bei dem das Modell das Argument --limit vergessen hatte. Die Vorhersage, die Zahl der Beschreibungen ohne Text koenne durch die Reinigung steigen, wurde durch Messung widerlegt (0). | Skripte, Tests und Entscheidungen nach eigener Pruefung uebernommen |
| 26.-27.08.2026 | ChatGPT | sol    | Paket C: Protokoll der Formulierungsprobe in Tabellenform bringen | Die von mir beim Lesen der zwoelf Pull Requests getroffenen Einstufungen, dazu Titel, Beschreibung, Kommentare und Diff-Angaben aus den GitHub-Seiten. Keine Rohdaten aus dem Datensatz, kein Token. | Ausgefuelltes docs/formatprobe_protokoll.md mit Kreuztabellen, Beispielsaetzen und Auswertungstabellen | Die Einstufungen stammen von mir; das Modell hat keine vorgeschlagen. Ich habe jede uebernommene Zeile gegen die Quelle gelesen. | Protokolltext uebernommen, Einstufungen sind meine eigenen |
| 23.-27.08.2026 | Claude | Opus | Paket C Schritte 1 bis 4: Kriterienkatalog und Bewertungsverfahren, Aufarbeitung von ISO/IEC/IEEE 29148 Abschn. 9.6, Ziehungsskript, Gegenpruefung der Formulierungsprobe | STATUS.md, entscheidungen.md, ki-protokoll.md, literaturmatrix.md, suchprotokoll.md, thesis.tex, build_interim.py, formatprobe_protokoll.md, Norm-Volltext, Terminalausgaben. Keine PR-Rohdaten, kein Token. | docs/formatauswahl.md mit K1 bis K10, Skala und Regeln R1 bis R8; Entscheidungen C1 bis C4; LaTeX-Abschnitt 2.1.7 mit Tabelle; src/analyze/draw_sample.py; Gegenpruefung von vier Pull-Request-Seiten | Jeden Befehl selbst ausgefuehrt und jede Ausgabe zurueckgemeldet. Sieben Fehler des Modells festgestellt, darunter eine falsche Tabellennummer, ein falsches Datum, ein erfundenes Commit-Praefix und eine Schichtregel, die offene Vorgaenge durch eine Luecke doch zuliess. Letztere vor dem Commit behoben. Das Modell hat ausserdem eine eigene Wortwahl zurueckgenommen, die von Abschnitt 2.2.2 abgewichen waere. | Skripte, Entscheidungen und Abschnitt 2.1.7 nach eigener Pruefung uebernommen; die Aenderung an PR 371 uebernommen |

## Hinweis zur Arbeitsteilung

Kapitelentwuerfe entstehen mit KI-Unterstuetzung: Das Modell liest die
Quelle, erlaeutert sie auf Deutsch und liefert einen Entwurf mit
Belegen. Ich lese den Entwurf, pruefe die Belege gegen die Quelle und
ueberarbeite ihn, bevor er uebernommen wird. Abschnitt 2.1 wurde von
mir inhaltlich erweitert.

Bei der Implementierung gilt dieselbe Trennung: Das Modell entwirft
Skripte und Anleitungen, ich fuehre jeden Befehl selbst aus und melde
die tatsaechliche Ausgabe zurueck. Kein Schritt gilt als erfolgreich,
bevor die Ausgabe geprueft ist. Vorschlaege des Modells wurden dabei
auch zurueckgewiesen; das ist in der Tabelle vermerkt.

Ab Paket D Teil 2 gilt zusaetzlich: Groessere Skripte werden vom Modell
vor der Uebergabe in seiner eigenen Umgebung mit erfundenen Testdaten
ausgefuehrt. Diese Testlaeufe erzeugen keine Ergebnisse der Arbeit; sie
dienen ausschliesslich der Fehlersuche. Jede in der Arbeit verwendete
Zahl stammt aus einem Lauf auf meinem Rechner mit den echten
Qrisp-Daten. Dasselbe gilt fuer die Erhebung: kein Datensatz und keine
Kennzahl wurde vom Modell erzeugt oder geschaetzt.

Ab Paket D Teil 3 gilt zusaetzlich: Die Testsuite wurde vom Modell
gegen absichtlich eingebrachte Fehler geprueft. Bei vertauschtem
outcome, bei einer Reinigung ohne Abschlussmarker, bei verworfenen
Dateieintraegen und bei umgekehrter Kuerzungsrichtung schlugen jeweils
mehrere Tests fehl. Damit ist belegt, dass die Tests nicht nur
bestehen, sondern auch anschlagen. Dieser Nachweis erfolgte in der
Umgebung des Modells; die 38 Tests selbst laufen auf meinem Rechner
unter Python 3.14.6.

Ab Paket C gilt zusaetzlich: Bei der Formulierungsprobe zu FF2 habe
ich die zwoelf Pull Requests selbst im Browser gelesen und jede
Einstufung selbst getroffen. ChatGPT hat diese Einstufungen nur in
die Protokollform gebracht. Claude hat anschliessend einen Teil der
Faelle unabhaengig an denselben Quellen gegengeprueft und eine
Abweichung gefunden, die ich uebernommen habe. Die Rollenverteilung
ist in docs/formatprobe_protokoll.md unter "Methodischer Status"
festgehalten.
