data = set("Hello") # Создает множество из уникальных букв
print(data)
data_1 = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4} # Без указания ключа мы создаем множество при помощи фигурных скобок
print(data_1)
data_1.add(32)
data_1.update(["32", True, 1, 4, 44, 55])
data_1.remove(1)
data_1.pop() # удалить первый элемент множества
data_1.clear() # очистить множество
nums = [1, 2, 3, 4, 5, 5, 5, 6, 4, 4, 4, 4]
nums = set(nums)
print(nums)
print(data_1)

new_data = frozenset([1, 2, 3, 4, 5, 6, 1, 2, True, "He"]) # Замороженные множества
print(new_data)