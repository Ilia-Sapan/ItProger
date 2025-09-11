import os
import json


# a) Verzeichnis erstellen und Daten speichern

verzeichnis = 'meine_daten'
if not os.path.exists(verzeichnis):
    os.makedirs(verzeichnis)
daten = [
    {'name': 'Max Mustermann', 'alter': 30, 'beruf': 'Ingenieur'},
    {'name': 'Erika Musterfrau', 'alter': 25, 'beruf': 'Architektin'},
    {'name': 'John Doe', 'alter': 40, 'beruf': 'Lehrer'}
]
with open(os.path.join(verzeichnis, 'daten.json'), 'w') as datei:
    json.dump(daten, datei)


# b) Daten lesen und auf der Konsole ausgeben

try:
    with open(os.path.join(verzeichnis, 'daten.json'), 'r') as datei:
        gelesene_daten = json.load(datei)
        print(gelesene_daten)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")


# c) Daten aktualisieren

def aktualisiere_daten():
    name = input("Name: ")
    alter = input("Alter: ")
    beruf = input("Beruf: ")
    neuer_eintrag = {'name': name, 'alter': alter, 'beruf': beruf}
    try:

        with open(os.path.join(verzeichnis, 'daten.json'), 'r+') as datei:
            daten = json.load(datei)
            daten.append(neuer_eintrag)
            datei.seek(0)
            json.dump(daten, datei)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
aktualisiere_daten()