# a
import math
import random
from random import randint

# b
def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    listen = [randint(1, max_wert) for i in range(anzahl)]
    return listen
# c
def berechne_durchschnitt(listen):
    listen = sum(listen)/len(listen)
    return f"Durchschnitt ist {listen}."
# d
def sort_and_divide(num):
    if len(num) % 2== 0:
        a = int(len(num) * 0.5)
        b = sorted(num[:a])
        c = num[a:]
        return f"Erse Liste ist {b}, die zweite ist {c}."
    else:
        a = int(len(num) * 0.5 + 1)
        b = sorted(num[:a])
        c = num[a:]
        return f"Erse Liste ist {b}, die zweite ist {c}."

# e
def erzeuge_zufallszahlen_liste_1(max_wert=100):
    listen = [randint(1, max_wert) for i in range(10)]
    return listen

numbers_neu = erzeuge_zufallszahlen_liste_1()
print(numbers_neu)
print(berechne_durchschnitt(numbers_neu))
print(sort_and_divide(numbers_neu))