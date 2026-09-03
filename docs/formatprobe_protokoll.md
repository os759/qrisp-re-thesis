# Protokoll der Formulierungsprobe (FF2)

Zweck: Nachweis der Messungen fuer K6 und K9. Jeder Versuch wird
festgehalten, auch der misslungene.

Grundlage: docs/formatauswahl.md, Entscheidung C2.
Stichprobe: docs/sample_formulation_probe.md
Bearbeitet von: Omar Assad Salem (Verfasser)
Schreibwerkzeug: ChatGPT, siehe Abschnitt "Methodischer Status"
Begonnen: 26.08.2026
Zuletzt geaendert: 02.09.2026
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
geaendert.

Am 30.08.2026 hat Claude die uebrigen acht Faelle gegengeprueft:
PR 408, 413, 464, 533, 577, 622, 692 und 711, jeweils in der
Ansicht "Conversation". Die Ansicht "Files changed" war dem Modell
nicht zugaenglich. Bei PR 711 blieben deshalb Rolle und
Systemreaktion ungeprueft; beide stuetzen sich auf den Diff. Vier
Eintraege wurden beanstandet und vom Verfasser geaendert: die
Verbindlichkeitsstufe bei PR 408, 533, 577 und 622. Grundlage waren
die zuvor festgelegten Regeln R9 und R10.

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
| (a) | Rolle | ja | Kommentar: ausdruecklicher Bezug auf moegliche Probleme bzw. painpoints von Nutzern. Pauschale Gruppe, nach R9 belegt und als generische Rolle gekennzeichnet |
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
| (c) | Verbindlichkeitsstufe | nein | keine Stufe fuer die rekonstruierte Anforderung erkennbar; die Soll-Aussage im Kommentar betrifft den Pull Request, in dem die Loesung umzusetzen sei (R10) |

Ends belegt: ja. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) nein, (b) ja, (c) nein

Beispielsatz:
The Qrisp documentation shall clarify the bit-ordering conventions
used across Qrisp.

Bemerkung: Der urspruengliche Implementierungsansatz wurde nach
begrifflicher Pruefung verworfen. Der Kommentar beschreibt als
konkrete Folgeloesung eine Dokumentationsseite, um die bestehende
Verwirrung zu beseitigen. Es gibt keine Codeaenderung. Der Ausgang
closed_unmerged ist deshalb nicht als einfache Ablehnung des
zugrunde liegenden Bedarfs zu lesen.
Zur Modalitaet: Der Kommentar enthaelt eine Soll-Aussage dazu, in
welchem Pull Request die Loesung umzusetzen sei. Nach R10 belegt sie
keine Verbindlichkeitsstufe der rekonstruierten Anforderung. Die
Aussage, eine Dokumentationsseite sei die beste konkrete Loesung,
ist ausdruecklich als eigene Einschaetzung des Verfassers des
Kommentars formuliert und wird ebenfalls nicht als Stufe gewertet.

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
| (c) | Verbindlichkeitsstufe | nein | die Soll-Aussage in der Beschreibung betrifft die laufende Pflege des Guides, also eine zweite, hier nicht rekonstruierte Anforderung (R10) |

Ends belegt: ja. EARS-Muster: Ubiquitous.
Ausloeser/Vorbedingung belegt: nein.

Gedeckt: (a) ja, (b) ja, (c) nein

Beispielsatz:
As a new contributor, I want a single discoverable Development Guide
so that I can navigate the codebase and find contribution standards
in one place.

Bemerkung: Die Beschreibung liefert Rolle, Aenderung und Nutzen
ausdruecklich. Der Guide wird zugleich als Ausgangspunkt und nicht
als endgueltiger Vorschlag beschrieben. Eine ausdrueckliche
Soll-Aussage zur Pflege des Guides betrifft eine zweite Anforderung
und liefert nach R10 keine Modalitaet fuer die hier rekonstruierte.

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
| (c) | Verbindlichkeitsstufe | nein | die Notwendigkeitsaussage betrifft den xDSL Context, also eine zweite, hier nicht rekonstruierte Anforderung (R10); zudem beschreibt sie eine technische Voraussetzung, keine normative Stufe |

Ends belegt: ja. EARS-Muster: WHILE.
Ausloeser/Vorbedingung belegt: ja (`lower_stablehlo=True`).

Gedeckt: (a) nein, (b) ja, (c) nein

Beispielsatz:
While lower_stablehlo is true, the scalar_linalg_folding pass shall
fold zero-dimensional linalg.generic operations into scalar
arithmetic.

Bemerkung: Der PR enthaelt mehrere eigenstaendige
Verhaltensaenderungen. Fuer den Beispielsatz wurde der
scalar_linalg_folding-Pass gewaehlt, weil Verhalten und Bedingung
ausdruecklich beschrieben sind. Die erkannte Notwendigkeitsstufe
bezieht sich in der Quelle auf den xDSL Context und damit auf eine
zweite Anforderung. Nach R10 belegt sie keine Stufe fuer die hier
rekonstruierte Anforderung.

### PR 622 (S1, merged, 13 Kommentare)

Quelllage: Beschreibung ja, ausfuehrlich. Kommentare 13 nach der
Stichprobenzaehlung. Diff nicht budgetbedingt gekuerzt. Vier
geaenderte Python-Dateien.

| Ebene | Bestandteil | belegt | Fundstelle |
|---|---|---|---|
| (a) | Rolle | ja | Beschreibung: users. Pauschale Gruppe, nach R9 belegt und als generische Rolle gekennzeichnet |
| (a) | Means | ja | Beschreibung: benutzerdefinierte Circuit-Transformation-Paesse ueber ein pm-/PassManager-Argument einspeisen |
| (b) | Systemname | ja | Titel und Beschreibung: QrispSimulatorBackend |
| (b) | Systemreaktion | ja | Beschreibung: der PassManager wird auf jeden Circuit vor der Simulation angewendet |
| (c) | Verbindlichkeitsstufe | nein | die Soll-/Empfehlungsaussage betrifft die abstrakte Backend-Klasse und wurde auf einen spaeteren Entwicklungszyklus vertagt; sie belegt nach R10 keine Stufe fuer die hier rekonstruierte Anforderung |

Ends belegt: ja. EARS-Muster: WHEN.
Ausloeser/Vorbedingung belegt: ja; Verarbeitung eines Circuits vor
der Simulation.

Gedeckt: (a) ja, (b) ja, (c) nein

Beispielsatz:
As a user, I want to inject custom circuit transformation passes into
QrispSimulatorBackend so that I can inspect or transform circuits
before simulation.

Bemerkung: Die Beschreibung liefert Rolle, Feature, Systemverhalten
und Nutzen deutlich. Debugging sowie transparente
Transpilation/Optimierung werden als Nutzen genannt. Fuer die
Systemreaktion ist ein Ausloeser belegt: Der PassManager wird auf
einen Circuit angewendet, bevor dieser simuliert wird. Deshalb wird
das EARS-Muster WHEN statt Ubiquitous verwendet. Die Soll-Aussage in
der Diskussion betrifft eine verwandte Architekturentscheidung zur
abstrakten Backend-Klasse und belegt nach R10 keine Stufe fuer diese
Anforderung. Die Rolle "users" ist pauschal und nach R9 als
generische Rolle gekennzeichnet.

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

Stand nach der Gegenpruefung vom 30.08.2026 und nach Anwendung von
R9 und R10 auf alle zwoelf Faelle.

| Ebene | gedeckt | von | Anteil | Note K9 |
|---|---:|---:|---:|---:|
| (a) | 4 | 12 | 33,3 % | 0 |
| (b) | 9 | 12 | 75,0 % | 1 |
| (c) | 0 | 12 | 0,0 % | 0 |
| (d) | n. a. | | | n. a. |

Schwellen nach docs/formatauswahl.md Abschnitt 6, umgerechnet auf
zwoelf Faelle: Note 2 ab 10 gedeckten Faellen, Note 1 ab 5, sonst
Note 0. Ein Fall entspricht 8,33 Prozentpunkten.

Zusatzzaehlung nach R9. Zwei der vier bei Ebene (a) gedeckten Faelle
stuetzen sich auf eine pauschale Rolle: PR 371 und PR 622. Ohne diese
Faelle waeren 2 von 12 gedeckt, also 16,7 Prozent. Die Note bleibt in
beiden Zaehlungen 0.

Empfindlichkeitspruefung nach R8, jeweils an der naechstgelegenen
Schwelle:
- Ebene (a): 4 von 12. Zur Schwelle von 5 Faellen fehlt genau ein
  Fall. Ein zusaetzlich gedeckter Fall ergaebe Note 1 statt Note 0.
- Ebene (b): 9 von 12. Zur Schwelle von 10 Faellen fehlt genau ein
  Fall. Ein zusaetzlich gedeckter Fall ergaebe Note 2 statt Note 1.
- Ebene (c): 0 von 12. Zur Schwelle von 5 Faellen fehlen fuenf Faelle.
  Diese Note ist als einzige unempfindlich gegen einen Einzelfall.
- Die Noten der Ebenen (a) und (b) haengen damit an je einem
  einzigen Pull Request. Das gehoert nach Kapitel 7.
- Ohne R10 waere Ebene (c) bei 4 von 12 und erhielte ebenfalls
  Note 0. R10 veraendert die Zahl, nicht die Entscheidung.

## Teil B: Messung fuer K6

Drei Referenzinhalte mal zwei bewertete Ebenen, also sechs Saetze.
Fuer die Ebenen (c) und (d) ist K6 nicht anwendbar. Die Festlegung
dazu steht in docs/formatauswahl.md, Abschnitt 2 bei K6 und in der
Aenderungshistorie zum 31.08.2026.

### Verworfene erste Fassung vom 26.08.2026

Die erste Fassung von Teil B benutzte drei konstruierte
Referenzinhalte der Form "For a user, it is mandatory that the
software ...". Sie enthielten Rolle, Systemname und
Verbindlichkeitsstufe bereits fertig. Jede Ebene musste sie nur
uebernehmen; ein Versuch konnte nicht misslingen. Alle vier Ebenen
erreichten 3 von 3. Diese Fassung wurde am 02.09.2026 verworfen. Ihr
Wortlaut bleibt ueber die Versionsgeschichte des Repositorys
nachvollziehbar.

### Rahmen und Referenzinhalte

Massgeblich ist die Festlegung vom 02.09.2026 in
docs/formatauswahl.md, Abschnitt 6. Sie wurde vor den
Formulierungsversuchen getroffen (R2).

Rahmen, fuer alle drei Inhalte gleich: Das betrachtete System ist
eine Software-Bibliothek (`the library`). Sie wird von entwickelnden
Personen beim Programmieren verwendet (`developers`). Der Rahmen
nennt keine Verbindlichkeitsstufe und keinen Nutzniesser der
einzelnen Anforderung.

| Art | Bezug zur Norm | Referenzinhalt |
|---|---|---|
| funktional | 29148 Abschn. 9.6.12 a | The inputs are checked for validity before they are processed. |
| leistungsbezogen | 29148 Abschn. 9.6.14 | 95 % of the transactions are processed in less than 1 s. |
| sicherheitsbezogen | 29148 Abschn. 9.6.18 c 5 | The integrity of data in critical variables is checked. |

Die Inhalte geben nur den fachlichen Kern der jeweiligen Art wieder.
Sie stehen in der Aussageform. Die Norm formuliert das
Leistungsbeispiel mit `shall`; das Modalverb wurde entfernt.

### Versuche

Die sechs Saetze stammen vom Verfasser. Claude hat sie anschliessend
unabhaengig gegengeprueft und allen sechs Einstufungen zugestimmt.

| Nr. | Ebene | Art | Satz |
|---|---|---|---|
| 1 | (a) User Story | funktional | As a developer, I want inputs to be checked for validity before they are processed. |
| 2 | (b) EARS | funktional | The library shall check inputs for validity before processing them. |
| 3 | (a) User Story | leistungsbezogen | As a developer, I want 95 % of transactions to be processed in less than 1 s. |
| 4 | (b) EARS | leistungsbezogen | The library shall process 95 % of transactions in less than 1 s. |
| 5 | (a) User Story | sicherheitsbezogen | As a developer, I want the integrity of data in critical variables to be checked. |
| 6 | (b) EARS | sicherheitsbezogen | The library shall check the integrity of data in critical variables. |

Ein Versuch gilt als gelungen, wenn der Satz alle Pflichtbestandteile
der Ebene besetzt und keine Angabe enthaelt, die Rahmen oder
Referenzinhalt nicht hergeben. Das Wort `shall` ist Formbestandteil
des EARS-Musters und zaehlt nicht als hinzugefuegte Angabe.

| Nr. | Pflichtbestandteil 1 | Pflichtbestandteil 2 | hinzugefuegt | Ergebnis |
|---|---|---|---|---|
| 1 | Rolle: a developer | Means: inputs to be checked for validity before they are processed | keine | gelungen |
| 2 | Systemname: the library | Systemreaktion: check inputs for validity before processing them | keine | gelungen |
| 3 | Rolle: a developer | Means: 95 % of transactions to be processed in less than 1 s | keine | gelungen |
| 4 | Systemname: the library | Systemreaktion: process 95 % of transactions in less than 1 s | keine | gelungen |
| 5 | Rolle: a developer | Means: the integrity of data in critical variables to be checked | keine | gelungen |
| 6 | Systemname: the library | Systemreaktion: check the integrity of data in critical variables | keine | gelungen |

Anmerkungen zu einzelnen Versuchen, ohne Wirkung auf das Ergebnis:

- Nr. 1, 3 und 5 stehen im Passiv und nennen das System nicht. Wer
  die Handlung ausfuehrt, bleibt offen. Die Erfolgsregel verbietet
  nur Hinzufuegungen, nicht Auslassungen. Der Unterschied zu Ebene
  (b), die das System jedes Mal nennt, gehoert zu K1.
- Nr. 2 enthaelt mit `before processing them` eine Zeitangabe im
  Systemreaktionsteil. Sie liesse sich auch als Ausloeser lesen und
  mit dem Event-driven-Muster abbilden. Beide Fassungen sind
  vertretbar; gewaehlt wurde das Ubiquitous-Muster.
- Zu Nr. 5 war vorab geprueft worden, ob die Rolle eine hinzugefuegte
  Angabe ist, weil 29148 Abschn. 9.6.18 c nicht sagt, wem der Schutz
  zugutekommt. Der Rahmen nennt entwickelnde Personen ausdruecklich;
  damit liegt keine Hinzufuegung vor. In dieselbe Richtung weist R9,
  die allerdings fuer K9 formuliert ist und hier nicht gebraucht wird.

### Auswertung Teil B

| Ebene | gelungen | von 3 | Note K6 |
|---|---:|---:|---:|
| (a) User Story | 3 | 3 | 2 |
| (b) EARS | 3 | 3 | 2 |
| (c) Modalitaet | - | - | n. a. |
| (d) Qualitaetsregeln | - | - | n. a. |

Empfindlichkeitspruefung nach R8: Die K6-Skala ist in Faellen
formuliert, nicht in Prozent; eine andere Schwelle gibt es nicht. Bei
3 von 3 bleibt die Note in jedem Fall 2. Empfindlich ist dagegen die
Regelanwendung. Wuerde eine vom Rahmen gelieferte Rolle nicht als
belegt gelten, faellt Ebene (a) auf 0 von 3 und damit auf Note 0.
Ebene (b) bliebe bei 3 von 3, weil die Systemreaktion aus dem
Referenzinhalt selbst stammt. Dieser Sprung ist in Kapitel 7 zu
berichten.

## Beobachtungen fuer Kapitel 7

- Rollen sind in den PR-Quellen deutlich seltener explizit als
  geforderte Aenderungen oder Systemverhalten. Dadurch scheitert
  Ebene (a) in Teil A haeufig bereits am Rollenbestandteil.
- Eine Systemreaktion kann belegt sein, obwohl kein Ausloeser genannt
  wird. Das Ubiquitous-Muster ist deshalb fuer viele PRs die passende
  EARS-Grundform.
- Explizite Verbindlichkeitsstufen fuer die jeweils rekonstruierte
  Anforderung kommen in der Stichprobe nicht vor. Modalaussagen
  finden sich zwar in mehreren Pull Requests, betreffen aber das
  Vorgehen im Pull Request, eine andere Anforderung oder ein
  benachbartes Bauteil. Nach R10 belegen sie keine Stufe. Ein Merge
  oder eine ausgefuehrte Aenderung wurde nicht als Muss-Stufe
  interpretiert. Fuer FF2 folgt daraus: Die Verbindlichkeitsstufe
  ist aus dieser Historie nicht belegbar und muesste beim
  Rekonstruieren gesetzt werden.
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
- Die erste Fassung von Teil B vom 26.08.2026 konnte nicht
  misslingen: Die Referenzinhalte enthielten Rolle, Systemname und
  Verbindlichkeitsstufe bereits. Alle vier Ebenen erreichten 3/3.
  Diese Fassung wurde am 02.09.2026 verworfen und durch Inhalte
  ersetzt, die nur den fachlichen Kern der Norm wiedergeben.
- Auch mit den neuen Referenzinhalten erreichen beide bewerteten
  Ebenen 3 von 3. K6 unterscheidet die Ebenen (a) und (b) nicht.
  Der Befund lautet: Keines der beiden Formate zeigt bei diesen drei
  Anforderungsarten eine typabhaengige Schwaeche. Zugleich misst K6
  in dieser Form vor allem, ob der Rahmen die Pflichtbestandteile
  liefert; die Aussagekraft des Kriteriums ist entsprechend gering.
- Beide bewerteten Ebenen beziehen je einen Pflichtbestandteil aus
  dem Rahmen: Ebene (a) die Rolle, Ebene (b) den Systemnamen. Die
  urspruengliche Annahme, nur Ebene (b) profitiere davon, ist durch
  die Messung widerlegt. Nach R4 gilt die Messung; der Widerspruch
  wird dokumentiert.
- Rollenverteilung zwischen Verfasser und Werkzeugen: siehe Abschnitt
  "Methodischer Status". Die Einstufungen stammen vom Verfasser und
  beruhen auf den dort genannten Quellen.
- Die Gegenpruefung durch ein zweites Modell ist fuer alle zwoelf
  Faelle erfolgt. Sie fuehrte zu fuenf Aenderungen (PR 371, 408, 533, 
  577, 622), alle bei Ebene (c). Die Zahlen fuer Teil A gelten damit
  als abgeschlossen. Teil B wurde am 02.09.2026 neu aufgesetzt und
  gegengeprueft; seine Zahlen gelten ebenfalls als abgeschlossen.

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
- Hinweis: Die hier genannten Zahlen geben den Stand vom 27.08.2026
  wieder. Der abschliessende Stand steht in der Auswertung Teil A.

## Aenderungen nach der Gegenpruefung am 30.08.2026

Grundlage: die am 30.08.2026 festgelegten Regeln R9 und R10 in
docs/formatauswahl.md (Commit 076c396). Claude hat die
Conversation-Ansicht der betroffenen Pull Requests geoeffnet; die
Einstufungen hat der Verfasser uebernommen.

- PR 408: Verbindlichkeitsstufe von ja auf nein geaendert. Die
  Soll-Aussage im Abschlusskommentar betrifft den Pull Request, in
  dem die Dokumentationsloesung umzusetzen sei, nicht die
  Verbindlichkeit der rekonstruierten Anforderung (R10).
- PR 413: alle fuenf Einstufungen bestaetigt.
- PR 464: alle fuenf Einstufungen bestaetigt.
- PR 533: Verbindlichkeitsstufe von ja auf nein geaendert. Die
  Soll-Aussage betrifft die laufende Pflege des Guides, nicht die
  rekonstruierte Anforderung (R10). Rolle, Means, Systemname und
  Systemreaktion bestaetigt. Die Rolle "new contributors and
  students" ist nicht pauschal; R9 greift hier nicht.
- PR 577: Verbindlichkeitsstufe von ja auf nein geaendert. Die
  Notwendigkeitsaussage betrifft den xDSL Context, nicht die
  rekonstruierte Anforderung (R10). Die uebrigen Einstufungen
  einschliesslich der Vorbedingung lower_stablehlo=True bestaetigt.
- PR 622: Verbindlichkeitsstufe von ja auf nein geaendert. Die
  Soll-Aussage betrifft die abstrakte Backend-Klasse und wurde
  vertagt (R10). Rolle, Means, Systemname, Systemreaktion und der
  Ausloeser bestaetigt. Die Rolle "users" ist pauschal und wird nach
  R9 als generische Rolle gekennzeichnet.
- PR 371: keine Aenderung der Einstufung. Die Rolle wird nachtraeglich
  als generische Rolle gekennzeichnet, weil R9 erst am 30.08.2026
  festgelegt wurde und gleichmaessig auf alle zwoelf Faelle wirkt.
- Generische Rollen in der Stichprobe: PR 371 und PR 622. Nicht
  generisch: PR 533 und PR 711.

## Abschluss

Inhaltlich ausgefuellt am: 26.08.2026
Zuletzt geaendert: 02.09.2026
Dauer: nicht dokumentiert; kein Wert wird geschaetzt.
Ergebnisse uebertragen nach docs/formatauswahl.md am: 02.09.2026
(Noten fuer K6). Die Noten fuer K9 werden in Schritt 4c uebertragen.

Status: Teil A vollstaendig ausgefuellt und vollstaendig unabhaengig
gegengeprueft (vier Faelle am 27.08.2026, acht am 30.08.2026). Bei
PR 711 blieben Rolle und Systemreaktion ungeprueft, weil die
Diff-Ansicht dem gegenpruefenden Modell nicht zugaenglich war. Teil B
wurde am 02.09.2026 mit neuen Referenzinhalten neu aufgesetzt und
gegengeprueft. Die Auswertungszahlen gelten als abgeschlossen.
