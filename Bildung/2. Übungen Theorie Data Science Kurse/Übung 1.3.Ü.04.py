data = [3, 1, 2, 3, 4, 3, 5, 2, 2, 2]

def modus(data):
    sammlung = {}

    for elements in data:
        sammlung[elements] = data.count(elements)
    a = max(list(sammlung.values()))
    b = [keys for keys, values in sammlung.items() if values == a]
    b = set(b)
    return b






print(modus(data))

# oder

from collections import Counter

def modus(data):
    count = Counter(data)  # Создаём словарь {элемент: частота}
    max_count = max(count.values())  # Ищем максимальную частоту
    return {key for key, val in count.items() if val == max_count}  # Множество модусов

data = [3, 1, 2, 3, 4, 3, 5, 2, 2, 2]
print(modus(data))  # {2, 3}