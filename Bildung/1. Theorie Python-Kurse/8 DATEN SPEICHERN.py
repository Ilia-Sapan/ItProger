# Format des Aufrufs
# open(file, [mode], [encoding])
# f = open(text.txt, mode = "r", encording = 'utf - 8')
# Чтение текста
# with open("text.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#
# # Запись текста
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write("Новая строка текста.")
#
# # Добавление текста
# with open("text.txt", "a", encoding="utf-8") as f:
#     f.write("\nЕщё одна строка.")
#
# # Чтение бинарного файла
# with open("image.png", "rb") as f:
#     binary_data = f.read()
#
# # Запись бинарного файла
# with open("image_copy.png", "wb") as f:
#     f.write(binary_data)
#
# f = open("text.txt", "w", encoding="utf-8")
# f.write("Привет, мир!")  # Данные могут оставаться в буфере
# f.flush()  # Гарантирует запись в файл сразу


# r+: Открывает файл для чтения и записи. Файл должен существовать.
# w+: Открывает файл для чтения и записи. Если файл существует, его содержимое удаляется. Если файла нет, он создаётся.
# a+: Открывает файл для чтения и добавления. Если файла нет, он создаётся.

# Текстовые файлы (.txt, .csv) → содержат символы.
# Бинарные файлы (.jpg, .mp3, .zip) → содержат байты (числа от 0 до 255).
# with open("image.jpg", "rb") as f:
#     data = f.read()
# print(data[:10])  # Выведет первые 10 байтов

# b = b'fdfwjjs-'
# print(list(b))
#  # decode() — метод строк в Python, который применяется к объектам типа bytes для преобразования их в строку (str).
# s = b.decode('utf-8')
# print(s)

# 8.5 Datenstrukturen speichern und laden: Das Modul pickle
# pickle — это модуль для сериализации и десериализации объектов Python.
# Он позволяет сохранять объекты в файл или передавать их по сети.
#
# pickle.dump(obj, file) – записывает объект obj в файл.
# pickle.load(file) – загружает объект из файла.
# pickle.dumps(obj) – сериализует объект в строку байтов.
# pickle.loads(data) – десериализует объект из строки байтов.


# import pickle
# liste = [1 , 2 , 3]
# with open('liste.dat', 'wb') as stream:
#     pickle.dump(liste,stream)
#
# with open('liste.dat', 'rb') as stream:
#     liste = pickle.load(stream)
# print(liste)
#
# # planer.py
# from time import time
# import pickle
#
# PFAD = 'plan.dat'
# MENÜ = '''
# n: neue Aktivität eingeben
# d: dringendste Aktivitäten
# e: Ende
# '''
#
#
# def laden():
#     try:
#         with open(PFAD, 'rb') as f:
#             plan = pickle.load(f)
#     except:
#         plan = []
#     return plan
#
#
# def speichern(plan):
#     with open(PFAD, 'wb') as f:
#         pickle.dump(plan, f)
#
#
# def eingabe(plan):
#     aktivität = input('Aktivität: ')
#     stunden = input('In wie viel Stunden zu erledigen? ')
#     plan += [(int(stunden) * 3600 + time(), aktivität)]
#     speichern(plan)
#
#
# def ausgabe(plan):
#     plan.sort()
#     dringend = plan[0:2]
#     for deadline, aktivität in dringend:
#         restzeit = (deadline - time()) / 60
#         print('Noch', round(restzeit), 'Minuten für:',
#               aktivität)
#
#
# plan = laden()
# auswahl = 'x'
# while auswahl != 'e':
#     print(MENÜ)
#     auswahl = input('Auswahl: ')
#     if auswahl == 'n':
#         eingabe(plan)
#     elif auswahl == 'd':
#         ausgabe(plan)
# print('Bis bald!')

# 8.7 Daten im JSON-Format speichern
# load() / dump() – работают с файлами.
# loads() / dumps() – работают со строками.


# import json
# TEL = '''
# {"Tom": ["0172 567 343", "03202 67231"],
# "Anna" : [],
# "Tina": ["0210 834434"]}'''
# tel = json.loads(TEL)
# for name in tel.keys():
#     print(name, tel[name])


