# Импортируем библиотеку tkinter для создания графического интерфейса
import tkinter as tk
# Импортируем filedialog для открытия файлов через диалоговое окно
from tkinter import filedialog
# Импортируем Thread для запуска файлового процесса в отдельном потоке
from threading import Thread

# Функция для загрузки файла
def datei_laden():
    # Вложенная функция, которая выполняет загрузку файла
    def laden():
        # Открываем диалоговое окно выбора файла и получаем путь к нему
        pfad = filedialog.askopenfilename()
        if pfad:  # Если файл был выбран
            with open(pfad, "r", encoding="utf-8") as file:
                text = file.read()  # Читаем содержимое файла
                text_widget.delete('1.0', tk.END)  # Очищаем текстовое поле
                text_widget.insert('1.0', text)  # Вставляем текст из файла в текстовое поле

    # Запускаем загрузку файла в отдельном потоке, чтобы не завис интерфейс
    thread = Thread(target=laden)
    thread.start()

# Функция для отображения выбранной пользователем опции из радиокнопок
def auswahl_anzeigen():
    ausgewaehlte_obstsorte = obst_var.get()  # Получаем значение выбранного варианта
    auswahl_label.config(text="Ausgewählt: " + ausgewaehlte_obstsorte)  # Обновляем текст метки

# Создаём главное окно приложения
fenster = tk.Tk()
fenster.title("Obstauswahl und Dateiöffner")  # Устанавливаем заголовок окна

# Переменная для хранения выбранного варианта
obst_var = tk.StringVar()

# Создаём радиокнопки с вариантами выбора фруктов
radiobuttons = [("Äpfel", "Äpfel"), ("Bananen", "Bananen"), ("Orangen", "Orangen")]
for obst, value in radiobuttons:
    rb = tk.Radiobutton(fenster, text=obst, variable=obst_var, value=value, command=auswahl_anzeigen)
    rb.pack(anchor=tk.W)  # Размещаем кнопку в окне

# Метка, отображающая выбранный фрукт
auswahl_label = tk.Label(fenster, text="Bitte wähle eine Obstsorte.")  # Текстовая метка
auswahl_label.pack()  # Добавляем в окно

# Кнопка для открытия файла
oeffnen_button = tk.Button(fenster, text="Datei öffnen", command=datei_laden)
oeffnen_button.pack()

# Текстовое поле для отображения содержимого файла
text_widget = tk.Text(fenster, height=10, width=50)
text_widget.pack()

# Кнопка для закрытия окна
schliessen_button = tk.Button(fenster, text="Schließen", command=fenster.destroy)
schliessen_button.pack()

# Запускаем главный цикл обработки событий
fenster.mainloop()
