# Значок * даёт возможность кортежу names распаковать элементы
#f-strings
# метод .format() подставляет переменные в порядке их написания
# 1 это индекс переменной "age" в .format(), и т.д.
# функция round(x, y) Округляет переменную x до y знаков
#import math
#value = 5.2
#print(math.ceil(value))   # Результат: 6 идет к верхнему результату
#print(math.floor(value))  # Результат: 5 идет к нижнему результату
#print(math.sqrt(16))          # Квадратный корень: 4.0
#print(math.log(8, 2))         # Логарифм по основанию 2: 3.0
#print(math.sin(math.radians(90)))  # Синус 90 градусов: 1.0
#numbers = [3, 5, -2, 9, 12]
#max_value = numbers[0]  # Начинаем с первого элемента
#for number in numbers:
#    if number > max_value:
#        max_value = number  # Обновляем max_value, если нашли большее число
#print(f"Максимальное значение: {max_value}") # Вывод: Максимальное значение: 12
from logging import exception

#Задание №1
coordinations = (2, 4, 6, 8, 10) #Заданы точки координат
first, *others, last = coordinations
print(f"Первая координата это {first}.")
print(f"Прочие это {others}")
print(f"А последняя это {last}.")
#Задание 2
DB = (1994, 6, 15)
a, b, c = DB
print(f"Чувачок родился в {a} году, {b} месяца и {c} дня.")

#Задание 3
fruits = ("Яблоко", "Банан", "Груша", "Апельсин")
first, second, *others = fruits
print(f"Первый фрукт это {first}.")
print(f"Второй фрукт это {second}.")
print(f"Все остальные фрукты это {others}.")

#Задание № 4
Zählen = (1, 3, 5, 7, 9, 11, 13, 15)
first, second, third, *others = Zählen
print(f"Первый элемент кортежа это {first}, второй это {second}, третий это {third}, а все остальные это {others}.")

#Задание № 5

numbers = (10, 20, 30, 40)
animals = ("кот", "собака", "мышь")
alphabet = ("a", "b", "c", "d")
general_tuple = list((numbers, animals, alphabet)) # кортеж кортежей переводим в список
first_elements_all = list((general_tuple[0][0],general_tuple[1][0], general_tuple[2][0])) #обращаемся только к первым элементам списка
a, b, c = first_elements_all #присваиваем первым элементам переменные
a, *others = numbers
print(list(others))
b, *others = animals
print(list(others))
c, *others = alphabet
print(list(others))






