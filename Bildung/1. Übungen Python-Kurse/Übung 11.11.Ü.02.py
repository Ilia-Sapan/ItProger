from tkinter import *  # Импортируем все необходимые компоненты из Tkinter для создания графического интерфейса

# Функция, которая изменяет фон окна в зависимости от выбранного радиокнопки
def farbe_aendern():
    wahl = farbwahl.get()  # Получаем выбранное значение радиокнопки
    if wahl == 'A':  # Если выбран первый вариант
        fenster.config(bg='red')  # Изменяем цвет фона на красный
    elif wahl == 'B':  # Если выбран второй вариант
        fenster.config(bg='green')  # Изменяем цвет фона на зеленый
    elif wahl == 'C':  # Если выбран третий вариант
        fenster.config(bg='blue')  # Изменяем цвет фона на синий

# Функция для сброса фона и очищения выбранной радиокнопки
def zuruecksetzen():
    fenster.config(bg='SystemButtonFace')  # Восстанавливаем стандартный фон окна
    farbwahl.set(None)  # Сбрасываем выбор радиокнопки

fenster = Tk()  # Создаем главное окно приложения
fenster.title("Farbwahl Quiz")  # Устанавливаем заголовок окна

farbwahl = StringVar(value=None)  # Создаем переменную для хранения выбранного значения радиокнопки, начальное значение None

# Создаем радиокнопки для выбора цвета
rb_rot = Radiobutton(fenster, text="Rot", variable=farbwahl, value='A')  # Красная кнопка
rb_gruen = Radiobutton(fenster, text="Grün", variable=farbwahl, value='B')  # Зеленая кнопка
rb_blau = Radiobutton(fenster, text="Blau", variable=farbwahl, value='C')  # Синяя кнопка

# Создаем кнопки для подтверждения и сброса
btn_bestätigen = Button(fenster, text="Bestätigen", command=farbe_aendern)  # Кнопка "Подтвердить"
btn_zuruecksetzen = Button(fenster, text="Zurücksetzen", command=zuruecksetzen)  # Кнопка "Сбросить"

# Размещаем элементы на сетке (grid)
rb_rot.grid(row=0, column=0)  # Размещение красной радиокнопки в первой строке и первом столбце
rb_gruen.grid(row=1, column=0)  # Размещение зеленой радиокнопки во второй строке и первом столбце
rb_blau.grid(row=2, column=0)  # Размещение синей радиокнопки в третьей строке и первом столбце
btn_bestätigen.grid(row=3, column=0)  # Размещение кнопки "Подтвердить" в четвертой строке
btn_zuruecksetzen.grid(row=3, column=1)  # Размещение кнопки "Сбросить" в четвертой строке и втором столбце

fenster.mainloop

