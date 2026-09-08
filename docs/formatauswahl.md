# Formatauswahl (FF2)

Zweck: Diese Datei dokumentiert das Verfahren, mit dem das
Anforderungsformat fuer die Extraktionspipeline ausgewaehlt wird.
Sie ist die Arbeitsgrundlage fuer den Abschnitt zur Formatauswahl in
Kapitel 4 und fuer die Limitationen in Kapitel 7.

Angelegt: 23.08.2026
Grundlage: Entscheidungen C1 bis C4 in docs/entscheidungen.md

Reihenfolge: Katalog, Skala und Regeln stehen vor jeder Bewertung
fest. Die Stichprobe wird erst danach gezogen. Nachtraegliche
Aenderungen werden in Abschnitt 9 mit Datum und Begruendung
vermerkt.

## 1. Die vier bewerteten Ebenen

Die vier betrachteten Ansaetze regeln unterschiedliche Aspekte einer
Anforderung und sind daher keine gleichartigen Alternativen. RFC 2119
legt ausschliesslich die Bedeutung von Schluesselwoertern fest und
trifft keine Aussage zum Satzbau. EARS gibt ein Satzmuster vor, kennt
aber keine Abstufung der Verbindlichkeit. Eine gemeinsame Rangliste
aller vier Ansaetze waere deshalb sachlich falsch. Bewertet werden
vier Ebenen getrennt.

- (a) Darstellungsperspektive: User Story (Lucassen et al. 2016)
- (b) Satz- und Syntaxmuster: EARS (Mavin et al. 2009, 2010)
- (c) Normative Modalitaet: RFC 2119 / RFC 8174, alternativ die
  Schluesselwoerter nach ISO/IEC/IEEE 29148 Abschn. 5.2.4
- (d) Qualitaets-, Sprach- und Attributregeln: ISO/IEC/IEEE 29148
  Abschn. 5.2.5 bis 5.2.8, ergaenzt um die acht Sprachprobleme aus
  Big EARS und die 13 QUS-Kriterien

Zuordnung von ISO/IEC/IEEE 29148 Abschn. 5.2.4, festgelegt am
07.09.2026: Der Abschnitt enthaelt drei verschiedene Regelarten und
faellt deshalb auf drei Ebenen. Der Aufbausatz und die Beispielsyntax
in Figure 1 gehoeren zu Ebene (b), die Schluesselwoerter zu Ebene (c),
die sprachlichen Vorgaben (positive Formulierung, Aktiv statt Passiv,
Vermeidung von "shall be able to") zu Ebene (d). Ebene (c) wird
ausschliesslich an den Schluesselwoertern gemessen.

Ebene (b) stuetzt sich damit auf zwei Quellen. Figure 1 gibt die
Bestandteile [Condition] [Subject] [Action] [Object] [Constraint of
Action] vor, in einer kurzen Variante auch ohne Condition. EARS
benennt dieselben Pflichtbestandteile, unterscheidet zusaetzlich fuenf
Muster und legt die Reihenfolge der Klauseln fest. EARS ist die
spezifischere der beiden Festlegungen und bleibt der bewertete
Vertreter der Ebene (b). Die Pflichtbestandteile Systemname und
Systemreaktion aendern sich dadurch nicht; die Messung fuer K9 bleibt
gueltig.

Sprache der erzeugten Anforderungen: Englisch (Entscheidung C1).

## 2. Kriterienkatalog

Zehn Kriterien. Acht davon ergeben sich aus der Zielsetzung der
Arbeit und aus FF2: Eindeutigkeit, formale Struktur,
Verifizierbarkeit, maschinelle Verarbeitbarkeit, Eignung fuer
LLM-Ausgaben, Eignung fuer die drei Anforderungsarten,
Verstaendlichkeit fuer das Qrisp-Team und automatische
Validierbarkeit. Zwei weitere wurden im Verlauf der Bearbeitung
ergaenzt: K9 und K10 (Entscheidung C4). Die inhaltliche Herleitung
jedes Kriteriums steht in der jeweiligen Zeile "Herkunft".


Je Kriterium: Leitfrage, woran es pruefbar ist, Herkunft, Quelle der
Note.

### K1 Eindeutigkeit
Leitfrage: Schraenkt der Ansatz die Zahl moeglicher Lesarten eines
Anforderungssatzes ein?
Pruefbar an: Benennt der Ansatz mindestens eine Formulierung, die er
ausschliesst oder ersetzt?
Herkunft: 29148 Abschn. 5.2.5 und 5.2.7; EARS.
Note aus: Literatur. Die Formulierungsprobe dient als Gegenpruefung
ohne eigene Note.

### K2 Formale Struktur
Leitfrage: Gibt der Ansatz feste, benannte Satzbestandteile und ihre
Reihenfolge vor?
Pruefbar an: Laesst sich ein Satz ohne Deutung in seine Bestandteile
zerlegen?
Herkunft: EARS Abschn. 4.1; QUS-Begriffsmodell; 29148 Abschn. 5.2.4.
Note aus: Literatur.

### K3 Verifizierbarkeit
Leitfrage: Erzwingt der Ansatz Angaben, an denen die Erfuellung
ueberpruefbar ist?
Pruefbar an: Verlangt er eine messbare Reaktion, eine Bedingung oder
ein Kriterium?
Abgrenzung zu K1: Ein Satz kann eindeutig und dennoch nicht
nachweisbar sein.
Herkunft: 29148 Abschn. 5.2.5, 9.6.14, 9.6.19.
Note aus: Literatur. Gegenpruefung durch die Probe ohne eigene Note.

### K4 Maschinelle Verarbeitbarkeit
Leitfrage: Laesst sich ein nach dem Ansatz formulierter Satz
verlustfrei in Datenfelder ueberfuehren?
Pruefbar an: Existiert eine feste Zuordnung von Satzteil zu
Feldname?
Herkunft: eigene Setzung, gestuetzt auf die Slotstruktur von EARS.
Note aus: Literatur.

### K5 Eignung fuer LLM-Ausgaben
Leitfrage: Wie zuverlaessig kann ein Sprachmodell das Muster
einhalten, ohne fehlende Bestandteile zu erfinden?
Pruefbar an: Zahl der Pflichtbestandteile, Zahl zulaessiger
Schreibvarianten, Vorhandensein eines Musters fuer den Fall, dass
keine Anforderung vorliegt.
Belegtes Risiko: RFC 2119 Abschn. 6 fordert sparsamen Gebrauch der
Schluesselwoerter. Ein Modell wird dazu neigen, alles als unbedingt
zu formulieren.
Herkunft: eigene Setzung; RFC 2119; QUS.
Note aus: Literatur.

### K6 Eignung fuer die drei Anforderungsarten
Leitfrage: Laesst sich mit dem Ansatz eine Anforderung jeder der drei
Arten gleich gut formulieren?
Pruefbar an: Je ein Formulierungsversuch zu 29148 Abschn. 9.6.12
(Funktion), 9.6.14 (Leistung) und 9.6.18 c (Sicherheit).
Anwendbarkeit: nur fuer die Ebenen (a) und (b). Beide geben
Satzbestandteile und deren Reihenfolge vor; nur dort ist ein
Formulierungsversuch ueberhaupt ein Versuch dieser Ebene. Ebene (c)
legt allein die Bedeutung von Schluesselwoertern fest, Ebene (d)
beurteilt eine bereits formulierte Anforderung. Fuer beide ist K6
nicht anwendbar (n. a.), festgelegt am 31.08.2026, siehe
Abschnitt 9.
Herkunft: 29148 Abschn. 9.6.12 bis 9.6.18.
Note aus: Formulierungsprobe, Ebenen (a) und (b). Schwellen in
Abschnitt 6.

### K7 Verstaendlichkeit fuer das Qrisp-Team
Leitfrage: Wie viel Vorwissen braucht eine entwickelnde Person, um
einen Satz richtig zu lesen?
Pruefbar an: Zahl der zu lernenden Schluesselwoerter und Regeln;
Abstand zur ueblichen Ausdrucksweise in den Pull Requests.
Vorbehalt: Dieses Kriterium wird hier nur ersatzweise bewertet.
Belastbar wird es erst durch die Bewertung in Paket H. Gehoert in
Kapitel 7.
Herkunft: Mavin 2009 Abschn. 2; teils eigene Setzung.
Note aus: Literatur, unter Vorbehalt.

### K8 Automatische Validierbarkeit
Leitfrage: Kann ein Programm feststellen, ob ein Satz dem Ansatz
entspricht?
Pruefbar an: Existiert ein geschlossenes Vokabular oder ein festes
Muster, das ein Programm suchen kann?
Abgrenzung zu K4: K4 fragt, ob sich der Satz einlesen laesst. K8
fragt, ob er sich pruefen laesst.
Herkunft: QUS und AQUSA; RFC 8174; 29148 Abschn. 5.2.7.
Note aus: Literatur.

### K9 Deckung durch die Quelldaten (ergaenzt)
Leitfrage: Verlangt der Ansatz Bestandteile, die sich aus Titel,
Beschreibung, Diskussion und Diff eines Pull Requests belegen
lassen?
Pruefbar an: Anteil der Stichprobe, bei dem jeder Pflichtbestandteil
ohne Erfindung besetzt werden kann.
Begruendung der Aufnahme: Ein Pflichtbestandteil ohne Beleg zwingt
das Modell zum Erfinden. Das widerspricht der
Belegstaerke-Systematik. Ohne K9 bliebe dieser Punkt eine Vermutung.
Gestuetzt durch die Erhebung: 46,6 Prozent der Pull Requests haben
keinen Kommentar; 11,8 Prozent haben keinen Beschreibungstext.
Herkunft: eigene Setzung, gestuetzt auf die Erhebung aus Paket D.
Note aus: Formulierungsprobe. Schwellen in Abschnitt 6.

### K10 Kombinierbarkeit mit anderen Ebenen (ergaenzt)
Leitfrage: Laesst sich der Ansatz mit den anderen Ebenen
widerspruchsfrei verbinden?
Pruefbar an: Gibt es eine Regel des Ansatzes, die einer Regel einer
anderen Ebene widerspricht?
Begruendung der Aufnahme: Da die vier Ebenen unterschiedliche
Aspekte einer Anforderung regeln, ist eine Verbindung mehrerer
Ebenen moeglich und daher ausdruecklich zu pruefen. Ohne K10 gaebe
es fuer diese Pruefung keinen Massstab.
Bekannter Konflikt: EARS verwendet ausschliesslich shall und kennt
keine Abstufung; RFC 2119 kennt fuenf Stufen. 29148 raet von must
ab, RFC 2119 setzt MUST und SHALL gleich.
Herkunft: RFC 2119; 29148 Abschn. 5.2.4 NOTE 2; EARS.
Note aus: Literatur.

## 3. Bewertungsskala

Die Skala ist ordinal. Sie kennt eine Rangfolge, aber keine gleichen
Abstaende. Ihre Werte werden deshalb nicht addiert.

| Wert | Bedeutung | Vergabebedingung |
|---|---|---|
| 2 | erfuellt | Der Ansatz enthaelt eine ausdrueckliche Regel oder einen Mechanismus fuer dieses Kriterium, belegbar mit Quelle und Abschnitt |
| 1 | teilweise erfuellt | Ein Mechanismus ist vorhanden, aber unvollstaendig, an Bedingungen geknuepft oder nur fuer einen Teil der Faelle wirksam |
| 0 | nicht erfuellt | Der Ansatz enthaelt keine solche Regel; das Kriterium muesste von aussen ergaenzt werden |
| n. a. | nicht anwendbar | Das Kriterium betrifft eine Eigenschaft, die diese Ebene ihrem Zweck nach nicht regelt |
| ? | nicht entscheidbar | Es liegt kein Beleg vor; die Zelle bleibt offen und wird in Kapitel 7 benannt |

Begruendung der Stufenzahl: Die Belege sind Textstellen aus Normen
und Aufsaetzen. Aus ihnen laesst sich ablesen, ob eine Regel
vorhanden, unvollstaendig oder abwesend ist. Feinere Stufen
taeuschten eine Genauigkeit vor, die die Quellen nicht hergeben.
Dies ist eine methodische Setzung des Verfassers.

## 4. Bewertungsregeln

R1 Belegpflicht. Jede Note braucht einen Beleg: eine Quelle mit
Abschnittsangabe oder eine Zahl aus der Formulierungsprobe. Ohne
Beleg wird ? eingetragen.

R2 Reihenfolge. Erst wird der Beleg gesucht, dann die Note vergeben.
Nie umgekehrt.

R3 n. a. ist keine schlechte Note. Der Wert wird nie wie 0 behandelt
und nie verrechnet.

R4 Vorrang der Messung. Widerspricht die Formulierungsprobe der
Literatur, gilt die Messung. Der Widerspruch wird in Kapitel 7
dokumentiert und nicht stillschweigend aufgeloest.

R5 Keine Summe, keine Gewichte. Es wird weder addiert noch
gewichtet. Begruendung: K2, K4 und K8 haengen voneinander ab. Eine
strenge Satzstruktur wuerde dreimal belohnt. Die Abhaengigkeit wird
in der Arbeit offengelegt.

R6 Begruendungspflicht. Zu jeder Note gehoeren hoechstens zwei
Saetze Begruendung, vollstaendig in dieser Datei, in der Arbeit
gekuerzt.

R7 Reihenfolge der Arbeitsschritte. Erst werden alle vier Ebenen
einzeln bewertet, danach wird die Kombination geprueft. Die
Kombination wird nicht rueckwaerts aus einem gewuenschten Ergebnis
hergeleitet.

R8 Empfindlichkeitspruefung. Bei K6 und K9 wird immer der gemessene
Wert berichtet, nicht nur die Note. Zusaetzlich wird geprueft, ob
eine andere Schwelle die Entscheidung aendern wuerde. Falls ja,
steht das in Kapitel 7.

R9 Pauschale Rollenangabe. Nennt die Quelle eine Personengruppe nur
pauschal, ohne sie von anderen Gruppen abzugrenzen (etwa "users"
oder "Nutzer"), gilt der Bestandteil Rolle als belegt.
Begruendung: K9 misst, ob die Quelle einen Bestandteil liefert, nicht
ob sie ihn trennscharf liefert. Die Trennschaerfe wird bei K1
bewertet. Eine nachtraegliche Verschaerfung dieser Regel wuerde
gegen R2 verstossen, weil das Messergebnis bereits vorliegt.
Zusatz: Jeder solche Fall wird im Protokoll als generische Rolle
gekennzeichnet. Die Deckungsquote der Ebene (a) wird in Kapitel 7
zusaetzlich ohne diese Faelle berichtet, damit der Einwand gegen die
Aussagekraft pauschaler Rollen sichtbar bleibt.

R10 Bezugspunkt der Modalitaet. Eine Verbindlichkeitsstufe gilt fuer
Ebene (c) nur dann als belegt, wenn sich die Modalaussage der Quelle
auf die rekonstruierte Anforderung selbst bezieht.
Nicht als Beleg gewertet werden:
- Aussagen ueber das Vorgehen im Pull Request, etwa was vor dem
  Zusammenfuehren zu tun ist oder in welchem Pull Request etwas
  umzusetzen sei;
- Aussagen ueber eine andere, im Protokoll nicht rekonstruierte
  Anforderung;
- der Umstand, dass ein Pull Request zusammengefuehrt wurde.
Begruendung: Andernfalls belegte eine Aussage ueber den Arbeitsablauf
eine Eigenschaft der Anforderung. Die Messung fuer K9 wuerde dann
etwas anderes zaehlen als das, was sie zu zaehlen vorgibt.
Diese Regel wurde bei PR 371 bereits angewandt und wird hier
nachgetragen, damit sie auf alle zwoelf Faelle gleich wirkt.

R11 Auslegung der Skalenstufe 2. Stufe 2 bemisst sich nach dem
Vorhandensein und der Reichweite einer ausdruecklichen Regel des
Ansatzes, nicht nach einem empirischen Wirksamkeitsnachweis. Note 1
wird vergeben, wenn die Regel selbst nach Reichweite oder Bedingungen
unvollstaendig ist. Berichtete Restprobleme einer Erprobung fuehren
fuer sich genommen nicht zu Note 1; sie werden in der Begruendung der
Zelle vermerkt und in Kapitel 7 aufgegriffen.
Begruendung: Die Vergabebedingung in Abschnitt 3 nennt eine
ausdrueckliche Regel oder einen Mechanismus, nicht deren Wirkung. Zwei
der vier Ebenen stuetzen sich auf Normen, zu denen keine
Wirksamkeitsstudie vorliegt. Verlangte Stufe 2 einen solchen Nachweis,
koennten diese Ebenen sie nie erreichen, und eine Quelle, die ihre
Restprobleme offen berichtet, stuende schlechter da als eine, die
dazu schweigt.
Verhaeltnis zur Stufe 1: Die Wendung "nur fuer einen Teil der Faelle
wirksam" in Abschnitt 3 bezieht sich auf die Reichweite der Regel,
nicht auf ein Messergebnis Dritter.
Verhaeltnis zu R4: R4 betrifft die Formulierungsprobe dieser Arbeit.
Befunde fremder Autoren bleiben davon unberuehrt.
Nachtraeglichkeit: R11 wurde nach der Vergabe von K1 formuliert. Alle
vier K1-Noten wurden daraufhin geprueft; keine aendert sich.

## 5. Entscheidungsverfahren

Statt einer Gesamtnote wird jeder Ebene eine Rolle zugewiesen.

- verpflichtend: Jede rekonstruierte Anforderung folgt diesem Muster.
- optional: Das Muster wird nur verwendet, wenn die Quelle es
  hergibt.
- nicht verwendet: Das Muster kommt nicht vor.

Erhalten mehrere Ebenen eine andere Rolle als "nicht verwendet",
entsteht eine Kombination. Nach Entscheidung C3 gilt sie als ein
festgelegtes Zielformat und wird vollstaendig spezifiziert.

E1 Ausschluss. Eine Ebene darf die Rolle "verpflichtend" nicht
erhalten, wenn K9 mit 0 bewertet ist. Die Rolle "optional" bleibt
moeglich.
Begruendung: Ein Pflichtbestandteil, den die Quelle nicht belegt,
erzwingt eine Erfindung des Modells oder eine Leerstelle. Beides
widerspricht der Belegstaerke-Systematik. Die Pipeline erzeugte dann
unbelegte Angaben durch Konstruktion, nicht durch Modellfehler.

E2 Vorrang bei aehnlichem Profil. Es entscheidet zuerst K9, dann K3,
dann K8.
Begruendung: FF1 fragt nach brauchbaren Anforderungen aus der
Historie. Belegbarkeit geht vor Nachweisbarkeit; beide gehen vor
Werkzeugkomfort.

E3 Dokumentationspflicht. Jede Rollenzuweisung wird mit hoechstens
drei Saetzen begruendet, unter Angabe der ausschlaggebenden
Kriterien.

## 6. Schwellenwerte fuer die gemessenen Kriterien

Diese Werte stehen vor dem Ziehen der Stichprobe fest (C2).

K9, Deckung durch die Quelldaten. Gemessen wird der Anteil der
Stichprobe, bei dem sich alle Pflichtbestandteile ohne Erfindung
besetzen lassen.

| Anteil | Note |
|---|---|
| 80 Prozent und mehr | 2 |
| 40 bis unter 80 Prozent | 1 |
| unter 40 Prozent | 0 |

K6, Eignung fuer die drei Anforderungsarten. Je bewerteter Ebene
werden drei Formulierungsversuche unternommen, einer je Art nach
29148 Abschn. 9.6.12, 9.6.14 und 9.6.18 c. Bewertet werden nur die
Ebenen (a) und (b); fuer (c) und (d) ist K6 nicht anwendbar, siehe
K6 in Abschnitt 2.

| Ergebnis | Note |
|---|---|
| alle drei gelingen | 2 |
| einer oder zwei gelingen | 1 |
| keiner gelingt | 0 |

Ein Versuch gilt als gelungen, wenn der Satz alle
Pflichtbestandteile des Ansatzes besetzt und keine Angabe enthaelt,
die die Quelle nicht hergibt.

Rahmen und Referenzinhalte fuer K6, festgelegt am 02.09.2026:

Rahmen, gilt fuer alle drei Inhalte gleich: Das betrachtete System
ist eine Software-Bibliothek (englisch: the library). Sie wird von
entwickelnden Personen beim Programmieren verwendet (englisch:
developers). Der Rahmen nennt keine Verbindlichkeitsstufe und
keinen Nutzniesser der einzelnen Anforderung.

| Art | Norm | Referenzinhalt |
|---|---|---|
| funktional | 9.6.12 a | The inputs are checked for validity before they are processed. |
| leistungsbezogen | 9.6.14 | 95 % of the transactions are processed in less than 1 s. |
| sicherheitsbezogen | 9.6.18 c 5 | The integrity of data in critical variables is checked. |

Die Inhalte geben nur den fachlichen Kern der jeweiligen Art
wieder. Sie stehen in der Aussageform, damit kein Schluesselwort
mitgeliefert wird. Die Norm formuliert das Leistungsbeispiel mit
shall; das Modalverb wurde entfernt.

Offenlegung: Die Grenzen 80 und 40 Prozent sind eine Setzung des
Verfassers und folgen aus keiner Quelle. Sie trennen "nahezu
durchgaengig" von "mehrheitlich" und dieses von "ueberwiegend
nicht". R8 verlangt deshalb die Empfindlichkeitspruefung.

Umrechnung auf die Stichprobengroesse. Die Stichprobe umfasst zwoelf
Pull Requests, gezogen am 25.08.2026 (siehe
docs/sample_formulation_probe.md). Ein Fall entspricht 8,33
Prozentpunkten. Wirksam sind damit die folgenden Trefferzahlen:

| Gedeckte Faelle von zwoelf | Anteil | Note |
|---|---|---|
| 10 bis 12 | 83,3 Prozent und mehr | 2 |
| 5 bis 9 | 41,7 bis 75,0 Prozent | 1 |
| 0 bis 4 | 0 bis 33,3 Prozent | 0 |

Die gesetzten Grenzen von 80 und 40 Prozent sind bei zwoelf Faellen
nicht erreichbar. Tatsaechlich wirksam sind 83,3 und 41,7 Prozent.
Dieser Versatz wird in Kapitel 7 benannt.

Fuer K6 ist keine Umrechnung noetig. Die Skala ist dort bereits in
Faellen formuliert: drei Versuche je bewerteter Ebene.

## 7. Abhaengigkeiten und Einschraenkungen (fuer Kapitel 7)

- Abhaengigkeitskette K2 nach K4 nach K8. Eine feste Satzstruktur ist
  die Ursache, gute Verarbeitbarkeit und gute Pruefbarkeit sind
  ihre Folgen. Deshalb R5.
- K1 und K3 liegen inhaltlich nah beieinander. Die Norm fuehrt
  Eindeutigkeit und Nachweisbarkeit getrennt; beide bleiben
  erhalten, die Naehe wird ausgewiesen.
- K7 wird ersatzweise bewertet. Belastbar erst nach Paket H.
- Die Formulierungsprobe ist eine Selbstbewertung des Verfassers.
- Die Schwellen in Abschnitt 6 sind gesetzt, nicht abgeleitet.
- Die Bewertung stuetzt sich auf sieben gelesene Quellen. Die
  systematische Suche der Straenge S1, S2 und S4 steht noch aus und
  betrifft nicht Ebene (a) bis (d).
- K6 ist nur fuer die Ebenen (a) und (b) anwendbar. Ebene (d) hat
  damit weder bei K6 noch bei K9 eine gemessene Note; alle ihre
  Noten stammen aus der Literatur. Ebene (c) hat als einzige
  gemessene Note die 0 aus K9. Der Einwand, die gemessenen
  Kriterien griffen nur dort, wo ein Satzmuster vorliegt, ist
  berechtigt und wird in Kapitel 7 benannt.
- Die typabhaengige Wirkung der Qualitaetsregeln von Ebene (d) wird
  dadurch nicht bei K6 erfasst. Sie wird bei K3 beruecksichtigt,
  weil dort die Nachweisbarkeit bewertet wird.
- Der Rahmen fuer K6 nennt ein System und eine Personengruppe, aber
  keinen Nutzniesser der einzelnen Anforderung. Beide bewerteten
  Ebenen beziehen daraus je einen Pflichtbestandteil: Ebene (a) die
  Rolle, Ebene (b) den Systemnamen. Die urspruengliche Annahme, nur
  Ebene (b) profitiere vom Rahmen, ist durch die Messung vom
  02.09.2026 widerlegt; nach R4 gilt die Messung. Der Einwand, K6
  messe damit vor allem den Rahmen und nicht die Formate, ist in
  Kapitel 7 zu benennen.
- K6 und K9 treffen dieselbe Schwachstelle, die Rolle. Sie messen
  sie an verschiedenen Quellen: K9 an zwoelf Pull Requests, K6 an
  drei Inhalten aus der Norm. Die Noten sind daher nicht
  unabhaengig voneinander.
- Ebene (b) stuetzt sich auf zwei Quellen: EARS und den Aufbausatz
  aus 29148 Abschn. 5.2.4 einschliesslich Figure 1. Bewertet wird
  EARS als die spezifischere Festlegung. Die Aufteilung von
  Abschn. 5.2.4 auf drei Ebenen ist eine Zuordnung des Verfassers und
  steht so nicht in der Norm.
- K4 ist eine eigene Setzung, gestuetzt auf die Slotstruktur von
  EARS. Ein aus einem Bewerber abgeleitetes Kriterium beguenstigt
  diesen Bewerber. Die Note fuer Ebene (b) ist daher nur begrenzt
  aussagekraeftig und wird in Kapitel 7 als Bedrohung der
  Konstruktvaliditaet ausgewiesen.

## 8. Offene Punkte

Erledigt seit dem 23.08.2026:
- Stichprobe gezogen (Schritt 3, 25.08.2026)
- Formulierungsprobe Teil A ausgefuellt (26.08.2026)
- Gegenpruefung aller zwoelf Faelle abgeschlossen (27. und
  30.08.2026); R9 und R10 auf alle Faelle angewandt
- Auswertung Teil A abgeschlossen: Ebene (a) 4 von 12 (Note 0),
  Ebene (b) 9 von 12 (Note 1), Ebene (c) 0 von 12 (Note 0),
  Ebene (d) nicht anwendbar
- K6 fuer die Ebenen (c) und (d) als nicht anwendbar festgelegt
  (31.08.2026, siehe Abschnitt 9). K6 wird nur noch fuer die
  Ebenen (a) und (b) gemessen.
- Schritt 4b abgeschlossen: Teil B mit neuen Referenzinhalten neu
  aufgesetzt und gegengeprueft. Ergebnis Ebene (a) 3 von 3 (Note 2),
  Ebene (b) 3 von 3 (Note 2), Ebenen (c) und (d) nicht anwendbar.

Noch offen:
- Schritt 4c: K1 bis K4, K6 und K9 stehen in Abschnitt 10. Offen sind
  die Noten fuer K5, K7, K8 und K10.
- Rollenzuweisung und Formatentscheidung (Schritt 5)
- Konflikt shall gegen must: wird bei der Rollenzuweisung der
  Ebene (c) entschieden

## 9. Aenderungshistorie

| Datum | Aenderung | Begruendung |
|---|---|---|
| 23.08.2026 | Datei angelegt: Katalog K1 bis K10, Skala, Regeln R1 bis R8, Verfahren E1 bis E3, Schwellen | Grundlage fuer die Entscheidungsmatrix, festgelegt vor jeder Bewertung |
| 25.08.2026 | Stichprobengroesse auf zwoelf festgelegt, Stichprobe geschichtet gezogen | Voraussetzung fuer die Umrechnung der Schwellen aus Abschnitt 6 in Trefferzahlen |
| 26.08.2026 | Pflichtbestandteile je Ebene festgelegt: (a) Rolle und Means, (b) Systemname und Systemreaktion, (c) Verbindlichkeitsstufe, (d) keine | Ohne festgelegte Pflichtbestandteile ist der Begriff "gedeckt" fuer K9 nicht pruefbar |
| 26.08.2026 | K9 fuer Ebene (d) als nicht anwendbar festgelegt | Ebene (d) schreibt keine Satzbestandteile vor, sondern Qualitaets- und Sprachregeln. Ein Deckungsanteil ist dort nicht definiert. Nach R3 ist n. a. keine schlechte Note. |
| 26.08.2026 | Erhebungsform fuer Teil A: je Pull Request eine Kreuztabelle und ein Beispielsatz in der am besten gedeckten Ebene, statt zwoelf mal vier ausformulierter Saetze | Gemessen wird die Deckung der Pflichtbestandteile, nicht die Formulierungsguete. Ausformulierte Saetze fuer nicht gedeckte Ebenen haetten keinen zusaetzlichen Messwert geliefert und zum Erfinden fehlender Bestandteile verleitet. |
| 26.08.2026 | Drei Referenzinhalte fuer Teil B konstruiert, vor den Formulierungsversuchen | R2: erst der Massstab, dann die Messung |
| 27.08.2026 | Einzelne Faelle erneut an der Quelle geprueft. Der Verfasser aenderte PR 413, 622 und 692. Eine unabhaengige Gegenpruefung von PR 48, 75, 191 und 371 fuehrte zur Aenderung von PR 371. | R4 Vorrang der Messung; Fehler und uneinheitliche Regelanwendung sollen sichtbar werden |
| 30.08.2026 | R9 (pauschale Rollenangabe) und R10 (Bezugspunkt der Modalitaet) ergaenzt | Beide Fragen waren bei der Messung faktisch entschieden, aber nicht schriftlich festgelegt. Ohne Festlegung waere die Gegenpruefung der acht offenen Faelle an einem anderen Massstab erfolgt als Teil A. |
| 30.08.2026 | Abschnitt 6 um die Umrechnung der Schwellen auf zwoelf Faelle ergaenzt; Abschnitt 8 auf den tatsaechlichen Stand gebracht | Die Prozentgrenzen 80 und 40 fallen auf keinen ganzen Fall. Ohne Umrechnung waere die Notenvergabe nicht eindeutig. |
| 31.08.2026 | K6 fuer die Ebenen (c) und (d) als nicht anwendbar festgelegt. Die Anwendbarkeit steht jetzt bei K6 in Abschnitt 2; in Abschnitt 6 heisst es entsprechend "je bewerteter Ebene". Abschnitt 7 um zwei Einschraenkungen ergaenzt; Abschnitt 8 fortgeschrieben, die Uebertragung in die Bewertung heisst jetzt Schritt 4c | K6 ist ueber einen Formulierungsversuch definiert. Nur die Ebenen (a) und (b) geben Satzbestandteile und deren Reihenfolge vor. Ebene (c) legt allein die Bedeutung von Schluesselwoertern fest, Ebene (d) beurteilt eine bereits formulierte Anforderung. In Teil B uebernahmen die Versuche fuer (c) und (d) deshalb den Satzbau der Ebene (b); ihre 3 von 3 waren keine Leistung dieser Ebenen. Nach R3 ist n. a. keine schlechte Note. Die Festlegung erfolgt vor der Wiederholung der Messung (R2). |
| 02.09.2026 | Rahmen und drei Referenzinhalte fuer K6 in Abschnitt 6 festgelegt; die bisherigen Inhalte aus Teil B werden verworfen. Abschnitt 7 um zwei Einschraenkungen ergaenzt | Die bisherigen Referenzinhalte enthielten Rolle, Systemnamen und Verbindlichkeitsstufe bereits. Ein Versuch konnte deshalb nicht misslingen; die Pruefung mass nichts. Die neuen Inhalte geben nur den fachlichen Kern der Norm wieder und lassen offen, wem der Nutzen zufaellt. Der Rahmen nennt ein System, weil jede Anforderung einen Gegenstand braucht, aber keine Rolle, weil nur Ebene (a) eine solche verlangt. Vorschlag des Modells, vom Verfasser gegen den Normtext geprueft und uebernommen. |
| 02.09.2026 | Teil B der Formulierungsprobe mit den neuen Referenzinhalten durchgefuehrt und gegengeprueft; Noten fuer K6 vergeben (Ebene (a) 2, Ebene (b) 2, Ebenen (c) und (d) n. a.). Der widerlegte Satz in Abschnitt 7 berichtigt, Abschnitt 8 fortgeschrieben | Beide bewerteten Ebenen erreichen 3 von 3. Die Annahme, nur Ebene (b) beziehe einen Pflichtbestandteil aus dem Rahmen, hat sich nicht bestaetigt: Ebene (a) bezieht die Rolle ebenso aus dem Rahmen. Nach R4 gilt die Messung; der Widerspruch wird dokumentiert statt aufgeloest. Empfindlichkeit nach R8: Ohne Anerkennung der Rahmenrolle faellt Ebene (a) auf 0 von 3. |
| 04.09.2026 | Abschnitt 10 (Entscheidungsmatrix) angelegt; Note fuer K1 je Ebene vergeben. Abschnitt 8 fortgeschrieben | Schritt 4c begonnen. Die Noten stammen aus den Volltexten der sieben gelesenen Quellen. Vorschlag des Modells nach C2a, vom Verfasser an den Quellen geprueft und uebernommen. |
| 07.09.2026 | R11 ergaenzt: Auslegung der Skalenstufe 2 | Abschnitt 3 knuepft Stufe 2 an eine ausdrueckliche Regel, nicht an deren Wirkung. Ohne die Klarstellung waeren Normen ohne Wirksamkeitsstudie strukturell benachteiligt, und eine Quelle, die ihre Restprobleme offen berichtet, stuende schlechter da als eine, die schweigt. Nach der Vergabe von K1 formuliert; alle vier K1-Noten wurden geprueft, keine aendert sich. |
| 07.09.2026 | Zuordnung von 29148 Abschn. 5.2.4 auf drei Ebenen in Abschnitt 1 festgelegt; Ebene (c) wird nur an den Schluesselwoertern gemessen. Abschnitt 7 um eine Einschraenkung ergaenzt | Der Abschnitt enthaelt Aufbausatz, Schluesselwoerter und sprachliche Vorgaben nebeneinander. Eine Erweiterung der Ebene (c) um den Aufbausatz haette die bereits festgelegten Pflichtbestandteile veraendert und die vorliegende K9-Messung entwertet (R2). Figure 1 wurde dabei erstmals eingesehen; sie zeigt ein Satzmuster mit benannten Bestandteilen und stuetzt die Zuordnung zu Ebene (b). |
| 07.09.2026 | Noten fuer K2 je Ebene vergeben; die Vorfrage n. a. gegen 0 fuer die Ebenen (c) und (d) zugunsten von n. a. entschieden. Die gemessenen Noten fuer K6 und K9 aus Abschnitt 6 und dem Protokoll in die Tabelle uebertragen | Erste Anwendung von R11: Die Erprobungsbefunde zu AQUSA und zur Musterabgrenzung bei EARS stehen in der Begruendung, nicht in der Note. Die Vorfrage folgt der Vergabebedingung der Skala und derselben Erwaegung wie bei K6 am 31.08.2026; das Gegenargument ist in Abschnitt 10 festgehalten. Vorschlag des Modells nach C2a. |
| 07.09.2026 | Noten fuer K3 je Ebene vergeben. Abschnitt 8 fortgeschrieben | Ebene (d) erhaelt als einzige die 2, weil 29148 Abschn. 5.2.5 die Nachweisbarkeit als eigenes Merkmal fuehrt und Abschn. 5.2.7 sie operationalisiert. Damit liegt Ebene (d) erstmals ueber Ebene (b). Zweite Anwendung von R11: die in Big EARS berichtete Restuntestbarkeit traegt die Note nicht. Vorschlag des Modells nach C2a, vom Verfasser an den Quellen geprueft und uebernommen. |
| 07.09.2026 | Noten fuer K4 je Ebene vergeben; Abschnitt 7 um den Vorbehalt zu K4 ergaenzt. Abschnitt 8 fortgeschrieben | K4 ist eine eigene Setzung, gestuetzt auf die Slotstruktur von EARS. Der Vorbehalt wurde nach R2 vor der Notenvergabe festgehalten. Erstmals ist keine Zelle nicht anwendbar. Ebene (a) erreicht dieselbe Note wie Ebene (b), weil Lucassen ein formales Begriffsmodell mitliefert. Vorschlag des Modells nach C2a, vom Verfasser an den Quellen geprueft und uebernommen. |


## 10. Entscheidungsmatrix (in Arbeit)

Diese Tabelle wird in Schritt 4c Kriterium fuer Kriterium gefuellt.
Die Noten fuer K6 und K9 stammen aus einer Messung (Abschnitt 6 und
docs/formatprobe_protokoll.md), alle uebrigen aus der Literatur.

| Kriterium | (a) User Story | (b) EARS | (c) Modalitaet | (d) Qualitaetsregeln | vergeben am |
|---|---|---|---|---|---|
| K1 Eindeutigkeit | 1 | 2 | 1 | 2 | 04.09.2026 |
| K2 Formale Struktur | 1 | 2 | n. a. | n. a. | 07.09.2026 |
| K3 Verifizierbarkeit | 1 | 1 | n. a. | 2 | 07.09.2026 |
| K4 Maschinelle Verarbeitbarkeit | 2 | 2 | 1 | 1 | 07.09.2026 |
| K5 Eignung fuer LLM-Ausgaben | offen | offen | offen | offen | - |
| K6 Eignung fuer die drei Anforderungsarten | 2 | 2 | n. a. | n. a. | 02.09.2026 |
| K7 Verstaendlichkeit fuer das Qrisp-Team | offen | offen | offen | offen | - |
| K8 Automatische Validierbarkeit | offen | offen | offen | offen | - |
| K9 Deckung durch die Quelldaten | 0 | 1 | 0 | n. a. | 30.08.2026 |
| K10 Kombinierbarkeit mit anderen Ebenen | offen | offen | offen | offen | - |

### Begruendungen und Belege je Zelle

#### K1 Eindeutigkeit, vergeben am 04.09.2026

Ebene (a) User Story, Note 1.
Beleg: Lucassen et al. 2016, Abschn. 2 (Begriffsmodell; ueber 80
syntaktische Varianten), Abschn. 2.3 (drei Bestandteile des Means, im
Uebrigen freier Text), Abschn. 3.1.6 (Unambiguous als eigenes
Kriterium).
Begruendung: Die Schablone trennt Rolle, Means und End und legt fuer
das Means drei grammatische Bestandteile fest; damit ist mindestens
ein Teil des Satzes einer festen Lesart zugeordnet. Der uebrige Text
bleibt frei formulierbar, und die Quelle behandelt Eindeutigkeit als
davon getrenntes Kriterium.
Gegenargument, fuehrt zu 0: Die Schablone ordnet den Satz, nennt aber
keine Formulierung, die sie ausschliesst.

Ebene (b) EARS, Note 2.
Beleg: Mavin et al. 2009, Abschn. 2 mit Fussnote 1 (Mehrdeutigkeit als
eins von acht Problemen, unterschieden nach lexikalisch, referenziell,
syntaktisch), Abschn. 4.1 (feste Klauselreihenfolge nach zeitlicher
Logik, drei Auslegungsregeln), Abschn. 5 Tabelle 1 (ersetzte
Formulierungen), Abschn. 6 (Mehrdeutigkeit reduziert, nicht beseitigt).
Begruendung: EARS legt Bestandteile und deren Reihenfolge fest und
gibt an, unter welcher Bedingung die Systemreaktion gilt; damit ist die
Lesart des ganzen Satzes geregelt, nicht nur eines Satzglieds. Die
Quelle fuehrt Mehrdeutigkeit als ausdruecklich adressiertes Problem und
zeigt an Beispielen, welche Formulierungen ersetzt werden.
Gegenargument, fuehrt zu 1: Abschn. 6 stellt selbst fest, dass
Mehrdeutigkeit nur reduziert wurde.

Ebene (c) Normative Modalitaet, Note 1.
Beleg: RFC 2119 Abschn. 1 bis 5 (fuenf Verbindlichkeitsstufen),
RFC 8174 Abschn. 2 (besondere Bedeutung nur bei durchgaengiger
Grossschreibung; klein geschrieben gewoehnliche englische Woerter).
Begruendung: Fuer das Modalwort ist die Lesart durch ein geschlossenes
Vokabular und die Grossschreibungsregel eindeutig festgelegt. Fuer den
uebrigen Satz trifft die Konvention keine Aussage, sodass die Zahl der
Lesarten dort unveraendert bleibt.
Gegenargument, fuehrt zu 2: Innerhalb ihrer Reichweite ist die Regel
vollstaendig und ohne Bedingung.
Nicht n. a. nach R3, weil Ebene (c) Lesarten sehr wohl regelt, nur eng.

Ebene (d) Qualitaets- und Sprachregeln, Note 2.
Beleg: ISO/IEC/IEEE 29148:2018 Abschn. 5.2.5 (Unambiguous als eines
der neun Merkmale), Abschn. 5.2.7 (normativ formuliert, acht
Aufzaehlungspunkte mit benannten Wortklassen); Mavin/Wilkinson 2010,
Abschn. "Testing the Hypothesis"; Lucassen et al. 2016, Tab. 1 und
Abschn. 3.1.6.
Begruendung: Abschnitt 5.2.7 ist die einzige der vier Ebenen, die
einzelne Formulierungen namentlich ausschliesst, und zwar in
normativer Form. Der Pruefmassstab von K1 ist damit woertlich erfuellt.
Gegenargument, fuehrt zu 1: Die Regeln nennen Wortklassen, aber kein
Verfahren, das Eindeutigkeit herstellt. Sie erkennen Verstoesse, sie
verhindern sie nicht.

Herkunft der Noten: Vorschlag des Modells nach C2a, vom Verfasser an
den Quellen geprueft und uebernommen.

#### K2 Formale Struktur, vergeben am 07.09.2026

Vorfrage, entschieden am 07.09.2026: Fuer die Ebenen (c) und (d) wird
n. a. vergeben und nicht 0. Massgeblich ist die Vergabebedingung der
Skala: n. a. gilt, wenn das Kriterium eine Eigenschaft betrifft, die
die Ebene ihrem Zweck nach nicht regelt. Beide Ebenen regeln keine
Satzbestandteile. Die Entscheidung folgt derselben Erwaegung, mit der
K6 fuer diese beiden Ebenen als nicht anwendbar festgelegt wurde.
Gegenargument, festgehalten fuer Kapitel 7: 29148 Abschn. 5.2.4 zeigt,
dass eine Schluesselwortkonvention mit einem Aufbausatz verbunden
werden kann; RFC 2119 verzichtet darauf. Zudem hat die Zuordnung vom
07.09.2026 den Aufbausatz aus den Ebenen (c) und (d) herausgenommen.
Das n. a. ist damit auch ein Ergebnis dieser Zuordnung.
Abgrenzung zu K1: Dort wurde fuer Ebene (c) ausdruecklich nicht n. a.
vergeben, weil sie Lesarten regelt, nur eng. Bei K2 regelt sie nichts.

Ebene (a) User Story, Note 1.
Beleg: Lucassen et al. 2016, Abschn. 2 mit Abb. 1 (Begriffsmodell aus
einer Rolle, einem Means, null oder mehr Ends und einem Format),
Abschn. 2.1 (Format: eine vorab vereinbarte Schablone, gewaehlt aus
vielen bestehenden), Abschn. 2.3 (drei Bestandteile des Means),
Abschn. 2 Einleitung (ueber 80 syntaktische Varianten), Abschn. 3.2.2
(Uniform: massgeblich ist die im Datensatz haeufigste Form),
Abschn. 4.7 (das Werkzeug ermittelt die haeufigste Form je Datensatz).
Begruendung: Das Begriffsmodell benennt vier Bestandteile und legt
fuer das Means drei grammatische Elemente fest; ein Satz in der
verbreiteten Schablone ist damit ohne Deutung zerlegbar. Die Schablone
selbst gibt der Ansatz jedoch nicht vor, sondern verweist auf ueber 80
Varianten und bestimmt die massgebliche Form je Datensatz nach
Haeufigkeit.
Gegenargument, fuehrt zu 2: Well-formed, Atomic und Minimal legen
normativ fest, welche Bestandteile ein Satz enthalten muss und was er
nicht enthalten darf; in der verbreiteten Form steht auch die
Reihenfolge fest.
Hinweis nach R11: Die Genauigkeit von AQUSA beim Kriterium Well-formed
von 42,3 Prozent ist ein Erprobungsbefund und traegt die Note nicht.
Die Note stuetzt sich allein darauf, dass der Ansatz die Schablone
offenlaesst.

Ebene (b) EARS, Note 2.
Beleg: Mavin et al. 2009, Abschn. 4.1 (generische Syntax aus
optionalen Vorbedingungen, optionalem Ausloeser, Systemname, shall und
Systemreaktion; die Klauselreihenfolge wird ausdruecklich fuer
bedeutsam erklaert, weil sie der zeitlichen Logik folgt), Abschn. 4.2
bis 4.6 (je eine Satzform mit festem Schluesselwort), Abschn. 4.7
(Kombination komplexer Muster); Mavin/Wilkinson 2010, Abschnitt
"EARS Templates".
Begruendung: EARS benennt vier Bestandteile und erklaert ihre
Reihenfolge ausdruecklich fuer verbindlich. Jedes der fuenf Muster
gibt zusaetzlich eine eigene Satzform mit festem Schluesselwort vor.
Gegenargument, fuehrt zu 1: Vorbedingung und Ausloeser sind optional,
und Mavin/Wilkinson 2010 berichten, dass die Abgrenzung zwischen
Ubiquitous und Event-driven schwierig sein kann.
Hinweis nach R11: Der zweite Teil dieses Einwands ist ein
Erprobungsbefund und traegt die Note nicht. Der erste Teil betrifft
die Reichweite der Regel: Optionale Satzteile heben eine festgelegte
Reihenfolge nicht auf, sie entfallen nur.

Ebene (c) Normative Modalitaet, n. a.
Beleg: RFC 2119 Abschn. 1 bis 5 und RFC 8174 Abschn. 2 treffen keine
Aussage zum Satzbau. Siehe literatur/notizen/bradner_1997_rfc2119.md.
Begruendung: Ebene (c) legt allein die Bedeutung von
Schluesselwoertern fest und regelt ihrem Zweck nach weder
Satzbestandteile noch deren Reihenfolge.
Gegenargument, fuehrt zu 0: siehe Vorfrage.

Ebene (d) Qualitaets-, Sprach- und Attributregeln, n. a.
Beleg: ISO/IEC/IEEE 29148:2018 Abschn. 5.2.7 (sprachliche Kriterien
und acht Klassen zu vermeidender Ausdruecke), Abschn. 5.2.8.1 und
5.2.8.2 (Attribute wie Kennung, Versionsnummer, Eigner, Prioritaet,
Risiko, Begruendung, Schwierigkeitsgrad); Lucassen et al. 2016 Tab. 1;
Mavin/Wilkinson 2010, Abschnitt "Testing the Hypothesis".
Begruendung: Ebene (d) beurteilt eine bereits formulierte Anforderung;
Abschn. 5.2.7 nennt zu vermeidende Wortklassen, Abschn. 5.2.8 nennt
Attribute neben dem Satz. Weder das eine noch das andere sind
Satzbestandteile oder eine Reihenfolge.
Gegenargument, fuehrt zu 0: siehe Vorfrage. Die Attribute aus 5.2.8
sind benannte Felder mit fester Bedeutung, stehen aber neben dem Satz
und nicht in ihm. Fuer K4 sind sie erheblich, fuer K2 nicht.

Einschraenkung zur Belegpruefung: Die Volltexte von RFC 2119 und
RFC 8174 lagen dem vorschlagenden Modell in dieser Runde nicht vor.
Sein Vorschlag zu Ebene (c) stuetzt sich auf die Lesenotiz. Die
uebrigen Belegstellen hat es im Volltext gelesen.

Herkunft der Noten: Vorschlag des Modells nach C2a, vom Verfasser an
den Quellen geprueft und uebernommen.

#### K3 Verifizierbarkeit, vergeben am 07.09.2026

Ebene (a) User Story, Note 1.
Beleg: Lucassen et al. 2016, Abschn. 1 (drei Bestandteile einer User
Story: Text, Gespraeche, Akzeptanzkriterien; INVEST wird dort als
hochgradig qualitativ bezeichnet), Abschn. 3.1.3 (Minimal: eine Story
enthaelt nichts ausser Rolle, Means und Ends; Hinweise zum Testen
gehoeren in gesonderte Notizen), Tab. 1 (keines der 13 Kriterien
betrifft die Nachweisbarkeit).
Begruendung: Der Ansatz zaehlt Akzeptanzkriterien ausdruecklich zu den
drei Bestandteilen einer User Story. Im Anforderungstext selbst duerfen
sie nach dem Kriterium Minimal jedoch nicht stehen, und keines der 13
Qualitaetskriterien prueft die Nachweisbarkeit.
Gegenargument, fuehrt zu 0: Bewertet wird der Anforderungstext. Fuer
ihn erzwingt der Ansatz keine ueberpruefbare Angabe; die
Akzeptanzkriterien liegen ausserhalb und bleiben ungeprueft.

Ebene (b) EARS, Note 1.
Beleg: Mavin et al. 2009, Abschn. 2 (Untestability als eines von acht
Problemen: Anforderungen, deren Erfuellung sich nach der Umsetzung
nicht als wahr oder falsch nachweisen laesst), Abschn. 4.1 (die Syntax
verlangt eine Systemreaktion); Mavin/Wilkinson 2010, Abschnitt
"Residual Problems".
Begruendung: Die Syntax erzwingt eine Systemreaktion und damit ein
beobachtbares Verhalten, und Untestbarkeit ist eines der acht
Probleme, die EARS ausdruecklich angeht. Eine Regel, die eine messbare
Groesse oder ein Abnahmekriterium verlangt, enthaelt der Ansatz nicht.
Gegenargument, fuehrt zu 2: Die Beseitigung der Untestbarkeit ist ein
erklaertes Ziel des Ansatzes, und die Bestandteile Vorbedingung,
Ausloeser und Systemreaktion benennen genau die Angaben, gegen die
geprueft wird.
Hinweis nach R11: Die in Mavin/Wilkinson 2010 berichtete
Restuntestbarkeit durch unquantifizierbare Woerter ist ein
Erprobungsbefund und traegt die Note nicht. Die Note stuetzt sich
allein darauf, dass eine Quantifizierungsregel fehlt.

Ebene (c) Normative Modalitaet, n. a.
Beleg: RFC 2119 und RFC 8174 treffen keine Aussage zur
Nachweisbarkeit. Siehe literatur/notizen/bradner_1997_rfc2119.md.
Begruendung: Die Konvention legt allein die Verbindlichkeitsstufe fest
und regelt ihrem Zweck nach nicht, woran die Erfuellung ueberprueft
wird. Das folgt der Vorfrage vom 07.09.2026.
Gegenargument, fuehrt zu 0: Die Verbindlichkeitsstufe entscheidet mit
darueber, ob etwas ueberhaupt nachzuweisen ist; die Konvention
beruehrt die Nachweisbarkeit damit mittelbar.

Ebene (d) Qualitaets-, Sprach- und Attributregeln, Note 2.
Beleg: ISO/IEC/IEEE 29148:2018 Abschn. 5.2.5, Merkmal Verifiable (die
Anforderung ist so aufgebaut und formuliert, dass ihre Umsetzung
nachgewiesen werden kann; Messbarkeit verbessert die Nachweisbarkeit);
Abschn. 5.2.7 (acht Klassen unbestimmter Ausdruecke, ausdruecklich mit
der Ueberpruefbarkeit begruendet).
Begruendung: Der Standard fuehrt die Nachweisbarkeit als eigenes
Merkmal jeder einzelnen Anforderung und begruendet die Liste
unzulaessiger Ausdruecke ausdruecklich mit der Ueberpruefbarkeit. Damit
liegt eine ausdrueckliche und weitgehend operationalisierte Regel vor.
Gegenargument, fuehrt zu 1: Messbarkeit wird nur als verbessernd
bezeichnet, nicht verlangt. Die Regeln sagen zudem, was zu vermeiden
ist, nicht, welche Angabe eine Anforderung enthalten muss.

Befund: Erstmals liegt Ebene (d) ueber Ebene (b). Die Ebenen ergaenzen
einander; die Matrix bestaetigt nicht durchgaengig EARS. Fuer die
Rollenzuweisung in Schritt 5 vorgemerkt.

Einschraenkung zur Belegpruefung: Die Volltexte von RFC 2119 und
RFC 8174 lagen dem vorschlagenden Modell auch in dieser Runde nicht
vor. Sein Vorschlag zu Ebene (c) stuetzt sich auf die Lesenotiz.

Herkunft der Noten: Vorschlag des Modells nach C2a, vom Verfasser an
den Quellen geprueft und uebernommen.

#### K4 Maschinelle Verarbeitbarkeit, vergeben am 07.09.2026

Vorbehalt, festgehalten vor der Notenvergabe: K4 ist nach Abschnitt 2
eine eigene Setzung, gestuetzt auf die Slotstruktur von EARS. Ein aus
einem Bewerber abgeleitetes Kriterium beguenstigt diesen Bewerber.
Die Note fuer Ebene (b) ist daher nur begrenzt aussagekraeftig. Der
Vorbehalt steht in Abschnitt 7 und gehoert nach Kapitel 7.

Ebene (a) User Story, Note 2.
Beleg: Lucassen et al. 2016, Abschn. 2 mit Abb. 1 (Begriffsmodell als
Klassendiagramm), Abschn. 2.3 (Means aus Subjekt, Handlungsverb,
direktem Objekt, optional indirektem Objekt und Adjektiv), Abschn. 3.2
Absatz "Notation" (eine User Story wird formal als Viertupel aus
Rolle, Means, Ends und Format definiert, das Means als Fuenftupel),
Abschn. 4.3 (die zerlegte Story wird als Objekt mit Rolle, Means und
Ends gespeichert).
Begruendung: Der Ansatz benennt die Bestandteile nicht nur, sondern
definiert sie formal als Tupel mit festen Feldern. Damit besteht eine
ausdrueckliche Zuordnung von Satzteil zu Feldname bis hinunter zur
grammatischen Ebene des Means.
Gegenargument, fuehrt zu 1: Das Format ist selbst eines der vier
Felder und wird nicht festgelegt. Ohne Kenntnis der verwendeten
Schablone bestimmt der Ansatz allein nicht, wo Rolle, Means und Ends
im Text beginnen.

Ebene (b) EARS, Note 2.
Beleg: Mavin et al. 2009, Abschn. 4.1 (generische Syntax mit benannten
Platzhaltern fuer Vorbedingungen, Ausloeser, Systemname und
Systemreaktion), Abschn. 4.2 bis 4.6 (je eine Satzform mit festem
Schluesselwort); Wilkinson/Mavin 2018, Tab. I (die Bestandteile einer
EARS-Anforderung werden einzeln benannt und getrennt untersucht).
Begruendung: Die generische Syntax besteht aus benannten Platzhaltern,
die im Satz durch feste Schluesselwoerter voneinander abgegrenzt sind.
Wilkinson/Mavin 2018 behandeln diese Bestandteile bereits als einzeln
adressierbare Teile.
Gegenargument, fuehrt zu 1: Die Quellen benennen Satzteile, definieren
aber kein Datenmodell und keine Feldnamen. Die Abbildung auf
Datenfelder ist eine Ergaenzung dieser Arbeit, nicht eine Regel des
Ansatzes.

Ebene (c) Normative Modalitaet, Note 1.
Beleg: RFC 2119 Abschn. 1 bis 5 (geschlossenes Vokabular aus fuenf
Verbindlichkeitsstufen), RFC 8174 Abschn. 2 (die Bedeutung gilt nur
bei durchgaengiger Grossschreibung). Siehe
literatur/notizen/bradner_1997_rfc2119.md.
Begruendung: Das Schluesselwort laesst sich verlustfrei auf ein
einzelnes Feld mit fuenf zulaessigen Werten abbilden, und die
Grossschreibungsregel grenzt es im Text eindeutig ab. Der Ansatz deckt
damit genau ein Feld ab und nicht den Satz.
Gegenargument, fuehrt zu n. a.: Ebene (c) bringt keinen Satz hervor;
die Leitfrage spricht von einem nach dem Ansatz formulierten Satz.
Nicht n. a. nach R3, weil die Ebene sehr wohl etwas Abbildbares
regelt, nur eng. Das entspricht der Erwaegung bei K1.

Ebene (d) Qualitaets-, Sprach- und Attributregeln, Note 1.
Beleg: ISO/IEC/IEEE 29148:2018 Abschn. 5.2.8.1 und 5.2.8.2 (Attribute
wie Kennung, Versionsnummer, Eigner, Prioritaet, Risiko, Begruendung,
Schwierigkeitsgrad).
Begruendung: Der Standard benennt Attribute als Felder mit fester
Bedeutung, die eine Anforderung begleiten. Sie stehen jedoch neben dem
Satz, und eine Zuordnung von Satzteil zu Feldname gibt der Ansatz
nicht vor.
Gegenargument, fuehrt zu 2: Fuer die Ausgabe der Pipeline sind gerade
diese Attribute die Felder neben dem Anforderungstext; ihre Benennung
ist normativ verankert und vollstaendig uebernehmbar.

Befund: Erstmals ist keine Zelle nicht anwendbar. Ebene (a) erreicht
dieselbe Note wie Ebene (b), obwohl sie bei K2 schwaecher lag. Grund
ist das formale Begriffsmodell bei Lucassen, das Mavin nicht bietet.
K4 unterscheidet die Ebenen (a) und (b) damit nicht, ebenso wenig wie
K6. Fuer Kapitel 7 vorgemerkt.

Einschraenkung zur Belegpruefung: Die Volltexte von RFC 2119 und
RFC 8174 lagen dem vorschlagenden Modell weiterhin nicht vor. Sein
Vorschlag zu Ebene (c) stuetzt sich auf die Lesenotiz.

Herkunft der Noten: Vorschlag des Modells nach C2a, vom Verfasser an
den Quellen geprueft und uebernommen.
