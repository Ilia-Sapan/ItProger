# a
import random
from random import  randint
number_lists = [randint(1,100) for i in range(10)] # Erzeuge eine Liste von 10 zufälligen Ganzzahlen zwischen 1 und 100
# b
def sortiere_und_zaehle(a: list):
    a = sorted(a)
    b = len(a)
    return f"Sortierte Liste: {a}. Die Länge der Liste: {b}."
# c
number_lists_mit_quadraten = [(x, x**2) for x in number_lists]
print(number_lists_mit_quadraten)

# d

for x, y in number_lists_mit_quadraten:
    print(f"Die Zahl {x} hat das Quadrat {y}.")

# e

# if anzahl_elemente > 5:
#     print("Mehr als 5 Elemente")
# else:
#     print("5 oder weniger Elemente")
