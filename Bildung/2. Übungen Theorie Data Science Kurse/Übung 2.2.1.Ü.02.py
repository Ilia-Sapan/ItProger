# # Импортируем библиотеки
# import pandas as pd  # для работы с данными (таблицами)
# import matplotlib.pyplot as plt  # для построения графиков
# import statistics as st  # для статистических расчётов (среднее)
# import numpy as np  # для математических вычислений
#
# # Исходные данные (например: температура и число посетителей)
# x = [28, 23, 32, 35, 29, 30, 27, 34, 32]  # Температура в градусах
# y = [400, 60, 630, 660, 420, 590, 376, 620, 612]  # Количество посетителей
#
# # Строим точечную диаграмму, чтобы наглядно увидеть связь
# plt.scatter(x, y)
# plt.xlabel('Temperatur (температура)')
# plt.ylabel('Besuchenzahl (число посетителей)')
#
#
# # Функция для вычисления ковариации (меры совместного изменения двух переменных)
# def kovarianz(x, y):
#     mean_x = np.mean(x)  # среднее значение x
#     mean_y = np.mean(y)  # среднее значение y
#     summanden = []  # список для хранения промежуточных результатов
#
#     for i in range(len(x)):
#         # Здесь допущена ошибка в исходном коде, исправим её:
#         summand = (x[i] - mean_x) * (y[i] - mean_y)  # вычисляем разность от средних и их произведение
#         summanden.append(summand)  # добавляем результат в список
#
#     kovarianz = sum(summanden) / len(y)  # среднее произведение разностей — ковариация
#     return kovarianz
#
#
# # Функция для вычисления корреляции (степень связи двух переменных)
# def korrelation(x, y):
#     cov = kovarianz(x, y)  # получаем ковариацию с помощью ранее определённой функции
#     std_x = np.std(x)  # стандартное отклонение x (разброс температуры)
#     std_y = np.std(y)  # стандартное отклонение y (разброс посетителей)
#     korrelation = cov / (std_x * std_y)  # формула корреляции
#     return korrelation
#
#
# # Функция для вычисления коэффициентов линейной регрессии (наклона и пересечения)
# def lineareRegression(x, y):
#     mean_x = st.mean(x)  # среднее x
#     mean_y = st.mean(y)  # среднее y
#
#     std_x = np.std(x)  # стандартное отклонение x
#     std_y = np.std(y)  # стандартное отклонение y
#
#     # Коэффициент наклона (steigung), он показывает, насколько изменится число посетителей при изменении температуры
#     steigung = (std_y / std_x) * korrelation(x, y)
#
#     # Коэффициент пересечения (achsenabschnitt) — значение y, когда x=0
#     achsenabschnitt = mean_y - steigung * mean_x
#
#     return steigung, achsenabschnitt
#
#
# # Получаем коэффициенты линейной регрессии
# steigung, achsenabschnitt = lineareRegression(x, y)
#
#
# # Функция регрессионной прямой (по найденным коэффициентам строит прогнозное значение y для каждого x)
# def regressionsGerade(x):
#     return steigung * x + achsenabschnitt
#
#
# # Вычисляем значения модели (предсказания) для каждого значения x
# my_model = list(map(regressionsGerade, x))
#
# # Строим регрессионную прямую на графике
# plt.scatter(x, y, label='Исходные данные')  # исходные данные
# plt.plot(x, my_model, c="green", label='Линия регрессии')  # линия регрессии
# plt.xlabel('Температура')
# plt.ylabel('Количество посетителей')
# plt.legend()
# plt.show()
#
# # Предсказываем, сколько посетителей будет при температуре 33 градуса
# predict = steigung * 33 + achsenabschnitt
# print(f"Предсказанное число посетителей (при температуре 33°C): {predict:.2f}")
#
a = "2.2.3.Programmierung einer linearen Regression mit dem scipy-Modul"
print(a.upper())