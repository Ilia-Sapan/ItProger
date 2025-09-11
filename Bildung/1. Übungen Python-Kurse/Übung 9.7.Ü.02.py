# a, b
strings = "\nDas ist ein String! \nNeue Zeile, \tTabulator, das ist \u2044Slash,\U0001F600Grinsendes Gesicht, und das ist Schach: " +  chr(9819)
#c
print(strings.count("\n"))
#d
stringlist = ["Das", "ist"]
stringlist = ", ".join(stringlist)
#e
with open(".txt & .json/neue_text.txt", "w", encoding="utf-8") as file:
    f = file.write(strings)
    print(f)
#f,g
try:
    with open(".txt & .json/neue_text.txt", "r", encoding="utf-8") as file:
        f = file.read()
        print(f)
except FileNotFoundError as e:
    print("Sorry, File nit found!")
except Exception as e:
    print(f"Sorry das ist {e}")

#h
import json
daten = {'name': 'Max', 'alter': 30}
with open('.txt & .json/daten.json', 'w', encoding='utf-8') as datei:
    json.dump(daten, datei)
try:
    with open('.txt & .json/daten.json', 'r', encoding='utf-8') as datei:
        geladene_daten = json.load(datei)
        print(geladene_daten)
except FileNotFoundError:
    print("Die JSON-Datei wurde nicht gefunden.")
