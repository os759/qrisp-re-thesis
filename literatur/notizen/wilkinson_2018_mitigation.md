# Wilkinson & Mavin 2018: Deriving Mitigation Requirements with EARS

BibTeX-Key: wilkinson2018mitigation
Quellentyp: Workshopbeitrag (1st International Workshop on EARS, IEEE)
Gelesen am: 06.08.2026
Status: gelesen
Bezug zu: FF4 (nachrangig), FF2 (Randnotiz)
Volltext liegt: literatur/volltexte/ (lizenzpflichtig, nicht im Repo)

## 1 Was die Quelle sagt

- Vollstaendige Anforderungssaetze muessen abweichendes Verhalten
  abfangen; Abweichungsanalysen setzen ueblicherweise am
  Systementwurf an, nicht an den Anforderungen (Abschn. I)
- Folge: Verlagerung der Analyse an Sicherheits- und
  Zuverlaessigkeitsingenieure und zeitliche Verzoegerung (Abschn. I)
- Vorschlag: jede Klausel einer EARS-Anforderung ausser dem
  Systemnamen wird auf Abweichungen untersucht (Abschn. III)
- Elf HAZOP-Leitwoerter erzeugten zu viele irrelevante Abweichungen;
  stattdessen begrenzter Verbsatz (Abschn. III)
- Tabelle I: Vorbedingung, Ausloeser, Systemreaktion, vorgelagerter
  und nachgelagerter Akteur, je mit Abweichungsklassen
- Abschn. IV: durchgerechnetes Beispiel, aus dem zusaetzliche
  EARS-Anforderungen abgeleitet werden (u. a. Zeitschranke,
  Warnmeldung bei ausbleibender Reaktion)
- Grenzen: ersetzt nicht die Pruefung des Systementwurfs; bisher
  wenige Ingenieure, wenige Fallstudien; Akteursdimension in der
  untersuchten Domaene wenig ergiebig (Abschn. V, VI)

## 2 Kernbegriffe und Definitionen

| Begriff | Definition laut Quelle | Fundstelle |
|---|---|---|
| Deviation | unbeabsichtigtes Verhalten ohne Nutzen fuer den Kunden oder mit Nachteil fuer ihn | Abschn. I |

## 3 Woertliche Zitate

Keine.

## 4 Art der Evidenz

Erfahrungsbericht mit einem durchgerechneten Beispiel. Keine Metriken,
keine Vergleichsgruppe. Zwei Seiten Umfang.

## 5 Meine Einordnung

- Behandelt safety (Betriebssicherheit), nicht security. FF4 zielt auf
  security nach BSI und Common Criteria. Diese Unterscheidung muss im
  Text ausdruecklich gemacht werden.
- Verwendung: eine Randbemerkung in 2.2.2, ausfuehrlicher erst bei der
  Konzeption des Sicherheitsrasters (Paket G)
- Als Fundament fuer FF4 nicht tragfaehig

## 6 Meine Schlussfolgerungen

- Der methodische Kern - systematische Ableitung von
  Zusatzanforderungen aus der Klauselstruktur - ist ein Vorbild fuer
  ein Gap-Analyse-Raster, unabhaengig von der safety-Ausrichtung
- Die Bruecke zum Security-Denken laeuft ueber den Misuse-Case-Verweis
  in Mavin et al. 2009, nicht ueber diese Quelle selbst

## 7 Einschraenkungen und Kritik

- Sehr geringer Umfang, keine quantitative Auswertung
- Domaenenspezifisch (Triebwerksregelung)
- Wirksamkeit im groesseren Massstab nach eigener Angabe offen

## 8 Offene Punkte und zu pruefen

- [ ] Klaeren, ob diese Quelle im Endtext ueberhaupt gebraucht wird
      oder nur als Beleg fuer die Erweiterbarkeit von EARS dient

## 9 Anschlussliteratur

Rueckwaerts: ARP 4754A, ARP 4761 (Luftfahrtnormen, fuer diese Arbeit
nicht relevant)
Vorwaerts: uebrige Beitraege des EARS-Workshops 2018
