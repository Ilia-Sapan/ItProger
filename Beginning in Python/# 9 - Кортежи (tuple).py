# Кортежи - это те же списки, только в которых невозможно производить изменения
# Используются для передачи данных, потому что пользователь не может их видоизменить
#
# data = (1, 2, 3, 4, True, "Hello", 2, 2, 3, 2)
# print(data[0]) # Обращаемся к списку по индексу
# print(data[2:4]) # Делаем срез
#
# print(data.count(2)) # Считаем количество элементов "2" в списке
# print(len(data)) # Длина кортежа
#
# data_new = 4, 5, 6, True, False # Кортеж может быть создан без скобок
#
# # Чтобы из списка создать кортеж используется функция .tuple()
# numbers = [1, 2, 3, 4, 5]
# new_numbers = tuple(numbers) # создаем новую переменную и используем функцию .tuple()
#
# word = "Hello, world!"
# word_new = tuple(word) # Образуется список ('H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l',...) и т.д.
# print(word_new)

#
#
# #Создание и работа с индексами
# my_tuple = (1, 2, 3, True, "Hello", "Marcy")
# print(f"Первый элемент в кортеже это {my_tuple[0]}, последний это {my_tuple[-1]}, а с индексом 2 это {my_tuple[2]}.")
# #Работа со срезами
# slice_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(slice_tuple[:3])
# print(slice_tuple[-3:])
# print(slice_tuple[2:6])
# #Подсчёт элементов
# count_tuple = (1, 1, 1, 3, 4, 5, 6, 66, 66, 66, 66)
# print(f"Число 1 встречает {count_tuple.count(1)} раз(а).")
# #Преобразование
# words = "Python is fun"
# words_new = tuple(words)
# print(words_new)
#
# lists = list(range(1,6))
# l_1 = tuple(lists)
# print(l_1)
#
# # Сравнение кортежей
# city = ("London", "Paris", "Rome", "Berlin", "Köln")
# city_user = ("London", "Paris", "Berlin", "Frankfurt", "Moscow")
#
# # Количество совпадающих значений
# count = 0
# # Количество совпадений по значениям и индексам
# count_1 = 0
#
# # Используем один цикл
# for i in range(len(city)):
#     if city[i] in city_user:
#         count += 1
#     if city[i] == city_user[i]:
#         count_1 += 1
#
# print(f"В кортежах количество одинаковых значений: {count}, а количество совпадений по индексу: {count_1}.")
#
# # Кортеж и словарь
# keylogger = dict(key1 = 1, key2 = 2, key3 = 3)
# print(keylogger)
#
# #Максимальное и минимальное значение
# cortage = (1, 2, 3, 4, 5, 6, 8)
# print(max(cortage)-min(cortage))
# print(cortage.index(max(cortage)))
# print(cortage.index(min(cortage)))
#
# #Объединение и сортировка
# numbers_one = (7, 5, 3)
# numbers_two = (2, 8, 6)
# numbers_three = numbers_one + numbers_two
# numbers_sorted = tuple(sorted(numbers_three))
# print(numbers_sorted)


