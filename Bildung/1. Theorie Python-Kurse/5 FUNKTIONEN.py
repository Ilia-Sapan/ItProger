# # 5.2. Definition und Aufruf einer Funktion
#
# print(len("Python"))
#
# # Projekt: Fallhöhe berechnen
# # fall.py
#
# def fallhöhe(t): # Definition einer Funktion mit dem Namen und einem Parameter
#     g = 9.81
#     s = 0.5 * 9.81 * t**2 # Berechnung der Fallhöhe
#     return s # Rückgabe des Ergebnisses
#
# zeit = float(input("Fallzeit in Secunden: "))
# höhe = fallhöhe(zeit)
# print("Fallöhe: ", round(höhe,2), "m")
#
# # 5.3 Optionale Parameter und voreingestellte Werte
#
# def fallhöhe(t, g = 9.81): # Definition einer Funktion mit dem Namen und einem Parameter
#     s = 0.5 * g * t**2 # Berechnung der Fallhöhe
#     return s # Rückgabe des Ergebnisses
# while True:
#     zeit = float(input("Fallzeit in Secunden: "))
#     beschleunigung = input("g in m/s^2:")
#     if beschleunigung:
#         höhe = fallhöhe(zeit, float(beschleunigung))
#     else:
#         höhe = fallhöhe(zeit)
#     print("Fallöhe: ", round(höhe,2), "m")



# 5.4 Eine Funktion in der Shell testen
# def ausgabe(zahl):
#     print("Die Zahl lautet: ", zahl)
#
# ausgabe(3)
# ausgabe(44)

# Die return-Anweisung

# def enthalten(kollektion, zahl):
#     for x in kollektion:
#         if round(x) == round(zahl):
#             return True
#     return False
# print(enthalten([1,2,3,4], 3.9))

# 5.6. Positionsargumente und Schlüsselwortargumente

# print(round(number= 12.33456, ndigits=5))
# print(round(ndigits=2, number= 12.33456))

# Funktionsannotationen
# def имя_функции(параметры) -> возвращаемый_тип:
#     # Тело функции
#     return значение

# def fallhöhe(t): -> float
#     g = 9.81
#     s = 0.5 * 9.81 * t**2 # Berechnung der Fallhöhe
#     return s # Rückgabe des Ergebnisses

#  Docstring

# def fallhöhe(t): # Definition einer Funktion mit dem Namen und einem Parameter
#     '''Berechnung der Fallhöle etc....'''
#     g = 9.81
#     s = 0.5 * g * t**2 # Berechnung der Fallhöhe
#     return s # Rückgabe des Ergebnisses

# Funktion help()
# def add(a: int, b: int) -> int:
#     """
#     Суммирует два числа.
#
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма чисел
#     """
#     return a + b
#
# help(add)

# 5.8 Die print()-Funktion unter der Lupe
#
# print(1,2,3, sep= "             ")
# for i in range(10):
#     print(i, end = "        ")


# Globale und Lokale Namen
#
# x = 10  # Глобальное имя
#
# def show_value():
#     global x
#     print(x)  # Используем глобальное имя
#
# show_value()  # Вывод: 10
#
# def calculate():
#     y = 20  # Локальное имя
#     print(y)
#
# calculate()  # Вывод: 20
# # print(y)  # Ошибка: переменная y недоступна за пределами функции

# Rekursive Funktionen
# def f(x):
#     print(x)
#     f(x/2)
#
# f(100)
#
#
# def fak(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fak(n-1)
#
# eingabe = input('Natürliche Zahl: ')
# while eingabe:
#     fakultät = fak(int(eingabe))
#     print('Fakultät von', eingabe, ':', fakultät)
#     print()
#     eingabe = input('Natürliche Zahl: ')

# Lambda - Funktionen

# lambda Parameter: Ausdruck

# lambda x, y: x * y


# Mapping
# map(Funktion, Kollektion)
def add(x,y):
    return x + y

summe = map(add, [1,2,3], [4,5,6]) # Aufruf der Funktion map()
print(list(summe)) #
#
# zahlen = filter(lambda x: x%4 == 0, range(20))
# print(list(zahlen))



















