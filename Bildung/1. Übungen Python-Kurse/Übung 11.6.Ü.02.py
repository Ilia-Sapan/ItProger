import tkinter
from tkinter import *
def change_but():
    button.config(text = "Button wurde geklickt!")
    label.config(text = "Ooops!..")
# создаем окно
fenster = Tk()
# называем окно
fenster.title("Mein GUI")
fenster.resizable(False, False) # Запрещаем перемены размера


# добавляем лейбл
label = Label(master = fenster, width=40, height=2, font=("Arial", 16),
              text="Willkommen zu deinem GUI!", bg="blue")
# Добавляем кнопку
button = Button(master=fenster, text="Klick mich!",command = change_but, height=2, width=20, anchor="center")

button.pack(pady=20)  # Размещаем кнопку с отступом

button.pack()
label.pack()
fenster.mainloop()
