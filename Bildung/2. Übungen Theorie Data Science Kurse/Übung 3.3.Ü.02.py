# Вручную

# I = [0.9, 0.1, 0.8]
# Wih = [[0.9, 0.2, 0.1], [0.3, 0.8, 0.5], [0.4, 0.2, 0.6]]
# Who = [[0.3, 0.6, 0.8], [0.7, 0.5, 0.1], [0.5, 0.2, 0.9]]
#
# H = []
# O = []
# for elements in Wih:
#     for numbers, num in zip(elements, I):
#         H.append(round((numbers * num),2)) # [0.81, 0.02, 0.08, 0.27, 0.08, 0.4, 0.36, 0.02, 0.48]
#         sums = [sum(H[i:i+3]) for i in range(0, len(H), 3)]
#
#
#
# for elements in Who:
#     for numbers, num in zip(elements, sums):
#         O.append((numbers * num))
#         sums_new = [sum(O[i:i+3]) for i in range(0, len(O), 3)]
#
# print(sums_new) # [1.411, 1.098, 1.379]

# С NumPy
import numpy as np
import scipy.special

I = np.array([0.9, 0.1, 0.8])
Wih = np.array([[0.9, 0.2, 0.1],
                [0.3, 0.8, 0.5],
                [0.4, 0.2, 0.6]])

Who = np.array([[0.3, 0.6, 0.8],
                [0.7, 0.5, 0.1],
                [0.5, 0.2, 0.9]])

# # Сначала умножаем вход на Wih.T (транспонируем!)
# H = np.dot(I, Wih.T)
#
# # Потом умножаем результат на Who.T (тоже транспонируем!)
# O = np.dot(H, Who.T)
#
# print("Результат H:", H)        # [0.91 0.75 0.86]
# print("Результат O:", O)        # [1.411 1.098 1.379]

# Сигмоида в SciPy

from scipy.special import expit
# # Функция expit – это надежный альтернативный вариант сигмоиды.
# print(expit(-1000))  # Результат: 0.0, даже при больших отрицательных значениях результат стабилен





