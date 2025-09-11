def z_score_scaling(liste):
    mean_value = sum(liste) / len(liste)
    std_dev = (sum((el - mean_value) ** 2 for el in liste) / len(liste)) ** 0.5  # Стандартное отклонение
    return list(map(lambda x: round((x - mean_value) / std_dev, 3), liste))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(z_score_scaling(a))  # [-1.57, -1.22, -0.87, ... , 1.57]
