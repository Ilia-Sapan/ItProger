# Aufgabe: Datentypen, Kontrollstrukturen


# A
# tupel = [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E")]
#
# #B
# def pruefer(buch, zahl):
#     if (buch, zahl) in tupel:
#         print(f'Element gefunden: ({buch, zahl})')
#     else:
#         print("Element nicht gefunden")

#C
# zahl = input("Bitte Zahl:")
# def typecasting(zahl):
#     try:
#         zahl = int(zahl)
#         print(f"Die deine gegebene Zeichenkette {zahl} "
#               f"in eine ganze Zahl umwandelt")
#     except ValueError:
#         print("Zahl!")
#
# typecasting(zahl)

# E


# Die Funktion, die sucht einem Element in der Liste
# def pruefen_zahl(zahl):
#     if zahl in numbers_user:
#         print(f"Dieser Zahl - {zahl} - in der Liste")
#     else:
#         print("Es gibt keinem diesem Element!")


# Die Funktion, die eine Zeichenkette in eine Zahl umzuwandelt

# def typecasting(zahl):
#     try:
#         print(f"Deine Zeichenkette in eine Zahl in float {float(zahl)} umzuwandelt ist.")
#     except ValueError:
#         print('Zahl, bitte!')

elemente = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
def pruefe_element(buchstabe, zahl):
    if (buchstabe, zahl) in elemente:
        print(f"Element gefunden: ({buchstabe}, {zahl})")
    else:
        print("Element nicht gefunden.")

def zeichenkette_in_zahl(zeichenkette):
    zahl = int(zeichenkette)
    print(f"Umwandlung erfolgreich: {zahl}")
    return zahl