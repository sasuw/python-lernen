# Hilfe bei Fehlern und Startproblemen

Fehlermeldungen gehören zum Programmieren. Meist führt die letzte Zeile in der
Shell zum Problem. Hier stehen typische Ursachen und passende nächste Schritte.

## Einen Fehler eingrenzen

1. Die letzte Zeile der Fehlermeldung lesen.
2. Die genannte Datei und Zeilennummer ansehen; auch die Zeile davor prüfen.
3. Die Stelle mit dem Beispiel vergleichen: Anführungszeichen, Klammern,
   Doppelpunkte und Leerzeichen am Zeilenanfang.
4. Eine Sache ändern, speichern und erneut starten.

Wenn Hilfe nötig ist, sind der betroffene Code, die genaue Meldung und die
erwartete Ausgabe nützlich. Private Angaben vor dem Teilen entfernen.

| Meldung oder Problem                                            | Was zu prüfen ist                                                                                                                              |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `SyntaxError`                                                   | Fehlt ein Anführungszeichen, eine Klammer oder ein Doppelpunkt? Gerade Anführungszeichen `"` oder `'` verwenden, keine typografischen.         |
| `IndentationError` oder `TabError`                              | Gehören alle Zeilen im Block zusammen? Vier Leerzeichen je Ebene verwenden; Tabs und Leerzeichen nicht mischen.                                |
| `NameError`                                                     | Ist der Variablenname überall gleich geschrieben? Groß- und Kleinschreibung zählen. Wurde der Wert vorher zugewiesen?                          |
| `ValueError` bei `int(...)`                                     | Kam wirklich eine ganze Zahl wie `13` an, statt `dreizehn`, `2,5` oder einer leeren Eingabe?                                                   |
| Fehler bei `import random` oder `import turtle`                 | Heißt eine eigene Datei `random.py` oder `turtle.py`? Diese Datei umbenennen und Thonnys Interpreter über den Stop/Neustart-Knopf neu starten. |
| Das Programm wartet scheinbar endlos.                           | Steht eine Frage von `input()` in der Shell? Dort hineinklicken, antworten und Enter drücken.                                                  |
| Eine Schleife hört nicht auf.                                   | Mit dem roten Stop/Neustart-Knopf anhalten; danach die `while`-Bedingung und die darin geänderten Werte prüfen.                                |
| F5 startet nichts.                                              | In den Editor klicken und den grünen Startknopf versuchen. Auf manchen Tastaturen ist Fn+F5 nötig.                                             |
| Das Fenster verschwindet beim Doppelklick auf eine `.py`-Datei. | Die Datei in Thonny öffnen und dort mit F5 starten, damit die Ausgabe sichtbar bleibt.                                                         |

## Thonny unter Windows

- **Die Shell fehlt:** Im Menü **Ansicht → Kommandozeile** nachsehen; auf Englisch
  **View → Shell**. Menütexte können je nach Version und Sprache abweichen.
- **Der Installer startet nicht:** Den Download von [thonny.org](https://thonny.org/)
  und den passenden Prozessortyp prüfen. Bei Sicherheits- oder Rechtefragen
  hilft eine erwachsene Begleitperson. Windows-Schutzfunktionen eingeschaltet lassen.
- **Python fehlt oder der falsche Interpreter läuft:** Unten rechts in Thonny
  den Interpreter prüfen und das mit Thonny gelieferte lokale Python auswählen.
  Beim normalen Windows-Installer ist es bereits eingerichtet.
- **Die Datei heißt `hallo.py.txt`:** Im Windows-Explorer die Dateinamenerweiterungen
  einblenden. In Thonny über **Speichern unter…** als Python-Datei mit Endung `.py`
  speichern.
- **Das Zeichenfenster reagiert nicht:** Das Turtle-Fenster nach dem Zeichnen
  schließen. Vor dem nächsten Start gegebenenfalls den Stop/Neustart-Knopf drücken.

## Werte Schritt für Schritt ansehen

In Thonny über **Ansicht → Variablen** (englisch: **View → Variables**) die
Variablenansicht öffnen. Ein Programm mit **Strg+F5** starten und mit **F6**
schrittweise weitergehen. Die Ansicht zeigt, wie sich Werte ändern. Das heißt
**Debugging**. Ein Einstieg ist das Beispiel `beispiele/02_begruessung.py`.
