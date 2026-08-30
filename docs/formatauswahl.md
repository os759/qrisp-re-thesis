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
Herkunft: 29148 Abschn. 9.6.12 bis 9.6.18.
Note aus: Formulierungsprobe. Schwellen in Abschnitt 6.

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

K6, Eignung fuer die drei Anforderungsarten. Je Ebene werden drei
Formulierungsversuche unternommen, einer je Art nach 29148
Abschn. 9.6.12, 9.6.14 und 9.6.18 c.

| Ergebnis | Note |
|---|---|
| alle drei gelingen | 2 |
| einer oder zwei gelingen | 1 |
| keiner gelingt | 0 |

Ein Versuch gilt als gelungen, wenn der Satz alle
Pflichtbestandteile des Ansatzes besetzt und keine Angabe enthaelt,
die die Quelle nicht hergibt.

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
Faellen formuliert: drei Versuche je Ebene.

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

## 8. Offene Punkte

Erledigt seit dem 23.08.2026:
- Stichprobe gezogen (Schritt 3, 25.08.2026)
- Formulierungsprobe Teil A ausgefuellt (26.08.2026)

Noch offen:
- Gegenpruefung von acht der zwoelf Faelle: 408, 413, 464, 533, 577,
  622, 692, 711
- Anwendung von R9 und R10 auf alle zwoelf Faelle, auch auf die vier
  bereits gegengeprueften
- Teil B der Formulierungsprobe neu aufsetzen. Die Referenzinhalte
  enthalten Rolle, Systemname und Modalitaet bereits; alle vier
  Ebenen erreichen dadurch 3 von 3 und K6 unterscheidet nicht.
- Ist K6 fuer die Ebenen (c) und (d) ueberhaupt anwendbar?
- Uebertragung der Messwerte in die Bewertung der vier Ebenen
  (Schritt 4)
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

