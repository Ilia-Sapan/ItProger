# x= 0 # присваиваем переменной значения
# while x == 0: #цикл
#     try: #пытаемся
#         x = int(input("Enter the Password: "))
#         x += 4
#         print(x)
#     except ValueError: # не пытаемся если вот такое
#         print("Password is number, not words!")
#     else: #еще, если пытаемся
#         print("Кого я люблю?")
#     finally: #и, наконец...
#         print("Я люблю Эллину Берендееву Сапан")
from fontTools.unicodedata import block
from psutil import users

#
# try:
#     count = 0  # Счетчик попыток
#     pin_code = 789  # Заданный PIN
#
#     while count < 3:  # Пока попыток меньше 3
#         try:
#             user_enter = int(input("Enter your PIN: "))  # Запрос ввода
#             if user_enter == pin_code:
#                 print("Welcome! You’ve entered the correct PIN.")
#                 break  # Прерываем цикл
#             else:
#                 count += 1
#                 if count < 3:
#                     print(f"Incorrect PIN. You have {3 - count} attempts left.")
#                 else:
#                     print("Too many incorrect attempts. Access denied.")
#         except ValueError:  # Если введено не число
#             print("PIN must be a number!")
# except Exception as e:  # Если есть другая ошибка
#     print(f"An unexpected error occurred: {e}")

#
# try:
#     num_1 = int(input("Введите первое число: "))
#     num_2 = int(input("Введите второе число: "))
#     num_3 = num_1 / num_2
#     print(f"Результат деления равен {num_3}.")
# except ValueError:
#     print("Ошибка: введите корректные числа.")
# except ZeroDivisionError:
#     print("Ошибка: на ноль делить нельзя!")
#
# try:
#     name_of_file = input("Введите имя файла: ")
#     with open(f"data/{name_of_file}.txt", "r", encoding="utf-8") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Ошибка: файл не найден.")
# except PermissionError:
#     print("Ошибка: недостаточно прав для открытия файла.")
# except Exception as e:  # Ловим любые другие ошибки для анализа
#     print(f"Произошла непредвиденная ошибка: {e}")


# Задача 1: Корень числа
# try:
#     #открываем конструкцию и запрашиваем число у пользователя
#     number = int(input("Введите число: "))
#     #возводим число в квадрат
#     number_quad = number **2
#     print(f"Квадрат числа {number} равен {number_quad}.\n")
#     # далее обрабатываем исключения
# except ValueError:
#     print("Пожалуйста, введите числовое значение.")
# finally:
#     print("Спасибо!")

# # Задача 2: Конвертация строки в число
# try:
#     #открываем конструкцию и запрашиваем данные у пользователя
#     user_string = input("Введите данные: ")
#     # преобразуем данную строку в тип данных int и float
#     new_string_1 = int(user_string)
#     new_string_2 = float(user_string)
#     print(f"{user_string} в типе int и float это {new_string_1} и {new_string_2} соответственно.")
# except ValueError:
#     print("Эти данные не преобразовываются.")

# Задача 3: Сложение слов
#
# try:
#     # открываем конструкцию try и запрашиваем два слова
#     user_word_1 = input("Введите слово первое: ")
#     user_word_2 = input("Введите слово второе: ")
#     # ставим условие, чтобы введенные данные были именно словами в строках
#     if user_word_1.isalpha() and user_word_2.isalpha():
#         user_word_3 = user_word_1 + user_word_2
#         print(user_word_3)
# #делаем исключение по типу данных
# except TypeError:
#     print("Введите корректные данные!")

# Задача 4: Индекс в строке
# while True:
#     try:
#         #открываем конструкцию try и запрашиваем два слова
#         user_string = str(input("Введите, пожалуйста, строчку: "))
#         user_index = int(input("Введите искомый индекс строки для вывода: "))
#         #Выводим искомый элемент, предварительно его сделав в верхнем регистре и беря в скобки для удобства
#         print(f'"{user_string[user_index].capitalize()}" является элементом строки по индексу {user_index}.')
#     # Вводим исключение
#     except ValueError:
#         print("Введите корректный индекс, носящий числовой характер.")
#     # Прописываем доступное количество индексов в заданной строке
#     except IndexError:
#         print(f"Введите доступный индекс, от 0 до {len(user_string) - 1}.")
#     # Заключительная часть попыток
#     finally:
#         print("Спасибо!")

# Задача 5: Создание файла
# try:
#     name_of_file = int(input("Введите имя файла: "))
#     with open(f"data/{name_of_file}.txt", "a", encoding="utf-8") as file:
#         file.write("Привет\n")
#         file.write("Как дела?\n")
# except ValueError:
#     print("Введите число.")

# Задача 6: Деление чисел с ручным исключением
# while True:
#     try:
#         number_1 = int(input("Введите первое число: "))
#         number_2 = int(input("Введите второе число: "))
#         #Результат деления
#         number_3 = int(number_1 / number_2)
#         #Ставим условия
#         if number_3 < 1:
#             raise ValueError("Результат должен быть больше единицы!")
#         else:
#             print(f"Результат деления двух чисел {number_3}")
#     #Исключаем ошибку и прописываем результат
#     except ValueError as e:
#         print(e)

# Задача 7: Вложенные try-except
# try:
#     # Вложенный блок для обработки ввода числа
#     try:
#         number_of_user = int(input("Введите число: "))
#     except ValueError:
#         print("Ошибка: введите число, а не букву или знак.")
#         raise  # Пробрасываем исключение наружу для обработки
#     # Выполняем деление
#     new_number = number_of_user / 7
#     print(f"Результат деления числа {number_of_user} на 7: {new_number:.2f}")
# except ValueError:
#     print("Ошибка ввода. Убедитесь, что вы ввели корректное число.")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль невозможно.")
# except Exception as e:
#     print(f"Произошла непредвиденная ошибка: {e}")

# # Задача 8: Работа со словарём
# users = {
#
#     "Ilya" : { "age" : 30,
#                "city" : "Düsseldorf",
#                "street": "Kölner Straße",
#                "№" : 217,
#                "profession": "Philosopher, researcher"},
#     "Ellina": { "age" : 30,
#                "city" : "Düsseldorf",
#                "street": "Kölner Straße",
#                "№" : 217,
#                "profession": "PR-specialist"},
#     "Ivan" : { "age" : 28,
#                "city" : "Moscow",
#                "street": "Leninskie Gory",
#                "№" : 1,
#                "profession": "Philosopher, researcher"},
#     "Timur": { "age" : 30,
#                "city" : "Moscow",
#                "street": "Lenina",
#                "№" : 33,
#                "profession": "Philosopher, teacher"},
#
# }
#
# try:
#     print("Введите искомый ключ: Ilya, Ellina, Ivan или Timur.")
#     user_key = input("Введите нужный вам ключ: ")
#     print(users[user_key])
# except KeyError:
#     print("Введите имеющийся ключ.")
# finally:
#     print("Спасибо!")
#
# try:
#     # Запрашиваем ввод
#     user_input = input("Пожалуйста, введите число: ").strip() # .strip(x) вычищает ненужное в строке, где x то самое ненужное
#
#     # Проверяем на пустой ввод
#     if not user_input:
#         raise ValueError("Пустой ввод недопустим. Введите число.")
#
#     # Преобразуем ввод в число
#     number_of_user = int(user_input)
#     print(f"Вы ввели число {number_of_user}!")
# except ValueError as e:
#     print(f"Ошибка: {e}")
# finally:
#     print("Благодарим за пользование программой!")

# # Задача 10: Индексы в списке
# user_list = ["apple", "banana", "roclette"]
# try:
#     index_user = input("Введите индекс: ").strip()
#     index_user = int(index_user)
#
#     if not index_user:
#         raise ValueError("Пустой ввод недопустим. Введите число.")
#     print(f"Вы ввели индекс {index_user}, данный индекс соответствует элементу '{user_list[index_user].capitalize()}'.")
# except ValueError:
#     print("Пожалуйста, введите число от 0 до 2")
# finally:
#     print("Благодарим за пользование программой!")
#
# try:
#     import re
#
#     # Ввод текста
#     user_sentence = input("Пожалуйста, введите строку из текста: ").strip()
#     if not user_sentence:
#         raise ValueError("Вы ничего не ввели. Попробуйте ещё раз.")
#
#     # Убираем знаки пунктуации и приводим текст к нижнему регистру
#     cleaned_sentence = re.sub(r'[^\w\s]', ' ', user_sentence.lower())
#
#     # Разбиваем текст на слова и оставляем только уникальные
#     unique_words = sorted(set(cleaned_sentence.split()))
#     print("Уникальные слова в тексте:", unique_words)
#
# except ValueError as e:
#     print(f"Ошибка: {e}")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# finally:
#     print("Благодарим Вас за пользование программой!")



# Задача: частота слов в тексте

try:
    import re

    # Ввод текста
    user_sentence = input("Пожалуйста, введите строку из текста: ").strip()
    if not user_sentence:
        raise ValueError("Вы ничего не ввели. Попробуйте ещё раз.")

    # Убираем знаки пунктуации и приводим текст к нижнему регистру
    cleaned_sentence = re.sub(r'[^\w\s]', ' ', user_sentence.lower())

    # Разбиваем текст на слова и оставляем только уникальные
    # unique_words = sorted(set(cleaned_sentence.split()))
    # print("Уникальные слова в тексте:", unique_words)
    cleaned_sentence_new = cleaned_sentence.split()




except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Благодарим Вас за пользование программой!")














