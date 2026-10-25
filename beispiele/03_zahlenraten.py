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
