import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sympy.stats.sampling.sample_numpy import numpy

# Полиномиальная регрессия – это расширение линейной регрессии,
# при котором зависимость между независимой переменной (или переменными)
# и целевой переменной моделируется с использованием полинома.
# Это позволяет учитывать нелинейные зависимости между переменными.

# Наборы данных x и y
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 99, 99, 99, 100]

# 1) Визуализируем исходные данные на диаграмме рассеяния (scatter plot)
plt.scatter(x, y)            # plt.scatter(X-координаты, Y-координаты)
# plt.show()                   # Показываем график

# 2) Строим полиномиальные модели разной степени (1, 2, 3, 4)

# Модель 1-й степени (линейная регрессия):
my_model1 = np.poly1d(np.polyfit(x, y, 1))
# Модель 2-й степени (квадратичная регрессия):
my_model2 = np.poly1d(np.polyfit(x, y, 2))
# Модель 3-й степени:
my_model3 = np.poly1d(np.polyfit(x, y, 3))
# Модель 4-й степени:
my_model4 = np.poly1d(np.polyfit(x, y, 4))

# 3) Готовим диапазон значений, на которых будем строить кривые наших моделей
myline = np.linspace(1, 25, 100)
# linspace(начало, конец, количество точек) — вернёт 100 равномерно распределённых точек от 1 до 25

# 4) Визуализируем исходные точки и полученные модели на одном графике

plt.scatter(x, y)                   # Снова рисуем исходные точки
plt.plot(myline, my_model1(myline), label='Grad 1')  # Кривая для модели 1-й степени
plt.plot(myline, my_model2(myline), label='Grad 2')  # Кривая для модели 2-й степени
plt.plot(myline, my_model3(myline), label='Grad 3')  # Кривая для модели 3-й степени
plt.plot(myline, my_model4(myline), label='Grad 4')  # Кривая для модели 4-й степени

plt.legend()    # Добавляем легенду, чтобы отличать кривые
plt.show()      # Отображаем итоговый график













