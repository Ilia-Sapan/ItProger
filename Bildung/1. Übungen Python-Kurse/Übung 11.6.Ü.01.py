# a
import tkinter
from tkinter import *

from aiohttp.web_routedef import delete

# # Создаем окно
# fenster = Tk()
# # Создаем метку, которая будет отображать текст "Привет, мир!"
# label = Label(master=fenster, width=40, height=2, font=("Arial", 20), text="Hello, Welt!", anchor="center")
# # Размещаем метку на экране
# label.pack()
# # Запускаем главный цикл приложения
# fenster.mainloop()

# b
# fenster = Tk()
# label = Label(master = fenster, height=5, width= 30, anchor="center", bg="yellow")
# entry = Entry(fenster)
# entry.pack()
# label.pack()
# fenster.mainloop()

# c
# from tkinter import Tk, Label, Entry, Button
#
# # Функция для удаления текста из поля ввода
# def delete_text():
#     entry.delete(0, "end")
#
# # Функция для закрытия приложения
# def close_program():
#     fenster.quit()
#
# # Создаем основное окно
# fenster = Tk()
#
# # Создаем метку, поле ввода и кнопки
# label = Label(master=fenster, height=10, width=40, anchor="center")
# entry = Entry(fenster, width=30)
# button_1 = Button(master=fenster, text="Delete", command=delete_text, height=2, width=10)  # Кнопка для удаления текста
# button_2 = Button(master=fenster, text="Close", command=close_program, height=2, width=10)  # Кнопка для закрытия программы
#
# # Размещаем все элементы
# entry.pack()
# button_1.pack()
# button_2.pack()
# label.pack()
#
# # Запускаем главный цикл приложения
# fenster.mainloop()

# d
# from tkinter import Tk, Label, Entry, Button
#
# # Funktion zum Löschen des Textes
# def delete_text():
#     entry.delete(0, "end")
#
# # Funktion zum Schließen des Fensters
# def close_program():
#     fenster.quit()
#
# # Erstelle eine Liste von Tupeln (Button-Text, Funktion)
# button_data = [
#     ("Delete", delete_text),
#     ("Close", close_program)
# ]
#
# # Erstelle das Hauptfenster
# fenster = Tk()
#
# # Erstelle die Label und Entry Widgets
# label = Label(master=fenster, height=5, width=30, anchor="center", bg="yellow")
# entry = Entry(fenster)
#
# # Packe das Label und Entry
# label.pack()
# entry.pack()
#
# # Schleife, um die Buttons basierend auf der Liste hinzuzufügen
# for button_text, function in button_data:
#     button = Button(master=fenster, text=button_text, command=function)
#     button.pack()
#
# # Hauptloop starten
# fenster.mainloop()


# e

from tkinter import Tk, Label, Entry, Button

# Funktion zum Löschen des Textes
def delete_text():
    entry.delete(0, "end")

# Funktion zum Schließen des Fensters
def close_program():
    fenster.quit()

# Erstelle eine Liste von Tupeln (Button-Text, Funktion)
button_data = [
    ("Delete", delete_text),
    ("Close", close_program)
]

# Erstelle das Hauptfenster
fenster = Tk()

# Erstelle das Label und Entry Widgets
label = Label(master=fenster, height=5, width=30, anchor="center", bg="yellow")
entry = Entry(fenster)

# Packe das Label oben
label.pack(side="top", fill="x", pady=10)  # Das Label wird oben und in voller Breite angezeigt

# Packe das Entry Widget darunter
entry.pack(side="top", fill="x", pady=10)  # Entry-Widget wird ebenfalls oben angeordnet

# Schleife, um die Buttons am unteren Rand hinzuzufügen
for button_text, function in button_data:
    button = Button(master=fenster, text=button_text, command=function)
    button.pack(side="bottom", pady=10)  # Buttons werden am unteren Rand des Fensters angeordnet

# Hauptloop starten
fenster.mainloop()



















