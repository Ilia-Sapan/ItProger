# import math  # 6.1 Importanweisungen
 # import modul
 # from modul import name 1, name 2, name 3...
 # from modul import *

# import math as m
# import random
#
# from sympy import sequence
#
# a = m.sqrt(4) # Quadratwurzel
# print(a)

# 6.2 Mathematische Funktionen: Das Modul math
# Das hat die eulersche Zahl e und die Kreiszahl π
#
# from math import pi
# r = 5
# S = 2 * pi * r**2
# print(S)
#
#
# from math import *
# print(sin(pi/2))
#
# print(sin(radians(45))) #
#
# import math
#
# # Преобразуем 90 градусов в радианы
# angle_degrees = 90
# angle_radians = math.radians(angle_degrees)
#
# print(angle_radians)  # Вывод: 1.5707963267948966 (π/2)
#
# # 6.3 Zufallsfunktionen: Das Modul random
#import random
#from random import *
#
# import random
#
# numbers = [1, 2, 3, 4, 5]
# print(random.choice(numbers))  # Вывод: случайное число из списка, например, 3
#
# # Генерация случайного числа от 1 до 10
# print(random.randint(1, 10))  # Вывод: случайное число, например, 7
# # random.randint(1.5, 5.5)  # TypeError: non-integer arg 1 for randrange()
# random.randint(1, 1)  # Всегда вернет 1
# # Генерация случайного числа
# print(random.random())  # Например: 0.723498243
# # Перемешиваем список
# random.shuffle(numbers)
# print(numbers)  # Например: [4, 1, 3, 5, 2]
#
# from random import randint
# for i in range(5):
#     zufallzahl = randint(1,6)
#     print(f"Zufallzahl ist {zufallzahl}")
#
# from random import choice
# personen = ["Alex", "Tina", "Annelie", "Tom"]
# person = choice(personen)
# print(f"{person} würde heute zufällig gewählt!")

# 6.4 Datum und Zeit

# import time
# from time import *
#
# zeitpunkt = localtime() # Die Funktion localtime() liefert ein Objekt, das den momentanen Zeitpunkt
# print(zeitpunkt.tm_year) # Result: 2025
# print(zeitpunkt.tm_mon) # Result: 1

# print(time.time())  # Пример: 1706019929.123456 (время в секундах с плавающей точкой)

# uhr
# from time import localtime, sleep # aus dem Modul die Funktionen importiert
#
# while True:
#     zeit = localtime() # Hier wird ein Zeit-Objekt mit dem Namen zeit erzeugt
#     print(f"{zeit.tm_hour} Uhr and {zeit.tm_min} Minuten und {zeit.tm_sec} Secunden.") # Die Zahlenwerte der Atribute
#     sleep(10) # 10 Secunden warten

# trainer.py

#
# import random, time
#
#
# print("Multiplikationstrainer")
# print("----------------------")
# startzeit = time.time()
# for i in range(5):
#     a = random.randint(1,20) # Hier wird eine zufällige ganze Zahl zwischen 1 und 20 erzeug
#     b = random.randint(1,10) # Hier wird eine zufällige ganze Zahl zwischen 1 und 10 erzeug
#     ergebnis = - 1
#     while ergebnis != a * b:
#         prompt = str(a) + ' * ' + str(b) + ' = '
#         ergebnis = int(input(prompt))
#         if ergebnis == a * b:
#             print('Richtig!')
#         else:
#             print('Falsch! Versuchen Sie noch mal!')
#
# zeit = round(time.time() - startzeit)
# print(f"{zeit} Secunden benötigt!")

# if __name__ == '__main__':


# Übung 1: Wie hoch ist der Baum?
# import math
#
# if __name__ == '__main__':
#     # Функция для вычисления высоты дерева
#     def hoehe_des_baums(entfernung, blickwinkel, augenhoehe=1.6):
#         # Преобразуем угол в радианы
#         blickwinkel = math.radians(blickwinkel)
#         # Вычисляем высоту дерева
#         hoehe_b = entfernung * math.tan(blickwinkel) + augenhoehe
#         return round(hoehe_b, 2)
#
#     # Пример использования функции
#     baum_1 = hoehe_des_baums(20, 40, augenhoehe=1.6)
#     print(baum_1)
#
#     # Бесконечный цикл для ввода данных
#     while True:
#         # Возможность завершить программу
#         if input("Beenden? (ja/nein): ").lower() == "ja":
#             break
#         else:
#             # Ввод данных
#             ent = float(input("Entfernung: "))  # Преобразуем в float
#             blick = float(input("Blickwinkel: "))  # Преобразуем в float
#             # Вычисляем высоту дерева
#             baum = hoehe_des_baums(entfernung=ent, blickwinkel=blick, augenhoehe=1.6)
#             print(f"Höhe des Baums: {baum} Meter")


# Übung 2: Zahlenraten
# import random
# from random import randint
# # print(random.randint(1, 100))
#
# random_number = int(random.randint(1,100))
# count = 0
# personal_number = int(input("Bitte geben Sie eine Zahl zwischen 0 and 100 ein: "))
# while personal_number != random_number:
#     try:
#         if personal_number > random_number:
#             print("Zu groß!")
#             count +=1
#             personal_number = int(input("Bitte geben Sie eine Zahl zwischen 0 and 100 ein: "))
#         elif personal_number < random_number:
#             print("Zu klein!")
#             count += 1
#             personal_number = int(input("Bitte geben Sie eine Zahl zwischen 0 and 100 ein: "))
#         elif personal_number == random_number:
#             count += 1
#             print("Herzlichen Glückwunsch! Sie haben die Zahl gefunden!")
#             print(f"Versuchmenge: {count}")
#             break
#     except ValueError as e:
#         print(f"Das ist {e}! Bitte geben Sie eine Zahl ein!")
#
# import random
#
# # Генерация случайного числа
# random_number = random.randint(1, 100)
# count = 0
#
# print("Willkommen zum Zahlenraten-Spiel!")
# print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Versuchen Sie, sie zu erraten!")
#
# while True:
#     try:
#         # Пользователь вводит число
#         personal_number = int(input("Bitte geben Sie eine Zahl zwischen 1 und 100 ein: "))
#         count += 1
#
#         if personal_number > random_number:
#             print("Zu groß!")
#         elif personal_number < random_number:
#             print("Zu klein!")
#         else:
#             print("Herzlichen Glückwunsch! Sie haben die Zahl gefunden!")
#             print(f"Versuchmenge: {count}")
#             break
#     except ValueError:
#         print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.")
# Übung 3: Passender Gruß
# import time
# from datetime import datetime
# from time import *
# zeitpunkt = localtime().tm_hour
# if zeitpunkt < 12:
#     print(f"Guten Morgen! Jetzt ist {zeitpunkt} Uhr!")
# elif zeitpunkt >= 12 and zeitpunkt <= 18:
#     print(f"Guten Tag! Jetzt ist {zeitpunkt} Uhr!")
# else:
#     print(f"Guten Abend! Jetzt ist {zeitpunkt} Uhr!")