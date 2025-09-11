def min_max_scaling(liste):
    min_val = min(liste)
    max_val = max(liste)
    return list(map(lambda x: round((x - min_val) / (max_val - min_val), 3), liste))

# Пример списка
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_max_scaling(a))  # [0.0, 0.111, 0.222, 0.333, 0.444, 0.556, 0.667, 0.778, 0.889, 1.0]

