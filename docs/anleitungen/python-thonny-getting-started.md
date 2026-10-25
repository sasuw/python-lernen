# Erste Schritte mit Python und Thonny

Mit dieser Anleitung entstehen auf einem Windows-PC die ersten Python-Programme
und später ein kleines Ratespiel. Programmiererfahrung ist nicht nötig.

**Benötigt:** Ein PC mit Windows 10 oder 11, eine Internetverbindung für den
Download und etwa 30–45 Minuten für den ersten Abschnitt. Danach funktionieren
die Beispiele auch ohne Internet. Für den ersten Tag reichen die Schritte 1–4;
Ratespiel und Zeichnen können auf weitere Tage verteilt werden.

Die Codebeispiele liegen auch fertig im Ordner [beispiele/](../../beispiele/README.md).
Selber abtippen hilft beim Lernen; bei einem Fehler ist Vergleichen erlaubt.
Der [Lernplan](../lernplan.md) enthält Hinweise für eine erwachsene Begleitperson.

## 1. Thonny und Python installieren

**Python** ist die Programmiersprache. **Thonny** ist das Programm zum Schreiben
und Starten von Python-Code. Im normalen Windows-Installer von Thonny ist Python
schon enthalten. Eine zusätzliche Python-Installation ist nicht nötig.

1. Im Browser die offizielle Webseite [thonny.org](https://thonny.org/) öffnen.
2. Unter **Official downloads for Windows** den `.exe`-Installer für **Intel
   oder AMD** auswählen. Bei einem PC mit ARM-/Snapdragon-Prozessor stattdessen
   den **Arm**-Installer nehmen. Der Prozessortyp steht in Windows unter
   **Einstellungen → System → Info**.
3. Die heruntergeladene Datei öffnen. Falls Windows eine Bestätigung verlangt,
   zunächst prüfen, dass es sich um den Download von der offiziellen Webseite
   handelt. Bei Unsicherheit hilft eine erwachsene Begleitperson.
4. Den Installationsschritten folgen. Die Installation nur für das aktuelle
   Benutzerkonto (**me only**) reicht normalerweise; die Voreinstellungen passen.
5. **Thonny** über das Windows-Startmenü öffnen.

**Geschafft, wenn:** Thonny geöffnet ist. Oben ist Platz für Code, unten steht
die **Kommandozeile** (englisch: **Shell**). Im weiteren Text heißt sie kurz Shell.
Fehlt dieser Bereich, im Menü **Ansicht → Kommandozeile** nachsehen; bei
englischer Oberfläche **View → Shell**. Menütexte können etwas abweichen.

## 2. Die Oberfläche kennenlernen

Thonny hat zwei wichtige Bereiche:

| Bereich                | Wozu er da ist                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Editor**, meist oben | Hier entsteht ein Programm, das als `.py`-Datei gespeichert wird.                          |
| **Shell**, meist unten | Hier erscheinen Ausgaben, hier werden Fragen beantwortet und einzelne Befehle ausprobiert. |

Die wichtigsten Tastenkürzel unter Windows:

| Aktion                                         | Tastenkürzel                   |
| ---------------------------------------------- | ------------------------------ |
| Neue Datei                                     | `Strg+N`                       |
| Datei öffnen                                   | `Strg+O`                       |
| Speichern                                      | `Strg+S`                       |
| Aktuelles Programm starten                     | `F5` oder der grüne Startknopf |
| Schrittweise starten                           | `Strg+F5`                      |
| Beim Debuggen einen großen Schritt weitergehen | `F6`                           |

`Strg` heißt auf manchen Tastaturen `Ctrl`. Bei manchen Laptops ist zusätzlich
die Taste **Fn** nötig, etwa **Fn+F5**. Der grüne Startknopf funktioniert ebenfalls.

Zum Ausprobieren in die **Shell** klicken. Jeden Ausdruck einzeln hinter dem
Zeichen `>>>` eingeben und mit Enter bestätigen. `>>>` selbst nicht mittippen.

```python
2 + 3
10 * 5
"Hallo" + " Welt"
```

Die Ergebnisse sind `5`, `50` und der Text `Hallo Welt`. Bei Text zeigt die Shell
zusätzlich Anführungszeichen. Danach andere Zahlen oder Wörter ausprobieren.

## 3. Das erste Programm: Hallo!

Für ein gespeichertes Programm in den **Editor** klicken und Folgendes eingeben:

```python
print("Hallo, Welt!")
print("Ich lerne Python!")
```

1. Mit **Strg+S** speichern.
2. Im entpackten Arbeitsordner `python-lernen` den Unterordner `spielwiese`
   auswählen und die Datei als **`hallo.py`** speichern. Falls der Arbeitsordner
   noch fehlt, hilft die [Vorbereitung im README](../../README.md).
3. Mit **F5** starten.
4. In der Shell sollte stehen:

```text
Hallo, Welt!
Ich lerne Python!
```

Das fertige Vergleichsbeispiel heißt [01_hallo.py](../../beispiele/01_hallo.py).
Die Programme werden in Thonny gestartet; ein Doppelklick im Windows-Explorer
kann ein Fenster öffnen, das sofort wieder verschwindet.

**Ausprobieren:** Die Nachrichten ändern, eine weitere Zeile mit `print()`
ergänzen oder mit `print(7 * 8)` eine Rechnung ausgeben.

`print(...)` zeigt etwas an. Text steht in Anführungszeichen; Python nennt ihn
**String**. Die Anweisungen laufen von oben nach unten.

## 4. Das Programm stellt eine Frage

Mit **Strg+N** eine neue Datei öffnen und diesen Code eingeben:

```python
name = input("Wie heißt du? ")
print("Hallo, " + name + "!")
```

Als **`spielwiese/begruessung.py`** speichern und mit **F5** starten. Sobald die
Frage erscheint, in die **Shell** klicken, einen Namen oder Spitznamen eingeben
und Enter drücken. Dann erscheint die persönliche Begrüßung.

`input(...)` nimmt eine Texteingabe entgegen. Die **Variable** `name` merkt sich
diese Antwort. Das Vergleichsbeispiel steht in
[02_begruessung.py](../../beispiele/02_begruessung.py).

**Ausprobieren:**

- Nach einem Lieblingsspiel fragen und die Antwort in einem Satz ausgeben.
- Zwei Fragen stellen und beide Antworten verwenden.
- Die Begrüßung dreimal ausgeben.

### Mit einer eingegebenen Zahl rechnen

In einer neuen Datei `spielwiese/alter.py` diesen Code ausprobieren:

```python
alter_text = input("Wie alt ist deine Spielfigur? ")
alter = int(alter_text)
print("Nächstes Jahr ist sie", alter + 1)
```

Bei der Eingabe `13` erscheint am Ende `14`. `input()` liefert immer Text.
`int(...)` wandelt Text wie `13` in eine ganze Zahl um, mit der Python rechnen
kann. Wörter oder leere Eingaben führen hier noch zu einem Fehler.

**Guter Haltepunkt für den ersten Tag:** Ein gespeichertes Programm läuft und
reagiert auf eine eigene Eingabe. Das reicht für einen gelungenen Anfang.

## 5. Das erste Spiel: Die geheime Zahl

Wenn Eingabe und Variablen schon vertraut sind, folgt das Ratespiel. In Thonny
eine neue Datei **`spielwiese/zahlenraten.py`** anlegen und diesen Code eingeben:

```python
import random

geheim = random.randint(1, 20)
tipp = 0
versuche = 0

print("Ich denke an eine Zahl zwischen 1 und 20.")

while tipp != geheim:
    tipp = int(input("Dein Tipp: "))
    versuche = versuche + 1

    if tipp < geheim:
        print("Zu klein!")
    elif tipp > geheim:
        print("Zu groß!")
    else:
        print("Richtig! Anzahl der Versuche:", versuche)
```

Speichern, mit **F5** starten und in der Shell raten. Zunächst nur **ganze
Zahlen** eingeben, etwa `7`; Wörter und leere Eingaben werden noch nicht
abgefangen. Das fertige Beispiel heißt
[03_zahlenraten.py](../../beispiele/03_zahlenraten.py).

Neue Ideen im Spiel:

- `import random` lädt ein Modul aus Pythons Standardbibliothek.
- `random.randint(1, 20)` wählt eine ganze Zahl von 1 bis einschließlich 20.
- `while` wiederholt den eingerückten Teil, solange die Bedingung wahr ist.
- `if`, `elif` und `else` entscheiden, welcher Hinweis erscheint.
- `!=` bedeutet „ungleich“. `==` bedeutet „ist gleich“; ein einzelnes `=`
  weist einer Variablen einen Wert zu.
- Nach `while`, `if`, `elif` und `else` steht ein Doppelpunkt. Die zugehörigen
  Zeilen sind um **vier Leerzeichen pro Ebene** eingerückt. Thonny hilft dabei.

**Das Spiel erweitern — eine Änderung nach der anderen:**

1. Den Bereich auf 1 bis 100 vergrößern und den Ansagetext passend ändern.
2. Höchstens sieben Versuche erlauben und auch eine verlorene Runde anzeigen.
3. Punkte vergeben, abhängig von der Zahl der Versuche.
4. Eine weitere Runde ohne Neustart ermöglichen.
5. Später: Mit `try` und `except ValueError` eine freundliche Meldung für
   ungültige Eingaben ergänzen, statt das Programm abbrechen zu lassen.

Nicht jede Erweiterung muss sofort gelingen. Eine Vermutung aufstellen, den Code
ändern und das Ergebnis beobachten ist bereits Programmieren.

## 6. Bonus: Mit Python zeichnen

Python bringt das Zeichenmodul **turtle** mit. In einer neuen Datei
**`spielwiese/zeichnen.py`** diesen Code ausprobieren:

```python
import turtle

stift = turtle.Turtle()
stift.speed(3)

for seite in range(4):
    stift.forward(100)
    stift.right(90)

turtle.done()
```

Nach dem Start entsteht in einem eigenen Fenster ein Quadrat. Das Fenster
bleibt durch `turtle.done()` offen und kann nach dem Zeichnen geschlossen werden.
Vor einem neuen Start gegebenenfalls Thonnys roten Stop/Neustart-Knopf verwenden.
Das Vergleichsbeispiel heißt [04_zeichnen.py](../../beispiele/04_zeichnen.py).

**Ausprobieren:**

- Für ein Dreieck `range(4)` durch `range(3)` und `90` durch `120` ersetzen.
- Nach der Schleife, vor `turtle.done()`, mit `stift.circle(60)` einen Kreis ergänzen.
- Vor der Schleife mit `stift.color("blue")` die Farbe ändern.
- Eine andere Streckenlänge oder Geschwindigkeit ausprobieren.

Die **`for`-Schleife** wiederholt hier die eingerückten Befehle viermal.

## 7. Fehler verstehen und Schritt für Schritt prüfen

Jedes Programm hat beim Entstehen Fehler. Zum Eingrenzen zuerst die letzte
Zeile der Meldung lesen, dann die genannte Codezeile prüfen. Fehlende Klammern,
Anführungszeichen, Doppelpunkte oder Einrückungen sind häufige Ursachen.

In Thonny **Ansicht → Variablen** (englisch: **View → Variables**) öffnen.
Das Begrüßungsprogramm mit **Strg+F5** starten. Mit **F6** schrittweise vorgehen;
bei `input()` die Antwort in der Shell eingeben. Die Variablenansicht zeigt,
wie `name` einen Wert bekommt. Dieses schrittweise Prüfen heißt **Debugging**.

Die [Fehlerhilfe](../nachschlagen/fehlerhilfe.md) erklärt typische Meldungen,
wartende Programme und Windows-Startprobleme. Zum Anhalten eines Programms dient
der rote Stop/Neustart-Knopf.

## 8. Weiterlernen

Der [Lernplan](../lernplan.md) schlägt weitere Etappen vor: Schere, Stein, Papier,
ein Quiz, Zeichnungen und ein Textabenteuer. Dazu gibt es
[Übungen](../../uebungen/README.md), [Projektideen](../../projekte/README.md),
einen [Spickzettel](../nachschlagen/python_spickzettel.md) und ausgewählte
[Materialien](../materialien.md).

### Checkliste für den Anfang

- [ ] Thonny ist installiert und startet.
- [ ] `2 + 3` ergibt in der Shell `5`.
- [ ] `hallo.py` ist gespeichert und läuft.
- [ ] Das Begrüßungsprogramm verarbeitet eine Eingabe.
- [ ] Mindestens eine eigene Änderung funktioniert.

### Für einen späteren Tag

- [ ] Das Zahlenratespiel läuft.
- [ ] Eine Erweiterung des Spiels ist ausprobiert.
- [ ] Im Turtle-Fenster ist ein eigenes Bild entstanden.

Das beste nächste Projekt ist eines, auf das die lernende Person Lust hat.

---

Deutsche Fassung der [englischen Vorlage](python-thonny-getting-started-en.md),
mit angepasstem Lerntempo, passenden Repository-Pfaden und Windows-Hinweisen.
Installationsangaben am 25. Oktober 2026 anhand der
[offiziellen Thonny-Webseite](https://thonny.org/) geprüft: Thonny 5.0.0 mit
Python 3.14 für Windows 10/11. Bei späteren Versionen können Downloadnamen und
Menütexte abweichen. Hinweise zu macOS und Linux stehen in der englischen Vorlage;
diese Anleitung konzentriert sich auf den Windows-PC.
