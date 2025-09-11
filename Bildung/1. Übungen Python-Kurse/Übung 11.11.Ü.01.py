import tkinter
from tkinter import *

# Функции
def ok():
    okay = entry.get()  # Получаем введенную строку
    label.config(text = f"Willkommen, {okay}!")  # Обновляем текст метки с использованием введенного имени

def abbrechen():
    app.quit()  # Завершаем приложение

# Основное окно приложения
app = Tk(screenName="GUI")
app.title("Mein erstes GUI-Programm")
app.geometry("400x200")  # Устанавливаем размер окна

# Виджет ярлыка с приветствием
label = Label(app, text="Willkommen zu meinem Programm!", font=('Arial', 14),
              bg="yellow", fg="blue", anchor="center")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Виджет для ввода текста (ширина 40 символов)
entry = Entry(master=app, width=40)
entry.grid(row=1, padx=10, pady=10)  # Добавляем отступы для лучшего визуального восприятия

# Кнопка "ОК"
ok_button = Button(app, text="OK", command=ok)
ok_button.grid(row=2, column=0, padx=10, pady=10)  # Добавляем отступы для выравнивания

# Кнопка "Abbrechen"
abb_button = Button(app, text="Abbrechen", command=abbrechen)
abb_button.grid(row=2, column=1, padx=10, pady=10)

# Запуск главного цикла приложения
app.mainloop()
