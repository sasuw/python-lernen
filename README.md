# Python lernen

Hier sammeln sich Lernmaterialien, kleine Programme und eigene Ideen. Der
Einstieg läuft mit **Thonny auf einem Windows-PC**. Vorkenntnisse sind nicht nötig.

## Hier geht's los

1. Die [Anleitung für Python und Thonny](docs/anleitungen/python-thonny-getting-started.md)
   führt von der Installation bis zum ersten eigenen Programm.
2. Der [Lernplan](docs/lernplan.md) gibt eine mögliche Reihenfolge vor.
3. In der [Spielwiese](spielwiese/README.md) ist Platz zum freien Ausprobieren.

Für den Anfang reichen Thonny und dieser Ordner. Python ist im normalen
Windows-Installer von Thonny enthalten. Git, eine Konsole und zusätzliche
Python-Pakete sind für die ersten Schritte nicht nötig.

## Den Ordner unter Windows vorbereiten

Falls das Repository noch nicht auf dem PC liegt: Auf der Repository-Seite über
das Download-Menü ein **ZIP-Archiv** herunterladen. Im Windows-Explorer das Archiv
mit **Alle extrahieren…** entpacken, zum Beispiel in den Ordner **Dokumente**.
Erst danach die Python-Dateien in Thonny öffnen.

Der lokale Arbeitsordner heißt hier `python-lernen`. Beim Entpacken kann er
zunächst einen Zusatz im Namen haben. Dann ist Umbenennen möglich.
Eine ZIP-Kopie aktualisiert sich nicht automatisch; beim späteren Herunterladen
die eigenen Programme behalten und einen neuen Ordner verwenden.

## Was liegt wo?

| Ordner                                                                 | Inhalt                                                  |
| ---------------------------------------------------------------------- | ------------------------------------------------------- |
| [docs/anleitungen/](docs/anleitungen/python-thonny-getting-started.md) | Schritt für Schritt etwas zum Laufen bringen.           |
| [docs/lernplan.md](docs/lernplan.md)                                   | Kleine Lernziele für mehrere Treffen.                   |
| [docs/nachschlagen/](docs/nachschlagen/python_spickzettel.md)          | Python-Spickzettel und Hilfe bei Fehlern.               |
| [docs/materialien.md](docs/materialien.md)                             | Ausgewählte Webseiten und Bücher.                       |
| [beispiele/](beispiele/README.md)                                      | Fertige, kleine Programme zum Starten und Verändern.    |
| [uebungen/](uebungen/README.md)                                        | Aufgaben mit Tipps; eigene Lösungen kommen hier hinein. |
| [projekte/](projekte/README.md)                                        | Ideen und Platz für größere eigene Programme.           |
| [spielwiese/](spielwiese/README.md)                                    | Freie Experimente ohne feste Aufgabe.                   |

## Ein Beispiel starten

1. In Thonny **Datei → Öffnen…** wählen (`Strg+O`; englisch: **File → Open…**).
2. Im Arbeitsordner `beispiele/01_hallo.py` öffnen.
3. Mit **F5** oder dem grünen Startknopf ausführen. Die Ausgabe erscheint unten
   in der **Shell** (auf Deutsch: **Kommandozeile**). Auf manchen Tastaturen ist
   **Fn+F5** nötig.
4. Für eigene Änderungen über **Datei → Speichern unter…** eine Kopie als
   `spielwiese/mein_hallo.py` speichern, einen Text ändern und erneut starten.

## Ein paar hilfreiche Gewohnheiten

- Kleine Schritte: erst starten, dann eine Sache ändern, dann wieder starten.
- Vor dem Start kurz überlegen: Welche Ausgabe wird wohl erscheinen?
- Fehler gehören dazu. Die [Fehlerhilfe](docs/nachschlagen/fehlerhilfe.md) hilft
  beim Lesen der Meldungen.
- Eigene Dateien bekommen klare Namen wie `mein_quiz.py`. Für Dateinamen sind
  kleine Buchstaben und Unterstriche praktisch, zum Beispiel `ue` statt `ü`.
  Texte im Programm dürfen natürlich Umlaute enthalten.
- Keine Dateien `random.py`, `turtle.py` oder `thonny.py` nennen. Diese Namen
  können mit Python-Modulen oder Thonny kollidieren.
- Passwörter, Zugangsdaten und private Angaben gehören nicht ins Repository.

Eine gute Lerneinheit dauert etwa **30–45 Minuten** und endet mit einem
gespeicherten Programm und einer Idee für das nächste Mal. Der Plan darf sich
nach den eigenen Interessen richten.
