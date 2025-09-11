# Функции строк


# word = "Programmer"
# print(word.count("m")) # Метод .count(x) выдаёт количество значений в списке, где x - искомое значение
# print(word.upper()) # метод .upper() делает буквы высокими
# print(word.isupper()) # метод .isupper()/.islower() проверяет, в верхнем/нижнем ли регистре буквы в строке (возвращает буль)
# print(word.capitalize()) # метод .capitalize() делает первую букву в строке в верхнем регистре
# print(word.find("t")) # метод .find() ищет значение, и выдаёт индекс, где находится искомое

# sports = "football, basketball, tennis, golf, wrestling, running"
# my_sports = sports.split(", ") # Метод .split(x) разделяет данные, где x - по какому принципу
# print(my_sports[2]) # Выведет теннис
# for i in range(len(my_sports)): # Цикл. Для каждого элемента в списке (i), в диапазоне (range) длины (len) списка (my_sports)
#     my_sports[i] = my_sports[i].capitalize() # Каждый элемент (i) по индексу равно, что каждый этот элемент увеличивается (capitalize)
# print(my_sports) # Выводим на экран
# result = ", ".join(my_sports) # Выводим строку при помощи метода .join(x), где x - данные, выводимые в строку
# print(result)

# Срезы
#
# word = "Football"
# print(word[0:4]) # Срез берется по индексам, в квадратных скобках, "срезая" нужный диапазон (выведет "foot")
# print(word[4:]) # Выведет с индекса 4 до конца
# print(word[4:7]) # Выведет с индекса 4 по 7 (равнозначно и print(word[4:-1])
# print(word[0:8:2]) # [x: y: z] x - начальный индекс, y - конечный, z - шаг
#
# # Задача 1: Считаем буквы
#
# word_user = input("Введите слово: ")
# alfa_user = input("Введите букву для поиска: ")
# print(f'Слово "{alfa_user}" встречается в слове  {word_user.count(alfa_user)} раз(а).')
#
# # Задача 2: Изменение регистра
#
# word_user = input("Введите слово: ")
# print(word_user.isupper())
# print(word_user.upper())
# print(word_user.lower())
#
# # Задача 3: Спорт и списки
# sports = "football, basketball, tennis, golf"
# my_sports = sports.split(", ")
# for i in range(len(my_sports)):
#     my_sports[i] = my_sports[i].capitalize()
# print(", ".join(my_sports))
#
# # Задача 4: Срезы и шаги
# word = "Basketball"
# print(word[:4])
# print(word[4:])
# print(word[::2])
#
# # Задача 5: Найди индекс
# word_user = input("Введите слово: ")
# alfa_user = input("Введите букву для поиска: ")
# if alfa_user:
#      print(word_user.find(alfa_user))
# else:
#      print("Символ не найден")


# # Задача 1: Замена слов в строке
# word_user = input("Введите строку: ") # Вводит строку
# word_back = input("Введите слово: ") #
# word_new = input("Введите слово: ")
# print(word_user.replace(word_back,word_new)) # используем метод .replace(x, y), где x - то, что, y - то, на что замена

# # Задача 2: Найти самое длинное слово
# stringsy = input("Введите несколько слов через запятую: ")
# diffy = stringsy.split(", ") # выдаст что-то вроде a, b, c, d
# longest_word = max(diffy, key=len) # функция max()
# print("Самое длинное слово:", longest_word)

# Задача 3: Сложные срезы
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# a = int(len(alphabet)) / 2
# print(alphabet[:int(a):]) # Первая половина алфавита
# print(alphabet[int(a)::]) # Вторая половина алфавита


# Задача 1: Подсчёт символов
# stringy_user = input("Введите строку: ")
# letters = len([x for x in stringy_user if x.isalpha()])
# numbers = len([x for x in stringy_user if x.isnumeric()])
# space = len([x for x in stringy_user if x.isspace()])
# symbol = len([x for x in stringy_user if x in '.,;:!?-()[]{}\'"'])
# print(f"В строке {space} пробелов, {letters} букв, {numbers} цифр и {symbol} символов!")

# Задача 2: Удаление слов по длине
# string_user = input("Введите строку: ")
# minimum_user = int(input("Введите минимальный размер слова: "))
#
# # Разбиваем строку на слова
# words = string_user.split()
#
# # Удаляем слова, длина которых меньше минимального значения
# filtered_words = [word for word in words if len(word) >= minimum_user]
#
# # Объединяем обратно в строку
# result_string = " ".join(filtered_words)
# print(f"Строка после удаления коротких слов: {result_string}")
#
# Задача 1: Найти все числа в строке
# import re # — это модуль для работы с регулярными выражениями, который помогает находить,
# # проверять и заменять текстовые шаблоны в строках.
#
# user_string = input("Bitte geben Sie etwas ein: ")
# # Находим все числа в строке
# numbers = [int(num) for num in re.findall(r'\d+', user_string)] # Буква r перед кавычками
# # делает строку сырой (raw string).
# # В регулярных выражениях \d означает "любая цифра"
# print(f"Найденные числа: {numbers}")
# print(f"Сумма чисел: {sum(numbers)}")
#
# user_string = input("Введите строку: ")
# user_letter = input("Введите букву: ").lower()  # Преобразуем букву в нижний регистр
#
# # Разбиваем строку на слова
# words = user_string.split()
#
# # Находим слова, начинающиеся с заданной буквы (без учёта регистра)
# matching_words = [word for word in words if word.lower().startswith(user_letter)] # Метод startswith
# # в Python используется для проверки,
# # начинается ли строка с определённого
# # символа или последовательности символов
#
# # Вывод результата
# if matching_words:
#     print(f'Слова, начинающиеся с буквы "{user_letter}": {matching_words}')
# else:
#     print(f'Слов, начинающихся с буквы "{user_letter}", нет.')

# Задача 1: Форматирование списка имен
# names = input("Введите список имён через запятую: ")
# new_name = names.split(", ")
# for name in range(len(new_name)):
#      new_name[name] = names[name].capitalize()
# print(new_name)






















