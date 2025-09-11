from tkinter import Tk, Label, Button, Entry, Radiobutton, Text, StringVar, END  # Импортируем все необходимые компоненты из Tkinter
from datetime import datetime  # Импортируем datetime для работы с датой и временем

# Функция для получения текущего времени в строковом формате
def aktuelle_zeit_als_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Возвращаем текущую дату и время в формате "Год-Месяц-День Часы:Минуты:Секунды"

# Функция для отображения приветствия
def begruessung():
    name = name_entry.get()  # Получаем имя, введенное пользователем в поле ввода
    zeit = zeit_var.get()  # Получаем выбранное время суток (например, "Guten Tag") из радиокнопок
    begruessungstext = f"{zeit}, {name}!"  # Формируем приветственное сообщение
    begruessungslabel.config(text=begruessungstext)  # Обновляем текст метки с приветствием
    log.insert(END, f"{aktuelle_zeit_als_string()}: {begruessungstext}\n")  # Вставляем в журнал текущее время и приветствие

# Основное окно приложения
app = Tk()
app.title("Begrüßungs-App")  # Устанавливаем заголовок окна

# Поле для ввода имени
name_entry = Entry(app)  # Создаем поле для ввода имени
name_entry.grid(row=0, column=1, padx=10, pady=10)  # Размещаем поле ввода на сетке в строке 0, столбце 1 с отступами

# Метка для отображения приветственного сообщения
begruessungslabel = Label(app, text="", font=('Arial', 16))  # Создаем метку для отображения приветствия
begruessungslabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Размещаем метку на сетке, она занимает 2 столбца

# Кнопка для запуска функции приветствия
begrussungsbutton = Button(app, text="Begrüßen", command=begruessung)  # Создаем кнопку с текстом "Begrüßen"
begrussungsbutton.grid(row=0, column=2, padx=10, pady=10)  # Размещаем кнопку на сетке в строке 0, столбце 2 с отступами

# Переменная для хранения выбранного времени суток
zeit_var = StringVar()
zeit_var.set("Guten Tag")  # Устанавливаем значение по умолчанию — "Guten Tag"

# Радиокнопки для выбора времени суток
Radiobutton(app, text="Guten Morgen", variable=zeit_var, value="Guten Morgen").grid(row=2, column=0)  # Утро
Radiobutton(app, text="Guten Tag", variable=zeit_var, value="Guten Tag").grid(row=2, column=1)  # День
Radiobutton(app, text="Guten Abend", variable=zeit_var, value="Guten Abend").grid(row=2, column=2)  # Вечер

# Многострочное поле для отображения журнала
log = Text(app, height=10, width=50)  # Создаем текстовое поле для отображения лога
log.grid(row=3, column=0, columnspan=3, padx=10, pady=10)  # Размещаем поле на сетке, оно занимает 3 столбца

# Запуск главного цикла приложения
app.mainloop()
