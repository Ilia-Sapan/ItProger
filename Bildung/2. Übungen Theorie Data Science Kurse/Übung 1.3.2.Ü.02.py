# Programmiere eine Funktion, die die Standardabweichung einer Liste berechnen kann.
import math
from math import sqrt


import math

def standardabweichung(liste):
    mean_value = sum(liste) / len(liste)  # Среднее арифметическое
    variance = sum((el - mean_value) ** 2 for el in liste) / len(liste)  # Дисперсия
    return math.sqrt(variance)  # Корень из дисперсии = стандартное отклонение

st_sp_pro_woche = [2, 3, 7, 5, 3]
print(standardabweichung(st_sp_pro_woche))  # 2.0
