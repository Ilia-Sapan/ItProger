import math
import pandas as pd

# Функция для вычисления энтропии
def entropy(data):
    """
    Вычисляет энтропию множества data.
    """
    total = len(data)  # Общее количество элементов
    counts = {}  # Словарь для хранения количества классов

    for item in data:  # Подсчитываем классы
        counts[item] = counts.get(item, 0) + 1

    probabilities = [count / total for count in counts.values()]  # Вероятности
    return -sum(p * math.log2(p) for p in probabilities)  # Формула энтропии

# Функция для вычисления информационного выигрыша
def information_gain(data, feature_values):
    """
    Вычисляет IG для одного признака.
    y - список классов (целевая переменная)
    feature_values - список значений признака
    """
    H_before = entropy(data)  # Энтропия до разбиения
    unique_values = set(feature_values)  # Уникальные значения признака
    total = len(data)

    H_after = 0  # Начальная энтропия после разбиения
    for value in unique_values:
        subset = [data[i] for i in range(total) if feature_values[i] == value]  # Выбираем элементы с этим значением
        H_after += (len(subset) / total) * entropy(subset)  # Взвешенная энтропия

    return H_before - H_after  # Возвращаем IG

 # Функция для вычисления отношения выигрыша
def gain_ratio(data,feature_values):
    a = information_gain(data,feature_values)
    b = entropy(feature_values)
    ration_gain = a / b
    return ration_gain

# def gain_ratio(data, feature_values):
#     IG = information_gain(data, feature_values)
#     total = len(data)
#     # Считаем SplitInformation (энтропию распределения feature_values)
#     from math import log2
#
#     # Подсчитаем доли для каждого значения признака
#     unique_vals = set(feature_values)
#     split_info = 0
#     for val in unique_vals:
#         subset_len = sum(1 for fv in feature_values if fv == val)
#         p = subset_len / total
#         split_info -= p * log2(p)  # энтропия признака
#
#     # Если split_info == 0, во избежание деления на ноль, возвращаем IG
#     if split_info == 0:
#         return IG
#     else:
#         return IG / split_info


file = r"C:\Users\isapa\Desktop\DS Kurse\Prüfungsrelevantes Zusatzmaterial\K4.0026_2.0_1.5.C.01_ProjectData.xlsx"
df = pd.read_excel(file)
# print(df.to_string())

data = df['Draussen Essen']

wetteraussicht = df['Wetteraussicht']
temperaturkategorie = df['Temperaturkategorie']
luftfeuchtigkeit = df['Luftfeuchtigkeit']
windstärke = df['Windstärke']




print(f'Энтропия данных об уличной торговле: {round(entropy(data), 4)}') # 0.9403
print(gain_ratio(data,wetteraussicht))