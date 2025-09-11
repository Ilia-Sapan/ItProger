# Listen
# a = ["Juli", 28, True] # Änderbare sequenzen
#
# # Tupel
# b = (11, 'November', 2021)
#
# # Komplexe Sequenzen
# c = [("Tom", "09384758 020"), ("Sindie", "8585885589")]
# t = ("Radiergummi", 0.45)
# artikel, preis = t # Mit dieser Technik kann man Iterationen über Listen von Tupeln besonders elegant definieren.
#
# warenbestand = [('Papier, 500 Blatt', 4.45),
#                 ('Laminierfolien Din A 4', 2.50),
#                 ('Radiergummi', 0.45)]
#
# for artikel, preis in warenbestand:
#     print(artikel, 'Preis: ', preis, "€")
#
# wort = 'Balensiaga'
# print(wort.count('a')) # count() zahlt die Menge

# Verschiedenen Operationen
# list[i] = x
# list.append(x)
# del list[i]
# list.index(x)
# list.inser(x,y)
# list.pop()
# list.remove()
# list.reverse()
# list.sort()
# list = [n**2 for n in range(10) if n % 2 == 0] # ausdruck for item in kollektion if bedingung
#
# list = [n for n in range(1,100) if n%4==0] # Liste von Zahlen zwischen 0 und 100, die durch 4 teilbar sind
# s = "Super Sex"
# ss = ["Anfang", "Antrag", "Asceleration", "Summary", "Load"]
# # Beispiel-Liste von Wörtern
# woerter_liste = ["Apfel", "Banane", "Ananas", "birne", "Avocado", "Traube", "aprikose"]
# # Filtern der Wörter, die mit 'a' oder 'A' beginnen
# gefilterte_woerter = [wort for wort in woerter_liste if wort.lower().startswith('a')]
# # Ausgabe der gefilterten Liste
# print("Wörter, die mit 'a' oder 'A' beginnen:", gefilterte_woerter)

#
# test_input = [("a", [1,2]), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
#
# def couple(lst):  # Избегайте использования зарезервированного слова 'list' в качестве имени параметра.
#     test_output = dict()
#     for key, value in lst:
#         test_output[key] = value  # Правильное добавление пары ключ-значение в словарь.
#     return test_output
#
# print(couple(test_input))

# 7.3 Dictionaries
atommasse = {'H': 1.0079, 'He': 4.0026, 'Li': 96.75}
# Operationen für Dictionaries
# atommasse['H']  обращение по ключу
# atommasse['H'] = 2.000 замена значения ключа
# del atommasse['H'] удаление ключа
# atommasse.keys() or atommasse.values() обращение к ключам или значениям

# vokabeltrainer.py

# import random
# from random import choice
#
# d = {
#     'sun': ['Sonne'],
#     'key': ['Taste', 'Schlüssel'],
#     'head': ['Kopf', 'Chef', 'Leiter']
#     }
#
#
# def aufgabe(d):
#     vokabel = choice(list(d.keys())) # Aus der Liste der englischen Wörter (Schlüssel) wird ein Wort zufällig ausgewählt
#     print(f"Nennen Sie ein deutsches Wort für {vokabel}!")
#     antwort = input("Deutsches Wort ist: ")
#     if antwort not in d[vokabel]:
#         print(f"Leider, falsch! {vokabel} bedeutet {d[vokabel]}.")
#     else:
#         print("Richtig!")
#         del d[vokabel]
#
# while d:
#     aufgabe(d)
# print('Sie habem alle Vokabeln gelernt!')
# eingabe = input()



#
# # Dieses Dictionary repräsentiert den Graphen mit 6 Knoten und 7 Kanten
# G = {
#     1 : [2, 4],
#     2 : [1, 3, 5],
#     3 : [2, 5],
#     4 : [1, 5],
#     5 : [4, 2, 3, 6],
#     6 : [5]
#     }
#
#
# def suche_weg(aktuell, ziel, besucht):
#     '''Der gesamte Algorithmus zur Wegesuche ist in dieser rekursiven
# Funktion enthalten. Sie ist rekursiv, weil sie sich selbst aufruft. Der
# Parameter aktuell steht für die Nummer des aktuell besuchten Knotens,
# und ziel ist die Nummer des Zielknotens. Der dritte Parameter besucht ist
# eine Liste der bereits besuchten Knoten. Diese Liste bildet den Anfang
# eines Weges zum Ziel, der bereits gefunden wurde'''
#     besucht = besucht + [aktuell]
#     if aktuell == ziel:
#         return besucht
#     else:
#         for k in G[aktuell]:
#             if not k in besucht:
#                 weg = suche_weg(k, ziel, besucht)
#                 if weg:
#                     return weg
#         return []
# while True:
#     start = int(input('Start: '))
#     ziel = int(input('Ziel: '))
#     weg = suche_weg(start, ziel, [])
#     print(f"Weg: {weg}.")

# 7.7. Übungen
# Übung 1: Lottozahlen
import random
from random import choice
s = [6, 25, 35, 36, 44, 49]
variant = choice(s)
print(variant)

# Übung 2: Verkehrsdichte*
import time

def verkehrsdichte_erfassen():
    print("Zählung gestartet! Drücke:")
    print("- 'a' für Auto")
    print("- 'f' für Fahrrad")
    print("- 'p' für Person")
    print("Zählung läuft für 1 Minute. Drücke 'Enter', um Eingaben zu beenden.")

    autos = 0
    fahrraeder = 0
    personen = 0

    startzeit = time.time()
    while True:
        # Warte auf Benutzereingabe
        eingabe = input("Eingabe: ").lower()

        # Stoppe nach einer Minute
        if time.time() - startzeit >= 60:
            print("\nZählung beendet!")
            break

        # Verarbeite Eingaben
        if eingabe == 'a':
            autos += 1
        elif eingabe == 'f':
            fahrraeder += 1
        elif eingabe == 'p':
            personen += 1
        elif eingabe == '':
            print("\nManuelle Beendigung durch 'Enter'")
            break
        else:
            print("Ungültige Eingabe. Bitte nur 'a', 'f' oder 'p' eingeben.")

    # Ergebnis ausgeben
    print("\n--- Ergebnis der Zählung ---")
    print(f"Autos: {autos}")
    print(f"Fahrräder: {fahrraeder}")
    print(f"Personen: {personen}")


# Programm starten
verkehrsdichte_erfassen()












