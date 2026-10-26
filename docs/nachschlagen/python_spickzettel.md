# Python-Spickzettel

Hier stehen kleine Beispiele zum Nachschlagen. Jeder Codeblock ist für sich
ausführbar. Die [Fehlerhilfe](fehlerhilfe.md) erklärt typische Fehlermeldungen.

## Text und Eingabe

```python
name = input("Wie heißt du? ")
print("Hallo, " + name + "!")
```

`input()` liefert Text. `print()` gibt etwas in der Shell aus. Eine Variable
wie `name` merkt sich einen Wert. `#` leitet einen Kommentar ein.

## Zahlen und Rechnen

```python
alter = int("13")
print(alter + 1)  # 14
print(7 * 8)  # 56
print(10 / 4)  # 2.5
```

| Zeichen | Bedeutung                        | Beispiel  |
| ------- | -------------------------------- | --------- |
| `+`     | Plus; bei Text: zusammenfügen    | `2 + 3`   |
| `-`     | Minus                            | `8 - 2`   |
| `*`     | Mal                              | `4 * 3`   |
| `/`     | Geteilt                          | `10 / 4`  |
| `//`    | Ganzzahlige Division, abgerundet | `10 // 4` |
| `%`     | Rest einer Division              | `10 % 4`  |
| `**`    | Potenz                           | `2 ** 3`  |

Für Dezimalzahlen steht im Python-Code ein Punkt: `2.5`. `int("13")` macht
aus dem Text eine ganze Zahl; `int("dreizehn")` führt zu einem `ValueError`.

## Entscheidungen und Vergleiche

```python
punkte = 8
if punkte >= 5:
    print("Geschafft!")
else:
    print("Noch einmal versuchen.")
```

`=` weist einen Wert zu. `==` prüft Gleichheit. Weitere Vergleiche sind `!=`
(ungleich), `<`, `>`, `<=` und `>=`. Nach `if`, `elif` und `else` steht ein
Doppelpunkt. Die zugehörigen Zeilen sind um vier Leerzeichen eingerückt.

## Wiederholungen

```python
for nummer in range(3):
    print(nummer)  # 0, dann 1, dann 2
```

`range(3)` liefert drei Zahlen, beginnend mit `0`.

```python
versuche = 0
while versuche < 3:
    versuche = versuche + 1
    print("Versuch", versuche)
```

`while` wiederholt den eingerückten Teil, solange die Bedingung wahr ist.

## Listen und Funktionen — für später

```python
spiele = ["Quiz", "Zahlenraten", "Abenteuer"]
for spiel in spiele:
    print(spiel)
print(spiele[0])  # Der erste Eintrag hat die Nummer 0.
```

```python
def begruesse(name):
    print("Hallo, " + name + "!")


begruesse("Alex")
begruesse("Sam")
```

Eine Funktion bündelt mehrere Anweisungen unter einem Namen. `def` legt sie an;
der Aufruf `begruesse("Alex")` führt sie aus.

## Selbst nachschlagen

Python erklärt sich zum Teil selbst. Diese Befehle direkt unten in der Shell
eintippen und mit **Enter** bestätigen:

```python
help(print)
```

`help()` zeigt eine Beschreibung. Bei `print` steht oben der Name der Funktion,
darunter ihre Parameter wie `sep` und `end`. Die Hilfe ist auf Englisch; der
genaue Text hängt von der Python-Version ab.

```python
dir("text")
```

`dir()` listet auf, was mit einem Wert möglich ist. Bei Text steht in der Liste
zum Beispiel `upper`. Ausprobieren: `"text".upper()` ergibt `'TEXT'`. Einträge
mit zwei Unterstrichen wie `__len__` dürfen am Anfang übersprungen werden.

In Thonny helfen außerdem:

- **Autovervollständigen:** Einen Namen anfangen, etwa `pri`, und **Strg+Leertaste**
  drücken. Thonny schlägt passende Befehle vor. Im Menü steht das unter
  **Bearbeiten → Autovervollständigen** (englisch: **Edit → Auto-complete**).
- **Assistent:** **Ansicht → Assistent** (englisch: **View → Assistant**) öffnet
  ein Fenster, das Fehlermeldungen in einfacheren Worten erklärt.
- **Hilfe:** **Hilfe → Hilfe Inhalt** (englisch: **Help → Help contents**)
  erklärt Thonny selbst.

Eine vollständige Liste der eingebauten Funktionen und weitere Kurse stehen in
den [Materialien](../materialien.md).

## Nützliche Module

Ein Modul bringt fertige Befehle mit. `import` lädt es; danach stehen seine
Befehle mit einem Punkt dahinter zur Verfügung.

### `random` — Zufall

```python
import random

wurf = random.randint(1, 6)
print("Gewürfelt:", wurf)
print(random.choice(["Schere", "Stein", "Papier"]))
```

`random.randint(1, 6)` liefert eine ganze Zahl von 1 bis 6, beide eingeschlossen.
`random.choice()` wählt einen Eintrag aus einer Liste. Jeder Start kann ein
anderes Ergebnis zeigen.
[Dokumentation zu `random`](https://docs.python.org/de/3/library/random.html)

### `turtle` — Zeichnen

```python
import turtle

stift = turtle.Turtle()
for seite in range(4):
    stift.forward(100)
    stift.left(90)
turtle.done()
```

Ein Fenster öffnet sich und die Schildkröte zeichnet ein Quadrat. Das Programm
endet, wenn das Fenster geschlossen wird.
[Dokumentation zu `turtle`](https://docs.python.org/de/3/library/turtle.html)

### `time` — Warten

```python
import time

for zahl in [3, 2, 1]:
    print(zahl)
    time.sleep(1)
print("Los!")
```

`time.sleep(1)` wartet eine Sekunde, bevor es weitergeht.
[Dokumentation zu `time`](https://docs.python.org/de/3/library/time.html)

### `math` — Mathematik

```python
import math

print(math.sqrt(16))  # 4.0
print(round(math.pi, 2))  # 3.14
```

`math.sqrt()` zieht die Wurzel, `math.pi` ist die Kreiszahl π. `round(…, 2)`
rundet auf zwei Nachkommastellen.
[Dokumentation zu `math`](https://docs.python.org/de/3/library/math.html)
