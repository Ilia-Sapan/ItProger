# Aufgabe:  Programmierübung – Der Insertion-Sort-Algorithmus


liste = [8,2,6,4,5]

# def insertionsort(array):
#     # Проходим по всем элементам начиная с индекса 1
#     for i in range(1, len(array)):
#         # Сохраняем текущий элемент для дальнейшего поиска его позиции
#         key_element = array[i]
#         # Устанавливаем индекс для элемента перед текущим
#         j = i - 1
#
#         # Сдвигаем элементы массива, которые больше текущего, на одну позицию вправо
#         while j >= 0 and key_element < array[j]:
#             array[j + 1] = array[j]  # Сдвигаем элемент
#             j = j - 1  # Переходим к предыдущему элементу
#
#         # Вставляем текущий элемент на его правильное место
#         array[j + 1] = key_element
#
# # Выводим список до сортировки
# print(liste)
#
# # Вызываем функцию сортировки
# insertionsort(liste)
#
# # Выводим отсортированный список
# print(liste)


