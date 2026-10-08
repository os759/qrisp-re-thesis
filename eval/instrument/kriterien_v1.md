# Bewertungskriterien, Fassung v1

Festgelegt am: 08.10.2026, vor der ersten Bewertung.
Grundlage: E2 mit den Nachtraegen vom 15.09., 21.09., 22.09. und
08.10.2026 in docs/entscheidungen.md; Kriterienliste v0
(eval/instrument/kriterien_v0.md, 21.09.2026).

Fassung v1 ergaenzt v0 um Umfang, Skala, Notenregeln, Art der
Erhebung und Auswertung. Name und Definition jedes Kriteriums stehen
in v0 und bleiben unveraendert; kein Kriterium kommt hinzu, keines
entfaellt. Bei einem Widerspruch zwischen v0 und v1 gilt fuer die
Definition v0, fuer alles andere v1.

Die Kennungen B1 bis B11b bezeichnen hier die Bewertungskriterien. Sie
haben nichts mit den Regeln B1 bis B9 der Belegstaerke aus E6 zu tun.

Nach dem Commit dieser Datei wird nichts mehr an ihr geaendert. Faellt
bei der Bewertung eine Luecke auf, wird sie als datierter Nachtrag in
docs/entscheidungen.md festgehalten und als Grenze berichtet; die Noten
werden dann nicht nachtraeglich angepasst.

## 1. Umfang

1. Gegenstand sind alle Anforderungen in den schemagueltigen
   Datensaetzen des Volllaufs 2026-09-25_full_v2 zu den 20 Pull
   Requests aus docs/sample_eval_e2.md (Startwert 20261005). Das ist
   dieselbe Menge wie die Menge Stichprobe aus G5: 85 Anforderungen aus
   18 Pull Requests. Eine weitere Ziehung gibt es nicht.
2. Ebene 1 (B1 bis B10) wird fuer jede dieser 85 Anforderungen
   erhoben, Ebene 2 (B11a, B11b) fuer jeden der 18 Pull Requests.
3. Die maschinellen Kriterien B8, B9 und B10 werden zusaetzlich ueber
   alle 1 467 Anforderungen der Grundmenge erhoben (G1 Punkt 1).
4. Ob eine Anforderung in einem Datensatz steht, den validate_output.py
   wegen eines Zitats oder der Belegstaerke ablehnt, spielt fuer die
   Auswahl keine Rolle.

## 2. Skala

Fuer die Kriterien, die von Hand bewertet werden (B1 bis B7, B11a,
B11b), gilt eine dreistufige ordinale Skala:

| Wert | Bedeutung |
|---|---|
| 2 | erfuellt |
| 1 | teilweise erfuellt |
| 0 | nicht erfuellt |
| ? | nicht beurteilbar |

- ? wird vergeben, wenn das Urteil Wissen ueber Quantencomputing
  verlangt, das der Bogen nicht liefert, oder wenn der Bogen eine
  Angabe nicht lesbar zeigt. Der Grund kommt in die Notiz. ? wird
  getrennt gezaehlt und nie wie 0 behandelt.
- Die Werte werden gezaehlt, nicht gemittelt, nicht addiert und nicht
  gewichtet.
- B11a erhaelt bei einem Pull Request mit genau einer Anforderung den
  Wert - (nicht anwendbar). Das setzt das Programm, nicht der
  Verfasser. - wird getrennt gezaehlt.

Die maschinellen Kriterien B8, B9 und B10 sind Regelpruefungen. Sie
haben zwei Werte: erfuellt oder nicht erfuellt.

## 3. Allgemeine Regeln fuer die Bewertung von Hand

- A1 Grundlage ist nur, was im Bogen steht. Den Link oeffnest du nur,
  um ein Zitat zu verstehen. Du ergaenzt nichts aus eigenem Wissen
  ueber Qrisp.
- A2 Das Wort shall ist eine Konvention dieser Arbeit (C5 Abschnitt 3).
  Es zaehlt bei keinem Kriterium als Mangel und nicht als Beleg.
- A3 Jedes Kriterium wird nur nach seiner eigenen Frage beurteilt. Ein
  Mangel darf bei mehreren Kriterien wirken, wenn er jedes von ihnen
  betrifft.
- A4 Reihenfolge je Anforderung: B1, B2, B3, B4, B5, B6, B7. B7 kommt
  zuletzt, weil es ein Gesamturteil ueber den Satz ist.
- A5 Bekannte Fachbegriffe von Qrisp (Namen von Klassen, Funktionen,
  Modulen, Seiten der Dokumentation) gelten als bestimmt, wenn der Satz
  sie als Namen eines Teils von Qrisp verwendet.
- A6 Im Zweifel zwischen zwei Noten gilt die niedrigere. Im Zweifel, ob
  ueberhaupt beurteilbar, gilt ?.
- A7 Das Urteil wird nach dem Abschluss der Bewertung (Befehl compare)
  nicht mehr geaendert. Das Programm sperrt die Antwortdatei per
  Pruefsumme.

## 4. Was der Bogen zeigt

Der Bogen ist verblindet. Er zeigt je Anforderung:
- Nummer, Kennung, Pull-Request-Nummer mit Link;
- den Anforderungssatz (Feld text);
- jeden Beleg mit Ort (location, locator) und Zitat (excerpt).

Er zeigt nicht: rationale, type, security_relevant, ears_pattern,
evidence_strength, source_form, supports, verification, uncertainties,
missing_information, beneficiary, component und kein Ergebnis eines
Programms (B8, B9, B10, gefundenes Zitat). Grund: Alle Kriterien von
Hand fragen nach dem Satz und, bei B5 und B6, nach seinem Verhaeltnis
zu den Zitaten. Die verborgenen Felder koennten das Urteil lenken.

Reihenfolge: Die Pull Requests stehen in einer mit dem Startwert
20261008 gemischten Reihenfolge, die Anforderungen eines Pull Requests
nach Kennung. Nach den Anforderungen eines Pull Requests folgt sein
Block fuer Ebene 2. Grund: B11a und B11b brauchen alle Saetze eines
Pull Requests nebeneinander.

## 5. Notenregeln, Ebene 1

### B1 Eindeutigkeit

Frage: Laesst der Satz nur eine Lesart zu?
- 2: Der Satz laesst nur eine Lesart zu.
- 1: Eine zweite Lesart ist denkbar, betrifft aber nur einen
  Nebenaspekt, etwa eine Mengenangabe oder einen Bezug innerhalb des
  Satzes, und nicht, was das System tun soll.
- 0: Mindestens zwei plausible Lesarten fuehren zu verschiedenem
  Verhalten des Systems.

### B2 Vollstaendigkeit des Satzes

Frage: Versteht man den Satz ohne weitere Angaben?
- 2: Der Satz ist ohne Pull Request, Zitate und Vorwissen ueber die
  Aenderung verstaendlich.
- 1: Der Satz ist verstaendlich, aber eine Angabe fehlt, die er selbst
  andeutet, etwa eine Bedingung, ein Bezugsobjekt oder eine Grenze.
- 0: Der Satz ist ohne den Pull Request nicht verstaendlich, etwa weil
  er auf "the change", "the new behaviour" oder einen nicht genannten
  Gegenstand verweist.

### B3 Einzelbezogenheit

Frage: Enthaelt der Satz genau eine Faehigkeit, Eigenschaft oder
Einschraenkung? Mehrere Bedingungen fuer dieselbe Faehigkeit sind
erlaubt (29148 Abschn. 5.2.5, NOTE 2).
- 2: genau eine Faehigkeit, Eigenschaft oder Einschraenkung.
- 1: eine Faehigkeit, angewandt auf eine Aufzaehlung gleichartiger
  Gegenstaende, oder ein Nebensatz, der eine zweite Eigenschaft nur
  nennt.
- 0: zwei oder mehr unabhaengig pruefbare Faehigkeiten, Eigenschaften
  oder Einschraenkungen.

### B4 Nachweisbarkeit

Frage: Laesst sich pruefen, ob Qrisp den Satz erfuellt?
- 2: Der Satz nennt ein beobachtbares Ergebnis oder eine beobachtbare
  Eigenschaft, die ein Test mit ja oder nein entscheiden kann, ohne
  dass dafuer etwas festgelegt werden muss.
- 1: Das Ergebnis ist beobachtbar, aber ein Massstab, eine Groesse
  oder ein Wertebereich fehlt. Beispiel aus der Formulierungsprobe:
  "The library shall check inputs for validity before processing
  them." Gegen welchen Massstab geprueft wird, bleibt offen.
- 0: Der Satz nennt kein beobachtbares Ergebnis, etwa bei "shall
  support", "shall handle" oder "shall improve".

### B5 Quellentreue

Frage: Behauptet der Satz etwas, das die gezeigten Zitate nicht
tragen? Massstab sind nur die Zitate im Bogen, nicht der ganze Pull
Request.
- 2: Systemname, Systemreaktion und jede Bedingung des Satzes sind von
  den Zitaten getragen.
- 1: Der Kern, also die Systemreaktion, ist getragen. Eine Einzelheit
  geht ueber die Zitate hinaus oder verallgemeinert sie, etwa ein
  Wert, eine Bedingung oder der Umfang.
- 0: Die Systemreaktion ist von keinem Zitat getragen, oder der Satz
  widerspricht einem Zitat.

### B6 Relevanz

Frage: Beschreibt der Satz eine dauerhafte Faehigkeit oder Eigenschaft
von Qrisp und keinen einmaligen Arbeitsschritt?
- 2: eine Faehigkeit, Eigenschaft oder Einschraenkung, die nach dem
  Pull Request dauerhaft gilt.
- 1: dauerhaft, aber als Veraenderung gegenueber einem frueheren Stand
  formuliert, etwa "shall no longer ..." oder "shall continue to ...".
- 0: ein einmaliger Arbeitsschritt, etwa umbenennen, entfernen,
  neu gestalten oder eine Version anheben. Beispiel aus der
  Formulierungsprobe: "The Tutorials page shall be redesigned."

### B7 Praktische Nutzbarkeit

Frage: Koennte der Satz ohne Umformulierung in eine
Anforderungsdokumentation von Qrisp uebernommen werden?
- 2: uebernehmbar, wie er steht.
- 1: uebernehmbar nach einer kleinen Aenderung, die keine neue Quelle
  braucht, etwa ein Wort ersetzen oder den Systemnamen genauer fassen.
- 0: muesste neu geschrieben werden oder gehoert nicht in eine
  Anforderungsdokumentation.

Der Verfasser bewertet B7 stellvertretend fuer das Qrisp-Team (v0,
Anmerkung 3). Das gehoert nach Kapitel 7.

## 6. Pruefregeln der maschinellen Kriterien

Alle drei pruefen das Programm src/analyze/evaluate_requirements.py.
Es enthaelt keine Regel ausser den hier genannten und ruft fuer B9 die
vorhandenen Funktionen aus validate_output.py, diagnose_excerpts.py
und count_requirements.py auf.

### B8 Formatkonformitaet

Erfuellt, wenn alle Teilpruefungen bestehen. Grundlage: Prompt v2,
Tabelle der Muster, und C5 Abschnitt 6. Die Teilpruefungen werden
einzeln berichtet.

- B8.1 Schema: Der Datensatz besteht die Schemapruefung. In der
  Stichprobe trifft das nach Abschnitt 1 auf alle 85 zu; berichtet
  wird B8.1 daher nur ueber den ganzen Volllauf (das ist M1 Teil b
  nach F3).
- B8.2 Muster: Das erste Wort des Satzes passt zum Wert von
  ears_pattern, ohne Beachtung der Gross- und Kleinschreibung:

  | ears_pattern | erstes Wort |
  |---|---|
  | ubiquitous | keines von While, During, When, If, Where |
  | state_driven | While oder During |
  | event_driven | When |
  | unwanted_behaviour | If, und vor shall steht das Wort then |
  | optional_feature | Where |
  | complex | eines der fuenf Schluesselwoerter, und vor shall stehen mindestens eines von While, During, Where und mindestens eines von When, If |

- B8.3 Reihenfolge: system_name steht, ohne Beachtung der Gross- und
  Kleinschreibung, im Teil des Satzes vor shall.
- B8.4 Modalwort: shall kommt als Wort genau einmal vor, und zwar
  klein geschrieben.
- B8.5 Keine anderen Modalverben: must, should, will und may kommen
  als Wort nicht vor, ohne Beachtung der Gross- und Kleinschreibung
  (29148 Abschn. 5.2.4).

### B9 Quellennachvollziehbarkeit

Erfuellt, wenn beide Bedingungen gelten:
- Jeder Beleg der Anforderung gilt als gefunden. Gefunden heisst wie
  in F3 (M2, Bedingung 1) und G1 Punkt 2: validate_output.py nimmt das
  Zitat an, oder diagnose_excerpts.py ordnet seine Ablehnung einer
  Ursache der Regel 1 zu.
- Die vom Modell angegebene Belegstaerke stimmt mit der nach E6 aus
  allen Belegen berechneten ueberein (derive_evidence_strength).

Zusaetzlich berichtet: Zahl der Anforderungen mit nur teilweise
gefundenen Belegen.

### B10 Sprachliche Kriterien

Erfuellt, wenn der Anforderungssatz (Feld text) keinen Ausdruck der
folgenden Liste enthaelt. Die Liste besteht genau aus den Beispielen
in 29148 Abschn. 5.2.7; sie ist abschliessend.

| Klasse nach 29148 Abschn. 5.2.7 | Ausdruecke |
|---|---|
| K1 Superlative | best, most |
| K2 subjektive Sprache | user friendly, easy to use, cost effective |
| K3 unbestimmte Pronomen | it, this, that |
| K4 mehrdeutige Adverbien, Adjektive und logische Verknuepfungen | almost always, significant, minimal, or, and/or |
| K5 offene, nicht pruefbare Wendungen | provide support, but not limited to, as a minimum |
| K6 vergleichende Wendungen | better than, higher quality |
| K7 Hintertueren | if possible, as appropriate, as applicable |
| K8 Ausdruecke der Vollstaendigkeit | all, always, never, every |
| K9 unvollstaendige Verweise | nicht maschinell pruefbar, nicht Teil von B10 |

Diese Klassennummern K1 bis K9 gelten nur in diesem Abschnitt. Sie
haben nichts mit den Kriterien K1 bis K10 der Formatauswahl zu tun.

Suchregeln:
- ohne Beachtung der Gross- und Kleinschreibung;
- nur ganze Woerter: vor und nach dem Ausdruck steht kein Buchstabe
  und keine Ziffer;
- ein Leerzeichen innerhalb eines Ausdrucks passt auch auf einen
  Bindestrich, etwa user-friendly;
- keine Beugungs- oder Ableitungsformen: its, everything oder everyone
  sind keine Treffer, weil an den Ausdruck ein Buchstabe anschliesst;
- der laengste Ausdruck gewinnt, und ein gefundener Ausdruck wird
  nicht ein zweites Mal gezaehlt: almost always zaehlt nur in K4,
  nicht zusaetzlich always in K8;
- and/or wird vor or gesucht.

Ein Treffer ist ein Hinweis auf ein moegliches Problem, kein
festgestellter Verstoss. Woerter wie that, it und or treten auch ohne
Mehrdeutigkeit auf. Berichtet werden deshalb die Treffer je Klasse und
je Ausdruck, nicht nur die Gesamtquote.

## 7. Notenregeln, Ebene 2

Grundlage sind nur die Anforderungssaetze des Pull Requests, nicht die
Zitate.

### B11a Widerspruchsfreiheit

Frage: Widersprechen sich die Anforderungen eines Pull Requests,
ueberschneiden sie sich, oder bezeichnen sie dieselbe Sache
verschieden (29148 Abschn. 5.2.6, Consistent)?
- 2: kein Widerspruch, keine Ueberschneidung, dieselben Woerter fuer
  dieselbe Sache.
- 1: kein Widerspruch, aber eine teilweise Ueberschneidung oder eine
  uneinheitliche Bezeichnung derselben Sache.
- 0: mindestens ein Widerspruch oder zwei Anforderungen, die dasselbe
  fordern.
- -: genau eine Anforderung im Pull Request (setzt das Programm).

### B11b Verstaendlichkeit

Frage: Geht aus den Anforderungen klar hervor, was erwartet wird und
welchen Teil von Qrisp es betrifft (29148 Abschn. 5.2.6,
Comprehensible)?
- 2: Beides geht klar hervor.
- 1: Eines von beiden geht nicht klar hervor.
- 0: Beides geht nicht klar hervor.

## 8. Nebenteil: Vergleich der Fundstellen mit der Formulierungsprobe

Grundlage: E2, Nebenteil. Verglichen werden nicht Saetze, sondern
Fundstellen. Gegenstand sind die Bestandteile Systemname und
Systemreaktion, die der Verfasser in docs/formatprobe_protokoll.md
(Teil A) fuer die zwoelf Pull Requests aus Paket C als belegt
eingestuft hat: 20 Bestandteile in elf Pull Requests. Sie stehen mit
ihrer Ortsart und der Fundstelle in Kurzform in
eval/instrument/fundstellen_paket_c.csv. Diese Datei ist eine
Abschrift aus dem Protokoll und enthaelt keine neue Einstufung.

Ortsarten: Titel = title, Beschreibung = body, Kommentar =
issue_comment oder review_comment (in der Datei: comment), Diff = diff.
Nennt die Formulierungsprobe zwei Orte, stehen sie in der Datei mit +
verbunden, etwa title+body.

N1, maschinell: Ein Bestandteil gilt als wiedergefunden, wenn im
schemagueltigen Datensatz des Volllaufs zu diesem Pull Request
mindestens eine Anforderung einen gefundenen Beleg (wie bei B9) hat,
der diesen Bestandteil in supports traegt und an einer Ortsart steht,
die auch die Formulierungsprobe nennt. Ist der Datensatz nicht
schemagueltig oder enthaelt er keine Anforderung, gilt der Bestandteil
als nicht wiedergefunden; das wird gesondert berichtet.

N2, von Hand: Fuer jeden der 20 Bestandteile zeigt ein zweiter Bogen
die Fundstelle aus der Formulierungsprobe und alle gefundenen Belege
der Pipeline in diesem Pull Request, die den Bestandteil tragen. Frage:
Gibt mindestens einer dieser Belege die Stelle wieder, die die
Formulierungsprobe nennt? Antwort ja, nein oder ?.

N2 wird erst nach der Sperre der Bewertung (A7) bearbeitet, damit der
Vergleich die Bewertung nicht beeinflusst. N2 ist nicht verblindet:
Der Verfasser kennt seine eigenen Fundstellen.

Explorativ berichtet: wie viele Anforderungen die Pipeline zu den drei
Pull Requests bildet, bei denen die Formulierungsprobe Ebene (b) nicht
gedeckt fand (PR 75, 413, 692).

## 9. Auswertung

- Je Kriterium von Hand: Zahl der Werte 2, 1, 0 und ?, dazu der Anteil
  der Note 2 an den beurteilten Faellen (ohne ?). Je Kriterium auch
  die Zahl der Pull Requests mit mindestens einer Note 0.
- Je maschinellem Kriterium: Anteil erfuellt in der Stichprobe (85) und
  in der Grundmenge (1 467), bei B8 je Teilpruefung, bei B10 je Klasse
  und je Ausdruck.
- Brauchbar im Sinne von FF1: Eine Anforderung gilt als brauchbar, wenn
  B1, B2, B3 und B4 jeweils mindestens 1 sind, B5 = 2, B6 = 2, B7
  mindestens 1, B8 erfuellt und B9 erfuellt. Grund: Sie hat dann keinen
  klaren Mangel bei Eindeutigkeit, Vollstaendigkeit, Einzelbezogenheit
  oder Nachweisbarkeit, ist quellentreu, beschreibt eine dauerhafte
  Eigenschaft, ist mit hoechstens kleiner Aenderung uebernehmbar, hat
  die Zielform und ist auf ihre Quelle zurueckfuehrbar. Eine Anforderung
  mit ? in einem der Kriterien B1 bis B7 zaehlt als nicht beurteilbar.
  Diese Regel ist eine Setzung des Verfassers. Berichtet werden
  zusaetzlich alle Einzelwerte, damit eine andere Lesart nachrechenbar
  bleibt.
- Nebenteil: N1 und N2 als Zahl wiedergefundener Bestandteile von 20,
  getrennt nach Systemname und Systemreaktion.
- Explorativ, als solche gekennzeichnet: Treffer von B10 gegen die Note
  bei B1; das Wort and im Teil nach shall gegen die Note bei B3; die
  Formen "shall not" und "shall be able to" (Nachtrag zu C5). Keine
  dieser Zaehlungen ist ein Kriterium.
- Keine Mittelwerte ordinaler Noten, keine Signifikanztests, keine
  Gewichtung. Die Stichprobe ist nach Pull Requests geschichtet;
  Anteile sind Schaetzungen mit dieser Einschraenkung.

## 10. Nicht Gegenstand dieser Liste

- M1 bis M6 fuer FF3 folgen F3 und seinem Nachtrag vom 01.10.2026,
  nicht dieser Liste.
- Die Bewertung durch das Qrisp-Team und den Betreuer folgt nach der
  Abgabe (Nachtrag zu E2 vom 15.09.2026).

## 11. Grenzen, fuer Kapitel 7

- Eine Person bewertet; es gibt kein Uebereinstimmungsmass.
- Der Verfasser kennt die 85 Anforderungen aus der Pruefung nach G5.
- Der Verfasser bewertet eine Pipeline, die er selbst gebaut hat (E2).
- Anforderungen desselben Pull Requests aehneln sich; ein Pull Request
  mit vielen Anforderungen praegt die Anteile stark.
- Die Wortliste von B10 erkennt Woerter, keine Mehrdeutigkeit, und
  deckt die Klasse der unvollstaendigen Verweise nicht ab.
- B8 prueft die Form, nicht ob eine Bedingung inhaltlich ein Ereignis
  oder ein Zustand ist.
- Die Merkmale der Anforderungsmenge (B11a, B11b) werden je Pull
  Request bewertet, nicht ueber alle Pull Requests; doppelte
  Anforderungen zwischen Pull Requests werden nicht gesucht.
- Die Notenregeln und die Regel fuer "brauchbar" sind Setzungen des
  Verfassers.
