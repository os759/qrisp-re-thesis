# Bearbeitungsstand

Letzte Aktualisierung: 04.10.2026
Abgabetermin: 15.10.2026 (Donnerstag; intern geplant auf Di 13.10.2026)

## Roter Faden

Stand 02.10.2026. Dieser Abschnitt erzaehlt ohne Kuerzel, wie die
Arbeit bis heute gelaufen ist und warum. Einzelheiten stehen weiter
unten und in docs/entscheidungen.md.

Worum es geht: Die Arbeit baut ein Programm, das aus alten
Aenderungsvorschlaegen (Pull Requests) des Projekts Qrisp
Softwareanforderungen herausschreibt. Ein Sprachmodell formuliert die
Anforderungen, das Programm prueft jede davon gegen ihre Quelle.

1. Literatur (Paket B, vor Paket D abgeschlossen): Vier Ansaetze,
   Anforderungen zu schreiben, wurden gelesen und in Kapitel 2
   beschrieben: die Norm ISO/IEC/IEEE 29148, die Schluesselwoerter aus
   RFC 2119, die Satzschablone EARS und User Stories. Das war noetig,
   weil die spaetere Formatwahl sonst nicht mit Quellen belegbar waere.

2. Daten (Paket D, 12.08. bis 21.08.2026): Alle 476 Pull Requests von
   Qrisp wurden bei GitHub abgerufen und zu einem Datensatz je Pull
   Request zusammengefuehrt. Sehr grosse Code-Aenderungen werden in
   drei Stufen gekuerzt (Entscheidung D1), weil einzelne Pull Requests
   ueber zwei Millionen Zeichen haben. Jede Kuerzung ist markiert.

3. Format (Paket C, 23.08. bis 11.09.2026): Eine Tabelle mit zehn
   Kriterien hat die vier Ansaetze verglichen, gestuetzt auf Literatur
   und auf eine Probe von Hand an zwoelf echten Pull Requests.
   Ergebnis ist das Zielformat EARS+29148: englische EARS-Saetze mit
   shall, geprueft nach Sprachregeln der Norm (Entscheidung C5).
   User Stories fielen weg, weil nur 4 der 12 Pull Requests eine Rolle
   nennen, zwei davon nur pauschal. Verbindlichkeitsstufen wie in
   RFC 2119 fielen weg, weil keiner der 12 Faelle eine solche Stufe
   belegt.

4. Vorbereitung der Extraktion (Paket E, ab 15.09.2026): Festgelegt
   wurden das Ausgabeformat (E1), die Evaluation (E2), das Budget von
   hoechstens 150 Euro (E3), die Auswahl der Pull Requests (E4) und
   die Regeln der Belegstaerke (E6). Das Modell bekommt 395 von 476
   Pull Requests. Noch offene Vorgaenge fehlen, weil sich ihr Inhalt
   noch aendern kann. Beitraege von Programmen fehlen, weil sie fast
   nur Versionen fremder Bibliotheken anheben oder nie uebernommen
   wurden (Nachtrag zu E4); fuer FF4 werden die Dependabot-Beitraege
   in Paket G gesondert gesichtet. Die Belegstaerke wird vom Programm berechnet,
   weil sie so reproduzierbar ist und keine freie Modellausgabe.
   Bewertet wird an einer neuen Stichprobe, weil die zwoelf Faelle aus
   Paket C schon die Formatwahl getragen haben. Was sich maschinell
   pruefen laesst, prueft ein Programm; den Rest bewertet der
   Verfasser von Hand, weil eine Bewertung allein durch ein Modell
   keinen unabhaengigen Massstab haette. Die Liste der
   Bewertungskriterien steht seit dem 21.09.2026 fest, vor dem ersten
   bezahlten Lauf. Das Qrisp-Team bewertet erst nach der Abgabe; der
   Betreuer hat zugestimmt. Danach entstand die Anweisung an das
   Modell (Prompt, E7).

5. Modell (19.09.2026): Gewaehlt ist gpt-5.6-terra von OpenAI (E8),
   weil es preislich gleichauf mit dem vergleichbaren Claude-Modell
   liegt und eine Doppelrolle vermeidet: Claude ist Arbeitswerkzeug und
   waere sonst zugleich Messgegenstand. Anmeldenamen in den Texten
   werden vorher durch person_NN ersetzt (E9), weil sie zu keiner
   Anforderung beitragen und nicht an einen fremden Anbieter gehen
   sollen.

6. Pilotlauf (Aufgabe A8, 21. und 22.09.2026): 20 Pull Requests gingen
   an das Modell, bevor alle 395 gesendet werden (E10). So werden
   Programm, Prompt und Kosten an wenigen Faellen geprueft. Alle 20
   Antworten waren gueltig. Das Pruefprogramm lehnte 5 ab, weil ein
   Zitat aus einem Code-Ausschnitt nicht woertlich in der Quelle
   stand. Ob das am Pruefprogramm oder am Modell liegt, ist offen.

7. Ursachen und zweiter Probelauf (24.09.2026): Alle abgelehnten
   Zitate gehen auf das Modell zurueck, keines auf das Pruefprogramm.
   Das Modell hat aus Kopfzeilen eines Diffs zitiert, entfernte Zeilen
   uebersprungen oder einzelne Zeichen veraendert. Die Regel fuer die
   Zuordnung stand vor der Suche fest, weil sie sonst nach dem Ergebnis
   haette gewaehlt werden koennen. Das Pruefprogramm prueft seitdem
   genau so streng wie der Prompt, weil es sonst verbotene Zitate als
   korrekt zaehlen wuerde. Eine zweite Fassung des Prompts formuliert
   die zwei verletzten Zitatregeln deutlicher. Sie wurde an denselben
   20 Pull Requests erprobt und nach einer vorab festgelegten Regel fuer
   den Volllauf uebernommen, weil sie etwas seltener falsch zitiert.
   Der Vorsprung ist klein. Eine dritte Fassung gibt es nicht, weil eine
   weitere Umformulierung wenig verspricht und das Pruefprogramm die
   verbleibenden Fehler abfaengt.

8. Volllauf (25. und 26.09.2026): Alle 395 Pull Requests gingen mit
   Prompt v2 an gpt-5.6-terra. Sie liefen im Normalbetrieb, also eine
   Anfrage nach der anderen, nicht im geplanten Stapelbetrieb. Das hat
   der Verfasser entschieden, weil der Stapelbetrieb im Konto der
   Nutzungsstufe 1 mehrere Tage und neuen Code gebraucht haette
   (Nachtrag zu E8). Alle 395 Antworten kamen vollstaendig und als
   gueltiges JSON zurueck. Das Pruefprogramm lehnte 126 Datensaetze
   ab, meist wegen Zitaten, die ueber eine entfernte Diffzeile
   hinweg verbinden. 8 abgelehnte Zitate gehen nach der vorab
   festgelegten Regel auf das Pruefprogramm zurueck, 28 muss der
   Verfasser selbst ansehen.

9. Pruefung nach Regel 1 (27. und 28.09.2026): Vor der Zaehlung fiel
   ein Fehler in der Reihenfolge des Suchprogramms auf. Ein Zitat, das
   bei einer unveraenderten Diffzeile das fuehrende Leerzeichen
   mitkopiert, verstoesst gegen den Prompt. Das Suchprogramm lastete
   es trotzdem dem Pruefprogramm an. Deshalb wurde zuerst eine Regel
   zur Trennung festgeschrieben und committet, erst dann gezaehlt.
   Ergebnis: Keines der 8 Zitate hatte das Leerzeichen mitkopiert. Das
   Pruefprogramm duldet seitdem Leerraum am Anfang und Ende eines
   Zitats, weil der Prompt genaue Leerzeichen nur im Inneren verlangt.
   6 der 8 Zitate gelten nun als gefunden. 2 bleiben abgelehnt, weil
   ohne den Rand weniger als 10 Zeichen uebrig bleiben. Die
   Mindestlaenge stand vorher fest und wird nicht nachtraeglich
   gestrichen, weil das eine Regelaenderung nach dem Ergebnis waere.

10. Pruefung nach Regel 3 und Abschluss von Paket E (28. und
    29.09.2026): Die 28 Zitate ohne vorab festgelegte Ursache hat der
    Verfasser selbst angesehen. Die Regel dafuer stand vorher fest und
    war committet, weil die Einordnung sonst nach dem Ergebnis haette
    gewaehlt werden koennen. Alle 28 gehen auf das Modell zurueck,
    keines auf das Pruefprogramm; die Programme bleiben deshalb
    unveraendert. Meist hat das Modell einzelne Zeichen veraendert
    (18), seltener Woerter (6) oder Stuecke ueber
    eine entfernte Zeile hinweg verbunden (4). Die
    Inhalte der Zitate sind dabei in den Chat gelangt; das ist
    offengelegt. Die Zahlen des Volllaufs sind jetzt endgueltig: 124
    von 395 Datensaetzen abgelehnt, 3 wegen des Formats, 6 wegen einer
    zu hoch angegebenen Belegstaerke, 115 wegen eines Zitats. Jeder
    Beleg hat einen Link auf seine Quelle, weil die Rueckverfolgbarkeit
    ein Bewertungskriterium ist. Kosten und Laufzeit stehen in der
    Kostenschaetzung.

11. Lokales Modell und Kontrollpunkt (29. und 30.09.2026): Fuer den
    Vergleich mit dem API-Modell lief ein Sprachmodell auf dem eigenen
    Rechner, ausgefuehrt vom Programm Ollama. Das bestehende
    Aufrufprogramm wurde dafuer nur erweitert, weil ein Unterschied
    sonst am Aufrufweg liegen koennte. Vor dem ersten Versuch stand
    eine Regel fest, was bei einem Fehlschlag gilt, weil eine Kuerzung
    sonst nach dem Ergebnis gewaehlt wirken koennte. Beide lokalen
    Modelle haben den Pilotfall vollstaendig beantwortet, aber das
    Format verfehlt: gpt-oss:20b brach mitten im JSON-Objekt ab,
    qwen3.6:27b setzte einen Markdown-Codeblock darum. Damit gilt die
    vorab festgelegte Stufe ohne Qualitaetsmessung eines lokalen
    Modells. FF3 vergleicht Kosten, Aufwand und Datenkontrolle, zur
    Qualitaet nur den Formatbefund an je einem Fall. Eine
    Zusatzmessung hat der Verfasser verworfen, weil sie nach dem
    Ergebnis beschlossen waere und die Zeit fuer die Pakete G und H
    fehlt.

12. Abschnitt 6.1 und Messgroessen (30.09. und 01.10.2026): Der
    Bericht ueber beide lokalen Versuche steht jetzt als Abschnitt 6.1
    in der Arbeit, weil jedes Paket mit einem Abschnitt endet. Die
    Abweichung vom Expose ist dort als Entscheidung des Verfassers
    begruendet, weil es ohne gueltige lokale Ausgabe keine Qualitaet
    zu vergleichen gibt. Eine Abstimmung mit dem Betreuer ist nicht
    vorgesehen. Danach wurden in F3 (Entscheidung Messgroessen fuer
    FF3) sechs Messgroessen festgelegt, weil sie vor jeder Zaehlung
    feststehen muessen: M1 Formatkonformitaet, M2 Unbelegtheitsrate,
    M3 Konsistenz ueber Wiederholungen, M4 Laufzeit je Vorgang, M5
    Kosten je Vorgang, M6 Speicherbedarf. Eine Anforderung gilt als
    unbelegt, wenn keiner ihrer Belege woertlich in der Quelle steht
    oder die berechnete Belegstaerke insufficient lautet; der zweite
    Teil folgt aus Regel B8 der Entscheidung E6. Ein Auszug aus dem
    Serverprotokoll steht jetzt im Repository, weil Abschnitt 6.1
    sich darauf stuetzt.

13. Belegbegriff und Grundzahlen (01. und 02.10.2026): Paket G hat
    mit einer Zaehlung begonnen, weil Stichprobe und Gap-Analyse ohne
    Grundzahlen geraten waeren. Vorher stand eine neue Regel fest, G1
    (Belegbegriff fuer FF4): Fuer die Sicherheitsfrage zaehlt eine
    Anforderung nur als belegt, wenn ihre Pflichtteile von Zitaten
    getragen werden, die wirklich im Pull Request stehen. Anlass war
    ein Befund am Code, weil die Berechnung der Belegstaerke auch
    nicht gefundene Zitate mitzaehlt. Die Unbelegtheitsrate fuer FF3
    blieb unveraendert, weil ihre Regel schon vorher feststand. Ein
    neues Zaehlprogramm ruft nur die vorhandenen Pruefungen auf, weil
    eine zweite Pruefregel abweichende Zahlen erzeugen koennte. Es hat
    alle bekannten Zahlen aus Paket E bestaetigt. Das Modell hat nur
    sehr wenige Anforderungen als sicherheitsrelevant markiert; die
    Pruefung der Klassifikation muss deshalb besonders nach
    uebersehenen Faellen suchen. Belegbegriff und Grundzahlen stehen
    als Abschnitte 4.2 und 6.2 in der Arbeit, weil seit dem 01.10.2026
    jedes Teilergebnis sofort geschrieben wird.
14. Sicherheitsraster und Streichung einer Kategorie (02.10.2026):
    Claude hat Common Criteria CC:2022 Teil 2 und 3, die
    BSI-Richtlinie TR-03185 in Version 1.1.1 und 29148 Abschn. 9.6
    gelesen, weil das Raster fuer FF4 auf gelesenen Primaerquellen
    stehen muss. Die BSI-Richtlinie hat seit 2026 keine getrennten
    Teile mehr; ihr Teil fuer Open-Source-Software enthaelt 20
    Anforderungen. Der Verfasser hat Option C gewaehlt, weil sie die
    Sicht auf das Produkt und auf den Entwicklungsprozess verbindet.
    Common Criteria dienen nur als Ordnungsrahmen, weil Qrisp keine
    Sicherheitsziele hat, an denen ihre Anforderungen haengen. Der
    Entwurf G2 (Aufnahmeregel und 29 Eintraege SR01 bis SR29) steht
    im Abschnitt Aktuell und ist noch nicht freigegeben. G3 streicht
    die Kategorie "nachweislich fehlende Sicherheitsfunktion", weil
    keine Code-, Test- oder Systempruefung zum Umfang gehoert und es
    ohne Sicherheitsziele keinen Massstab fuer "fehlt" gibt.

15. Sicherheitsraster festgelegt und geschrieben (04.10.2026): Der
    Verfasser hat G2 (die Entscheidung ueber den Ausschnitt der
    Pruefliste) mit drei Aenderungen freigegeben. Ae1 aendert Regel 2,
    weil sie jedem Eintrag einen Verweis auf die Common Criteria
    versprach, sechs Eintraege aber keinen haben. Ae2 fuegt die Spalte
    Stufe hinzu, weil so sichtbar wird, ob die BSI-Richtlinie etwas
    verlangt, empfiehlt oder nur erlaubt. Ae3 kennzeichnet die
    Einstufung von SR07 und SR08 als Einordnung, weil sie nicht am Code
    geprueft ist. G2 wurde einzeln committet, weil der Commit belegt,
    dass die Liste vor jeder Zuordnung feststand. Danach sind
    Abschnitt 2.4 und zwei Unterabschnitte in 4.2 entstanden, weil
    jedes Teilergebnis sofort geschrieben wird. Claude hat Teil 2 der
    Common Criteria als PDF gelesen, weil Text und Literaturangabe eine
    gepruefte Quelle brauchen. Die Pruefliste steht in zwei Tabellen,
    weil sie als eine Tabelle hoeher als eine Seite war.

Warum der naechste Schritt jetzt kommt: Als Naechstes kommt Schritt 4,
das Klassifikationsschema. Es ordnet die sechs Typwerte mit Fundstellen
aus 29148 den Klassen funktional und nicht-funktional zu und legt
security_relevant endgueltig fest, gemessen am Raster aus G2. Es kommt
jetzt, weil Schritt 5 (Pruefplan) und Schritt 6 (Pruefung von Hand)
eine feste Definition brauchen und beide vor der Pruefung committet
sein muessen. Paket G sollte am 04.10.2026 enden; die Schritte 4 bis 9
ueberschneiden sich deshalb mit dem Beginn von Paket H.

Geschrieben sind Teile von Kapitel 2 (seit 04.10.2026 mit Abschnitt
2.4), die Abschnitte 4.1, 4.2, 6.1 und 6.2 und Anhang A.
Abgabe am 15.10.2026, intern am 13.10.2026. Der Plan hat keine
Reserve. Groesstes Risiko: Paket G ist am 04.10.2026 nicht
abgeschlossen; die Schritte 4 bis 9 ueberschneiden sich mit Paket H
(Bewertung Mo 05. und Di 06.10.).


## Zusammenarbeit im Chat

Diese Regeln gelten fuer jeden Chat und gehen Annahmen vor.

- Projektwissen enthaelt ausschliesslich Unveraenderliches:
  exposee.tex und 29148-2018.pdf. Arbeitsdateien werden pro Chat
  hochgeladen, nie im Projektwissen abgelegt - dort veralten sie
  unbemerkt.
- Wenn Claude den Inhalt einer Datei braucht, muss er sie ausdruecklich
  anfordern und dabei den vollstaendigen Pfad nennen. Claude arbeitet
  nie mit einer aus dem Gedaechtnis rekonstruierten Fassung. Bewaehrt:
  in Paket D Teil 3 hat Claude von sich aus gemeldet, dass ihm zwei
  Dateien nicht mehr vorliegen, statt sie nachzubauen.
- Commit-Nachrichten werden erst nach dem git diff formuliert, nie
  vorab. In Paket D Teil 3 hat eine vorformulierte Nachricht eine
  Aenderung behauptet, die der Commit nicht enthielt (1d83472).
- Stopp-Punkte in Anleitungen sind verbindlich. Sie stehen dort, wo
  etwas unwiederbringlich ueberschrieben werden kann.
- Claude testet groessere Skripte vor der Uebergabe in seiner eigenen
  Umgebung mit erfundenen Testdaten und sagt das dazu. Bewaehrt: hat in
  Paket D Teil 2 jeden Fehler vor dem echten Lauf gefunden.
- Ab Paket D Teil 3: Claude prueft eine Testsuite zusaetzlich gegen
  absichtlich eingebrachte Fehler und zeigt, welche Tests dabei
  anschlagen. Nur so ist belegt, dass ein bestandener Test etwas misst.
- Es gelten unveraendert der Zweckbindungs-Block und die technische
  Schritt-fuer-Schritt-Regel der Projektanweisung. Keine Kurzfassung.
- Eine Messung, die die Arbeit selbst ausmacht, trifft der Verfasser.
  Das Modell darf erklaeren, gegenpruefen und formulieren. Wer eine
  Bewertung ausgefuellt hat, gehoert ins Protokoll.
- Claude darf Pull-Request-Seiten selbst oeffnen, um Bewertungen
  gegenzupruefen. Es sagt dann ausdruecklich, welche Seiten es
  geoeffnet hat und welche nicht.
- Soll eine Zeile hinzukommen, sagt Claude ausdruecklich "anhaengen,
  nichts ersetzen", und nennt die Zeile darueber als Anker. In Paket C
  Schritt 4b hat eine Ersetzungsanweisung zweimal eine Tabellenzeile
  geloescht (02.09.2026).
- Kommt ein Wortlaut in einer Datei mehrfach vor, warnt Claude vorher
  und nennt die gemeinte Stelle mit Zeilennummer. In Paket C Schritt 4b
  blieb "Zuletzt geaendert" an der zweiten Stelle stehen.
- Ein Pruefbefehl darf nicht nach Formulierungen suchen, die auch im
  neuen Text vorkommen. Sonst meldet er neu geschriebenen Text als
  Rest.
- Umfangsangaben fuer LaTeX-Text nennt Claude erst nach einer
  Testuebersetzung. In Paket C Anhang A lag die Schaetzung vorab
  deutlich zu niedrig (10.09.2026).
- Git-Befehle mit Pfaden wie thesis/thesis.tex setzen den
  Repository-Stamm als Arbeitsverzeichnis voraus. Wer im Ordner
  thesis/ steht, schreibt thesis.tex (11.09.2026). 
- Nach jeder Einfuegung in thesis.tex prueft vor dem Commit ein grep
  mit Suchtext ohne Umlaute die Einfuegestelle. Eine abweichende
  Zeilenzahl im git diff --stat ist ein Stoppsignal. In Paket C
  Anhang A fehlte dadurch eine Zeile im Vorspann (11.09.2026).
- Commits werden gebuendelt: ein Commit je abgeschlossenem
  Teilergebnis, nicht je Einzelschritt (Wunsch des Verfassers,
  28.09.2026). Ausnahme: Eine Regel, die vor einer Zaehlung feststehen
  muss, wird vorher einzeln committet, weil nur so ihr Zeitpunkt
  belegt ist. Qualitaet und Verstaendlichkeit gehen vor Tempo.
- Codeaenderungen liefert Claude als Patchdatei mit SHA-256-Summe. Der
  Verfasser prueft die Summe und fuehrt git apply --check vor git apply
  aus, weil so beim Kopieren kein Zeichen verloren geht. Bewaehrt am
  27.09.2026.
- Vor jedem Pruefungslauf nennt Claude die erwarteten Zahlen und sagt,
  was daran unsicher ist, weil eine Abweichung sonst unbemerkt bliebe.
  Eine Abweichung wird gemeldet und erklaert, nicht nachtraeglich
  passend gemacht (27.09.2026: 2 Zitate mehr als erwartet, Grund war
  die vorab festgelegte Mindestlaenge).
- Aendert ein Schritt mehr als drei Stellen in bestehenden Dateien,
  darf Claude die Ersetzungen als Python-Skript liefern: mit altem und
  neuem Wortlaut, Abbruch vor dem Schreiben, wenn ein alter Wortlaut
  nicht genau einmal vorkommt, Werte aus der Quelle statt abgetippt,
  SHA-256-Summe. Das Skript liegt ausserhalb des Repositorys. Grund:
  Handanweisungen fuer viele Stellen sind fehleranfaellig. Steht so in
  der Projektanweisung (Ersetzungen per Skript), hier seit 29.09.2026.
- Ausgaben, die Inhalte von Pull Requests zeigen (etwa --only des
  Anzeigeskripts), gehen nicht in den Chat; zurueckgemeldet werden nur
  Zahlen. Am 28.09.2026 sind die Inhalte aller 28 Zitate der Regel 3
  trotzdem in den Chat gelangt (Nachtrag zu E10 vom 28.09.2026,
  Teil 4). Claude hat daraufhin keine Zuordnung vorgeschlagen.
- Schreiben im Paket (Wunsch des Verfassers, 01.10.2026, ersetzt die
  Regel vom 30.09.2026): Sobald in einem Paket ein Teilergebnis
  feststeht, also eine Entscheidung committet oder ein Messwert
  gezaehlt ist, schlaegt Claude im selben Chat unaufgefordert den
  passenden Abschnitt fuer thesis/thesis.tex vor: Zieldatei,
  Einfuegestelle und Feingliederung. Nach Freigabe folgt der
  LaTeX-Text. Grund: Das Wissen ist dann frisch und muss nicht aus
  Notizen rekonstruiert werden. Was noch nicht belegt ist, steht als
  markierter Platzhalter im Text und wird nicht erfunden. Jedes Paket
  endet weiterhin mit mindestens einem Abschnitt, bevor der Chat
  wechselt. Gilt fuer die Pakete G, H und I.
- Lueckenpruefung (Wunsch des Verfassers, 01.10.2026): Nach Paket H,
  spaetestens vor dem Korrekturdurchgang am Mo 12.10.2026, geht Claude
  thesis/thesis.tex Kapitel fuer Kapitel durch. Geprueft wird: Ist
  jede der vier Forschungsfragen beantwortet? Ist jede Stelle aus
  STATUS.md und docs/entscheidungen.md mit dem Vermerk "gehoert nach
  Kapitel 5, 6 oder 7" aufgenommen? Ist jeder Platzhalter aufgeloest
  oder benannt? Laeuft kein Verweis ins Leere? Ergebnis ist eine Liste
  der Luecken mit Fundstelle. Claude ergaenzt nichts stillschweigend.
- Installationen ueber Homebrew koennen andere Pakete mit anheben. Am
  29.09.2026 hob brew install ollama Python von 3.14.6 auf 3.14.7.
  Claude nennt das vorher. Befehle, die nachfragen koennen, werden
  einzeln eingefuegt.
- Eine Erfolgsbedingung trennt technisches Gelingen von der
  Messgroesse. F1 hat beides verbunden: Ein Formatfehler, selbst ein
  Messwert, zaehlte als misslungener Pilotfall (30.09.2026).
- Vor jedem Vorschlag prueft Claude STATUS.md und
  docs/entscheidungen.md auf bestehende Regeln und Festlegungen, weil
  sonst Widersprueche entstehen. Anlass: Die Unbelegtheit wurde am
  30.09.2026 zuerst ohne Abgleich mit Regel B8 aus E6 vorgeschlagen
  (Wunsch des Verfassers, 30.09.2026).
- Fragen an den Verfasser stellt Claude ohne doppelte Verneinung, weil
  die Antwort sonst mehrdeutig ist (Frage zu 09:03:52 am 30.09.2026).
- Ersetzungsskript und Einfuegen von Hand werden nicht gemischt. Wer von
  Hand einfuegt, fuehrt das Skript nicht mehr aus, weil es dann
  abbricht. Claude vergleicht den Text danach maschinell mit dem
  Entwurf (Befund 04.10.2026).

## Kuerzel

Doppelt belegte Kuerzel - immer mit Klartext verwenden:
- E1, E2, E3 bezeichnen zwei verschiedene Dinge.
  (1) Die drei Verfahrensregeln der Formatauswahl in
      docs/formatauswahl.md Abschnitt 5 (Z. 299 bis 316):
      Ausschlussregel E1: Eine Ebene erhaelt die Rolle verpflichtend
      nicht, wenn K9 mit 0 bewertet ist; die Rolle optional bleibt
      moeglich. Auch in C4, entscheidungen.md Z. 742.
      Vorrangregel E2: Bei aehnlichem Profil entscheidet zuerst K9,
      dann K3, dann K8. Angewandt in C5, entscheidungen.md Z. 855.
      Dokumentationsregel E3: Jede Rollenzuweisung wird mit
      hoechstens drei Saetzen begruendet.
  (2) Die Entscheidungen aus Paket E in docs/entscheidungen.md:
      E1 Datenmodell, E2 Form der Evaluation, E3 API-Budget, alle
      vom 15.09.2026.
- B-Nummern bezeichnen zwei verschiedene Dinge.
  (1) B1 bis B9 = Regeln der Belegstaerke aus E6,
      docs/entscheidungen.md ab Z. 1435.
  (2) B1 bis B10, B11a und B11b = Bewertungskriterien in
      eval/instrument/kriterien_v0.md vom 21.09.2026, etwa
      B8 Formatkonformitaet, B9 Quellennachvollziehbarkeit,
      B10 Sprachliche Kriterien. Der Nachtrag zu E2 vom 22.09.2026
      meint diese Kriterien.
- Weg A: In C6 (entscheidungen.md Z. 1125) eine verworfene Form von
  Anhang A, nur mit Notentabelle. Im Zeitplan W10 und im Commit
  d858275 dagegen die Art der Bewertung aus dem Nachtrag zu E2 vom
  22.09.2026 (entscheidungen.md Z. 2010): Die Bewertungskriterien
  B8 (Schema), B9, B10 und Teile von B3 prueft ein Programm, die
  uebrigen bewertet der Verfasser von Hand. Dort steht der Name
  "Weg A" nicht.

Weitere Kuerzel:
Paket A bis I = Arbeitspakete (je ein Chat). A1 bis A8 = Aufgaben in
Paket E; A8 = Pilotlauf mit 20 Pull Requests, Teilschritte 1 bis 12.
C, D, E, F mit Nummer = Entscheidungen der Pakete C, D, E, F in
docs/entscheidungen.md, ausser den oben genannten Regeln E1 bis E3.
Stufen a bis d = Stufen von F1, Umfang von FF3 nach dem Kontrollpunkt;
es gilt Stufe d. Pilotfall = PR 64, gesendet an ein lokales Modell
nach F1.
F3 = Entscheidung Messgroessen fuer FF3 vom 30.09.2026.
M1 bis M6 = die sechs Messgroessen aus F3: M1 Formatkonformitaet, M2
Unbelegtheitsrate (Ebene der Anforderung), M3 Konsistenz ueber
Wiederholungen, M4 Laufzeit je Vorgang, M5 Kosten je Vorgang, M6
Speicherbedarf. M3 ist nicht der Prozessor Apple M3 Pro aus dem
Abschnitt Umgebung.
K1 bis K10 = Kriterien der Formatauswahl, docs/formatauswahl.md
Abschnitt 2. R1 bis R11 = Regeln fuer die Noten, dort Abschnitt 4.
Ebenen (a) bis (d) = die vier Ebenen einer Anforderung: (a) Sicht,
User Story; (b) Satzmuster, EARS; (c) Verbindlichkeit, RFC 2119;
(d) Qualitaetsregeln, 29148.
S1 bis S6 = Schichten der Stichprobenziehung in draw_sample.py.
L01 ff. = Quellen-IDs in literatur/literaturmatrix.md.
W1 bis W11 = Wochen des Zeitplans.
person_NN = Platzhalter fuer Personen (E9, gilt auch in der Arbeit).
Die Kennungen A01 ff. werden nicht verwendet (Nachtrag zu E9 vom
21.09.2026).
Ursachennamen wie hunk_header oder spans_removed_line = Kategorien
des Suchprogramms src/extract/diagnose_excerpts.py fuer abgelehnte
Zitate; Liste und Bedeutung im Kopf des Programms.
Regel 1 bis 3 = Zuordnung einer Ablehnung: 1 Pruefprogramm schuld,
2 Modell schuld, 3 der Verfasser sieht nach (Nachtrag zu E10 vom
24.09.2026).
v1, v2 = Fassungen des Prompts unter prompts/.
H1 = Hinweis des Anzeigeskripts src/extract/inspect_excerpts.py, ob ein
Zitat ohne Rand-Leerraum im Quellblock des Modells vorkommt (Nachtrag
zu E10 vom 28.09.2026, Teil 3).
Unterarten pruefprogramm, zusammengesetzt, umformuliert, zeichen,
ohne_gegenstueck = Art der Abweichung eines Zitats nach Regel 3,
festgelegt in Teil 3 und Teil 3a desselben Nachtrags.
G1 = Entscheidung Belegbegriff fuer die Gap-Analyse (FF4) vom
01.10.2026: Belegstaerke nur aus gefundenen Belegen, belegt bei direct
oder indirect. G2 = Entscheidung Ausschnitt des Sicherheitsrasters
fuer FF4: Option C, am 04.10.2026 freigegeben, Text in
docs/entscheidungen.md. G3 = Entscheidung vom 02.10.2026, die
Kategorie "nachweislich fehlende Sicherheitsfunktion" zu streichen.
G4 ff. = weitere Entscheidungen von Paket G.
SR01 bis SR29 = Eintraege des Sicherheitsrasters nach G2; SR01
bis SR09 aus 29148, SR10 bis SR29 aus TR-03185 Abschn. 2.3.
Option A bis D = Optionen fuer den Ausschnitt des Rasters vom
02.10.2026: A Produktsicht, B Lebenszyklussicht, C Kombination
(gewaehlt), D nur 29148 (verworfen, weil das Expose CC- bzw.
BSI-Orientierung verlangt).
TR-03185 = Technische Richtlinie des BSI "Secure Software Lifecycle".
CC = Common Criteria. T2, T3 = Teil 2 (Sicherheitsfunktionen) und
Teil 3 (Vertrauenswuerdigkeit) von CC:2022. ALC = Lebenszyklus-Klasse
in Teil 3.
Schritte 1 bis 9 von Paket G = Arbeitsplan aus dem Phasenstart vom
01.10.2026, siehe Abschnitt Aktuell. Nicht zu verwechseln mit den
Teilschritten 1 bis 12 von A8.
Ae1 bis Ae3 = drei Aenderungen am Entwurf G2 vom 04.10.2026: Ae1
Regel 2 (Verweis auf die Common Criteria nur, soweit erkennbar), Ae2
Spalte Stufe (Modalverb der TR-03185), Ae3 Einstufung von SR07 und
SR08 als Einordnung des Verfassers gekennzeichnet.
Neue Kuerzel duerfen keinen dieser Namen wiederverwenden.

## Umgebung

MacBook Pro, Apple M3 Pro, 36 GB RAM, ca. 515 GB frei
macOS-27.0-arm64 (laut Manifest, berichtigt 24.09.2026) - Python 3.14.7 (Homebrew; bis 29.09.2026 3.14.6, angehoben durch brew install ollama) - pip 26.1.2 - Git 2.50.1
TeX Live 2026
Ollama 0.34.4 (Homebrew, stabile Fassung), Modelle gpt-oss:20b und
qwen3.6:27b, abgeleitet gpt-oss-20b-ctx64k und qwen3.6-27b-ctx64k aus
config/ollama/. Bis zur Abgabe kein brew upgrade, weil sonst die
Version wechselt (F2).
Repository: /Users/omar/Developer/qrisp-re-thesis
Remote: github.com/os759/qrisp-re-thesis (privat, SSH)
Pakete laut requirements.txt: requests 2.34.2, pytest 9.1.1, jsonschema 4.26.0 sowie 
certifi, charset-normalizer, idna, iniconfig, packaging, pluggy,
Pygments, urllib3

## Repository-Struktur

config/ · data/{raw,interim,processed,manifests} · docs/ ·
eval/{instrument,sample,responses} · experiments/ ·
literatur/{notizen,volltexte,pdf} · prompts/ ·
src/{collect,prepare,extract,classify,analyze} · tests/ · thesis/

src/ enthaelt eine README.md, die alle Unterordner beschreibt. Die
Unterordner selbst haben keine README.md - bewusst so entschieden.
tests/ hat eine eigene README.md, die die Testbereiche und die
bewusst offenen Luecken benennt.

Per .gitignore ausgeschlossen: .env, config/config.yaml, *.key, *.token,
data/raw/, data/interim/, eval/responses/, docs/pseudonyme.csv,
models/, literatur/pdf/, literatur/volltexte/, .venv/, __pycache__/,
LaTeX-Hilfsdateien in thesis/, .DS_Store, .vscode/, .idea/
Nicht ausgeschlossen und damit versioniert: data/manifests/
Geprueft am 21.08.2026: __pycache__/ und .pytest_cache/ erscheinen
nicht in git status.

## Abgeschlossen

Arbeitspaket A (Setup) vollstaendig:
- Repository, .gitignore, README.md, STATUS.md, Ordnerstruktur
- SSH-Schluessel (Fingerabdruck gegen GitHub-Doku geprueft)
- Virtuelle Umgebung .venv, requests 2.34.2, requirements.txt
- GitHub-Token qrisp-thesis-readonly (fein granuliert, nur oeffentliche
  Repositories, im Passwortmanager)

Arbeitspaket B (Literatur und Grundlagen) inhaltlich abgeschlossen:
- literatur/suchprotokoll.md und literaturmatrix.md fortgeschrieben
  (16 Quellen erfasst, davon 7 gelesen und eingearbeitet:
  L05, L06, L07, L11, L14, L15, L16)
- Sechs Lesenotizen unter literatur/notizen/
- LaTeX-Vorlage nach thesis/ uebernommen, kompiliert fehlerfrei
- Abschnitte 2.1, 2.2.1, 2.2.2, 2.2.3 ausformuliert

Arbeitspaket D, Teil 1 (Pilotabruf) abgeschlossen:
- .env mit GITHUB_TOKEN, config/collect.toml
- src/collect/: github_api.py, api_test.py, explore_fields.py,
  compare_objects.py, fetch_pull_list.py
- Erhebung 12.08.2026: 476 Pull Requests

Arbeitspaket D, Teil 2 - alle vier Abrufe abgeschlossen:
- src/collect/fetch_pull_details.py, fetch_pull_comments.py,
  fetch_pull_files.py, analyze_pull_details.py, analyze_pull_files.py
- github_api.py um sha256_of, current_commit, read_jsonl, append_jsonl,
  retry_delay_seconds, request_with_retry, fetch_paginated ergaenzt.
  fetch_pull_list.py importiert die ersten beiden von dort.
- config/collect.toml um pause_seconds = 0.2 und max_retries = 5
  ergaenzt
- docs/findings_pull_details.md und findings_pull_files.md erzeugt
- Entscheidungen D1 bis D4 in docs/entscheidungen.md festgeschrieben

Arbeitspaket D, Teil 3 (Aufbereitung und Tests) abgeschlossen:
- config/collect.toml um den Abschnitt [prepare] ergaenzt
- src/prepare/build_interim.py: fuehrt die vier Rohdateien zu einem
  Datensatz je Pull Request zusammen, reduziert die Felder,
  normalisiert Zeilenenden, entfernt Vorlagenkommentare und setzt die
  drei Kuerzungsstufen aus D1 um
- Lauf vom 19.08.2026 ueber alle 476 Pull Requests, Manifest versioniert
- tests/: conftest.py und fuenf Testdateien mit 38 Tests, alle bestanden
- tests/README.md neu gefasst
- Entscheidungen D5 bis D8 in docs/entscheidungen.md
- docs/ki-protokoll.md fuer Teil 2 und Teil 3 nachgetragen

Arbeitspaket C (Formatauswahl) vollstaendig abgeschlossen am
11.09.2026, siehe Abschnitt "Aktuell". Darin Schritte 1 bis 3 sowie 4a und 4b
erledigt (4a = Gegenpruefung und Auswertung Teil A, 4b = Messung
fuer K6):
- Vorentscheidungen C1 bis C4 in docs/entscheidungen.md
- docs/formatauswahl.md: zehn Kriterien K1 bis K10, dreistufige ordinale Skala, zehn Bewertungsregeln R1 bis R10
  (R9 und R10 ergaenzt am 30.08.2026),
  Entscheidungsverfahren ueber Rollen je Ebene, Schwellen fuer K6/K9
- Abschnitt 2.1.7 in thesis/thesis.tex zu ISO/IEC/IEEE 29148 Abschn.
  9.6, mit Tabelle 2.1 zu den Inhaltsbloecken
- src/analyze/draw_sample.py und docs/sample_formulation_probe.md:
  zwoelf Pull Requests geschichtet und reproduzierbar gezogen
- docs/formatprobe_protokoll.md ausgefuellt (Arbeitsentwurf)
- Regeln R9 (pauschale Rollenangabe) und R10 (Bezugspunkt der
  Modalitaet) am 30.08.2026 ergaenzt, vor der Gegenpruefung
- Schwellen aus Abschnitt 6 auf zwoelf Faelle umgerechnet:
  Note 2 ab 10, Note 1 ab 5, sonst Note 0
- Alle zwoelf Faelle der Formulierungsprobe unabhaengig
  gegengeprueft. Fuenf Aenderungen, alle bei Ebene (c):
  PR 371 (27.08.), PR 408, 533, 577, 622 (30.08.)
- Auswertung Teil A abgeschlossen
- Schritt 4b: K6 fuer die Ebenen (c) und (d) als nicht anwendbar
  festgelegt (31.08.2026); Rahmen und drei Referenzinhalte aus 29148
  Abschn. 9.6.12 a, 9.6.14 und 9.6.18 c 5 festgelegt (02.09.2026),
  jeweils vor der Messung
- Teil B des Protokolls neu gefasst: sechs Formulierungsversuche,
  alle gelungen. K6: Ebene (a) 3 von 3 (Note 2), Ebene (b) 3 von 3
  (Note 2), Ebenen (c) und (d) n. a.
- docs/ki-protokoll.md um die Zeilen fuer den 30.08.2026 und den
  02.-03.09.2026 ergaenzt

Arbeitspaket E (Prompt und API-Modell) abgeschlossen am 29.09.2026:
- Entscheidungen E1 bis E11 mit Nachtraegen in docs/entscheidungen.md
- Prompt v2, Aufrufprogramm run_extraction.py, Pruefprogramm
  validate_output.py und Suchprogramm diagnose_excerpts.py mit Tests
- Pilotlaeufe 2026-09-22_pilot und 2026-09-24_pilot_v2 sowie Volllauf
  2026-09-25_full_v2 mit 395 Vorgaengen, Manifeste committet
- Pruefung des Volllaufs nach Regel 1 und Regel 3 abgeschlossen
  (Nachtrag zu E10 vom 27.09.2026 und vom 28.09.2026, Teil 1 bis 4)
- Links je Beleg (Teilschritt 10 von A8) und Messwerte des Volllaufs
  in experiments/kostenschaetzung.md, Abschnitt 6.3
- Stand am Ende von Paket E als Git-Tag thesis-v1.0 eingefroren

Arbeitspaket F (Lokales Modell und Modellvergleich) abgeschlossen am
01.10.2026:
- Kontrollpunkt mit gpt-oss:20b und qwen3.6:27b, beide nicht
  gelungen, es gilt F1 d (FF3 ohne Qualitaetsmessung eines lokalen
  Modells)
- Abschnitt 6.1 sec:eval-pilot-lokal mit den Tabellen
  tab:pilot-bedingungen und tab:pilot-ergebnisse, BibTeX-Eintrag
  ollamaopenai in online.bib
- F3 Messgroessen fuer FF3; F1 d und F2 Begruendung 1 berichtigt
- docs/ollama_protokollauszug.md mit den belegenden Zeilen des
  Serverprotokolls vom 30.09.2026

## Datensaetze (alle lokal, nicht im Repository)

data/raw/pulls_2026-08-12.jsonl - 476 PRs
  SHA-256 88a6652c1de9c2f2a1d2e60dbe9bef7291c8e1f3fada14418f4bf5bc387bead1
data/raw/pull_details_2026-08-14.jsonl - 476 Detailobjekte
  SHA-256 19bc97ad11d3e097e873eb72cc84df283d20c9fffb61d8a1f7013151dfa03bd9
data/raw/issue_comments_2026-08-19.jsonl - 639 Kommentare
  SHA-256 7d9918c628bd51bc2c9245fcbc2a678c20ec963c3d92481809fbdd724c760459
data/raw/review_comments_2026-08-19.jsonl - 1713 Kommentare
  SHA-256 d1c0dd08487402bf6020c2fd43b0243903c010d761c75e98cda8a86c7c12c7a4
data/raw/pull_files_2026-08-19.jsonl - 8424 Dateisaetze
  SHA-256 7315f5254a914278618c85c23422d7f2a04d1460ee8d8c6c6733f4e91533bbdc
data/interim/pulls_prepared_2026-08-19.jsonl - 476 aufbereitete PRs, 20 MB
  SHA-256 138e60ce47c1e6508d14ea6cec113c11e72772407fef2232870e2b1b981a4683
data/processed/model_input_2026-09-19.jsonl - 395 Quellbloecke, 8,5 MB
  Manifest versioniert unter demselben Namen mit .manifest.json
  Ersetzt model_input_2026-09-15.jsonl, siehe E9.
data/interim/mention_map.json - Zuordnung der 34 Anmeldenamen,
  lokal, durch .gitignore ausgeschlossen
data/processed/extraction_2026-09-22_pilot.raw.jsonl - 20 vollstaendige
  Antworten der Schnittstelle, lokal
  SHA-256 5209e484ed6ec2fd88277b4832469afd3104ac5b9df5593b0bce72dbb663ac0b
data/processed/extraction_2026-09-22_pilot.jsonl - 20 Modellausgaben,
  lokal
  SHA-256 6bfda3cfae8c1d38f7f7a243d5dd91cc38f5736268e130e0bc1fca6bbd871602
  Manifest versioniert unter demselben Namen mit .manifest.json.

data/processed/extraction_2026-09-25_full_v2.raw.jsonl - 395 vollstaendige
  Antworten der Schnittstelle, lokal
  SHA-256 319b909fe07119184986794e31224ae79870587fdf204bfef07f07366d7456da
data/processed/extraction_2026-09-25_full_v2.jsonl - 395 Modellausgaben,
  lokal
  SHA-256 3dbc74b24438cac24feba080eca69ef66a4b495b4f7fd677de0f22d7d91e569d
  Manifest versioniert unter demselben Namen mit .manifest.json.

Dazu je eine .progress.jsonl fuer Kommentare und Dateien, ebenfalls
lokal. Alle Manifeste unter data/manifests/ sind versioniert:
manifest_pulls_2026-08-12.json, manifest_pull_details_2026-08-14.json,
manifest_issue_comments_2026-08-19.json,
manifest_review_comments_2026-08-19.json,
manifest_pull_files_2026-08-19.json,
manifest_prepared_2026-08-19.json

## Belegte Fakten aus Paket D (Stand 19.08.2026)

Erhebung
- Token: Kontingent 5000/Stunde, Ablauf 2027-05-31.
- Repository eclipse-qrisp/Qrisp, oeffentlich, ID 632066325.
- 476 Pull Requests, Nummern 5 bis 797, keine Duplikate. Die Luecken
  entstehen durch den gemeinsamen Zaehler von Issues und Pull Requests.
  Jede Verarbeitung muss die Nummern aus der Datei lesen.
- Listenendpunkt 36 Felder, Detailendpunkt 48.
- state kennt nur open und closed; merged_at unterscheidet
  zusammengefuehrt von verworfen.

Struktur des Korpus
- outcome: merged 314 (66,0 %), closed_unmerged 109 (22,9 %),
  open 53 (11,1 %).
- 61 Autoren; die drei aktivsten schrieben 236 der 476 PRs (49,6 %),
  die zehn aktivsten rund 79 Prozent.
- Bots: 31 PRs (6,5 %), dependabot[bot] 28 und Copilot 3. Copilot endet
  nicht auf "[bot]" und wird nur ueber user.type erkannt.
- 222 PRs (46,6 %) ohne jeden Kommentar; nur 113 (23,7 %) mit
  Review-Kommentaren.
- 56 PRs (11,8 %) ohne Beschreibungstext.
- Vorlagentext "<!--" in 124 von 420 Beschreibungen (29,5 %),
  CRLF-Zeilenenden in 259 (61,7 %).
- labels nur bei 36 PRs (7,6 %) - keine Klassifikationsgrundlage.
- locked konstant False. draft 66-mal True (13,9 %).
- author_association nur CONTRIBUTOR (435) und NONE (41).
- Durchgehend leer: requested_teams, auto_merge, active_lock_reason.
- Fuenf PRs ohne jede Codeaenderung: 169, 332, 407, 408, 578.

Groessen
- additions + deletions je PR: Median 162, p90 2424, p99 18474,
  Maximum 30166, Summe 583821.
- 8424 Dateisaetze, 32557763 Zeichen Aenderungstext, entspricht bei rund
  3,5 Zeichen je Token grob 9 Millionen Token.
- Zeichen je Datei: Median 1397, p90 9534, Maximum 99478.
- Zeichen je PR: Median 9627, p90 112459, Maximum 2761999.
- .py haelt 81,0 Prozent des Aenderungstextes; src und tests zusammen
  80,7 Prozent. Die groessten PRs sind handgeschriebener Python-Code.
- GitHub liefert bei 331 von 8424 Dateien (3,9 %) kein patch-Feld.

Abweichungen
- PR 639: erwartet 1, geholt 4 allgemeine Kommentare. Geklaert, drei
  Kommentare vom 18.08.
- PR 470: erwartet 7, geholt 14 Dateien. Geklaert, updated_at von
  13.06. auf 17.08. gewandert, Commits 16 -> 22.
- PR 331, 344, 767: je ein Review-Kommentar weniger als gezaehlt. Nicht
  aufloesbar, reproduzierbar. 3 von 1716, 0,17 Prozent.
- Alle fuenf Abweichungen erscheinen unveraendert im Manifest der
  Aufbereitung. Keine neue Abweichung.

## Belegte Fakten aus der Aufbereitung (Lauf 19.08.2026)

Quelle: manifest_prepared_2026-08-19.json, erzeugt von
src/prepare/build_interim.py.

Vollstaendigkeit
- 476 Pull Requests, 639 allgemeine und 1713 Review-Kommentare, 8424
  Dateien uebernommen. Kein Datensatz verloren.
- 31 Bot-Beitraege enthalten und markiert (D7).
- 5 Pull Requests ohne Codeaenderung, 222 ohne Kommentar, 56 ohne
  Beschreibung - alle enthalten und markiert (D6).

Reinigung
- Zeilenenden bei 259 Beschreibungen vereinheitlicht.
- Vorlagentext bei 124 Beschreibungen entfernt.
- 0 Beschreibungen wurden durch die Reinigung leer. Die Zahl 56 bleibt
  unveraendert. Widerlegt die Vorabvermutung, sie koenne steigen.
- 0 unabgeschlossene Kommentarmarker im gesamten Korpus.
- Zeichenzahl 32555716 statt 32557763 im Rohabruf. Die Differenz von
  2047 Zeichen entfaellt auf CRLF-Zeilenenden, die zu LF werden. Kein
  Inhaltsverlust.

Wirkung der Kuerzung nach D1
- Stufe 1: 497 Dateien ohne Patch-Text (Dateityp oder kein patch-Feld).
- Stufe 2: 258 Dateien auf 10000 Zeichen gekuerzt.
- Stufe 3: 61 Dateien gekuerzt, 4580 Dateien ohne Patch-Text wegen
  erschoepftem Budget. Das sind 54,4 Prozent aller Dateien.
- 32555716 Zeichen werden zu 7396580, also 22,7 Prozent. Bei rund
  3,5 Zeichen je Token grob 2,1 statt 9,3 Millionen Token.
- 183 von 476 Pull Requests (38,4 %) sind irgendwie gekuerzt.
- Ergebnisdatei 476 Zeilen, 20 MB.

Diese Wirkung ist die groesste Einzelentscheidung der Datenaufbereitung
und gehoert nach Kapitel 5 und Kapitel 7. Der Budgetwert steht in
config/collect.toml und ist in Paket E ohne Codeaenderung anpassbar;
der Lauf ist dann zu wiederholen.

## Struktur eines aufbereiteten Datensatzes

Eine Zeile je Pull Request. Felder:
number, title, body, has_body, body_had_crlf, body_had_template,
body_template_unterminated, state, outcome, draft, author,
author_is_bot, author_association, created_at, updated_at, closed_at,
merged_at, html_url, labels, base_ref, base_sha, head_sha,
counts_api, counts_dataset, has_code_changes, has_patch_text,
truncation, issue_comments, review_comments, files

- counts_api enthaelt die Zaehlfelder von GitHub, counts_dataset die
  tatsaechlich vorliegenden Anzahlen. Beide bleiben getrennt, damit die
  bekannten Abweichungen sichtbar bleiben.
- truncation zaehlt je Pull Request: stage1_dropped, stage2_truncated,
  stage3_truncated, stage3_dropped, chars_original, chars_kept.
- Je Datei: filename, status, additions, deletions, changes, patch,
  patch_kept, patch_drop_reason, patch_truncated, patch_chars_original,
  patch_chars_kept. Gruende: no_patch_from_api, excluded_file_type,
  pull_budget_exhausted.
- Je Review-Kommentar zusaetzlich: path, line, side, commit_id,
  review_id, diff_hunk. Der diff_hunk gibt die Codezeilen, auf die sich
  der Kommentar bezieht - wertvoll fuer die Rueckverfolgbarkeit.
- Kommentare sind nach created_at sortiert, Dateien in der
  Lieferreihenfolge der API.

## Testsuite

414 Tests, ausfuehren aus der Projektwurzel:
python -m pytest tests/ -v
Zuletzt gruen am 02.10.2026 (414 passed) unter Python 3.14.7,
abgelesen vom Aktualisierungsskript.

tests/conftest.py setzt den Importpfad auf src/collect, src/prepare
und src/extract. Ohne diese Datei finden die Tests die Module nicht.

Bereiche: test_resume.py (Wiederaufnahme), test_outcome.py,
test_normalisation.py, test_jsonl_io.py, test_truncation.py,
test_schema_validation.py (70 Tests, Schema, Belegstaerke und
Zitatregeln des Prompts, seit 27.09.2026 auch Leerraum am Rand),
test_prompt_input.py (21 Tests, Auswahl und Budget),
test_prompt_files.py (30 Tests, Prompt v1 und v2 gegen Schema; v2
darf nur die Regeln fuer Zitate aus Diffs aendern),
test_pseudonymise.py (28 Tests, Ersetzung von Erwaehnungen),
test_draw_sample.py (15 Tests, Schalter --sizes und --exclude, E10 a),
test_run_extraction.py (45 Tests, Aufrufprogramm ohne Netz, mit
erfundenen Antworten; seit 30.09.2026 auch der lokale Aufrufweg,
geprueft gegen 15 absichtlich eingebaute Fehler), test_diagnose_excerpts.py (51 Tests,
Ursachensuche fuer abgelehnte Zitate), test_inspect_excerpts.py
(35 Tests, Anzeige und Auszaehlung fuer Regel 3),
test_breakdown_rejections.py (17 Tests, Ablehnungen nach
Art), test_cost_report.py (18 Tests, Abschnitt 6.3 aus dem
Manifest), test_add_links.py (18 Tests, Links je Beleg),
test_count_requirements.py (22 Tests, Zaehlprogramm nach F3 und G1
seit 01.10.2026, geprueft gegen 16 absichtlich eingebaute Fehler,
setzt seinen Importpfad selbst). Die
beiden neuen Dateien vom 21. und 22.09.2026, test_diagnose_excerpts.py
und die vier Dateien vom 28.09.2026 setzen ihren Importpfad selbst.
Die vier Dateien vom 28.09.2026 wurden in der Umgebung von Claude
gegen 34 absichtlich eingebaute Fehler geprueft: 33 erkannt, einer
ohne Wirkung, weil eine zweite Pruefung denselben Fall abfaengt.
Nicht abgedeckt: Netzschicht in github_api.py, Auswertungsskripte,
draw_sample.py ausserhalb der neuen Schalter (siehe D4a).

## Ungepruefte Beobachtungen

- Ob die 321 Nummernluecken alle Issues sind: plausibel, nicht gemessen.
- Zu PR 344: vermutet ein Review im Zustand pending, nur seinem
  Verfasser sichtbar. Nicht pruefbar.
- PR 674 und 676 sind fast gleich gross (574/575 Dateien) - vermutlich
  zwei Anlaeufe derselben Umbauaktion. Nicht geprueft.
- Warum author_association nie OWNER oder MEMBER annimmt: unbekannt.
- Ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben enthalten:
  Vermutung aus D7, nicht gemessen. Relevant fuer FF4.
- Erledigt durch E5: Quellblock hoechstens 80 000 Zeichen, kein
  Vorgang scheitert an der Kontextgroesse des Modells (E8).
- PR 408 hat auf GitHub einen Commit, gilt im Datensatz aber als
  Pull Request ohne Codeaenderung. Der Head-Branch wurde geloescht.
  Ob das zusammenhaengt: ungeprueft. Falls ja, betrifft es die
  Vollstaendigkeit der Erhebung und gehoert nach Kapitel 7.
- Im Diff von PR 533 stehen Soll-Saetze, die Inhalt der neuen
  Dokumentation sind (etwa: jede oeffentliche Funktionalitaet
  sollte durch mindestens einen Test abgedeckt sein). Sie wurden
  nicht als Fundstelle gewertet. Fuer Paket E interessant: Solche
  Saetze sind selbst rekonstruierbare Anforderungen.

## Aktuell

Paket C, Schritt 5 abgeschlossen am 08.09.2026, Schritt 6 am
09.09.2026. Die Rollenzuweisung und die Formatentscheidung stehen als C5 in
docs/entscheidungen.md, der Abschnitt 4.1 steht in
thesis/thesis.tex. Ergebnis: die Ebenen (b) EARS und (d)
Qualitaetsregeln sind verpflichtend, die Ebenen (a) und (c) werden
nicht verwendet. Das Zielformat heisst EARS+29148.

Paket C ist am 11.09.2026 abgeschlossen. Anhang A enthaelt die
gekuerzten Einzelbegruendungen zu allen zehn Kriterien, K1 bis K5 aus
Durchgang 1 und K6 bis K10 aus Durchgang 2. Er steht nach dem
Literaturverzeichnis; Abschnitt 4.1.3 verweist mit dem Label
cha:anhang-einzelbegruendungen darauf. Die Uebersetzung laeuft ohne
Fehler und ohne undefinierte Verweise, das Dokument hat 54 Seiten,
Anhang A die Seiten 39 bis 50. Der Verfasser hat den Entwurf gelesen
und geprueft.

Anhang A enthaelt keine Note, die nicht schon in Abschnitt 10 von
docs/formatauswahl.md oder im Formulierungsprotokoll steht. Bei K6
und K9 geht er in drei Punkten ueber Abschnitt 10 hinaus, weil dort
keine Einzelbegruendungen stehen: eine Vorbemerkung zur Herkunft der
gemessenen Noten, die Tabelle A.1 mit den sechs
Formulierungsversuchen sowie je ein zusaetzliches Gegenargument bei
K6 Ebene (b) und K9 Ebene (c). Festgehalten im Nachtrag zu C6.

Seit dem 07.09.2026 gilt zusaetzlich R11: Die Skalenstufe 2 bemisst
sich am Vorhandensein und an der Reichweite einer ausdruecklichen
Regel, nicht an einem empirischen Wirksamkeitsnachweis. Berichtete
Restprobleme einer Erprobung fuehren fuer sich genommen nicht zu
Note 1. Alle vier K1-Noten wurden daraufhin geprueft, keine aendert
sich.

Ebenfalls seit dem 07.09.2026: ISO/IEC/IEEE 29148 Abschn. 5.2.4 ist
auf drei Ebenen aufgeteilt. Aufbausatz und Figure 1 gehoeren zu
Ebene (b), die Schluesselwoerter zu Ebene (c), die sprachlichen
Vorgaben zu Ebene (d). Ebene (c) wird ausschliesslich an den
Schluesselwoertern gemessen. Ebene (b) stuetzt sich damit auf zwei
Quellen; bewertet wird EARS als die spezifischere. Die
Pflichtbestandteile aendern sich nicht, die K9-Messung bleibt
gueltig.

Verfahren seit 04.09.2026 (C2a): Das Modell legt je Zelle die
Belegstelle, einen Notenvorschlag und das Gegenargument vor. Der
Verfasser liest die Belegstelle in der Quelle nach und vergibt die
Note. Vorgegangen wird kriterienweise ueber alle vier Ebenen.

Volltexte, die dem Modell am 04.09.2026 vorlagen und die es selbst
gelesen hat: Mavin 2009, Mavin/Wilkinson 2010, Wilkinson/Mavin 2018,
Lucassen 2016, RFC 2119, RFC 8174, ISO/IEC/IEEE 29148 Abschn. 5.2.4
bis 5.2.7.

Erledigt am 08.09.2026: Die Zellen der Ebene (c) wurden an den
Volltexten von RFC 2119 und RFC 8174 gegengeprueft. Die Lesenotiz
literatur/notizen/bradner_1997_rfc2119.md enthielt keinen Fehler.
Vier Ungenauigkeiten entstanden erst beim Verkuerzen in die Zellen
und sind berichtigt; keine Note aendert sich. Am 09.09.2026 wurden
zusaetzlich Mavin et al. 2009 und Lucassen et al. 2016 im Volltext
geprueft. Damit sind alle Belegstellen der Matrix und des
Abschnitts 4.1 an den Quellen kontrolliert. Am 10.09.2026 kam
Mavin/Wilkinson 2010 hinzu; dabei wurde ein falscher
Abschnittsverweis in Abschnitt 4.1 berichtigt. Damit liegt zu jeder
in Kapitel 2 und Abschnitt 4.1 zitierten Quelle der Volltext vor
und ist geprueft.

Messergebnis K9, Stand 30.08.2026:
- Ebene (a) User Story: 4 von 12 gedeckt (33,3 %), Note 0.
  Zwei davon stuetzen sich auf eine pauschale Rolle (PR 371, 622).
  Ohne diese: 2 von 12 (16,7 %), Note bleibt 0.
- Ebene (b) EARS: 9 von 12 gedeckt (75,0 %), Note 1.
- Ebene (c) Modalitaet: 0 von 12 gedeckt, Note 0.
- Ebene (d) Qualitaetsregeln: K9 nicht anwendbar.

Die Noten von (a) und (b) haengen an je einem einzigen Fall. Die
Note von (c) nicht: dafuer fehlen fuenf Faelle.

Messergebnis K6, Stand 02.09.2026:
- Ebene (a) User Story: 3 von 3 gelungen, Note 2.
- Ebene (b) EARS: 3 von 3 gelungen, Note 2.
- Ebenen (c) und (d): K6 nicht anwendbar.
- K6 unterscheidet die Ebenen (a) und (b) nicht. Beide beziehen je
  einen Pflichtbestandteil aus dem Rahmen: (a) die Rolle, (b) den
  Systemnamen. Wuerde die Rahmenrolle nicht anerkannt, faellt (a)
  auf 0 von 3. Beides gehoert nach Kapitel 7.

Paket E begonnen am 15.09.2026, abgeschlossen am 29.09.2026. Elf
Entscheidungen sind gefallen.
E11 Denkaufwand, Schemapruefung beim Anbieter und Prompt-Version fuer
den Volllauf (24.09.2026) und E10 Rahmen des Pilotlaufs kommen zu den
folgenden neun hinzu:
E1 Datenmodell, E2 Evaluationsform, E3 API-Budget, E4 Auswahlregel,
E5 Budget der Modelleingabe, E6 Belegstaerke, E7 Prompt Version 1,
E8 Modellwahl, E9 Ersetzung von Erwaehnungen. Dazu Nachtraege zu C5,
E1 und E6.

Stand der Aufgaben in Paket E:
- A1 bis A5 fertig und committet.
- A6 Prompt Version 1 abgeschlossen am 17.09.2026. Dateien:
  prompts/extraction_system_v1.md, prompts/extraction_user_v1.md,
  src/extract/prompt_files.py, tests/test_prompt_files.py.
- A7 Modellwahl und Kostenschaetzung abgeschlossen am 19.09.2026.
- A8 Pilotlauf abgeschlossen am 24.09.2026. Teilschritt 10 (Links)
  am 28.09.2026 fuer den Volllauf nachgeholt, Variante B (Nachtrag zu
  E10 vom 28.09.2026, Teil 4). Datei lokal:
  data/processed/extraction_2026-09-25_full_v2.links.jsonl,
  2 711 Zeilen, SHA-256 e5ba8c6c9d09c1da70638ce1f7d9e5d01ac77cc6bb9614bdb1b5f0a43a06a187.
  Fuer die Pilotlaeufe nicht erzeugt; bei Bedarf mit demselben
  Programm. Stand der Teilschritte 1 bis 8 vom 22.09.2026:
  Festgelegt in E10 mit Nachtraegen zu
  E2, E9 und E10. Kriterienliste eval/instrument/kriterien_v0.md vor
  dem ersten bezahlten Aufruf committet. Pilotstichprobe
  docs/sample_pilot_a8.md, 20 Vorgaenge, Startwert 20260921, ohne die
  zwoelf Faelle aus Paket C. Aufrufprogramm
  src/extract/run_extraction.py mit config/api_run.toml.
  Lauf 2026-09-22_pilot: 20 von 20 beantwortet, keine abgeschnitten,
  alle 20 gueltiges JSON, store bei allen 20 von der Schnittstelle als
  false bestaetigt. Messwerte (Token, Dauer, Kosten) nur im Manifest
  data/processed/extraction_2026-09-22_pilot.manifest.json.
  validate_output.py: 5 von 20 Datensaetzen abgelehnt, alle an der
  Zitatpruefung, alle bei Zitaten aus Diffs (PR 71, 86, 166, 299, 316).
  Schema- und Belegstaerkepruefung bestanden alle 20. Ursache der
  Ablehnungen ungeklaert: Werkzeug oder Modell.
  Ausnahme von der Regel "neue Kennung nach Programmaenderung": Die
  Antwort zu PR 64 stammt aus dem Probeaufruf vor der Korrektur der
  Kostenrechnung. Die Korrektur betrifft nur die Nachberechnung aus
  der Rohdatei, nicht die Anfrage. Festgehalten im Nachtrag zu E10 vom
  24.09.2026, zusammen mit dem Laufdatum laut Manifest (PR 64 am 22.09.,
  die uebrigen 19 am 23.09.).
  Teilschritt 9, Ursachen: Das Suchprogramm
  src/extract/diagnose_excerpts.py ordnet jedes abgelehnte Zitat einer
  Ursache zu und gibt keine Inhalte aus. Die Regel dazu stand vor der
  Suche fest (Nachtrag zu E10 vom 24.09.2026). Ergebnis: alle
  Ablehnungen nach Regel 2 (Modell), keine nach Regel 1.
  validate_output.py prueft seit dem 24.09.2026 nach den Zitatregeln
  des Prompts (Sperre an entfernten Zeilen und @@-Zeilen, bei
  Review-Kommentaren nur der Text), weil es sonst verbotene Zitate als
  korrekt zaehlte. Dadurch lehnt es im Lauf v1 mehr ab als am 22.09.
  Prompt v2 (prompts/extraction_system_v2.md, Vorlage
  extraction_user_v2.md unveraendert) fasst die Regeln zu @@-Zeilen
  und entfernten Zeilen deutlicher. Lauf 2026-09-24_pilot_v2, Manifest
  committet. Nach der vorab festgelegten Uebernahmeregel gilt v2 fuer
  den Volllauf (E11 c); config/api_run.toml steht auf v2. Keine
  Version 3 (E11 d). Eine weitere Ursachensuche gibt es nur mit einem
  neuen, schriftlich begruendeten Anlass.
  Teilschritt 11: Messwerte beider Laeufe und Hochrechnung fuer den
  Volllauf in experiments/kostenschaetzung.md, Abschnitt 6. Laufzeit:
  Summe von duration_seconds in den Manifesten. Alle Zahlen zu
  Ablehnungen und Ursachen stehen in E11 und im Nachtrag zu E10 vom
  24.09.2026, nicht hier.
  Beobachtung fuer Kapitel 6 und 7: Das Modell gibt Backslashes in
  LaTeX-Ausdruecken aus Python-Kommentarbloecken nicht verlaesslich
  wieder (PR 316 und PR 294, E11 e).

Am 19.09.2026 wurde die Modelleingabe neu gebaut, weil Erwaehnungen
von Anmeldenamen ersetzt werden (E9). Gueltig ist
data/processed/model_input_2026-09-19.jsonl mit 395 Quellbloecken und
8 533 169 Zeichen. 34 Anmeldenamen wurden ersetzt; im Fliesstext
steht keine unersetzte Erwaehnung mehr. Nachgezaehlt vom Verfasser.

OpenAI-Zugang eingerichtet am 21.09.2026: Projekt qrisp-re-thesis,
Schluessel als OPENAI_API_KEY in .env, hartes Limit und Datenfreigabe
wie im Nachtrag zu E10. Seit dem Nachtrag zu E8 liegt das harte
Limit fuer Organisation und Projekt bei 35 US-Dollar. Das Schema
person_NN aus E9 gilt auch fuer den Text der Arbeit (Nachtrag zu E9
vom 21.09.2026).

Volllauf 2026-09-25_full_v2, Paket E: Kein Stapelbetrieb, sondern
Normalbetrieb, Entscheidung des Verfassers (Nachtrag zu E8), weil
der Stapelbetrieb in Stufe 1 mindestens drei Stapel mit je bis zu 24
Stunden Frist und neuen Code gebraucht haette. Liste aller 395
Vorgaenge: docs/sample_full_run_e.md, erzeugt mit draw_sample.py und
vollen Schichten, ohne Codeaenderung. Probelauf mit 5 Vorgaengen am
25.09., die uebrigen 390 am 26.09.2026 nach vorab festgelegten
Bedingungen. Ergebnis laut Programm: 395 von 395 beantwortet, keine
abgeschnitten, 395 gueltige JSON-Objekte, kein Aufruf wiederholt.
Konfiguration und Systemanweisung haben dieselben Pruefsummen wie im
Lauf 2026-09-24_pilot_v2; fuer diese 20 Vorgaenge liegen damit zwei
Durchgaenge mit gleichen Einstellungen vor (Material fuer FF3,
Konsistenz). Token und Kostenobergrenze stehen im Manifest.
Abrechnung laut Konto, abgelesen am 26.09.2026: Gesamtverbrauch
23,80 US-Dollar, davon vor dem Volllauf 2,40. Pruefung mit
validate_output.py und diagnose_excerpts.py, beide Stand f9eef00:
126 von 395 Datensaetzen abgelehnt, darunter PR 796 wegen des
fehlenden Feldes requirements (Formatfehler des Modells). 214
abgelehnte Zitate: Regel 1 (Pruefprogramm) 8, Regel 2 (Modell) 178,
Regel 3 (Verfasser sieht ein) 28. Stand nach Regel 1 am 27.09.2026
(Nachtrag zu E10, Rahmen des Pilotlaufs, vom 27.09.2026, Teil 1 und
2; dort alle Zahlen und Commits): 124 von 395 Datensaetzen
abgelehnt, 208 von 2 711 Zitaten, davon Regel 1: 2, Regel 2: 178,
Regel 3: 28.
validate_output.py duldet seitdem Leerraum am Rand eines Zitats;
beide Programme nutzen dieselbe Pruefung. Nach Regel 3 am 28. und
29.09.2026 gehen alle 28 auf das Modell zurueck. Endgueltig: Regel 1
2, Regel 2 206 von 208 abgelehnten Zitaten. Ablehnungen nach der
ersten verletzten Pruefung: Schema 3, E6 6, Zitat 115 (Nachtrag zu
E10 vom 28.09.2026, Teil 4; dort alle Zahlen).

Paket F, Kontrollpunkt am 29. und 30.09.2026: Ollama mit gpt-oss:20b
(F2) und dem Ersatzmodell qwen3.6:27b, beide mit Kontextfenster
65 536, Aufruf ueber run_extraction.py mit config/local_run.toml und
config/local_run_qwen.toml. Der Pilotfall ist mit beiden Modellen
nicht gelungen, es gilt F1 d (Nachtrag zu F1, Teil 1 und 2). Messwerte
in den Manifesten der Laeufe 2026-09-30_local_pilot_v2_r1 und
2026-09-30_local_qwen_pilot_v2_r1. Rohdateien lokal, Serverprotokoll
unter ~/qrisp-ollama-logs/, Auszug in docs/ollama_protokollauszug.md.

Abschnitt 6.1 Kontrollpunkt und Pilotfall der lokalen Modelle
(sec:eval-pilot-lokal) steht in thesis/thesis.tex, im Kapitel
cha:evaluation hinter dem Platzhalter des Kapitels. Die Uebersetzung
laeuft ohne Fehler und ohne undefinierte Verweise; das Dokument hat
60 Seiten, Kapitel 6 die Seiten 35 bis 41. Zwei Platzhalter bleiben:
Verweis auf den Abschnitt zur lokalen Ausfuehrung in Kapitel 5 und
Verweis auf den Abschnitt mit den Messgroessen. Zusaetzliche Befunde
im Abschnitt: Der Denkteil der lokalen Modelle steckt offenbar in der
gemeldeten Ausgabezahl, weil das Serverprotokoll am Ende jeder Anfrage
fast genau Eingabe plus Ausgabe als Token im Kontext zaehlt
(Schlussfolgerung von Claude). Die Ollama-Dokumentation nennt das Feld
store fuer /v1/responses nicht; F2 ist entsprechend berichtigt.

Messgroessen fuer FF3 stehen als F3 in docs/entscheidungen.md. M1,
M4, M5 und M6 sind aus vorhandenen Daten bekannt. M2, M3 und Teil b
von M1 im Pilotlauf werden in Paket H gezaehlt, weil die Auswertung
dort ohnehin laeuft. Weil vier Zahlen vor der Festlegung bekannt
waren, folgen die Definitionen nur aus aelteren Regeln; das gehoert
nach Kapitel 7.

Die freigegebene Feingliederung vom 30.09.2026 ist umgesetzt und
bleibt nur zur Nachvollziehbarkeit stehen. Zieldatei war
thesis/thesis.tex, im Kapitel cha:evaluation. Der Platzhalter des Kapitels bleibt, weil
Design und Auswertung noch fehlen; die genaue Zeile legt der neue Chat
fest.
  \section{Kontrollpunkt und Pilotfall der lokalen Modelle},
  Label sec:eval-pilot-lokal. Einleitung: FF3 verlangt einen
  praktischen Vergleich; das lokale Modell war das groesste
  Zeitrisiko, daher ein Kontrollpunkt mit vorab festgelegter Regel.
  1. Vorab festgelegte Regel, subsec:pilot-regel: Pilotfall,
     Erfolgsbedingung, Frist, Stufen a bis d in Kurzform, gleiche
     Einstellungen wie beim API-Modell, Zeitpunkt durch Commits
     belegt, Lesart ein Versuch, Zuordnungsregel vor der
     Ursachensuche.
  2. Versuchsbedingungen, subsec:pilot-bedingungen, Tabelle
     tab:pilot-bedingungen: Rechner, nutzbarer Grafikspeicher,
     Laufzeitumgebung mit Version, Schnittstelle, Prompt-Version,
     Kontextfenster (Standard waere 32 768 gewesen), Denkeinstellung
     je Modell, nicht gesendete Auswahlwerte, Datenkontrolle.
     Einzelheiten in Kapitel 5, hier nur ein Verweis.
  3. Erster Versuch mit gpt-oss:20b, subsec:pilot-gptoss: Ergebnis,
     Formpruefung, ausgeschlossene Ursachen, Protokoll ohne
     Stoppmeldung, nicht entscheidbar.
  4. Zweiter Versuch mit qwen3.6:27b, subsec:pilot-qwen: Wahl nach der
     Regel, Codeblock, die Diagnose (innen ein gueltiges Objekt)
     ausdruecklich nicht gewertet, spricht nicht fuer Ollama als
     gemeinsame Ursache.
  5. Folge fuer FF3, subsec:pilot-folge: F1 d als Entscheidung des
     Verfassers mit Begruendung (Nachtrag zu F1, Teil 2, Punkt 5);
     was FF3 danach vergleicht; Tabelle tab:pilot-ergebnisse fuer PR 64 mit
     gpt-5.6-terra (Pilot v2 und Volllauf), gpt-oss und qwen:
     Eingabe- und Ausgabe-Token, Dauer, gueltiges JSON-Objekt;
     explorativ, ein Vorgang je Modell.
  Validitaetsbedrohungen nicht hier, sondern in Kapitel 7 (Liste im
  Nachtrag zu F1, Teil 2, Punkt 6). Belege: Manifeste und
  docs/entscheidungen.md; in online.bib die Ollama-Dokumentation zur
  OpenAI-Kompatibilitaet, abgerufen am 29.09.2026. Weitere Quellen zu
  den Modellen erst nach dem Lesen.

Paket G, Schritte 0 und 1 am 01. und 02.10.2026: G1 (Belegbegriff
fuer die Gap-Analyse) committet, bevor gezaehlt wurde. Zaehlprogramm
src/analyze/count_requirements.py, Lauf mit dem Code-Commit aus der
Ergebnisdatei experiments/requirement_counts_2026-09-25_full_v2.json;
alle bekannten Zahlen aus Paket E bestaetigt, beide Pruefpunkte aus
F3 beantwortet (Nachtrag zu F3 vom 01.10.2026). Abschnitt 4.2
(sec:konzeption-gap, Belegbegriff) und Abschnitt 6.2
(sec:eval-grundzahlen, Grundzahlen) stehen in thesis/thesis.tex. Die
Uebersetzung laeuft ohne Fehler und ohne undefinierte Verweise, mit
14 Overfull hboxen, keine davon im neuen Text.

Paket G, Schritt 2 und Schreiben am 04.10.2026: G2 mit Ae1 bis Ae3
freigegeben und einzeln nach docs/entscheidungen.md committet, bevor
eine Anforderung dem Raster zugeordnet wurde. Abschnitt 2.4
(sec:cc-bsi) und in 4.2 die Unterabschnitte subsec:sicherheitsraster
und subsec:gap-kategorien stehen in thesis/thesis.tex. Damit ist der
Schreibauftrag aus G3 fuer 4.2 erledigt; der Teil fuer Kapitel 7
steht aus. Die Pruefliste steht in zwei Tabellen, weil sie als eine
Tabelle hoeher als die Seite war. Der Verfasser hat den Text von Hand
eingefuegt; Claude hat ihn danach maschinell mit dem Entwurf
verglichen, er ist identisch, ausser der vom Verfasser selbst
formulierten Einleitung von 4.2. Die Uebersetzung laeuft ohne Fehler
und ohne undefinierte Verweise, ohne zu hohe Tabelle, mit
14 Overfull hboxen; die einzige im neuen Bereich ist die
schon vorher vorhandene Ueberschrift von Abschnitt 2.4.

Arbeitsplan Paket G (Phasenstart 01.10.2026, Reihenfolge vom
Verfasser freigegeben):
1. Grundzahlen zaehlen - erledigt.
2. Sicherheitsraster: Common Criteria CC:2022 Teil 2 und 3, BSI
   TR-03185 und 29148 Abschn. 9.6 lesen, Ausschnitt festlegen und
   begruenden (naechste freie Nummer G2). Gelesen und Option C
   gewaehlt am 02.10.2026. Erledigt am 04.10.2026: G2 freigegeben
   und committet, Abschnitte 2.4 und 4.2 geschrieben.
3. Kategorie "nachweislich fehlende Sicherheitsfunktion" beibehalten
   oder streichen; Pflichtentscheidung nach der Projektanweisung.
   Erledigt am 02.10.2026: gestrichen, siehe G3, mit Schreibauftrag.
4. Klassifikationsschema: Zuordnung der sechs Typwerte zu funktional
   und nicht-funktional mit Fundstellen aus 29148, weil das Expose
   diese Dreiteilung verlangt (Wunsch des Verfassers vom 01.10.2026:
   Claude macht die belegte Zuordnung); endgueltige Definition von
   security_relevant am Raster; Regeln und Grenzfaelle.
5. Pruefplan fuer die Klassifikation, vor der Durchfuehrung
   committet: alle als sicherheitsrelevant markierten Anforderungen
   von Hand, dazu eine Suche nach uebersehenen Faellen, etwa mit
   Suchwoertern aus dem Raster (offen); gemeinsame oder getrennte
   Stichprobe mit der Evaluation nach E2 (offen).
6. Pruefung von Hand durch den Verfasser, nur Zahlen in den Chat.
7. Dependabot-Sichtung nach E4 und D7; offen, ob alle 28 oder nur die
   25 abgeschlossenen Beitraege.
8. Gap-Analyse mit den vier Kategorien der Projektanweisung.
9. Zu jedem Teilergebnis ein Abschnitt in thesis.tex.
Verschoben (Verfasser einverstanden am 01.10.2026): Kriterienliste v1
auf Mo 05.10.2026 vor der ersten Bewertung, wie E2 es erlaubt;
Literatursuche Phase 2 und Kapitel 5 aus W9 heraus.

G2 (Ausschnitt des Sicherheitsrasters) steht seit 04.10.2026 mit
Aufnahmeregel und Raster SR01 bis SR29 in docs/entscheidungen.md.
Der Entwurf steht hier nicht mehr, weil es sonst zwei Fassungen gaebe.

Quellen von Paket G Teil 2 (unter literatur/pdf/, nicht versioniert,
Pruefsummen vom Skript aus den Dateien gelesen):
- BSI-TR-03185.pdf, Version 1.1.1 vom 02.07.2026, SHA-256
  199c87754dec3eab884c18da6c3f6030e6fa7ced282f06e87fed7fe7841e8329
- CC2022PART3R1.pdf, CC:2022 Teil 3 Revision 1, SHA-256
  96d471dec3b1d79da2429dd71cbde379b31d6d866be8ae3e5b2b081d6846a5b8
- CC2022PART2R1.pdf, CC:2022 Teil 2 Revision 1, SHA-256
  16c853ad1ccf6eb10120726b15fe9ecfa95ac381f85d8edb84c12b0d0ecf1b01
  am 04.10.2026 vom CC-Portal geladen (Adresse in thesis.bib,
  cc2022teil2). Gelesen am 04.10.2026: Vorwort, Einleitung, Abschn. 1,
  6 und 7.1.1; frueher online: Inhaltsverzeichnis, Abschn. 1 bis 6.

Vorgemerkt fuer die Lueckenpruefung (3a): thesis.tex Z. 1456 bis 1457
sagt, das Qrisp-Team entscheide in Kapitel 6. Nach E2 (Form der
Evaluation) bewertet das Team erst nach der Abgabe.

Naechste Schritte in dieser Reihenfolge:
1. Paket G Teil 4 im neuen Chat ab Mo 05.10.2026: Schritt 4
   (Klassifikationsschema mit belegter Zuordnung der sechs Typwerte,
   endgueltige Definition von security_relevant am Raster), dann
   Schritt 5 (Pruefplan, vor der Pruefung committet), dann die
   Schritte 6 bis 9. Offen: Dependabot alle 28 oder nur die 25
   abgeschlossenen Beitraege; gemeinsame oder getrennte Stichprobe mit
   E2; Zeitplan zwischen Paket G und Paket H. Vor jedem Vorschlag
   prueft Claude STATUS.md und docs/entscheidungen.md auf bestehende
   Regeln.
2. Paket H: Bewertung, dazu die Zaehlung von M1 (Teil b im
   Pilotlauf) und M3 nach F3. M2 ist am 01.10.2026 gezaehlt, beide
   Pruefpunkte aus F3 sind beantwortet (Nachtrag zu F3 vom
   01.10.2026). Offen ist dort nur Angabe (i), Punkt 4 des Nachtrags;
   dafuer wird src/analyze/count_requirements.py erweitert.
3. Phase 2 der Literatursuche fuer Kapitel 3, verkleinert.
3a. Lueckenpruefung von thesis/thesis.tex nach der Regel in
   "Zusammenarbeit im Chat", nach Paket H, spaetestens vor dem
   12.10.2026.
4. Nicht blockierend: zehn Overfull hboxen in Anhang A
   (Korrekturdurchgang 12.10.), der Platzhalter zum Datenmodell in
   4.1.4 (das Datenmodell steht als E1, E6 und der Nachtrag zu E1
   fest) und zwei Platzhalter in Abschnitt 6.1.

## Getroffene Entscheidungen

Vollstaendig in docs/entscheidungen.md. Kurzfassung:

- Repository privat. Nach Abgabe umstellbar.
- R11 (07.09.2026): Skalenstufe 2 bemisst sich am Vorhandensein und
  an der Reichweite einer Regel, nicht an einem Wirksamkeitsnachweis.
- Zuordnung von 29148 Abschn. 5.2.4 auf drei Ebenen (07.09.2026);
  Ebene (c) wird nur an den Schluesselwoertern gemessen.
- D4a (07.09.2026): keine automatischen Tests fuer draw_sample.py.
  Stattdessen Wiederholungslauf am 08.09.2026, Ergebnis identisch.
- E2 (15.09.2026, mit dem Betreuer abgestimmt): Evaluation als
  Selbstbewertung des Verfassers an einer neuen, ueberschneidungs-
  freien Stichprobe, ergaenzt um einen Fundstellenvergleich mit den
  zwoelf Faellen aus Paket C. Bewertung durch Qrisp-Team und
  Betreuer erst nach der Abgabe. Die Abweichung vom Expose
  (Meilenstein M5 in Woche 9) ist abgestimmt, siehe Nachtrag zu E2.
- FF3: Dasselbe Modell als Werkzeug und Evaluationsgegenstand waere
  eine Bedrohung der Konstruktvaliditaet. Mit E8 (Modell von OpenAI)
  entfaellt sie, weil Claude nur Werkzeug ist.
- E1 (15.09.2026): Datenmodell der Ausgabe in drei Ebenen. Schema in
  config/requirement_schema_v1.json, abgeloest durch v2.
- E3 (15.09.2026): API-Budget hoechstens 150 Euro.
- E4 (15.09.2026): Modelleingabe ohne Programme und ohne offene
  Vorgaenge, 395 von 476. Entwuerfe, fehlende Beschreibung und
  fehlende Codeaenderung schliessen nicht aus, weil Titel und Diff
  auch dann eine Quelle bleiben.
  Programme ausgeschlossen, weil sie fast nur Versionen anheben oder
  nie uebernommen wurden (Nachtrag zu E4 vom 23.09.2026).
- E5 (15.09.2026): Budget der Modelleingabe. Diff-Ausschnitt je
  Review-Kommentar hoechstens 500 Zeichen, Quellblock hoechstens
  80 000 Zeichen, weil der Diff-Ausschnitt ueberwiegend Code
  wiederholt, der schon im Diff der Datei steht. D1 bleibt
  unveraendert. Keine Anmeldenamen im Block, nur author_association.
  Durch E9 praezisiert: das galt nur fuer die Kopfzeilen, im Text
  standen weiterhin Erwaehnungen.
- E6 (15.09.2026): Belegstaerke wird aus Deckung und Aussageform
  berechnet, Regeln B1 bis B9. Schema Version 2 laesst bis zu drei
  Belege je Anforderung zu.
- E7 (17.09.2026): Prompt Version 1 in zwei Dateien unter prompts/,
  englisch, modellneutral, ohne vollstaendiges Beispiel. Quellblock
  zwischen festen Begrenzungszeilen.
- E8 (19.09.2026): API-Modell ist gpt-5.6-terra. Pilot im
  Normalbetrieb, Volllauf im Stapelbetrieb. Kostenschaetzung in
  experiments/kostenschaetzung.md. Der Volllauf ist geaendert, siehe
  Nachtrag zu E8.
- E9 (19.09.2026): Erwaehnungen von Anmeldenamen werden im Fliesstext
  durch @person_NN ersetzt, nie im Diff. Ausnahmeliste jaspify, jax,
  pytest, rus. Zuordnung lokal in data/interim/mention_map.json.
- E10 (21.09.2026): Rahmen des Pilotlaufs A8. 20 Vorgaenge,
  Startwert 20260921, ohne die zwoelf Faelle aus Paket C. Die Regel
  fuer E11 (Denkaufwand) stand vor dem Lauf fest und nutzt nur
  maschinell messbare Werte, weil ein Qualitaetsurteil an 20 Faellen
  ohne Bewertungsbogen nicht belastbar waere.
- Nachtrag zu E10 (24.09.2026): Die Regel fuer die Ursache einer
  Ablehnung stand vor der Suche fest, weil sie sonst nach dem Ergebnis
  gewaehlt werden koennte. Massstab ist der Prompt. Das Pruefprogramm
  prueft seither genau nach den Zitatregeln des Prompts, weil es sonst
  nachsichtiger mass, als der Prompt verlangt.
- E11 (24.09.2026): Denkaufwand bleibt medium, keine Schemapruefung
  beim Anbieter, Prompt v2 fuer den Volllauf, keine Version 3. Weil die
  vorab festgelegten Regeln erfuellt sind und eine Hilfe beim Format den
  Messwert fuer die Formatkonformitaet (FF2) verfaelschen wuerde.
- Nachtrag zu E8 (24.09.2026): Volllauf im Normalbetrieb statt im
  Stapelbetrieb, Entscheidung des Verfassers. Weil der Stapelbetrieb
  in Nutzungsstufe 1 mindestens drei Stapel mit je bis zu 24 Stunden
  Frist und neuen Code gebraucht haette, und weil Pilot und Volllauf
  so denselben Aufrufweg nutzen. Hartes Limit 35 US-Dollar.
- Nachtrag zu C5 (17.09.2026): drei Sprachregeln aus 29148
  Abschn. 5.2.4 kommen zur Ebene (d) hinzu.
- Nachtrag zu E1 (17.09.2026): sechster Typwert human_factors.
- Nachtrag zu E6 (17.09.2026): complex braucht Vorbedingung und
  Ausloeser.
- Kapitel nicht in Einzeldateien. Alles in thesis/thesis.tex.
- BibTeX-Eintragstyp misc statt standard.
- API-Version 2022-11-28, explizit, in config/collect.toml.
- Speicherformat JSONL. Keine Datensaetze im Repository, Nachweis ueber
  SHA-256 im Manifest.
- Datenminimierung: vom user-Objekt nur login, weil nur er die
  Rueckverfolgbarkeit sichert. Personen erscheinen in der Arbeit als
  person_NN aus E9; A01 ff. und docs/pseudonyme.csv entfallen
  (Nachtrag zu E9 vom 21.09.2026).
- D1 dreistufige Kuerzung, erst in der Aufbereitung:
  Stufe 1 Typausschluss .ipynb, .drawio, .bkp, .svg und Dateien ohne
  patch-Feld; Dateiname, status, additions, deletions bleiben.
  Stufe 2 hoechstens 10000 Zeichen je Datei.
  Stufe 3 Budget 50000 Zeichen je Pull Request, unter Vorbehalt Paket E.
  Alle Werte in die Konfiguration, jede Kuerzung wird markiert.
  Ergaenzung 21.08.: Das Budget wird in der Lieferreihenfolge der API
  verbraucht. Die Schwaeche dieser Regel steht in Kapitel 7.
- D2 Bots markieren (author_is_bot), nicht loeschen. Regel: user.type
  gleich "Bot" ODER Login endet auf "[bot]".
- D3 eine Rohdatei je Endpunkt, Zusammenfuehrung erst in data/interim/.
  Jedes Manifest traegt source_dataset mit Pruefsumme.
- D4 pytest, Tests dort, wo ein Fehler still Daten verfaelscht:
  Wiederaufnahme, outcome, Normalisierung, JSONL-Ein- und Ausgabe.
  Kein Nachbau der API.
- D5 ein Datensatz je Pull Request, Kommentare und Dateien eingebettet.
- D6 Pull Requests ohne Beschreibung und ohne Codeaenderung bleiben
  enthalten und werden markiert. Reinigung entfernt nur vollstaendige
  Kommentarbloecke und wird nie auf Patch-Text angewandt.
- D7 praezisiert D2: Bots bleiben in data/interim/. Der Ausschluss
  erfolgt erst bei der Erzeugung der Modelleingabe, weil
  Dependabot-Beitraege fuer FF4 einschlaegig sein koennten.
- D8 ergaenzt D4 um einen fuenften Testbereich: die Kuerzungsstufen.
- Sprache: Programme unter src/ geben Meldungen und Berichte auf
  Englisch aus, einschliesslich der Berichtsdateinamen. docs/ und
  literatur/ bleiben deutsch.
- C1 Rekonstruierte Anforderungen werden auf Englisch formuliert. Die
  Arbeit bleibt deutsch. Damit entfaellt die deutsche
  Modalitaetskonvention.
- C2 Die Entscheidungsmatrix stuetzt sich auf Literatur plus eine
  Formulierungsprobe von Hand an zwoelf echten Pull Requests. Kein
  Sprachmodell trifft die Bewertung.
- C2a (04.09.2026) praezisiert C2: Bei den Literaturnoten darf das
  Modell Belegstellen und Notenvorschlaege liefern. Die Note vergibt
  der Verfasser nach Pruefung an der Quelle. An der Formulierungsprobe
  bleibt kein Sprachmodell beteiligt. Die Praezisierung gilt nur fuer
  Paket C; sonst gilt der Abschnitt "Zusammenarbeit im Chat".
- C3 Faellt die Wahl auf eine Kombination mehrerer Ebenen, gilt sie als
  ein festgelegtes Zielformat und wird vollstaendig spezifiziert.
- C4 Zehn Kriterien K1 bis K10, dreistufige ordinale Skala mit n. a.
  und ?, keine Gesamtsumme und keine Gewichte. Entscheidung ueber
  Rollen je Ebene mit Ausschlussregel E1.
- Quelltext und Arbeitsunterlagen werden mit abgegeben. docs/ und
  literatur/ muessen daher ohne Kenntnis der Projektanweisung
  verstaendlich sein.
- Erst Quelltext committen, dann abrufen oder aufbereiten.
- C5 (08.09.2026): Rollenzuweisung und Zielformat EARS+29148.
  Ebenen (b) und (d) verpflichtend, (a) und (c) nicht verwendet.
  Schluesselwortkonvention nach 29148 Abschn. 5.2.4; RFC 2119
  nicht uebernommen. Die Verbindlichkeit wird als Konvention
  gesetzt und nicht rekonstruiert. Ausschnitt der Ebene (d):
  5.2.7 vollstaendig, fuenf der neun Merkmale aus 5.2.5, drei
  Attribute aus 5.2.8.2. Rolleninformation ins Attribut Rationale.
- Weg C (09.09.2026, C6): Die Notentabelle steht in Kapitel 4, die
  Einzelbegruendungen kommen gekuerzt in Anhang A. Anhang A steht
  nach dem Literaturverzeichnis (10.09.2026). Kuerzungsregeln und
  Form eines Eintrags stehen in C6.
- K10 fuer Ebene (c) bleibt bei Note 1 (08.09.2026). Die Matrix
  soll nicht vom Ergebnis der Entscheidung abhaengen, die sie
  stuetzt. Der Vorbehalt ist durch einen datierten Nachtrag ersetzt.
- G1 (01.10.2026): Belegbegriff fuer die Gap-Analyse. Fuer FF4 gilt
  eine Anforderung als belegt, wenn die Belegstaerke aus den
  gefundenen Belegen allein direct oder indirect lautet. M2 bleibt
  unveraendert, weil seine Regel vor der Zaehlung feststand.
- Nachtrag zu F3 (01.10.2026): M2 in Paket G gezaehlt, beide
  Pruefpunkte beantwortet; die Zahlen stehen nur in der Ergebnisdatei.
- Literaturmatrix L07 am 01.10.2026 nach Abschnitt 2.1.7 berichtigt,
  weil bei diesem Widerspruch thesis.tex gilt (Wunsch des Verfassers).
- Option C fuer den Ausschnitt des Sicherheitsrasters (02.10.2026):
  Eintraege aus 29148 und TR-03185 Teil 2, Common Criteria als
  Ordnungsrahmen. Als G2 am 04.10.2026 mit Ae1 bis Ae3 freigegeben
  und committet.
- G3 (02.10.2026): Kategorie "nachweislich fehlende
  Sicherheitsfunktion" gestrichen, weil keine Code-, Test- oder
  Systempruefung zum Umfang gehoert. Schreibauftrag fuer 4.2 und
  Kapitel 7 in G3.

## LaTeX-Konventionen

Zitierschluessel in thesis.bib: iso29148, mavin2009ears, mavin2010bigears,
wilkinson2018mitigation, lucassen2016qus.
Zitierschluessel in online.bib: rfc2119, rfc8174.

Labels in thesis.tex (Stand 11.09.2026, vollstaendig):
cha:einleitung · cha:grundlagen · cha:verwandte-arbeiten · cha:konzeption ·
cha:implementierung · cha:evaluation · cha:diskussion · cha:fazit
sec:anforderungsqualitaet · sec:anforderungsformate · sec:llm-grundlagen ·
sec:cc-bsi · sec:ears (ist eine subsection, Praefix historisch)
subsec:re-begriffe · subsec:anforderungsaufbau · subsec:merkmale-einzeln ·
subsec:merkmale-menge · subsec:sprachkriterien ·
subsec:anforderungsattribute · subsec:rfc2119 · subsec:userstories
subsec:srs-inhalte (neu 23.08.2026)
tab:29148-srs-inhalte (Tabelle 2.1) · tab:ears-muster (2.2) ·
tab:qus-kriterien (2.3) · tab:aqusa (2.4)
Abschnitt 4.1 (seit 09.09.2026): sec:formatauswahl ·
subsec:auswahlverfahren · subsec:formulierungsprobe ·
subsec:bewertungsergebnis · subsec:rollenzuweisung ·
subsec:formatauswahl-grenzen · tab:kriterienkatalog ·
tab:schichtung · tab:deckung · tab:referenzinhalte ·
tab:entscheidungsmatrix
Anhang A (seit 11.09.2026): cha:anhang-einzelbegruendungen ·
sec:anhang-k1 bis sec:anhang-k5; Durchgang 2 fuegt sec:anhang-k6
bis sec:anhang-k10 an.
Abschnitt 4.2 (seit 01.10.2026): sec:konzeption-gap ·
subsec:belegbegriff-ff4
Abschnitt 6.2 (seit 02.10.2026): sec:eval-grundzahlen ·
subsec:grundzahlen-daten · subsec:grundzahlen-typen ·
subsec:grundzahlen-belege · tab:typverteilung · tab:belegstatus
Lange Dateinamen im Fliesstext mit \path{...} aus dem Paket url, weil
\texttt{...} nicht umbricht (02.10.2026).
Abschnitt 2.4 (seit 04.10.2026): sec:cc-bsi · subsec:common-criteria ·
subsec:tr03185 · subsec:cc-bsi-einordnung · tab:tr03185-bereiche
Abschnitt 4.2, neu seit 04.10.2026: subsec:sicherheitsraster ·
tab:sicherheitsraster-produkt · tab:sicherheitsraster-prozess ·
subsec:gap-kategorien
BibTeX-Schluessel seit 04.10.2026 in thesis.bib: cc2022teil2,
cc2022teil3, bsitr03185.
Seitenmasse laut thesis/preamble.tex: Textbreite 14 cm, Texthoehe
22 cm, Zeilenabstand 1,15. Tabellen prueft Claude in einem Nachbau mit
preamble.tex und hyphenations.tex, weil eine Ersatzumgebung eine zu
hohe Tabelle nicht erkannt hat (Befund 04.10.2026).

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
- (d) Qualitaets- und Sprachregeln: 29148 Abschn. 5.2.5-5.2.8,
  ergaenzt um die acht NL-Probleme aus Big EARS und die 13
  QUS-Kriterien

Ergebnis der vollstaendigen Entscheidungsmatrix, Stand 08.09.2026.
Die Noten je Zelle stehen in docs/formatauswahl.md Abschnitt 10 und
werden hier nicht wiederholt. Die Befunde in Kurzform:
- Ebene (d) erreicht bei K3, K7 und K10 die Note 2 und steht mit
  keiner anderen Ebene im Widerspruch. Sie ist ein Querschnitt, kein
  Konkurrent.
- Die Ebenen (a) und (b) schliessen einander im Satz aus. Nur eine
  von beiden kann die Satzform stellen.
- Ebene (c) erreicht bei K8 die Note 2. Ihre Zelle bei K10 haengt an
  der noch offenen Wahl zwischen RFC 2119 und den Schluesselwoertern
  aus 29148 Abschn. 5.2.4.
- K4 und K6 unterscheiden die Ebenen (a) und (b) nicht.
- K5 und K9 sind nicht unabhaengig, ebenso wenig K6 und K9. Alles
  drei ist in Abschnitt 7 der formatauswahl.md vermerkt.

Zur Norm:
- 29148 Abschn. 5.2.5 neun Merkmale einzelner Anforderungen, 5.2.6 fuenf
  Merkmale von Anforderungsmengen, 5.2.7 sprachliche Kriterien.
- Abschn. 5.2.7 laesst sich in maschinell pruefbare Regeln ueberfuehren.
- Abschn. 5.2.4 (NOTE 2) schliesst User Stories nicht aus.
- 29148 sieht shall vor und raet von must ab; RFC 2119 behandelt MUST und
  SHALL als gleichbedeutend. In der Matrix zu entscheiden.
- Schluesselwortkonvention nur fuer Englisch formuliert. Durch C1
  erledigt: die Anforderungen werden englisch formuliert.
- Abschn. 8.4 und 8.5 gelesen: Gliederungsvorlagen auf Dokumentebene,
  kein Satzmuster. 8.5 verweist fuer den Inhalt auf 9.6.
- Abschn. 9.6 gelesen und in Abschn. 2.1.7 eingearbeitet. 9.6.10
  Vorgaben je Anforderung, 9.6.11-9.6.18 Inhaltsbloecke, 9.6.18 c
  sechs Beispiele fuer Sicherheitsanforderungen, 9.6.19 Verifikation.
- Anhang C.1 gelesen: Anpassung schliesst volle Konformitaet aus.
- 9.6.3 bis 9.5 nicht gelesen, kein Bedarf erkennbar.

Zu RFC 2119 / 8174:
- Fuenf Verbindlichkeitsstufen; Abschn. 6 fordert sparsamen Gebrauch.
- RFC 8174: besondere Bedeutung nur bei durchgaengiger Grossschreibung.
- Risiko: Ein Sprachmodell wird dazu neigen, alles als MUST zu
  formulieren. Im Prompt-Entwurf zu adressieren, im Modellvergleich zu
  messen.

Zu EARS:
- Fuenf Muster: Ubiquitous, State-driven (WHILE), Event-driven (WHEN),
  Unwanted behaviour (IF-THEN), Optional feature (WHERE).
- EARS verwendet ausschliesslich shall, kennt keine Modalitaetsstufen.
- Zweistufiges Verfahren aus Big EARS ist Vorbild fuer das
  Prompt-Design in Kapitel 4.
- Schluesselwoerter und feste Klauselfolge erlauben regelbasierte
  Formatpruefung -> Vergleichsmass fuer FF3.
- Slotstruktur auf JSON-Schema abbildbar.
- Grenze: fuer hochrangige Stakeholder-Anforderungen entwickelt.
- Evidenz: Fallstudien in einem Unternehmen, Selbstbewertung der
  Autoren. Die 99-Prozent-Angabe darf nicht als Wirksamkeitsnachweis
  zitiert werden.

Zu User Stories:
- Vier Bestandteile im Begriffsmodell, drei Bestandteile des Konzepts.
  Ueber 80 syntaktische Varianten.
- QUS: 13 Kriterien, getrennt nach Einzelstory und Menge.
Formatentscheidung, Stand 09.09.2026 (Einzelheiten in C5):
- (a) nicht verwendet, (b) verpflichtend, (c) nicht verwendet,
  (d) verpflichtend im Ausschnitt.
- Zielformat EARS+29148: englischsprachiger EARS-Satz mit
  durchgehendem shall, geprueft gegen 29148 Abschn. 5.2.7 und
  fuenf Merkmale aus 5.2.5, mit den Pflichtfeldern Identification,
  Rationale und Type.
- Maschinell pruefbar sind Muster, Klauselreihenfolge, shall, das
  Fehlen anderer Modalverben und die Wortklassen aus 5.2.7. Die
  inhaltlichen Merkmale aus 5.2.5 sind es nicht.
- AQUSA erreicht mikro-gemittelt 93,8 Prozent Trefferquote bei 72,2
  Prozent Genauigkeit an 1023 Stories aus 18 Datensaetzen.
- Perfect Recall Condition: belegter Grundsatz fuer die Arbeitsteilung
  Mensch/Werkzeug.
- Kernproblem: Well-formed verlangt eine Rolle. PR-Daten sind
  entwicklerzentriert und nennen den Nutzniesser meist nicht.
  Durch die Erhebung gestuetzt: die Daten sind entwicklerzentriert.

Nicht belegbare Merkmale aus 29148: Notwendigkeit, Umsetzbarkeit und
Korrektheit. Eindeutigkeit, Einzelbezug, Nachweisbarkeit und
Vorlagenkonformitaet sind am Text pruefbar.

Aus der Erhebung fuer die Matrix nutzbar:
- labels traegt nichts bei (nur 7,6 %). Die Klassifikation muss aus
  Text und Code kommen.
- author_association unterscheidet nur CONTRIBUTOR und NONE. Keine
  Rollenzuordnung fuer User Stories ableitbar.
- 46,6 Prozent der Pull Requests haben keinen Kommentar. Die
  Begruendung einer Anforderung stammt bei ihnen allein aus Titel,
  Beschreibung und Diff.

Aus der Formulierungsprobe (Stand 30.08.2026, Commit ecf4a40):
- Eine explizite Verbindlichkeitsstufe fuer die jeweils
  rekonstruierte Anforderung kommt in keinem der zwoelf Faelle vor.
  Modalaussagen gibt es, sie betreffen aber das Vorgehen im Pull
  Request, eine andere Anforderung oder ein benachbartes Bauteil.
  Fuer FF2 heisst das: Die Modalitaet ist aus dieser Historie nicht
  belegbar und muesste beim Rekonstruieren gesetzt werden.
- Nach Regel E1 darf Ebene (c) damit nicht die Rolle
  "verpflichtend" erhalten. "optional" bleibt moeglich. Das ist in
  Schritt 5 zu entscheiden.
- Ohne R10 stuende Ebene (c) bei 4 von 12 und erhielte ebenfalls
  Note 0. Der frueher hier stehende Zusatz, die Regel veraendere nur
  die Zahl und nicht die Entscheidung, ist am 11.09.2026 berichtigt
  worden. Er zaehlt nur die vier Faelle nach der schriftlichen
  Festlegung von R10; PR 371 wurde schon am 27.08.2026 nach demselben
  Grundsatz geaendert. Ohne diesen Grundsatz insgesamt waeren 5 von
  12 gedeckt, die Note laege bei 1, und E1 wuerde Ebene (c) nicht
  mehr sperren. Die Regel bleibt unveraendert; die Empfindlichkeit
  gehoert nach Kapitel 7.
- Rollen sind seltener belegt als Systemverhalten. Ebene (a)
  scheitert meist am Rollenbestandteil.
- Das EARS-Muster Ubiquitous passt fuer die meisten Faelle; WHEN
  bei PR 622, WHILE bei PR 577.

Aus Teil B der Formulierungsprobe (Stand 02.09.2026, Commit a56bb5e):
- Beide bewerteten Ebenen koennen alle drei Anforderungsarten
  ausdruecken: funktional, leistungsbezogen, sicherheitsbezogen.
  Eine typabhaengige Schwaeche zeigt sich bei keiner von beiden.
- K6 ist fuer die Ebenen (c) und (d) nicht anwendbar. Beide geben
  keine Satzbestandteile vor: (c) regelt nur die Verbindlichkeit,
  (d) beurteilt eine bereits fertige Formulierung.
- Die User-Story-Saetze nennen das System nicht, weil sie im Passiv
  stehen. Die EARS-Saetze nennen es jedes Mal. Dieser Unterschied
  gehoert zu K1 und ist bei der Formatentscheidung zu beachten.

Folge fuer Schritt 5, aus E1 und den Messwerten:
- Ebene (a) und Ebene (c) haben bei K9 die Note 0. Nach E1 kann
  keine von beiden die Rolle "verpflichtend" erhalten; "optional"
  bleibt fuer beide moeglich.
- Ebene (d) ist nicht ausgeschlossen, weil K9 dort n. a. ist und
  n. a. nach R3 nie wie 0 wirkt.
- Fuer "verpflichtend" kommen damit nur die Ebenen (b) und (d) in
  Frage. Das steht vor Schritt 5 fest und ist keine Vorwegnahme der
  Entscheidung, sondern deren Rahmen.

## Zugangsdaten

- GitHub-Token qrisp-thesis-readonly, im Passwortmanager und in
  .env im Projektwurzelverzeichnis. Ablauf 2027-05-31.
- SSH-Schluessel ed25519 fuer das eigene Repository.
- Git-Identitaet: Omar Assad Salem, GitHub-Noreply-Adresse.

## Offene Punkte

Extern, mit Vorlauf:
- Umfangsfrage gegenueber dem Qrisp-Team. Stand am Ende von Paket E
  als Git-Tag thesis-v1.0 eingefroren (29.09.2026 statt wie geplant
  27.09.); alles Weitere in den Ausblick.
- Kriterienliste v1 (Skala, Regeln, Umfang der Auswahl) vor der
  ersten Bewertung, laut Zeitplan in W9 (Nachtrag zu E2 vom
  21.09.2026).
- Erledigt am 28.09.2026: Links fuer Teilschritt 10. GitHub hat je
  Kommentar einen eigenen Link geliefert; Variante B (Nachtrag zu E10
  vom 28.09.2026, Teil 4).
- Erledigt am 30.09.2026: Die Gegenpruefung entfaellt (F3), weil es
  keinen Weg ohne Mehraufwand gibt. Fuer Kapitel 7: Die Zuordnung nach
  Regel 3 stammt von einer Person. Bisheriger Stand:
  Gegenpruefung der Zuordnung nach Regel 3 durch Claude: angeboten
  am 28.09.2026. Der Verfasser wuenscht sie seit dem 30.09.2026, wenn
  sie keinen Mehraufwand macht. Sie braucht die Inhalte der 28 Zitate,
  die nach der Regel zu Inhalten nicht in den Chat gehen. Deshalb nur,
  wenn sich dafuer ein Weg ohne Mehraufwand findet. Sonst bleibt fuer
  Kapitel 7: eine Person ordnet zu.
- Commit d09a1df steht nicht in der Commit-Liste von Paket E; bei der
  Uebergabe am 24.09.2026 mit git log nachgetragen.
- Ab dem ersten Lauf darf die Zuordnung der Platzhalter nicht mehr
  neu vergeben werden (E9).
- Platzhalter fuer Personen in der Arbeit: person_NN aus E9, siehe
  Nachtrag zu E9 vom 21.09.2026. Offen ist nur die Regel fuer eine
  Person, die nicht in der Zuordnung steht.
- KI-Formulierung fuer vorspann.tex mit Professor abstimmen.
- Korreferent in thesis.tex eintragen (Platzhalter Zeile 23)
- Phase 2 der Literatursuche nachholen, verkleinert, bis Ende W9.
  Kapitel 3 hat sonst keine Materialgrundlage.
- Namenskonflikt: Schicht S5 in draw_sample.py spricht von "per pull
  request budget" und meint D1. Seit E5 gibt es ein zweites Budget
  mit demselben Wort. In Kapitel 5 trennen.

Inhaltlich offen:
- Ein Platzhalter in Abschnitt 4.1: Verweis auf den Abschnitt zum
  Datenmodell (4.1.4, faellt in Paket E). Der Verweis auf Anhang A
  in 4.1.3 ist am 11.09.2026 gesetzt.
- K9 Ebene (c) ist empfindlicher als bisher dokumentiert: ohne den
  Grundsatz von R10 waeren 5 von 12 Faellen gedeckt und die Note
  laege bei 1. Gehoert nach Kapitel 7, zusammen mit dem Umstand,
  dass die Noten der Ebenen (a) und (b) an je einem Fall haengen.
- Abschnitt 4.1.5 spricht von einem "Ausschnitt der Inhaltsvorgaben"
  von 29148. Der gewaehlte Ausschnitt stammt aber aus Abschn. 5.2,
  nicht aus den Inhaltsvorgaben in Abschn. 9. Formulierung pruefen.
- Abschn. 2.2.3 und Lesenotiz zu Mavin/Wilkinson 2010: Die Aussage,
  Bewertende und Umformulierende seien dieselbe Personengruppe,
  steht so nicht im Volltext. Belegt sind nur die Festlegung der
  Komplexitaetsschwelle durch die Autoren (Fussnote 3) und die
  Umformulierung durch eine fachuebergreifende Ingenieursgruppe
  (Abschnitt Method). Pruefen und gegebenenfalls abschwaechen.
- Platzhalter in thesis.tex Abschn. 2.2 veraltet: er kuendigt User
  Stories und EARS an, die inzwischen als 2.2.2 und 2.2.3
  geschrieben sind. Nur die Spezifikationsvorlagen aus 29148
  fehlen dort noch.
- Phase 2 der systematischen Literatursuche (S1, S2, S4), nach
  Schritt 4 von Paket C
- INVEST: Lucassen loest das S als Scalable auf. Gegen Wake 2003 pruefen.
- Titelvariante Mavin 2009 vereinheitlichen.
- docs/entscheidungen.md Z. 142 und 658 verweisen auf die
  Projektanweisung. Da das Repository mit abgegeben wird, durch eine
  inhaltliche Begruendung ersetzen - als datierte Praezisierung, nicht
  durch Aendern der gepushten Commits.
- Pruefen, ob in docs/findings_pull_details.md und
  findings_pull_files.md GitHub-Anmeldenamen stehen. Die Suche nach "@"
  fand nur docs/entscheidungen.md (zwei Bot-Namen, unproblematisch);
  ein Name ohne "@" wuerde so nicht gefunden.
- Wegweiser in README.md ergaenzen: welche Datei erklaert was und in
  welcher Reihenfolge sie zu lesen ist (Paket I).
- src/analyze/draw_sample.py: Tests nur fuer --sizes und --exclude
  (E10 a). Fuer das uebrige Skript die Ausnahme von D4 in Kapitel 5
  begruenden.
- PR 711: Rolle und Systemreaktion sind die einzigen zwei Felder der
  Stichprobe, die nicht unabhaengig gegengeprueft wurden. Die
  Diff-Ansicht war dem gegenpruefenden Modell nicht zugaenglich.
  Steht im Protokoll unter "Methodischer Status".
- Vier Datumsangaben in der Aenderungshistorie von
  docs/formatauswahl.md sind auf den 26.08.2026 geschaetzt
  (Pflichtbestandteile, K9 bei Ebene (d), Erhebungsform Teil A).
  Belegt ist nur "Begonnen: 26.08.2026" im Protokoll.

Aus Paket D in spaetere Pakete uebernommen:
- Erledigt: Budget der Stufe 3 bleibt (E5, D1 unveraendert).
  Auswahlregel festgelegt (E4).
- Messen, ob die 28 Dependabot-Beitraege sicherheitsbezogene Angaben
  enthalten (Paket G, FF4).
- Erledigt: Schemavalidierung mit 54 Tests (E6).

Technisch und redaktionell:
- Erledigt am 30.09.2026: Lokale Inferenz braucht kein eigenes
  Python. Ollama ist ein eigenes Programm; run_extraction.py sendet nur
  HTTP-Anfragen (F2).
- Erledigt am 01.10.2026: Auszug des Serverprotokolls vom 30.09.2026
  in docs/ollama_protokollauszug.md, mit Zeilennummern und SHA-256 der
  Protokolldatei (F3). Das vollstaendige Protokoll bleibt lokal unter
  ~/qrisp-ollama-logs/. Ein Protokoll des Probeaufrufs vom 29.09.2026
  liegt nicht vor; seine Werte aus F2 stehen gleichlautend im
  Protokoll vom 30.09.2026.
- Anfrage an /api/generate um 09:03:52 am 30.09.2026: Der Verfasser
  erinnert sich nicht sicher, nimmt aber an, dass keine Daten dieser
  Arbeit gesendet wurden. Gestuetzt wird das durch das Protokoll: Nur
  die Zeilen 335 und 1475 melden das Ende einer Verarbeitung (stop
  processing), beide gehoeren zu den gezaehlten Versuchen. Das ist
  eine Schlussfolgerung von Claude, keine Gewissheit. Fuer Kapitel 7
  als Restunsicherheit festhalten.
- Ollama-Dokumentation (L19 in der Literaturmatrix) hat Claude am
  30.09.2026 gelesen, der Verfasser noch nicht. Vor der Abgabe die
  Abschnitte Responses API und Setting the local context size selbst
  ansehen.
- tests/README.md nennt noch 373 Tests. Beim naechsten Code-Commit
  oder in Paket I auf den Stand der Testsuite nachziehen.
- Platzhalter in thesis.tex, Stand 04.10.2026, vom
  Aktualisierungsskript aus den Zeilen mit \textbf{[ gelesen:
  Z. 20: Noch zu ergaenzen: Abgabedatum
  Z. 23: Noch zu ergaenzen: Korreferent
  Z. 29: Noch zu ergaenzen: Abstract. Wird zuletzt geschrieben, wenn ...
  Z. 39: Noch zu ergaenzen: Motivation, Problemstellung, Zielsetzung, ...
  Z. 902: Zu pruefen: Primaerquelle Femmer et al.\ noch nicht gelesen; ...
  Z. 909: Noch zu ergaenzen
  Z. 1111: Noch zu ergaenzen: LLMs im Requirements Engineering, ...
  Z. 1119: Noch zu ergaenzen: Architektur, Datenmodell, Prompt-Design, ...
  Z. 1613: Noch zu ergaenzen: Verweis auf den Abschnitt zum ...
  Z. 1719: Noch zu ergaenzen: Klassifikationsschema.
  Z. 1734: Noch zu ergaenzen: Verweis auf den Abschnitt zum ...
  Z. 1746: Noch zu ergaenzen: Verweis auf den ...
  Z. 1753: Noch zu ergaenzen: Verweis auf den Abschnitt zur Pruefung ...
  Z. 2012: Noch zu ergaenzen: Regel fuer die Zuordnung der ...
  Z. 2059: Noch zu ergaenzen: GitHub-API, Aufbereitung, Extraktion, ...
  Z. 2066: Noch zu ergaenzen: Design, Durchfuehrung, Ergebnisse, ...
  Z. 2158: Noch zu ergaenzen: Verweis auf den Abschnitt zur lokalen ...
  Z. 2356: Noch zu ergaenzen: Verweis auf den Abschnitt mit den ...
  Z. 2433: Noch zu ergaenzen: Verweis auf den Abschnitt zur Pruefung ...
  Z. 2441: Noch zu ergaenzen: Verweis auf den Abschnitt zur ...
  Z. 2501: Noch zu ergaenzen: Verweis auf den Abschnitt mit den ...
  Z. 2552: Noch zu ergaenzen: Beantwortung der Forschungsfragen, ...
  Z. 2560: Noch zu ergaenzen
- Overfull hboxen, Behebung am 12.10.: Stand 04.10.2026 14
  Stueck, vom Aktualisierungsskript aus thesis/thesis.log gezaehlt.
  Die Liste mit Zeilennummern gibt nach einer Uebersetzung
  grep "Overfull" thesis/thesis.log aus. Zeilennummern stehen hier
  nicht mehr, weil sie sich mit jedem neuen Abschnitt verschieben.
  Darunter die Ueberschrift von Abschnitt 2.4; eine kuerzere
  Ueberschrift wuerde sie beheben.
- Schreibauftrag aus G3 fuer Kapitel 7 steht aus (4.2 erledigt am
  04.10.2026).
- CC:2022 Errata und Interpretationen Version 1.2 vom 15.10.2025
  (CC-Portal) nicht gelesen; in Kapitel 7 als Grenze nennen.
- Abschnitte 2.4.3 und 4.2.3 sagen, fuer Qrisp liege kein
  Schutzprofil, keine Sicherheitsvorgabe und keine dokumentierte
  Sammlung von Sicherheitsanforderungen vor. Das beruht auf Kenntnis
  des Verfassers und ist nicht am Repository geprueft.
- Die Beschreibung der Optionen A und B in 4.2.2 hat Claude aus
  STATUS.md abgeleitet (Kuerzel und Rueckfallregel); der Verfasser hat
  den Diff gelesen und nichts beanstandet.
- Literaturverzeichnis beginnt ohne Seitenumbruch unter dem Fazit und
  fehlt im Inhaltsverzeichnis (Befund 10.09.2026). Eine Behebung
  aendert die Vorlagenstruktur und braucht Abstimmung; Paket I.
- Demo-Dateien der Vorlage in thesis/figures/ vor Abgabe entfernen


## Arbeitsweise

- Vor jedem Python-Befehl: source .venv/bin/activate
- Skripte immer aus der Projektwurzel starten
  (python src/collect/<n>.py bzw. python src/prepare/<n>.py), sonst
  wird github_api nicht gefunden
- Tests: python -m pytest tests/ -v aus der Projektwurzel
- Erst Quelltext committen, dann abrufen oder aufbereiten. Dann stimmt
  collector_commit bzw. builder_commit im Manifest exakt.
- Vor dem vollen Lauf immer ein Probelauf mit --limit 5
- Probelaeufe erzeugen ein Manifest. Vor dem Commit loeschen, sonst
  landet ein Probelauf in der Historie.
- Nach Abbruch: denselben Befehl erneut ausfuehren. Die Abrufskripte
  lesen ihren Fortschritt aus der bereits geschriebenen Datei.
- --day <Datum> mitgeben, wenn in eine bestehende Datei
  weitergeschrieben werden soll
- build_interim.py schreibt nie in eine vorhandene Datei. Zum Neubau
  --overwrite mitgeben.
- Kompilieren: cd thesis && pdflatex thesis.tex && bibtex thesis1 &&
  bibtex thesis2 && pdflatex thesis.tex && pdflatex thesis.tex
  (nicht make all - braucht LibreOffice und ImageMagick)
- Commit-Ablauf: status -> diff -> gezieltes add -> diff --staged ->
  commit -> log -1 -> status -> push
- Kein git add . und kein git add ordner/
- Commit-Praefixe: lit:, bib:, tex:, code:, test:, docs:, chore:
- Bereits gepushte Commits werden nicht nachtraeglich geaendert.
- BibTeX-Felder mit Umlauten oder Backslashes in {...} setzen.
- Eigennamen im BibTeX-Titel in {...} setzen.
- requirements.txt nie von Hand bearbeiten: pip freeze > requirements.txt

## Konfiguration (config/collect.toml)

[source] owner eclipse-qrisp, repo Qrisp, repo_id 632066325
[api] base_url https://api.github.com, version 2022-11-28,
      per_page 100, state all
[fetch] timeout_seconds 30, pause_seconds 0.2, max_retries 5
[prepare] skip_patch_extensions .ipynb .drawio .bkp .svg,
      max_patch_chars_per_file 10000, max_patch_chars_per_pull 50000,
      truncation_marker "\n[... truncated ...]\n"

## Aufruf des Aufbereitungsskripts

python src/prepare/build_interim.py \
  --details data/raw/pull_details_2026-08-14.jsonl \
  --issue-comments data/raw/issue_comments_2026-08-19.jsonl \
  --review-comments data/raw/review_comments_2026-08-19.jsonl \
  --files data/raw/pull_files_2026-08-19.jsonl

Optional: --limit N (Probelauf), --day JJJJ-MM-TT, --overwrite

## Commits Paket D Teil 2

fe95a1a Detailabruf mit Wiederaufnahme
d26c682 Auswertung der Detaildaten, Befund, Entscheidungen D1-D4
c4f0dee Kommentarabruf fuer beide Endpunkte
a8d649b Manifeste des Kommentarabrufs und Befund zu den Abweichungen
44c669f Abruf der geaenderten Dateien und Diffs
336422d Dateiabruf ausgewertet, D1 endgueltig, Berichte auf Englisch

## Commits Paket D Teil 3

1c47a39 Kuerzungsparameter aus D1 in die Konfiguration
f7f8c52 build_interim.py und Testsuite (26 Tests)
d56feec Manifest des aufbereiteten Datensatzes vom 19.08.2026
c63f700 Kuerzungsstufen aus D1 getestet (12 weitere Tests)
acacebb KI-Protokoll fuer Paket D Teil 3
ea16a7c Entscheidungen D5 bis D8
1d83472 Zeilenumbruch am Dateiende in github_api.py,
        docs/ki-protokoll.md und tests/README.md. Achtung: Die
        Commit-Nachricht kuendigt zusaetzlich das Entfernen einer
        Leerzeile in github_api.py an. Das ist in diesem Commit nicht
        geschehen und wurde nachgeholt.
95175fb Leerzeile in github_api.py entfernt, Richtigstellung zu 1d83472

## Commits Paket C

9eb9052 Vorentscheidungen C1 bis C3 zur Formatauswahl
e78f491 29148 Abschn. 9.6 und Anhang C.1 in Notiz und Matrix
0a72cdf Abschnitt 2.1.7 Inhalte einer Software-Anforderungsspezifikation
9147cc0 Kriterienkatalog, Skala und Entscheidungsverfahren
6be91a8 Ziehungsskript und Stichprobe fuer die Formulierungsprobe
076c396 Regeln R9 und R10, Formulierungsprobe aufgenommen
ecf4a40 Gegenpruefung der Formulierungsprobe abgeschlossen
7ba386e Stand nach Abschluss von Paket C Schritt 4a
ecd907c K6 fuer die Ebenen (c) und (d) nicht anwendbar, Schritt 4c ergaenzt
bf3f137 Rahmen und drei Referenzinhalte fuer K6 festgelegt
98c3ca4 Datum der K6-Referenzinhalte auf 02.09.2026 korrigiert
a56bb5e Teil B neu aufgesetzt, K6 mit Note 2 fuer die Ebenen (a) und (b)
2951149 KI-Protokoll um Paket C Schritt 4a und 4b ergaenzt
cfe44ca Entscheidungen vor K2: R11, Zuordnung 29148 Abschn. 5.2.4, D4a
c062d92 Entscheidungsmatrix K2 vergeben, K6 und K9 uebertragen
c8b48b5 Entscheidungsmatrix K3 und K4 vergeben, Vorbehalt zu K4 in Abschnitt 7
b3367ae Quattrocchi 2026 und Paiva 2026 geprueft und aufgenommen
a2f3e48 Entscheidungsmatrix K5 vergeben, Vorbehalt zu K5 in Abschnitt 7
cb856ca Entscheidungsmatrix K7, K8 und K10 vergeben, Schritt 4c abgeschlossen
d63c549 Paket C Schritt 5, Formatentscheidung C5
20d4761 Abschnitt 4.1 Auswahl des Anforderungsformats
e2187b8 29148 Abschn. 5.2.7 bei K2 und K3 auf neun Aufzaehlungspunkte berichtigt
7db9ae1 Anhang A, Einzelbegruendungen K1 bis K5 (Durchgang 1)
7861f29 Anhang A, fehlende Zeile im Vorspann ergaenzt
a5a9339 Uebergabe Anhang A Durchgang 1, Entscheidung C6, KI-Protokoll
c73f63e Anhang A, Einzelbegruendungen K6 bis K10 (Durchgang 2)
9db8601 Verweis auf Anhang A in 4.1.3, zwei Berichtigungen zu EARS
feb68c6 Stand nach Abschluss von Paket C

## Commits Paket E

e0d3f66 Schema und Pruefung der strukturierten LLM-Ausgabe
d22b83b  Auswahl und Budget der Modelleingabe
cee3b7e Commit-Kuerzel aus Paket C in STATUS.md nachgetragen
b261e6f Belegstaerke wird berechnet statt behauptet
e091d7f Prompt Version 1 mit Ladeprogramm, Schema um human_factors ergaenzt
c1d53a4 14 Tests fuer die Prompt-Dateien
1a80c14 Entscheidung E7, Nachtraege zu C5, E1 und E6, KI-Protokoll
2df90fd Herkunftsangaben in E7 berichtigt
595f79f Erwaehnungen werden vor der Modelleingabe ersetzt
224dcda Manifest der Modelleingabe vom 19.09.2026
b8b9307 Entscheidungen E8 Modellwahl und E9 Ersetzung von Erwaehnungen
15cdcf1 Kostenschaetzung fuer die API-Laeufe nach E3
78122e6 Stand nach Abschluss von A6 und A7
fc31b3d STATUS.md berichtigt, Commit-Kuerzel aus Paket E nachgetragen
2ddc434 Entscheidung E10 Rahmen des Pilotlaufs, Nachtraege zu E2 und E9
b977a4f Bewertungskriterien v0 vor dem Pilotlauf festgelegt
1fa9dcf draw_sample.py um --sizes, --exclude und --title erweitert (E10)
b4b8407 Tests fuer --sizes und --exclude von draw_sample.py
c2a98e0 Pilotstichprobe A8 gezogen, Startwert 20260921
fb16642 Aufrufprogramm run_extraction.py mit Konfiguration api_run.toml (E10)
d858275 Nachtrag zu E10 (Recherche, Konto, Berichtigung) und zu E2 (Weg A)
c01f3ab Kosten mit Zuschlag fuer Cache-Schreibungen, angewandte Einstellungen im Manifest
f80a30a Kostenrechnung am echten Aufruf von Pull Request 64 geprueft
Hinweis: d858275 enthaelt zusaetzlich tests/test_run_extraction.py.
ababa14 docs: STATUS.md und KI-Protokoll nach Pilotlauf A8, Zeitplan fuer Abgabe 15.10., Lizenz-Fundstelle
9225339 docs: Manifest des Pilotlaufs 2026-09-22_pilot
d09a1df docs: Roter Faden, Kuerzel und Begruendung des Bot-Ausschlusses
5bd1499 docs: Nachtrag zu E10, Regel fuer die Ursache der Ablehnungen im Pilot
bb57a5c code: Diagnoseskript fuer abgelehnte Zitate mit 31 Tests (Nachtrag zu E10)
ec360b3 code: Pruefprogramm prueft Zitate nach den Regeln des Prompts, Diagnose angepasst (Nachtrag zu E10, Punkt 5)
1cb8849 code: Diagnose ordnet Zitate mit zwei Verstoessen der ersten verletzten Regel zu
863d045 docs: Nachtrag zu E10, Ergebnis der Ursachensuche und Regel fuer die Uebernahme von Prompt v2
8cdaaca code: Prompt Version 2 mit deutlicheren Regeln fuer Zitate aus Diffs, Konfiguration auf v2
ea9f0a4 docs: Manifest des Laufs 2026-09-24_pilot_v2 (Prompt v2)
0443533 docs: E11, Messwerte beider Pilotlaeufe und Hochrechnung fuer den Volllauf
7df8cda docs: STATUS.md und KI-Protokoll nach Abschluss von A8
da88bb6 docs: Nachtrag zu E8, Volllauf im Normalbetrieb statt im Stapelbetrieb
38dc3bb docs: Abrechnung des Laufs v2 berichtigt, Kontosumme 2,40 US-Dollar
f9eef00 docs: Liste aller 395 Vorgaenge fuer den Volllauf, volle Schichten aus draw_sample.py
8ee96a1 docs: Manifest des Volllaufs 2026-09-25_full_v2, 395 Vorgaenge
1ef4e7e docs: STATUS.md und KI-Protokoll nach Volllauf 2026-09-25_full_v2
a9eed1f docs: Nachtrag zu E10 Teil 1, Zuordnungsregel fuer edge_whitespace im Volllauf
6b379dc code: Ursache context_marker_kept im Suchprogramm, 13 Tests (Nachtrag zu E10 Teil 1)
b3cf18d code: Pruefprogramm duldet Rand-Leerraum ausser Kennzeichenrest, Tests (Nachtrag zu E10 Teil 1, Punkt 3)
8e277a6 docs: Nachtrag zu E10 Teil 2, Ergebnis Regel 1 im Volllauf
7c83268 docs: STATUS.md und KI-Protokoll nach Regel 1 im Volllauf
167f49b code: Anzeigeskript fuer Regel 3 und Aufschluesselung der Ablehnungen nach Art, 52 Tests
4742be8 docs: Nachtrag zu E10 Teil 3, Zuordnungsregel fuer Regel 3 im Volllauf
92a6803 code: Abschnitt 6.3 aus dem Manifest und Links je Beleg (Teilschritt 10), 36 Tests
8543bb9 docs: Nachtrag zu E10 Teil 3a, Auslegung von 1 b bis 1 d vor dem Ausfuellen
44c1162 docs: Abschluss Paket E, Nachtrag zu E10 Teil 4 (Regel 3), Zuordnungstabelle, Abschnitt 6.3, STATUS, KI-Protokoll, tests/README.md auf 373 Tests
Tag thesis-v1.0 auf 44c1162

## Commits Paket F

8237e56 code: Lokaler Aufrufweg ueber Ollama (Paket F): ohne Schluessel nur auf diesem Rechner, Kontextfenster vor dem ersten Aufruf geprueft, Laufzeitstand je Antwort im Manifest, 19 Tests; config/local_run.toml und Modelfile
bb5d8bb docs: F1 Umfang von FF3 nach dem Kontrollpunkt (Frist Mi 30.09.2026, 12:00 Uhr), F2 Ollama 0.34.4 und gpt-oss:20b; STATUS: Abschlusscommit und Tag thesis-v1.0 in der Commit-Liste von Paket E, Material der Unbelegtheitsrate berichtigt
767a381 docs: Nachtrag zu F1 Teil 1, Pilotfall mit gpt-oss nicht gelungen (Antwort endet mitten im JSON-Objekt), Lesart 1, Zuordnungsregel fuer den zweiten Versuch; Manifest des Laufs 2026-09-30_local_pilot_v2_r1
6a2ff11 code: Ersatzmodell qwen3.6:27b fuer den zweiten Versuch nach F1 c (Stoppgrund nicht entscheidbar), Modelfile mit Kontextfenster 65536 und config/local_run_qwen.toml
9fedc96 docs: Uebergabe Paket F Teil 1, Nachtrag zu F1 Teil 2 (Ursache nicht entscheidbar, qwen verfehlt das Format, F1 d mit Begruendung), STATUS mit Feingliederung fuer Kapitel 6 und Schreibregel, KI-Protokoll; Manifest des Laufs 2026-09-30_local_qwen_pilot_v2_r1
3bcf201 tex: Abschnitt 6.1 Kontrollpunkt und Pilotfall der lokalen Modelle (sec:eval-pilot-lokal) mit Tabellen tab:pilot-bedingungen und tab:pilot-ergebnisse; online.bib: Ollama-Dokumentation zur OpenAI-Kompatibilitaet; STATUS: Uebergabe-Commit von Paket F Teil 1 in Commits Paket F nachgetragen
4914543 docs: F3 Messgroessen fuer FF3 (M1 bis M6, Unbelegtheit auf Ebene der Anforderung nach B8), F1 d und F2 Begruendung 1 berichtigt, Protokollauszug Ollama vom 30.09.2026; tex: Abschnitt 6.1 mit Beleg aus ollama show, Kontextfenster fuer beide Modelle, Denkteil in der Ausgabezahl, Begruendung der Abweichung vom Expose
4e5f3f4 docs: Uebergabe Paket F Teil 2 und Abschluss Paket F (Abschnitt 6.1, F3 Messgroessen M1 bis M6), STATUS mit Rotem Faden, Kuerzeln, Arbeitsregel zum Abgleich vor Vorschlaegen und Commits 3bcf201 und 4914543, KI-Protokoll, Literaturmatrix L19

## Commits Paket G

24e803e docs: G1 Belegbegriff fuer die Gap-Analyse (FF4), vor der Zaehlung festgelegt: Belegstaerke nur aus gefundenen Belegen, M2 unveraendert
6822271 docs: STATUS mit Uebergabe-Commit 4e5f3f4, Regeln Schreiben im Paket und Lueckenpruefung, Schritt 3a; Literaturmatrix L07 nach Abschn. 2.1.7 berichtigt (29148 Abschn. 8.5.1)
c76feb1 tex: Abschnitt 4.2 Konzeption der Klassifikation und der Gap-Analyse (sec:konzeption-gap) mit Unterabschnitt Belegbegriff (subsec:belegbegriff-ff4) nach G1, vier markierte Platzhalter
af23216 code: Zaehlprogramm count_requirements.py fuer Typ, Sicherheitsbezug und Belegstatus nach F3 (M2) und G1, ohne eigene Pruefregeln, 22 Tests
45264f4 docs: Grundzahlen des Volllaufs nach F3 (M2) und G1 in experiments/requirement_counts_2026-09-25_full_v2.json, Nachtrag zu F3 (beide Pruefpunkte beantwortet, M2 in Paket G gezaehlt)
a0e211f tex: Abschnitt 6.2 Grundzahlen des Volllaufs (sec:eval-grundzahlen) mit Tabellen tab:typverteilung und tab:belegstatus, Zahlen aus experiments/requirement_counts_2026-09-25_full_v2.json, drei markierte Platzhalter
ead09fe tex: Abschnitt 6.2 ohne Overfull hboxen (Dateipfad mit path-Befehl aus dem Paket url, Spaltenbreiten in tab:typverteilung); docs: ueberzaehlige Leerzeile vor Offene Entscheidungen entfernt
4f302b3 docs: Uebergabe Paket G Teil 1 (Schritte 0 und 1): STATUS mit Rotem Faden, Kuerzel G1, Arbeitsplan Paket G, Commits Paket G, Testsuite, Platzhalter und Overfull-Stand aus den Quellen gelesen; KI-Protokoll
4c2a21e docs: G3 Kategorie nachweislich fehlende Sicherheitsfunktion gestrichen, mit Schreibauftrag; STATUS mit Entwurf G2 (Option C, Raster SR01 bis SR29), Rotem Faden, Kuerzeln und Uebergabe-Commit 4f302b3; Literaturmatrix L08 und L20; KI-Protokoll
b6bfd91 docs: G2 Ausschnitt des Sicherheitsrasters fuer FF4 (Option C), Aufnahmeregel und Raster SR01 bis SR29 mit Stufe und CC-Bezug, vor jeder Zuordnung festgelegt; Offene Entscheidungen nachgezogen
9e73b6c tex: Abschnitt 2.4 Common Criteria und BSI-orientierte Pruefungen (sec:cc-bsi) mit tab:tr03185-bereiche; Abschnitt 4.2 Unterabschnitte Raster (subsec:sicherheitsraster, tab:sicherheitsraster-produkt und -prozess) und Kategorien der Gap-Analyse (subsec:gap-kategorien) nach G2 und G3; bib: cc2022teil2, cc2022teil3, bsitr03185

## Aufruf des Ziehungsskripts

python src/analyze/draw_sample.py \
  --input data/interim/pulls_prepared_2026-08-19.jsonl

Optional: --output, --seed (Standard 20260823), --overwrite, seit E10
zusaetzlich --sizes, --exclude und --title. Ohne die drei neuen
Schalter unveraendertes Verhalten, am 22.09.2026 durch Wiederholung
der Ziehung vom 25.08.2026 geprueft.
Das Skript importiert nichts aus github_api.py und laeuft aus der
Projektwurzel. Ausgeschlossen werden Bot-Beitraege und Vorgaenge mit
outcome = open. Sechs Schichten S6 bis S1, von der seltensten zur
haeufigsten zugeordnet, jeder Datensatz nur einmal.

Lauf vom 25.08.2026: 476 gelesen, 31 Bots, 50 offen, 395 verbleibend.
Gezogen: 48, 75, 191, 371, 408, 413, 464, 533, 577, 622, 692, 711.
Lauf vom 22.09.2026 fuer den Pilot A8:
python src/analyze/draw_sample.py \
  --input data/interim/pulls_prepared_2026-08-19.jsonl \
  --output docs/sample_pilot_a8.md --seed 20260921 \
  --sizes S6=1,S5=4,S4=3,S3=3,S2=4,S1=5 \
  --exclude 48,75,191,371,408,413,464,533,577,622,692,711 \
  --title "Pilot sample for step A8 (FF1)"
Gezogen: siehe docs/sample_pilot_a8.md. Die Evaluationsstichprobe nach
E2 schliesst diese 20 und die zwoelf aus Paket C aus.

## Aufruf des Extraktionsprogramms

python src/extract/run_extraction.py --sample docs/sample_pilot_a8.md \
  --run-id 2026-09-22_pilot [--dry-run] [--limit N]

Aus der Projektwurzel. Einstellungen in config/api_run.toml, Schluessel
OPENAI_API_KEY in .env. --dry-run sendet nichts und schreibt nichts.
--limit 0 berechnet Extraktionsdatei und Manifest nur aus der Rohdatei
neu. Ein erneuter Aufruf mit derselben Kennung setzt fort und sendet
nichts doppelt. Der echte Lauf verweigert sich bei nicht committeten
Aenderungen unter src/, config/ und prompts/. Bei langen Laeufen
caffeinate -i davorsetzen; den Deckel nicht schliessen.

Pruefung der Ausgabe:
python src/extract/validate_output.py \
  --input data/processed/extraction_<Kennung>.jsonl \
  --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
  --mentions-map data/interim/mention_map.json \
  --allowlist "jaspify,jax,pytest,rus"
Ohne --allowlist werden Zitate mit @jax und Aehnlichem faelschlich
abgelehnt.

Die Prompt-Version kommt aus config/api_run.toml, seit dem 24.09.2026
v2. Laeufe bisher: 2026-09-22_pilot (v1), 2026-09-24_pilot_v2 (v2),
2026-09-25_full_v2 (v2, Volllauf, Liste docs/sample_full_run_e.md).

Lokale Laeufe (Paket F, F2): zuerst den Server in einem eigenen
Fenster starten,
  mkdir -p ~/qrisp-ollama-logs
  OLLAMA_NO_CLOUD=1 OLLAMA_NUM_PARALLEL=1 ollama serve 2>&1 | tee -a ~/qrisp-ollama-logs/serve_$(date +%F).log
dann run_extraction.py mit --config config/local_run.toml (gpt-oss)
oder --config config/local_run_qwen.toml (qwen). Kein Schluessel; das
Programm fragt vor dem ersten Aufruf Version und Kontextfenster ab und
sendet nichts, wenn das Fenster nicht 65 536 ist. Laeufe:
2026-09-30_local_pilot_v2_r1 (gpt-oss) und
2026-09-30_local_qwen_pilot_v2_r1 (qwen), beide nur PR 64 mit
--limit 1, nicht fortgesetzt (F1 d).

Ursachensuche fuer abgelehnte Zitate, gibt keine Inhalte aus:
python src/extract/diagnose_excerpts.py \
  --input data/processed/extraction_<Kennung>.jsonl \
  --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
  --model-input data/processed/model_input_2026-09-19.jsonl \
  --mentions-map data/interim/mention_map.json \
  --allowlist "jaspify,jax,pytest,rus"

## Zeitplan

W1 03.-09.08. Setup, Literaturstart                    erledigt
W2 10.-16.08. Python, JSON/REST, erster GitHub-Abruf   erledigt
W3 17.-23.08. Extraktion, Formatauswahl                Paket D
                                                       erledigt 21.08.
W4 24.-30.08. LLM-Extraktion mit API-Modell
W5 31.08.-06.09. Prompt-Iteration, lokales Modell
W6 07.-13.09. Modellvergleich (Kontrollpunkt lokales Modell)
              tatsaechlich: Paket C abgeschlossen am 11.09.
              Kontrollpunkt und Modellvergleich verschoben
W7 14.-20.09. Paket E: Entscheidungen E1 bis E6 am 15.09. erledigt.
              Rest der Woche: Prompt v1, API-Budget, Modellrecherche
Plan ab 23.09.2026, neu aufgestellt wegen des Abgabetermins 15.10.2026.
Er ersetzt den Plan vom 15.09.2026 ab W8. Geschrieben wird ab sofort
parallel, nicht am Ende.

W8 21.-27.09. Paket E: A8 abgeschlossen Do 24.09., ausser den Links
              (Teilschritt 10, nach dem Volllauf).
              Fr 25.09. Stapelbetrieb umsetzen, danach Volllauf.
              tatsaechlich: kein Stapelbetrieb (Nachtrag zu E8),
              Volllauf am 25. und 26.09. erledigt.
              Paket F: lokales Modell einrichten ab Fr 25.09.
              (verschoben von Do 24.09., weil A8 den Tag brauchte)
              tatsaechlich: Paket F nach Paket E, ab Di 29.09.
              Git-Tag thesis-v1.0 am So 27.09.
              tatsaechlich: am Di 29.09., am Ende von Paket E.
              Schreiben: Kapitel 4 Rest (4.1.4 Datenmodell)
              tatsaechlich: So 27. und Mo 28.09. Pruefung nach
              Regel 1 abgeschlossen (Nachtrag zu E10 vom 27.09.).
W9 28.09.-04.10. Paket F: Laeufe des lokalen Modells an derselben
              Stichprobe, Modellvergleich FF3 bis Mi 30.09.
              tatsaechlich: Kontrollpunkt am 29. und 30.09., F1 d,
              keine Laeufe ueber die Stichprobe.
              Paket G: Klassifikation, Sicherheitsraster,
              Gap-Analyse FF4 von Do 01.10. bis So 04.10.
              Kriterienliste v1, Evaluationsstichprobe ziehen.
              Literatursuche Phase 2, verkleinert.
              Schreiben: Kapitel 5 Implementierung
              tatsaechlich: Paket G Schritte 1 bis 3 und
              Abschnitte 2.4 und 4.2 bis So 04.10.; Schritte 4 bis 9
              offen.
W10 05.-11.10. Paket H: Bewertung nach Weg A Mo 05. und Di 06.10.,
              Auswertung Mi 07.10.
              Schreiben: Kapitel 6, Kapitel 3, Kapitel 7, 8 und 1
W11 12.-15.10. Mo 12.10. Korrekturdurchgang
              Di 13.10. Endkontrolle, interne Abgabe
              Mi 14.10. Puffer
              Do 15.10. Abgabe

Ueberholt am 23.09.2026, nur zur Planungsgeschichte:
Stand 11.09.2026, W6. Paket D war drei Tage vor Plan fertig. Paket C
lief vom 23.08. bis zum 11.09.2026 und ist abgeschlossen: Schritte 1
bis 6, Anhang A mit beiden Durchgaengen, der Verweis in 4.1.3 und
die Ueberschrift von Abschnitt 10 in docs/formatauswahl.md. Paket E
hat noch nicht begonnen und liegt rund zwei Wochen hinter dem Plan
fuer W4. Der Kontrollpunkt fuer das lokale Modell in W6 ist nicht zu
halten. Bis zur internen Abgabe am 30.10.2026 verbleiben sieben
Wochen; verbindlicher Abgabetermin ist der 01.11.2026.

Stand 23.09.2026, W8. A8 bis einschliesslich Pilotlauf erledigt. Offen
in Paket E: Teilschritte 9 bis 12, danach Volllauf. Der Abgabetermin
ist auf den 15.10.2026 vorgezogen. Bis zur internen Abgabe am
13.10.2026 verbleiben 20 Tage, bis zur Abgabe 22 Tage. Der Plan hat
keine Reserve ausser dem 14.10.; jede Verzoegerung verschiebt das
Schreiben.

Stand 02.10.2026, W9. Paket G, Schritte 0 und 1 erledigt: G1,
Grundzahlen, Abschnitte 4.2 und 6.2. Offen in Paket G: Schritte 2 bis
9 bis So 04.10. Kriterienliste v1 auf Mo 05.10. verschoben,
Literatursuche Phase 2 und Kapitel 5 aus W9 heraus (Verfasser
einverstanden am 01.10.2026). Bis zur internen Abgabe am 13.10.2026
verbleiben 11 Tage, bis zur Abgabe 13 Tage.

Stand 01.10.2026, W9. Paket F abgeschlossen: Abschnitt 6.1
geschrieben, Messgroessen F3 festgelegt. Paket G beginnt heute wie
geplant. Bis zur internen Abgabe am 13.10.2026 verbleiben 12 Tage,
bis zur Abgabe 14 Tage.

Stand 30.09.2026, W9. Kontrollpunkt entschieden, es gilt F1 d. Die
Laeufe des lokalen Modells ueber die Stichprobe entfallen. Paket F
endet mit dem Abschnitt zum Pilotfall in Kapitel 6 und den
Messgroessen fuer FF3, danach Paket G ab Do 01.10. Bis zur internen
Abgabe am 13.10.2026 verbleiben 13 Tage, bis zur Abgabe 15 Tage.

Stand 29.09.2026, W9. Paket E abgeschlossen, die Pruefung des
Volllaufs ist endgueltig. Paket F beginnt heute, nach Paket E statt
parallel. Der Modellvergleich war bis Mi 30.09. geplant und ist damit
knapp. Bis zur internen Abgabe am 13.10.2026 verbleiben 14 Tage, bis
zur Abgabe 16 Tage.

Stand 26.09.2026, W8. Volllauf erledigt, Manifest committet. Offen in
Paket E: Regel 1 und Regel 3 der Ursachensuche, Aufschluesselung der
Ablehnungen, Abschnitt 6.3 der Kostenschaetzung, Links. Bis zur
internen Abgabe am 13.10.2026 verbleiben 17 Tage, bis zur Abgabe 19
Tage.

Stand 24.09.2026, W8. A8 abgeschlossen bis auf die Links. Paket F
beginnt einen Tag spaeter als geplant; der Kontrollpunkt Di 29.09.
bleibt. Bis zur internen Abgabe am 13.10.2026 verbleiben 19 Tage, bis
zur Abgabe 21 Tage.

Drei Risiken, in dieser Reihenfolge:
1. Erledigt am 30.09.2026: Lokales Modell (Paket F). Der
   Kontrollpunkt ist entschieden, es gilt F1 d, FF3 ohne
   Qualitaetsmessung eines lokalen Modells. Python 3.14 war kein
   Hindernis.
2. Umfang. Pakete F, G und H liegen in zweieinhalb Wochen. Jede
   Kuerzung muss alle vier FF beantwortbar lassen und wird mit dem
   Betreuer abgestimmt. Kapitel 3 und Phase 2 der Literatursuche
   laufen verkleinert.
3. Bewertungsbogen fuer E2. Kriterienliste v0 steht seit dem
   21.09.2026, vor dem Pilot. Skala, Regeln und Umfang der Auswahl
   (Fassung v1) muessen vor der ersten Bewertung fertig sein
   (Nachtrag zu E2 vom 21.09.2026).