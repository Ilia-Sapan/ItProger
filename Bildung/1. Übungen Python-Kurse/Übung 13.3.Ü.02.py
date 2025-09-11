import os


def ist_sortiert(numbers_list):
    return all(numbers_list[i] <= numbers_list[i + 1] for i in range(len(numbers_list) - 1))


def verbessere_quicksort(numbers_list) -> list:
    '''Die Funktion, die den Quicksort-Algorithmus implementiert und zusätzlich eine Verbesserung beinhaltet'''

    # Проверка, отсортирован ли список
    assert not ist_sortiert(numbers_list), 'Die Liste ist bereits sortiert!'

    if len(numbers_list) <= 1:
        return numbers_list
    else:
        pivot = numbers_list[len(numbers_list) // 2]
        left = [x for x in numbers_list if x < pivot]
        middle = [x for x in numbers_list if x == pivot]
        right = [x for x in numbers_list if x > pivot]

        # Проверка переменной среды DEBUG и вывод для отладки
        if os.getenv('DEBUG') == 'True':
            print(f"Vor der Sortierung: {numbers_list}")
            print(f"Aufspaltung: {left}, {middle}, {right}")

        # Рекурсивная сортировка
        sorted_list = verbessere_quicksort(left) + middle + verbessere_quicksort(right)

        if os.getenv('DEBUG') == 'True':
            print(f"Nach der Sortierung: {sorted_list}")

        return sorted_list


# Пример использования:
my_list_0 = [22, 44, 5, 6, 17, 14, 67, 33, 896, 596, 475]

# Убедитесь, что переменная среды DEBUG установлена в True, если хотите увидеть отладочную информацию
os.environ['DEBUG'] = 'True'

probe_0 = verbessere_quicksort(my_list_0)
print(f"Endergebnis: {probe_0}")
