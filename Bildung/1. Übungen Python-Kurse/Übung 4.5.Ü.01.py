# # Aufgabe: Kontrollstrukturen
# #a) Das Programm bietet den Benutzer, eine ganze Zahle einzugeben
# benutzerzahl = int(input("Bitte geben Sie Zahl ein: "))
# if benutzerzahl > 10:
#     print(f"{benutzerzahl} > 10.")
# elif benutzerzahl == 10:
#     print(f"{benutzerzahl} = 10.")
# else:
#     print(f"{benutzerzahl} < 10.")
#
# for x in range(benutzerzahl + 1):
#     print(x)

def speed(S,t):
    v = S/t
    return print(f"Скорость равна {v} км/ч.")


def dichtheit (m, V):
     p = m/V
     print(f"Плотность равна {p} кг/метр")

def schwerkraft (m,g):
    f = m * g
    print(f"Сила тяжести {f} Ньютон.")

def federpendel(m,k):
    T = 2 * 3.14 * ((m/k)**0.5)
    print(f"Пружинный маятник равен {T} секунд.")

federpendel(45,5)
