# Lesenotiz: RFC 2119 (und RFC 8174)

Kurzangabe: Scott Bradner, Key words for use in RFCs to Indicate
Requirement Levels, RFC 2119, BCP 14, IETF, Maerz 1997.
Ergaenzend: Barry Leiba, Ambiguity of Uppercase vs Lowercase in
RFC 2119 Key Words, RFC 8174, BCP 14, IETF, Mai 2017.
Quellentyp: Standard (Best Current Practice), frei verfuegbar
Matrix-ID: L06 und L11
Umfang: RFC 2119 drei Seiten, vollstaendig gelesen
Datum: 06.08.2026
Status: eingearbeitet in Abschnitt 2.2.1

## Fragestellung

Welche Verbindlichkeitsstufen definiert RFC 2119, und eignet sich die
Konvention fuer automatisiert erzeugte Anforderungen? (FF2)

## Inhalt der Quelle

RFC 2119 definiert fuenf Verbindlichkeitsstufen:
- MUST, REQUIRED, SHALL: unbedingte Anforderung
- MUST NOT, SHALL NOT: unbedingtes Verbot
- SHOULD, RECOMMENDED: Abweichung nur nach Abwaegung der Folgen
- SHOULD NOT, NOT RECOMMENDED: in Einzelfaellen vertretbar
- MAY, OPTIONAL: echte Wahlfreiheit

Abschnitt 6 fordert einen sparsamen Gebrauch: Die Ausdruecke sollen
nur dort verwendet werden, wo sie fuer die Zusammenarbeit von
Implementierungen erforderlich sind oder schaedliches Verhalten
begrenzen, nicht um eine bestimmte Umsetzungsmethode vorzuschreiben.

RFC 8174 stellt klar, dass die Schluesselwoerter die beschriebene
Bedeutung ausschliesslich in durchgaengiger Grossschreibung tragen.
Klein geschrieben gelten sie als gewoehnliche englische Woerter.
Ferner: Normativer Text muss die Schluesselwoerter nicht zwingend
verwenden, um normativ zu sein.

## Meine Einordnung

RFC 2119 ist kein Anforderungsformat, sondern eine reine
Modalitaetskonvention. Es sagt nichts ueber den Satzbau einer
Anforderung. In der Vieranalyse der Projektanweisung betrifft es
Ebene (c), nicht (a) oder (b). Es ist daher mit EARS oder User
Stories kombinierbar und keine Alternative dazu.

Die Einhaltung ist maschinell gut pruefbar: geschlossenes Vokabular,
durch die Grossschreibungsregel zusaetzlich eindeutig abgegrenzt.

Risiko fuer die Pipeline: Ein Sprachmodell wird dazu neigen, alles als
MUST zu formulieren. Das widerspricht der Sparsamkeitsregel. Diese
Uebergeneralisierung ist im Prompt-Entwurf zu adressieren und im
Modellvergleich zu messen.

## Offene Punkte

- Konflikt zu 29148: dort ist shall vorgesehen und von must
  abgeraten; RFC 2119 setzt beide gleich. Nicht gleichzeitig
  anwendbar. In der Entscheidungsmatrix zu klaeren.
- Die Konvention ist fuer englischsprachige Spezifikationen gedacht.
  Fuer deutschsprachige Anforderungen ist eine Entsprechung
  festzulegen oder englisch zu formulieren.
- Wer RFC 2119 heute zitiert, ohne RFC 8174 zu nennen, zitiert einen
  ueberholten Stand.

## Verwendung in der Arbeit

Kapitel 2, Abschnitt 2.2.1 (Normative Schluesselwoerter).
Spaeter: Entscheidungsmatrix in Kapitel 4, Formatvalidierung in
Kapitel 5.
