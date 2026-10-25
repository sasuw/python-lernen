# Übungen für die Grundlagen

Hier gibt es kleine Aufgaben zum Selberlösen. Die eigenen `.py`-Dateien kommen
in diesen Ordner, zum Beispiel `01_steckbrief.py`. Ein Beispiel darf als Vorlage
dienen; fertige Lösungen sind keine Voraussetzung für die nächste Lerneinheit.

## 1. Ein erfundener Steckbrief

**Ziel:** Drei Zeilen beschreiben eine erfundene Spielfigur: Name, Superkraft und
Lieblingsessen. Es sind keine echten persönlichen Daten nötig.

**Tipp:** Das [Hallo-Beispiel](../beispiele/01_hallo.py) zeigt `print()`.

**Prüfen:** Jede Angabe erscheint in einer eigenen Zeile. Nach einer Textänderung
erscheint beim nächsten Start der neue Text.

## 2. Zwei Fragen

**Ziel:** Das Programm fragt nach einem Spitznamen und einem Lieblingsspiel.
Danach erscheint ein Satz mit beiden Antworten.

**Tipp:** Für jede Antwort eine eigene Variable verwenden.

**Prüfen:** Zwei Durchläufe mit verschiedenen Antworten ergeben passende Sätze.

## 3. Ein Minutenrechner

**Ziel:** Das Programm fragt nach einer ganzen Zahl von Stunden und gibt die
zugehörige Anzahl Minuten aus.

**Tipp:** `input()` liefert Text. `int()` macht daraus eine ganze Zahl.

**Prüfen:** `2` ergibt `120` Minuten; `0` ergibt `0` Minuten. Was passiert bei
`abc`? Die [Fehlerhilfe](../docs/nachschlagen/fehlerhilfe.md) erklärt die Meldung.

## 4. Zahlenraten umbauen

**Ziel:** Eine Kopie des [Ratespiels](../beispiele/03_zahlenraten.py) verwendet
Zahlen von 1 bis 100. Der Text nennt denselben Bereich.

**Tipp:** Erst den Bereich und die Ansage ändern. Als weitere Herausforderung
höchstens sieben Versuche erlauben, mit einer Meldung nach einer verlorenen Runde.

**Prüfen:** Hinweise für zu kleine und zu große Tipps ausprobieren. Die
Versuchszahl muss auch beim erfolgreichen Tipp stimmen.

## 5. Ein Quiz

**Ziel:** Drei Fragen stellen und für jede richtige Antwort einen Punkt zählen.
Am Ende erscheint die Punktzahl von 0 bis 3.

**Tipp:** Mit `punkte = 0` beginnen. `if` vergleicht jede Antwort mit der Lösung.
Zunächst ohne Schleife arbeiten; feste Fragen reichen.

**Prüfen:** Ein Durchlauf mit nur richtigen und einer mit nur falschen Antworten
ergibt jeweils die passende Punktzahl.

## 6. Ein Bild verändern

**Ziel:** Aus dem [Quadrat](../beispiele/04_zeichnen.py) wird ein Dreieck.
Danach eine andere Farbe ausprobieren.

**Tipp:** Drei Seiten, jeweils 120 Grad Drehung. `stift.color("blue")` färbt den
Stift blau. Die Änderung gehört vor die Schleife.

**Prüfen:** Die Form ist geschlossen und hat drei Seiten. Das Fenster lässt
sich schließen. Weitere Ideen stehen bei den [Projekten](../projekte/README.md).
