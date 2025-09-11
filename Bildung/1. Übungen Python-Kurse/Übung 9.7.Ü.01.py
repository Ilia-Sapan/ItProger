# a)
text = "Hier ist ein Beispieltext mit einigen besonderen Zeichen: \nNeue Zeile, \tTabulator, \\Backslash, \u2764Herz Emoji, \U0001F600Grinsendes Gesicht."
# b)
# suchword = text.count(input('Ihre gesuchende Word ist: '))
# print(suchword)
#c)
# wexword = text.replace(input('Ihre alte Word ist: '), input('Ihre neue Word ist: '))
# print(wexword)
#
# with open("modifizierter_text.txt", "w", encoding="utf-8")as file:
#     file.write(wexword)
#d)
# import json
# try:
#     with open('daten.json', 'r', encoding='utf-8') as datei:
#         daten = json.load(datei)
#         print("Inhalt der 'daten.json':")
#         print(daten)
# except FileNotFoundError:
#     print("Die Datei 'daten.json' wurde nicht gefunden.")