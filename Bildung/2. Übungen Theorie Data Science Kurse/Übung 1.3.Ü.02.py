def median(liste) -> float:  # float, потому что медиана может быть дробной
    liste.sort()  # Убедимся, что список отсортирован
    elements_lang = len(liste)

    if elements_lang % 2 == 0:
        num_1 = liste[elements_lang // 2 - 1]  # Левая середина
        num_2 = liste[elements_lang // 2]  # Правая середина
        return (num_1 + num_2) / 2
    else:
        return liste[elements_lang // 2]  # Средний элемент


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]

print(median(a))  # 3
print(median(b))  # 2.5
