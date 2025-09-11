# # nums = [1, 2, 3, 4, 4, 6, 7] # создание списка (массива данных) при помощи квадратных скобок
# # diff =["the Python", 5.44, 222, 1212.45, 212, True] # разные типы данных в списке
# #
# # nums[0] = 400 # Обращаюсь к списку по индексу, меняю его на 400
# # nums_in_nums = [[1, 2, 3], [2, 3, 5], [4, 5, 6]]
# # print(nums[6]) # Выведет на экран элемент списка с индексом 6 (7)
# # print(nums[-1]) # Выведет на экран элемент списка, первого с конца, т.е. в данном случае тоже (7)
# #
# # print(nums_in_nums[1][2]) # Обращается к элементу списка и  далее к элементу списка в списке (5)
#
# numbers = [1, 2, 3, 4]
# numbers.append(100) # метод .append() добавляет в конец списка необходимые данные
# print(numbers) # получится [1, 2, 3, 4, 100]
#
# numbers.insert(1, True) # метод .insert(x,y) добавляет элемент по индексу, где x это индекс, y это элемент
# print(numbers)
#
#
# b = [5, 6, 6]
# numbers. extend(b) # метод .extend() расширяет список, добавляя в конец ещё множество элементов
# print(numbers)
# numbers.sort() # метод .sort() сортирует элементы в списке по возрастанию
# numbers.reverse() # метод .reverse() все элементы переворачивает в обратную сторону
# print(numbers)
#
# numbers.pop() # метод .pop() удаляет последнее значение в списке
# numbers.remove(True) # метод .remove(x) удаляет конкретный элемент x
# print(numbers)
#
# numbers.clear() # метод .clear() полностью удаляет элементы
# print(numbers)
# print(numbers.count(6)) #метод .count(x) подсчитывает количество x в списке
# print(len(numbers)) # метод .len(x) выводит количество элементов списка, где x - список, его название
from nt import remove
from random import random

#Практические задания

# fruits = ["apple", "banana", "cherry", "apple"]
# print(fruits)
# fruits.append("orange")
# print(fruits)
# fruits.insert(1, "kiwi")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# berries = "strawberry", "blueberry", "raspberry"
# fruits.extend(berries)
# print(fruits)
# banana = fruits.count("banana")
# print(banana)
#
# # Подсчёт количества "banana"
# banana_count = fruits.count("banana")
# print(banana_count)
#
# # Сортируем список и выводим его длину
# fruits.sort()
# print(fruits)
# print(len(fruits))
#
# Задание 2
#
# numbers = [] #создаем список
# numbers.extend(range(1,11)) #расширяем список при помощи метода extend and range
# print(f"Вот список всех чисел: {numbers}") #показываем
# for num in numbers: # перебираем каждый элемент списка
#     if num %2==0: #выставляем условие четности
#         numbers.remove(num) #если чётное, удаляем
# print(f"Вот чётные числа {numbers}") #вывели все числа без четных
# numbers.extend(range(11,16)) # Добавляем в конец списка числа от 11 до 15
# print(f"Вот список с добавленными числами {numbers}") #Выводим обновленный список
# result = sum(numbers) #Используем функцию sum
# print(f"Сумма элементов в списке равно {result}.") #Выводим результат
# doubled = [x * 2 for x in numbers] # удваиваем
# print(f"Удвоенный список {doubled}.")
# doubled.sort() # метод .sort() сортирует элементы в списке по возрастанию
# doubled.reverse() # метод .reverse() все элементы переворачивает в обратную сторону
# print(f"Вот список {doubled}. И его длина равна {len(doubled)}!")
#
# # Создаем список
# numbers = []
# numbers.extend(range(1, 11))  # Расширяем список числами от 1 до 10
# print(f"Вот список всех чисел: {numbers}")
#
# # Удаляем чётные числа
# numbers = [num for num in numbers if num % 2 != 0]  # Используем списковое включение для фильтрации
# print(f"Вот список без чётных чисел: {numbers}")
#
# # Добавляем числа от 11 до 15
# numbers.extend(range(11, 16))  # Добавляем числа в конец списка
# print(f"Вот список с добавленными числами: {numbers}")
#
# # Сумма всех чисел
# result = sum(numbers)  # Суммируем элементы списка
# print(f"Сумма элементов в списке равна {result}.")
#
# # Умножение каждого элемента на 2
# doubled = [x * 2 for x in numbers]  # Создаем новый список с удвоенными элементами
# print(f"Удвоенный список: {doubled}")
#
# # Сортируем список по убыванию
# doubled.sort(reverse=True)  # Сортируем по убыванию
# print(f"Вот отсортированный список: {doubled}")
#
# # Длина списка
# print(f"Длина списка равна {len(doubled)}!")

# Задача 3

#
#
from random import randint
#
# numbers = []
# for num in range(10):
#     numbers.append(randint(1, 50))
# print(f"Минимальное число - это {min(numbers)}, максимальное число в списке - это {max(numbers)}!")
# min_value = min(numbers) # Обозначаем минимальное число
# max_value = max(numbers) # Обозначаем максимальное число
# numbers = [0 if num == min_value else 100 if num == max_value else num for num in numbers]
# print(numbers) #Выводим обновленный список с заменой минимума и максимума
# numbers = [num for num in numbers if num %3 ==0]
# print(numbers)
# result = sum(numbers) # Создаем переменную суммы
# print(f"Сумма чисел равно {result}") #Выводим сумму
# numbers = [num*3 for num in numbers]
# print(f"Вот умноженные на три числа: {numbers}!")
# numbers.sort(reverse=True)
# print(f"Вот вам в порядке убывания: {numbers}, а вот и длинна списка: {len(numbers)}.")


# numbers = []
# numbers.extend(range(1,11))
# numbers = [num**2 for num in numbers if num %2 ==0]
# print(numbers)
#
# fruits = ["apple", "banana", "cherry", "kiwi", "orange", "grape"]
# #Создаёт новый список, содержащий строки длиной более 5 символов, переведённые в верхний регистр
# fruits = [str(fruit).upper() for fruit in fruits if len(fruit)>5]
# print(fruits)
#
# #Задача 1: Кратные числа
# numbers = [] # Создаем пустой список
# numbers.extend(range(1,51)) #Расширяем список при помощи метода .range(), генерирующего числа от 1 до 50 включительно
# numbers = [num*2 for num in numbers if num % 3 == 0 and num % 5 ==0]# Создаем списковое включение, выставляем релевантные условия
# print(numbers) # Выводим числа на экран
#
# #Задача 2: Обратные строки
# # Дан список
# languages = ["python", "java", "c++", "ruby", "go", "javascript"]
#
# # Строки длиной менее 5 символов преобразуем в верхний регистр
# short_languages = [language.upper() for language in languages if len(language) < 5]
# print(short_languages)
#
# # Строки длиной 5 и более символов переворачиваем
# long_languages = [language[::-1] for language in languages if len(language) >= 5]
# print(long_languages)
# # Создаём список чисел от 1 до 20
# nummy = list(range(1, 21))
#
# # Формируем новый список с условиями FizzBuzz
# nummy = [
#     "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
#     "Fizz" if num % 3 == 0 else
#     "Buzz" if num % 5 == 0 else
#     num
#     for num in nummy
# ]
#
# # Выводим итоговый список
# print(nummy)
#
# # Создаём список строк
# words = ["apple", "banana", "kiwi", "cherry", "pear", "orange", "grape"]
# # Гласные буквы
# vowels = "aeiou"
# # Формируем новый список
# words = [
#     word.upper() if word[0] in vowels else word.lower()
#     for word in words
# ]
# # Сортируем список по длине строки
# words.sort(key=len)
# # Выводим результат
# print(words)

# numbers = list(range(1,21))
# numbers = [
#     "Even" if num % 2 == 0 else
#     "Odd" if num % 2 != 0 else
#     num
#     for num in numbers
# ]
#
# numbers_count = numbers.count("Even")
# numbers_count_1 = numbers.count("Odd")
#
# print(f"Вот тебе список {numbers}.\nВот количество чётных - {numbers_count}.\nНечётных - {numbers_count_1}.")