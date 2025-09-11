

# Импорт необходимых библиотек
import pandas as pd                  # для работы с табличными данными
import numpy as np                   # для массивов и чисел
import matplotlib.pyplot as plt      # для визуализации изображений

# === 1. Загрузка данных из CSV-файла ===
dateipfad = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial für Übungen\K4.0026_2.0_3.5.Ü.01_mnist_data.csv"        # путь к файлу (r - чтобы не экранировать \)
df = pd.read_csv(dateipfad, header=None)  # читаем CSV без заголовков

# === 2. Преобразуем DataFrame в список списков ===
# каждая строка будет выглядеть так: [метка, пиксель_1, пиксель_2, ..., пиксель_784]
daten_liste = df.values.tolist()

# === 3. Визуализация первых 4-х изображений на едином холсте ===
fig, achsen = plt.subplots(1, 4, figsize=(10, 5))  # создаём фигуру с 4 подграфиками по горизонтали

# Проходим по первым 4-м строкам датасета
for i in range(4):
    label = daten_liste[i][0]                        # метка (цифра, изображённая на картинке)
    pixelwerte = daten_liste[i][1:]                  # только значения пикселей
    bild = np.array(pixelwerte).reshape(28, 28)      # преобразуем список в 28x28 изображение

    achsen[i].imshow(bild, cmap="gray")              # рисуем изображение в оттенках серого
    achsen[i].set_title(f"Цифра: {label}")           # добавляем заголовок с меткой
    achsen[i].axis("off")                            # убираем оси (чтобы было красиво)

# === 4. Показать финальный холст с изображениями ===
plt.tight_layout()     # немного отступов, чтобы не налезали надписи
plt.show()             # отображаем всё

