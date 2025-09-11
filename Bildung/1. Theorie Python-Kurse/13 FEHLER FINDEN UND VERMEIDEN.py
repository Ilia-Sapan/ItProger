from sympy.polys.subresultants_qq_zz import pivot


def verdopple(x):
    assert type(x) in [int, float]
    return 2 * x

verdopple(5) # ничего не произойдет, т.к. assert — это встроенная
# конструкция в Python для проверки условий во время выполнения программы,
# но если есть ошибка в условии, будет AssertionError

def entferne_min(s):
    'Entferne das Minimum in der Liste s.'
    assert type(s) in [list]
    m = min(s)
    s.remove(m)
    return s

s =  [1,2,3,4,5]
print(entferne_min(s))

from random import randint


def quicksort(s):
    # Если список содержит 0 или 1 элемент, он уже отсортирован, возвращаем его
    if len(s) <= 1:
        return s
    else:
        # Выбираем первый элемент списка как "опорный" (pivot)
        pivot = s[0]

        # Создаем список s1, куда помещаем все элементы, которые меньше pivot
        s1 = [x for x in s[1:] if x < pivot]

        # Создаем список s2, куда помещаем все элементы, которые больше или равны pivot
        s2 = [x for x in s[1:] if x >= pivot]

        # Если код выполняется напрямую (а не импортируется как модуль), выводим промежуточные шаги
        if __name__ == '__main__':
            print("Ich sortiere: ", s)  # Вывод текущего списка, который обрабатывается
            print('Aufspaltung:', s1, pivot, s2)  # Вывод разбиения списка

        # Рекурсивно сортируем s1 и s2 и объединяем их с pivot
        return quicksort(s1) + [pivot] + quicksort(s2)


# Если код выполняется напрямую, запускаем сортировку
if __name__ == '__main__':
    s = [17, 7, 85, 15, 11, 20, 9, 5, 87]  # Исходный список
    print('Sortierte Liste:', quicksort(s))  # Выводим отсортированный список
    input()  # Ожидаем нажатия клавиши перед закрытием программы (актуально для Windows)

# 13.3 Debugging mit IDLE
    