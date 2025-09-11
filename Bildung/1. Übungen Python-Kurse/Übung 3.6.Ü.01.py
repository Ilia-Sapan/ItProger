# Aufgabe:  Fehler finden
# #A
# lists = [55, 45, 66, 7]
# #Wir berechnen der Summe
# print(f"Summa ist {sum(lists)}.")
# # Durchschnitt dieser Zahlen
# print(f"Durschnitt ist {sum(lists)/len(lists)}.")
#
# #B
# zahl = input("Geben bitte die Zahl ein: ") # das eine Zeichenkette (String) von einem Benutzer
# print(type(zahl)) # Ergebnis ausgeben, welche Typ
# try:
#     int(zahl)
#     print("Die eingabe is eine Ganzzahl.")
# except ValueError:
#     print("Die Eingabe ist weder eine Ganzzahl noch eine Gleitkommazahl.")
#
# try:
#     float(zahl)
#     print("Die Eingabe ist eine Gleitkommazahl.")
# except ValueError:
#     print("Die Eingabe ist weder eine Ganzzahl noch eine Gleitkommazahl.")
#
# # C
#
# # Eingabe: Fordere den Benutzer auf, zwei Zahlen einzugeben
#
# zahl1 = float(input("Bitte gib die erste Zahl ein: "))
# zahl2 = float(input("Bitte gib die zweite Zahl ein: "))
# # Verarbeitung: Multipliziere die beiden Zahlen
#
# ergebnis = zahl1 * zahl2
# # Ausgabe: Gib das Ergebnis der Multiplikation aus
#
# print("Das Ergebnis der Multiplikation ist:", ergebnis)
#
# # D

print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = int(input("Bitte gib eine Zahl ein: "))
zahl2 = int(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)







