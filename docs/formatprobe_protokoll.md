# Protokoll der Formulierungsprobe (FF2)

Zweck: Nachweis der Messungen fuer K6 und K9. Jeder Versuch wird
festgehalten, auch der misslungene.

Grundlage: docs/formatauswahl.md, Entscheidung C2.
Stichprobe: docs/sample_formulation_probe.md
Bearbeitet von: Omar Assad Salem (Verfasser)
Schreibwerkzeug: ChatGPT, siehe Abschnitt "Methodischer Status"
Begonnen: 26.08.2026
Zuletzt geaendert: 28.08.2026
Sprache der Anforderungssaetze: Englisch (C1).


## Methodischer Status

Entscheidung C2 legt fest, dass an der Formulierungsprobe kein
Sprachmodell beteiligt ist. Wer welchen Beitrag geleistet hat, wird
deshalb hier offengelegt.

Der Verfasser hat am 26.08.2026 alle zwoelf Pull Requests im Browser
geoeffnet und gelesen, jeweils die Ansicht "Conversation" und die
Ansicht "Files changed". Am 27.08.2026 hat er einzelne Faelle erneut
an der Quelle geprueft; die daraus folgenden Aenderungen stehen im
Abschnitt "Aenderungen nach erneuter Quellenpruefung".

Die Einstufung jedes Bestandteils als belegt oder nicht belegt hat
der Verfasser beim Lesen selbst getroffen. ChatGPT diente
ausschliesslich als Schreibwerkzeug: Es hat die vom Verfasser
getroffenen Einstufungen in die Tabellenform des Protokolls gebracht
und die Formulierungen vereinheitlicht. Es hat keine Einstufung
vorgeschlagen.

Am 27.08.2026 hat Claude (Anthropic) vier der zwoelf Faelle
unabhaengig an den GitHub-Seiten gegengeprueft: PR 48, 75, 191 und
371, bei PR 75 zusaetzlich die Dateiansicht. Drei Eintraege wurden
bestaetigt. Bei PR 371 wurde Ebene (c) beanstandet und vom Verfasser
geaendert. Die uebrigen acht Faelle (408, 413, 464, 533, 577, 622,
692, 711) sind noch nicht gegengeprueft.

Diese Gegenpruefung ersetzt die Messung nicht. Sie ist eine zweite,
unabhaengige Beurteilung derselben Quellen und dient dazu, Fehler und
uneinheitliche Anwendung der Regeln sichtbar zu machen.

Fundstellen stammen ausschliesslich aus Titel, Beschreibung,
Kommentaren und Diff des jeweiligen Pull Requests. Fuer Stratum,
Ausgang, Kommentarzahl und budgetbedingt ausgelassene Dateien gilt
docs/sample_formulation_probe.md. Commit-Nachrichten und verlinkte
Issues werden nicht als Fundstellen verwendet.

## Grundregel

Ein Bestandteil gilt als belegt, wenn er sich aus Titel,
Beschreibung, Kommentaren oder Diff des Pull Requests entnehmen
laesst. Muesste er ergaenzt werden, ohne ihn in der Quelle zu finden,
gilt er als nicht belegt. Im Zweifel: nicht belegt.

K9 fragt, ob die Quelle einen Bestandteil liefert, nicht ob sie ihn
praezise liefert. Unschaerfe wird unter Bemerkung vermerkt und bei
K1 und K3 beruecksichtigt.

Keine Konto- oder Personennamen aus den Pull Requests in diesem
Protokoll.

## Pflichtbestandteile je Ebene

| Ebene | Pflichtbestandteile | gedeckt, wenn |
|---|---|---|
| (a) User Story | Rolle, Means | beide belegt |
| (b) EARS | Systemname, Systemreaktion | beide belegt |
| (c) Modalitaet | Verbindlichkeitsstufe | belegt |
| (d) Qualitaetsregeln | keine | K9 nicht anwendbar |

Hinweis zu Ebene (b): Die generische EARS-Struktur enthaelt
Vorbedingung und Ausloeser als optionale Satzteile; fest sind
Systemname, shall und Systemreaktion. Das Ubiquitous-Muster kommt
ohne Schluesselwort und ohne Bedingung aus. Eine Systemreaktion muss
daher nicht die Antwort auf ein Ereignis sein. Ob ein Ausloeser oder
eine Vorbedingung belegt ist, wird gesondert erfasst.

Das Wort `shall` in einem EARS-Beispielsatz ist ein Formbestandteil
des EARS-Musters. Es wird nicht nachtraeglich als Beleg fuer eine
Verbindlichkeitsstufe der PR-Quelle gewertet.

Hinweis zu Ebene (d): Diese Ebene schreibt keine Satzteile vor,
sondern stellt Qualitaets-, Sprach- und Attributregeln auf. K9 ist
fuer sie nicht anwendbar.

## Teil A: Messung fuer K9

Zwoelf Pull Requests. Je Pull Request eine Kreuztabelle und ein
Beispielsatz in der am besten gedeckten Ebene. Wenn keine Ebene
vollstaendig gedeckt ist, wird kein Beispielsatz konstruiert.

### PR 48 (S3, closed_unmerged)

Quelllage: Beschreibung ja, ein Satz. Kommentare 1. Diff nicht
budgetbedingt gekuerzt. Eine geaenderte Python-Datei.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung, Kommentar oder Diff genannt |
| (a) | Means | ja | Titel und Beschreibung: weitere Gates in die Catalyst-Gate-Uebersetzung aufnehmen |
| (b) | Systemname | ja | Titel: catalyst gate translation dictionary |
| (b) | Systemreaktion | ja | Titel und Beschreibung: das Woerterbuch soll weitere Gates enthalten |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe erkennbar; die spaetere Uebernahme allein belegt keine Stufe |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) ja, (c) nein

Beispielsatz:
The catalyst gate translation dictionary shall include additional gates.

Bemerkung: Die geforderte Faehigkeit ist unbestimmt formuliert;
welche Gates gemeint sind, wird erst im Diff konkret. Der Ausgang
closed_unmerged bedeutet hier keine inhaltliche Ablehnung: Ein
Kommentar bestaetigt, dass die Aenderung manuell uebernommen wurde.
Die Systemreaktion wird mit ja bewertet, weil EARS keine
Ereignisbedingung verlangt.

### PR 75 (S4, merged, keine Beschreibung, 0 Kommentare)

Quelllage: Keine Beschreibung. Kommentare 0. Diff nicht
budgetbedingt gekuerzt. 16 geaenderte `.rst`-Dateien; die
Files-changed-Ansicht zeigt ausschliesslich geloeschte
Dokumentationsdateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel oder Diff genannt |
| (a) | Means | ja | Titel und Diff: Korrektur der Dokumentation durch Entfernen betroffener Dokumentationsdateien |
| (b) | Systemname | nein | kein eindeutiges Qrisp-System oder Bauteil als Subjekt benannt; "documentation" ist nur ein allgemeiner Artefaktbereich |
| (b) | Systemreaktion | ja | Diff: die betroffenen Dokumentationsdateien werden entfernt |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe erkennbar; der Merge allein belegt keine Stufe |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) nein, (c) nein

Beispielsatz:
Nicht gebildet: Keine Ebene ist vollstaendig gedeckt.

Bemerkung: Der Titel "fixes of documentation" ist sehr unspezifisch.
Der Diff belegt die Entfernung von 16 Dokumentationsdateien, liefert
aber keinen eindeutigen Systemnamen und keinen Zweck der Aenderung.
Deshalb wird kein Systemname ergaenzt.

### PR 191 (S2, merged, 0 Kommentare)

Quelllage: Beschreibung ja, ein kurzer Satz. Kommentare 0. Diff nicht
budgetbedingt gekuerzt. 29 geaenderte Dateien: 11 PNG-Dateien,
1 PPTX-Datei, 2 Python-Dateien, 13 RST-Dateien und 2 SVG-Dateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung oder Diff genannt |
| (a) | Means | ja | Beschreibung: Redesign der Tutorials page |
| (b) | Systemname | ja | Beschreibung: Tutorials page |
| (b) | Systemreaktion | ja | Beschreibung: die Tutorials page soll neu gestaltet werden |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe erkennbar |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) ja, (c) nein

Beispielsatz:
The Tutorials page shall be redesigned.

Bemerkung: Die Beschreibung benennt die Aenderung, aber weder eine
Nutzerrolle noch einen Zweck. Einzelheiten der Neugestaltung sind
nur im Diff sichtbar und werden fuer die K9-Entscheidung nicht
hinzugedichtet.

### PR 371 (S3, closed_unmerged, 4 Kommentare)

Quelllage: Beschreibung ja, ausfuehrlich. Kommentare 4. Diff nicht
budgetbedingt gekuerzt. 25 geaenderte Dateien: 10 Python-Dateien und
15 RST-Dateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | ja | Kommentar: ausdruecklicher Bezug auf moegliche Probleme bzw. painpoints von Nutzern |
| (a) | Means | ja | Beschreibung: Einfuehrung einer neuen BlockEncoding class als erweiterbare Struktur fuer Block-Encodings |
| (b) | Systemname | ja | Titel und Beschreibung: BlockEncoding class |
| (b) | Systemreaktion | ja | Beschreibung: die Klasse stellt eine erweiterbare Struktur bereit und kann zugehoerige Methoden buendeln |
| (c) | Verbindlichkeitsstufe | nein | keine Stufe fuer die rekonstruierte Anforderung erkennbar; die Soll-Aussage im Kommentar betrifft das Vorgehen vor dem Merge, nicht die Verbindlichkeit der Klasse |

Ends belegt: ja. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) ja, (b) ja, (c) nein

Beispielsatz:
As a user, I want block encodings to be represented by a
BlockEncoding class so that the representation can evolve without
breaking changes.

Bemerkung: Die Quelllage ist reichhaltig. Die Beschreibung nennt
konkrete Schwaechen der bisherigen Tupelstruktur, darunter fehlende
Normalisierungsinformation, nur eine Ancilla-Variable und mangelnde
Erweiterbarkeit. Ein Kommentar nennt Nutzerprobleme und empfiehlt,
vor einem Merge weitere Funktionen aufzubauen. Diese Empfehlung
betrifft das Vorgehen im Pull Request und wird deshalb nicht als
Verbindlichkeitsstufe der Anforderung gewertet.

### PR 408 (S6, closed_unmerged, keine Codeaenderung, 1 Kommentar)

Quelllage: Beschreibung ja, aber ausdruecklich unvollstaendig.
Kommentare 1. Keine geaenderten Dateien; es gibt keinen Diff-Inhalt.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung oder Kommentar genannt |
| (a) | Means | ja | Kommentar: neue Qrisp-Dokumentationsseite zur Klaerung der Bit-Ordering-Konventionen |
| (b) | Systemname | ja | Kommentar: neue Dokumentationsseite in Qrisp |
| (b) | Systemreaktion | ja | Kommentar: die Dokumentationsseite soll die Bit-Ordering-Konventionen in Qrisp klaeren |
| (c) | Verbindlichkeitsstufe | ja | Kommentar: die Dokumentationsloesung sollte in einem separaten PR umgesetzt werden |

Ends belegt: ja. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) ja, (c) ja

Beispielsatz:
The Qrisp documentation shall clarify the bit-ordering conventions
used across Qrisp.

Bemerkung: Der urspruengliche Implementierungsansatz wurde nach
begrifflicher Pruefung verworfen. Der Kommentar beschreibt als
konkrete Folgeloesung eine Dokumentationsseite, um die bestehende
Verwirrung zu beseitigen. Es gibt keine Codeaenderung. Der Ausgang
closed_unmerged ist deshalb nicht als einfache Ablehnung des
zugrunde liegenden Bedarfs zu lesen.

### PR 413 (S5, closed_unmerged, 36 Dateien ohne Patch-Text, 0 Kommentare)

Quelllage: Beschreibung ja, aber nur als Verweis auf ein Issue.
Kommentare 0. 97 geaenderte Dateien. Fuer 36 Dateien fehlt in der
aufbereiteten Stichprobe wegen des PR-Budgets Patch-Text.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung oder verfuegbarem Diff genannt |
| (a) | Means | ja | Titel: metric caching fix |
| (b) | Systemname | nein | kein eindeutig benanntes Qrisp-Bauteil als Subjekt; "metric caching" bezeichnet den betroffenen Mechanismus, aber keinen eindeutigen Systemnamen |
| (b) | Systemreaktion | nein | Titel nennt nur einen "metric caching fix"; eine konkrete Handlung bzw. Sollreaktion eines benannten Bauteils ist nicht belegt |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe in den zugelassenen Quellen erkennbar |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) nein, (c) nein

Beispielsatz:
Nicht gebildet: Keine Ebene ist vollstaendig gedeckt.

Bemerkung: Die Beschreibung enthaelt nur einen Issue-Verweis. Der
Inhalt des verlinkten Issues wird nach der Grundregel nicht als
Ersatzquelle verwendet. Wegen der sehr grossen Aenderungsmenge und
36 Dateien ohne Patch-Text wird keine konkrete Fehlerursache oder
Sollreaktion rekonstruiert. Der Titel reicht fuer einen groben
Means-/Verhaltenshinweis, nicht fuer einen eindeutigen Systemnamen.

### PR 464 (S2, merged, 0 Kommentare)

Quelllage: Beschreibung ja, ein Satz plus Issue-Verweis. Kommentare 0.
Diff nicht budgetbedingt gekuerzt. Zwei geaenderte Dateien:
README.md und ein Notebook.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung oder Diff genannt |
| (a) | Means | ja | Beschreibung: Implementierung der exponentiation by squaring im Factoring-Demo korrigieren |
| (b) | Systemname | ja | Beschreibung: factoring (Shor's algorithm) demo |
| (b) | Systemreaktion | ja | Beschreibung: das Demo soll die korrigierte Implementierung der exponentiation by squaring verwenden |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe erkennbar |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) ja, (c) nein

Beispielsatz:
The factoring (Shor's algorithm) demo shall use the corrected
exponentiation-by-squaring implementation.

Bemerkung: Der Fehlerbereich und das betroffene Demo sind klar
benannt. Die Beschreibung nennt aber weder eine Nutzerrolle noch
einen Zweck. Der verlinkte Issue-Inhalt wird nicht als Fundstelle
verwendet.

### PR 533 (S1, merged, 75 Kommentare)

Quelllage: Beschreibung ja, ausfuehrlich. Kommentare 75 nach der
Stichprobenzaehlung. Diff nicht budgetbedingt gekuerzt. Neun
geaenderte RST-Dokumentationsdateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | ja | Beschreibung: new contributors und students |
| (a) | Means | ja | Beschreibung: neuer Development Guide in der API-Referenz |
| (b) | Systemname | ja | Titel und Beschreibung: Development Guide |
| (b) | Systemreaktion | ja | Beschreibung: der Guide stellt einen zentral auffindbaren Einstiegspunkt bereit und dokumentiert Beitragskonventionen |
| (c) | Verbindlichkeitsstufe | ja | Beschreibung: ausdrueckliche Soll-Aussage, den Guide bei neuen Pipelines und Aenderungen aktuell zu halten |

Ends belegt: ja. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) ja, (b) ja, (c) ja

Beispielsatz:
As a new contributor, I want a single discoverable Development Guide
so that I can navigate the codebase and find contribution standards
in one place.

Bemerkung: Die Beschreibung liefert Rolle, Aenderung und Nutzen
ausdruecklich. Der Guide wird zugleich als Ausgangspunkt und nicht
als endgueltiger Vorschlag beschrieben. Eine ausdrueckliche
Soll-Aussage zur Pflege des Guides liefert die Modalitaet.

### PR 577 (S1, merged, 3 Kommentare)

Quelllage: Beschreibung ja, sehr ausfuehrlich. Kommentare 3 nach der
Stichprobenzaehlung. Diff nicht budgetbedingt gekuerzt. Acht
geaenderte Python-Dateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe als Nutzerrolle in Beschreibung, Kommentaren oder Diff genannt |
| (a) | Means | ja | Beschreibung: neue xDSL-Rewrite-Paesse zur Bereinigung des erzeugten IR und Rueckgabe des benoetigten xDSL Context |
| (b) | Systemname | ja | Beschreibung: scalar_linalg_folding bzw. FoldScalarLinalgGeneric |
| (b) | Systemreaktion | ja | Beschreibung: 0-dimensionale linalg.generic-Operationen werden in skalare Arithmetik zurueckgefaltet |
| (c) | Verbindlichkeitsstufe | ja | Beschreibung: der xDSL Context wird ausdruecklich als fuer das Ausfuehren von xDSL-Transformationspaessen erforderlich bezeichnet |

Ends belegt: ja. EARS-Muster: WHILE.
Ausloeser/Vorbedingung belegt: ja (`lower_stablehlo=True`).

Gedeckt: (a) nein, (b) ja, (c) ja

Beispielsatz:
While lower_stablehlo is true, the scalar_linalg_folding pass shall
fold zero-dimensional linalg.generic operations into scalar
arithmetic.

Bemerkung: Der PR enthaelt mehrere eigenstaendige
Verhaltensaenderungen. Fuer den Beispielsatz wurde der
scalar_linalg_folding-Pass gewaehlt, weil Verhalten und Bedingung
ausdruecklich beschrieben sind. Die erkannte Notwendigkeitsstufe
bezieht sich in der Quelle auf den xDSL Context; sie wird nicht aus
dem Merge abgeleitet.

### PR 622 (S1, merged, 13 Kommentare)

Quelllage: Beschreibung ja, ausfuehrlich. Kommentare 13 nach der
Stichprobenzaehlung. Diff nicht budgetbedingt gekuerzt. Vier
geaenderte Python-Dateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | ja | Beschreibung: users |
| (a) | Means | ja | Beschreibung: benutzerdefinierte Circuit-Transformation-Paesse ueber ein pm-/PassManager-Argument einspeisen |
| (b) | Systemname | ja | Titel und Beschreibung: QrispSimulatorBackend |
| (b) | Systemreaktion | ja | Beschreibung: der PassManager wird auf jeden Circuit vor der Simulation angewendet |
| (c) | Verbindlichkeitsstufe | ja | Kommentar: ausdrueckliche Soll-/Empfehlungsaussage zu einer PassManager-Referenz in der abstrakten Backend-Klasse |

Ends belegt: ja. EARS-Muster: WHEN.
Ausloeser/Vorbedingung belegt: ja; Verarbeitung eines Circuits vor
der Simulation.

Gedeckt: (a) ja, (b) ja, (c) ja

Beispielsatz:
As a user, I want to inject custom circuit transformation passes into
QrispSimulatorBackend so that I can inspect or transform circuits
before simulation.

Bemerkung: Die Beschreibung liefert Rolle, Feature, Systemverhalten
und Nutzen deutlich. Debugging sowie transparente
Transpilation/Optimierung werden als Nutzen genannt. Fuer die
Systemreaktion ist ein Ausloeser belegt: Der PassManager wird auf
einen Circuit angewendet, bevor dieser simuliert wird. Deshalb wird
das EARS-Muster WHEN statt Ubiquitous verwendet. Eine Soll-Aussage in
der Diskussion belegt zusaetzlich eine Verbindlichkeitsstufe fuer
eine verwandte Architekturentscheidung.

### PR 692 (S5, closed_unmerged, 14 Dateien ohne Patch-Text, 0 Kommentare)

Quelllage: Beschreibung ja, ein Satz. Kommentare 0. 33 geaenderte
Dateien: 1 IPYNB-, 25 Python-, 5 RST-, 1 TOML- und 1 YML-Datei.
Fuer 14 Dateien fehlt in der aufbereiteten Stichprobe wegen des
PR-Budgets Patch-Text.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | nein | keine Personengruppe in Titel, Beschreibung oder verfuegbarem Diff genannt |
| (a) | Means | ja | Beschreibung: Thread-Safety-Probleme in cudaq_kernel.py wurden behoben bzw. sollen behoben sein |
| (b) | Systemname | ja | Beschreibung: cudaq_kernel.py |
| (b) | Systemreaktion | nein | Beschreibung nennt Thread-Safety-Probleme, aber keine konkrete Handlung des Bauteils; der fehlende Patch-Text wird nicht rekonstruiert |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe erkennbar |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) nein, (c) nein

Beispielsatz:
Nicht gebildet: Keine Ebene ist vollstaendig gedeckt.

Bemerkung: Die Beschreibung nennt Thread-Safety als Fehlerbereich,
erklaert aber weder den konkreten Defekt noch eine konkrete Handlung
des betroffenen Bauteils. Die Aussage zum Pipeline-Test wird nicht
als User-Story-Ends interpretiert. Wegen 14 Dateien ohne Patch-Text
wird keine Sollreaktion aus nicht sichtbarem Diff-Inhalt
rekonstruiert. Deshalb wird die Systemreaktion mit nein bewertet.

### PR 711 (S4, merged, keine Beschreibung, 0 Kommentare)

Quelllage: Keine Beschreibung. Kommentare 0. Diff nicht
budgetbedingt gekuerzt. Zwei geaenderte Dateien: eine PNG-Datei und
eine RST-Datei. Der RST-Diff enthaelt sieben Ergaenzungen.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | ja | Diff-Kontext des Development Guide: new contributors |
| (a) | Means | ja | Titel und Diff: Development-Guide-Slide bzw. Bild in den Development Guide aufnehmen |
| (b) | Systemname | ja | Titel und Diff: Development Guide |
| (b) | Systemreaktion | ja | Diff: der Development Guide bindet das Qrisp-Development-Bild ein |
| (c) | Verbindlichkeitsstufe | nein | keine Muss-, Soll- oder Kann-Stufe in Titel oder Diff erkennbar |

Ends belegt: nein. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) ja, (b) ja, (c) nein

Beispielsatz:
The Development Guide shall include the Qrisp development slide.

Bemerkung: Die Rolle ist nur im unmittelbar sichtbaren RST-Diff-
Kontext belegt: Der Guide wird dort als fuer neue Beitragende
einladend beschrieben. Der Diff erklaert jedoch nicht ausdruecklich,
welchen eigenen Zweck gerade das neu eingefuegte Bild erfuellt;
deshalb wird Ends fuer diese konkrete Aenderung nicht als belegt
gewertet.

### Auswertung Teil A

| Ebene | gedeckt | von | Anteil | Note K9 |
|---|---:|---:|---:|---:|
| (a) | 4 | 12 | 33,3 % | 0 |
| (b) | 9 | 12 | 75,0 % | 1 |
| (c) | 4 | 12 | 33,3 % | 0 |
| (d) | n. a. | | | n. a. |

Schwellen nach docs/formatauswahl.md Abschnitt 6:
ab 80 Prozent Note 2, ab 40 Prozent Note 1, darunter Note 0.

Empfindlichkeitspruefung nach R8:
- Ebene (a): Eine obere Schwelle von 70 oder 90 Prozent aendert die
  Note nicht; 33,3 Prozent bleiben unter 40 Prozent.
- Ebene (b): Beim festgelegten 80-Prozent-Schwellenwert ergibt
  75,0 Prozent Note 1. Bei einer alternativen Schwelle von
  70 Prozent waere es Note 2; bei 90 Prozent bleibt es Note 1.
- Ebene (c): Eine obere Schwelle von 70 oder 90 Prozent aendert die
  Note nicht; 41,7 Prozent bleiben im Bereich der Note 1.

## Teil B: Messung fuer K6

Drei Referenzinhalte mal vier Ebenen, also zwoelf Saetze. Alle Ebenen
tragen denselben fachlichen Inhalt, damit der Vergleich fair ist.

### Festlegung der Referenzinhalte

Die drei Referenzinhalte wurden am 26.08.2026 vor den
Formulierungsversuchen in Teil B konstruiert. Das ist im
Protokoll-Template ausdruecklich als moegliche Herkunft vorgesehen.

Die fachlichen Kerne stammen unmittelbar aus ISO/IEC/IEEE 29148:2018:
- 9.6.12 nennt unter anderem Validitaetspruefungen von Eingaben als
  funktionalen Inhalt.
- 9.6.14 verlangt messbare Leistungsanforderungen und gibt als
  Zahlenbeispiel 95 Prozent der Transaktionen in weniger als einer
  Sekunde an.
- 9.6.18 c nennt fuer Security unter anderem die
  Integritaetspruefung kritischer Variablen.

Damit K6 die Eignung fuer die drei Anforderungsarten prueft und nicht
erneut die Quellvollstaendigkeit von K9 misst, enthalten alle drei
konstruierten Referenzinhalte zusaetzlich dieselben neutralen
Metainformationen: Rolle `user`, Systemname `software` und eine
verbindliche Muss-Stufe. Diese Ergaenzungen sind Teil der
konstruierten Referenzinhalte und werden nicht der Norm zugeschrieben.

### Die drei Referenzinhalte

| Art | Bezug zur Norm | Inhalt in einem Satz | Herkunft |
|---|---|---|---|
| funktional | 29148 Abschn. 9.6.12 | For a user, it is mandatory that the software validates each input before processing. | konstruiert aus 9.6.12, Validitaetspruefung von Eingaben |
| leistungsbezogen | 29148 Abschn. 9.6.14 | For a user, it is mandatory that the software processes 95 % of transactions in less than 1 s. | konstruiert aus dem messbaren Zahlenbeispiel in 9.6.14 |
| sicherheitsbezogen | 29148 Abschn. 9.6.18 c | For a user, it is mandatory that the software checks data integrity for critical variables. | konstruiert aus 9.6.18 c, Integritaetspruefung kritischer Variablen |

### Versuche

| Ebene | funktional | leistungsbezogen | sicherheitsbezogen |
|---|---|---|---|
| (a) User Story | As a user, I want the software to validate each input before processing. | As a user, I want the software to process 95 % of transactions in less than 1 s. | As a user, I want the software to check data integrity for critical variables. |
| (b) EARS | The software shall validate each input before processing. | The software shall process 95 % of transactions in less than 1 s. | The software shall check data integrity for critical variables. |
| (c) Modalitaet | The software MUST validate each input before processing. | The software MUST process 95 % of transactions in less than 1 s. | The software MUST check data integrity for critical variables. |
| (d) Qualitaetsregeln | The software shall validate each input before processing. | The software shall process 95 % of transactions in less than 1 s. | The software shall check data integrity for critical variables. |

Ein Versuch gilt als gelungen, wenn der Satz alle
Pflichtbestandteile der Ebene besetzt und keine Angabe enthaelt, die
der Referenzinhalt nicht hergibt.

Bewertung der Versuche:
- Ebene (a): alle drei gelungen. Rolle und Means sind jeweils
  vorhanden; kein Ends wird hinzuerfunden. Die Ebene bildet die
  Modalitaet nicht selbst ab, verlangt sie aber auch nicht als
  Pflichtbestandteil.
- Ebene (b): alle drei gelungen. Systemname und Systemreaktion sind
  jeweils vorhanden; das Ubiquitous-Muster reicht aus, weil kein
  Ausloeser Bestandteil des Referenzinhalts ist.
- Ebene (c): alle drei gelungen. Die Referenzinhalte kennzeichnen die
  Anforderungen ausdruecklich als verbindlich; `MUST` bildet diese
  Stufe ab.
- Ebene (d): alle drei gelungen. Die Saetze sind jeweils singular,
  positiv und ohne vage offene Formulierung; die Leistungsanforderung
  ist quantitativ messbar. Ebene (d) verlangt keine zusaetzlichen
  Satzbestandteile.

### Auswertung Teil B

| Ebene | gelungen | von 3 | Note K6 |
|---|---:|---:|---:|
| (a) | 3 | 3 | 2 |
| (b) | 3 | 3 | 2 |
| (c) | 3 | 3 | 2 |
| (d) | 3 | 3 | 2 |

Empfindlichkeitspruefung nach R8:
- Ebene (a): 33,3 Prozent. Der Abstand zur 40-Prozent-Grenze betraegt
  weniger als einen Fall. Ein zusaetzlich gedeckter Fall ergaebe
  41,7 Prozent und damit Note 1 statt Note 0.
- Ebene (b): 75,0 Prozent. Ein zusaetzlich gedeckter Fall ergaebe
  83,3 Prozent und damit Note 2 statt Note 1.
- Ebene (c): 33,3 Prozent. Ein zusaetzlich gedeckter Fall ergaebe
  41,7 Prozent und damit Note 1 statt Note 0.
- Alle drei Noten haengen an einem einzigen Fall. Das gehoert in
  Kapitel 7. Die Pruefung an den Werten 70 und 90 Prozent wurde
  gestrichen: sie liegt bei keiner Ebene an der naechstgelegenen
  Schwelle und sagt deshalb nichts aus.

## Beobachtungen fuer Kapitel 7

- Rollen sind in den PR-Quellen deutlich seltener explizit als
  geforderte Aenderungen oder Systemverhalten. Dadurch scheitert
  Ebene (a) in Teil A haeufig bereits am Rollenbestandteil.
- Eine Systemreaktion kann belegt sein, obwohl kein Ausloeser genannt
  wird. Das Ubiquitous-Muster ist deshalb fuer viele PRs die passende
  EARS-Grundform.
- Explizite Verbindlichkeitsstufen treten nur in einem Teil der
  ausfuehrlicheren Beschreibungen oder Kommentare auf. Ein Merge oder
  eine tatsaechlich ausgefuehrte Aenderung wurde nicht als Muss-Stufe
  interpretiert.
- PR 48 zeigt, dass `closed_unmerged` nicht automatisch inhaltliche
  Ablehnung bedeutet, weil ein Kommentar die manuelle Uebernahme der
  Aenderung bestaetigt.
- PR 408 zeigt einen anderen Sonderfall: Ein urspruenglicher
  Implementierungsansatz wurde geschlossen, waehrend im Kommentar
  eine Dokumentationsloesung als Folgeschritt vorgeschlagen wurde.
- Bei PR 413 und PR 692 begrenzt fehlender Patch-Text die
  Nachvollziehbarkeit. Nicht sichtbare Implementierungsdetails wurden
  deshalb nicht rekonstruiert. Bei beiden PRs reicht die knappe
  Formulierung nicht fuer eine konkrete Systemreaktion.
- Bei sehr knappen PRs wie PR 75 oder PR 413 reicht der Titel fuer
  einen groben Means-/Verhaltenshinweis, aber nicht fuer alle
  Pflichtbestandteile einer vollstaendig gedeckten Ebene.
- Teil B zeigt bei den bewusst vollstaendig konstruierten
  Referenzinhalten keine Unterscheidung zwischen den vier Ebenen:
  alle erreichen 3/3. Das ist als Befund zu dokumentieren und nicht
  nachtraeglich durch schwierigere Referenzinhalte zu veraendern.
- Die Referenzinhalte fuer Teil B waren im urspruenglichen
  Protokoll-Template noch nicht konkret festgelegt. Sie wurden am
  26.08.2026 vor den Teil-B-Versuchen festgelegt. Diese zeitliche
  Festlegung sollte in der Aenderungshistorie von
  docs/formatauswahl.md dokumentiert werden, wenn die Messung
  uebernommen wird.
- Rollenverteilung zwischen Verfasser und Werkzeugen: siehe Abschnitt
  "Methodischer Status". Die Einstufungen stammen vom Verfasser und
  beruhen auf den dort genannten Quellen.
- Die Gegenpruefung durch ein zweites Modell ist erst fuer vier von
  zwoelf Faellen erfolgt. Solange sie nicht abgeschlossen ist, gelten
  die Zahlen in den Auswertungstabellen als vorlaeufig.

## Aenderungen nach erneuter Quellenpruefung am 27.08.2026

- PR 413: Systemreaktion von ja auf nein geaendert. Der Titel
  "metric caching fix" nennt keine konkrete Handlung eines Bauteils.
- PR 622: EARS-Muster von Ubiquitous auf WHEN geaendert und
  Ausloeser/Vorbedingung auf ja gesetzt. Die Quelle beschreibt die
  Anwendung des PassManagers auf einen Circuit vor der Simulation.
- PR 692: Systemreaktion von ja auf nein geaendert. Die Beschreibung
  nennt Thread-Safety-Probleme, aber keine konkrete Handlung; nicht
  sichtbarer Patch-Text wurde nicht rekonstruiert. Dadurch ist Ebene
  (b) fuer PR 692 nicht mehr gedeckt.
- PR 371: Verbindlichkeitsstufe von ja auf nein geaendert, nach
  Gegenpruefung durch Claude an der Quelle. Die Soll-Aussage im
  Kommentar betrifft das Vorgehen vor dem Merge, nicht die
  Verbindlichkeit der rekonstruierten Anforderung.
- Folge fuer K9 Ebene (c): 4 von 12 = 33,3 Prozent, damit Note 0
  statt Note 1.
- Folge fuer K9 Ebene (b): 9 von 12 = 75,0 Prozent, damit Note 1
  nach der festgelegten 80-Prozent-Schwelle.

## Abschluss

Inhaltlich ausgefuellt am: 26.08.2026
Zuletzt geaendert am: 29.08.2026
Dauer: nicht dokumentiert; kein Wert wird geschaetzt.
Ergebnisse uebertragen nach docs/formatauswahl.md am: noch nicht
erfolgt.

Status: Teil A vollstaendig ausgefuellt. Vier von zwoelf Faellen
unabhaengig gegengeprueft. Teil B ist neu aufzusetzen, weil die drei
Referenzinhalte Rolle, Systemname und Modalitaet bereits enthalten
und K6 dadurch nicht unterscheidet. Die Auswertungszahlen sind
vorlaeufig.
