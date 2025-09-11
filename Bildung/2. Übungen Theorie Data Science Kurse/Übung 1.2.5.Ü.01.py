import math

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

# Данные (классы + признаки)
y = ["positive", "positive", "negative", "positive", "negative"]  # Целевая переменная
feature1 = [0, 0, 1, 1, 0]  # Признак 1
feature2 = [0, 1, 0, 1, 0]  # Признак 2

# Вычисляем IG для каждого признака
ig_feature1 = information_gain(y, feature1)
ig_feature2 = information_gain(y, feature2)
print(f'Энтропия для данных составляет: {round(entropy(y),4)}')
print(f"IG для признака 1: {round(ig_feature1, 4)}")
print(f"IG для признака 2: {round(ig_feature2, 4)}")
