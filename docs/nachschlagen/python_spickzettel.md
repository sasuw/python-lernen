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
