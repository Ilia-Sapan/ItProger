# # #2
# # from idlelib.pyshell import usage_msg
# #
# #
# # def log():
# #     try:
# #         # Ввод чисел от пользователя через пробел
# #         user_points = input("Введите числа через пробел: ")
# #         user_points_int = list(map(int, user_points.split()))  # Преобразуем ввод в список чисел
# #
# #         # Ввод особого числа k
# #         k = int(input("Введите число k: "))
# #
# #         # Разделяем числа на делимые и неделимые на k
# #         k_ja = [num for num in user_points_int if num % k == 0]
# #         k_nein = [num for num in user_points_int if num % k != 0]
# #
# #         # Вывод результатов
# #         print(f"Числа, делимые на k: {k_ja}")
# #         print(f"Числа, неделимые на k: {k_nein}")
# #     except ValueError:
# #         print("Ошибка: введите только числа.")  # Сообщение об ошибке
# #
# # if __name__ == "__main__":
# #     log()
# # #3
# # def minmax():
# #     try:
# #         # Ввод чисел от пользователя через пробел
# #         user_zahl = input("Введите числа через пробел: ")
# #         user_zahl_int = list(map(int, user_zahl.split()))  # Преобразуем ввод в список чисел
# #
# #         # Инициализация переменных для хранения максимального и минимального значений
# #         max_val = user_zahl_int[0]
# #         min_val = user_zahl_int[0]
# #
# #         # Цикл для поиска максимального и минимального значений
# #         for zahl in user_zahl_int:
# #             if zahl > max_val:
# #                 max_val = zahl
# #             if zahl < min_val:
# #                 min_val = zahl
# #
# #         # Вывод результатов
# #         print(f"Максимальное значение: {max_val}")
# #         print(f"Минимальное значение: {min_val}")
# #
# #     except ValueError:
# #         print("Ошибка: введите только числа.")  # Сообщение об ошибке
# #
# # if __name__ == "__main__":
# #     minmax()
#
# # # Числа Фибоначчи
# # fibonacci = [0, 1]  # Начало последовательности в виде списка
# #
# # # Ввод количества чисел
# # n = int(input("Введите количество чисел Фибоначчи: "))
# #
# # # Вычисляем последовательность
# # for i in range(2, n):
# #     next_number = fibonacci[i-1] + fibonacci[i-2]  # Сумма двух предыдущих чисел
# #     fibonacci.append(next_number)
# #
# # # Выводим результат
# # print(f"Числа Фибоначчи: {fibonacci}")
#
# #Числа Трибоначчи
# #
# # tribonacci = [0,1,1]
# # n = int(input("Введите искомое количество чисел Трибоначчи: "))
# # #Вычисляем последовательность
# # for x in range(3, n):
# #     next_number = tribonacci[x-1] + tribonacci[x-2] + tribonacci[x-3]   # Сумма трех предыдущих чисел
# #     tribonacci.append(next_number)
# # print(f"Числа трибоначчи до {n} числа это {tribonacci}")
#
# string = "1 2 3 4 66 77 90 010 22"
# string_lists = list(string) #Преобразовали строку в список
# number_1 = string_lists[0]
# for number in string_lists:
#     if number %2 == 0: #Если число делится на два без остатка, то...
#         print(f"Четные числа: {number}") #Выводим чётные числа
#     elif number > 10 and number %2 == False:
#         print(f"Числа, больше десяти и неделимые на два это {number}, а его половина это {number/2}")
# x = "42" # Присваиваем переменной x строку 42
# print(int(x) + 8) #выводим на экран переведенное в int число x, суммируя с 8
# y = [1, 2, 3, 4] #дан список y
# del y[2] #удаляем при помощи del число в списке по индексу 2
# print(y) #выводим на экран
# z = 10 #переменная z
# z *= 3
# print(z)
#
# fruits = "apple banana cherry" # дана строка
# fruits = list(fruits.split()) #переводим строку в список слов при помощи метода .split()
# print(fruits) #выводим результат на экран
# sentence = "I love Python programming"
# sentence = list(sentence.split())  # Разделяем строку на список слов
# sentence[2] = "JavaScript"  # Заменяем третье слово на "JavaScript"
# # new_sentence = " ".join(sentence)  # Объединяем слова обратно в строку
# # print(new_sentence)
# words = ["apple", "kiwi", "banana", "cherry", "pear"]
#
# for i in range(len(words)):  # Проходим по списку
#     for j in range(len(words) - 1):  # Сравниваем каждую пару
#         if len(words[j]) > len(words[j + 1]):  # Если текущее слово длиннее следующего
#             words[j], words[j + 1] = words[j + 1], words[j]  # Меняем их местами
#
# print(words)
#
# sentence = "Learning Python is fun and very rewarding"
# sentence = sentence.split()  # Разбиваем строку на список слов
#
# # Находим самое длинное слово
# longest_word = max(sentence, key=len)
#
# # Выводим результат
# print(f"Самое длинное слово: \"{longest_word}\", длина: {len(longest_word)}")
#
# text = "Python is fun"
#
# # Счётчик для количества букв
# count = 0
#
# # Проходим по каждому символу строки
# for char in text:
#     if char.isalpha():  # Проверяем, является ли символ буквой
#         count += 1  # Увеличиваем счётчик
#
# print(f"Количество букв: {count}")

