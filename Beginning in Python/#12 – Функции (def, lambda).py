#Функция это подпрограмма, в которой находится часто повторяющийся код.
#К примеру, есть функция print(), но она уже заложена, и занимается тем, что
#выводит текст на экран. Ты же можешь создать свою.

# def test_func():
#     pass # Вызывая pass, ничего не происходит.
#
# test_func() #вызываем функцию test_funk() которую создали, обязательно круглая скобка, как у print()
#
# def hallochen(): # обязательно должны быть отступы, табуляция под функцией
#     print("Hello, world!", end="\n\n")
#     print("!")
#
# hallochen() # вызываем функцию hallochen
#
# def lalambra(word): # Параметр word работает только в самой функции
#     print(word)
#
# lalambra("Hello") # Параметру word присвоили значение "Hello"
# lalambra(5) #Параметру word присвоили значение 5
#
# def summary(a,b,c):
#     result = a + b * c
#     print(result)
#
# summary(5, 6, 6)
# summary(33, 55, 66)
# summary("Hello", "my", 4)
#
# def summary_1(a, b):
#     resulty = a - b
#     return resulty # функция return возвращает resulty
#
# resulty = summary_1(3, 4)
# print(resulty)

# geburtsdatum = [1994, 1968, 1974, 2001, 1987, 1965, 1111] # Дан список годов рождения
# minimum = geburtsdatum[0] # минимальный равен первому элементу списка
# for datum in geburtsdatum: # для даты в списке дат:
#     if datum < minimum:
#         minimum = datum
# print(minimum)
#
# def minimum_minimorum(list):
#     minimum = list[0]
#     for i in list:
#         if i < minimum:
#             minimum = i
#     return minimum
#
# minimum_minimorum(geburtsdatum)
#
# numbers = [13, 2, 3, 55, 77, 90, 88, 94, 67, 55]
# babbls = (1.22, 33.44, 77.55, 0.55, 1.33)
#
# numbers_1 = minimum_minimorum(numbers)
# babbls_1 = minimum_minimorum(babbls)
#
#
# if numbers_1 > babbls_1: # если 2 меньше 0.55
#     print(babbls_1) # пиши 0.55
# else: # в противном случае
#     print(numbers_1) # пиши 2

# lambda-функции
#
# summary = lambda x, y: x * y # Потаённая функция при помощи lambda
# summary(3,2)
# print(summary(3,2))


# 1. Создание функции с параметрами
# def arithmetic(a, b): # Создаём функцию arithmetic с параметрами
#     result_sum = a + b
#     result_diff = a - b
#     result_prod = a * b
#     general_result = (f"Произведение чисел {a} и {b} равно {result_prod}, "
#                       f"разность равна {result_diff}, "
#                       f"а сумма равна {result_sum}.")
#     return general_result
# numbers_1 = arithmetic(1,2)
# numbers_2 = arithmetic(4,7)
# numbers_3 = arithmetic(66, 78)
# print(numbers_1,"\n",numbers_2,"\n",numbers_3)

# 2. Поиск максимального значения
#
# def findmax(list):
#         maximum = max(list)
#         print(f"Максимальное значение: {maximum}")
#         return maximum
#
# numbers = [1,2,3,4,5]
# findmax(numbers)
#
#3. Сортировка списка
# def sort_by_length(words):
#     return sorted(words, key=len)  # Сортируем список по длине слов
#
# words = ["apple", "kiwi", "banana", "cherry"]
# sorted_words = sort_by_length(words)
# print(f"Список, отсортированный по длине: {sorted_words}")
#
# #4. Использование lambda
# squares = list(map(lambda x: x ** 2, range(1, 11)))  # Возводим в квадрат числа от 1 до 10
# print(f"Квадраты чисел от 1 до 10: {squares}")
#
# #5
# def calculate_ages(birth_years):
#     current_year = 2024
#     ages = [current_year - year for year in birth_years]  # Вычисляем возраст для каждого года
#     return ages
#
# years = [1994, 2001, 2024, 1968, 1974]
# ages = calculate_ages(years)
# print(f"Возраст для каждого года рождения: {ages}")
# #
# employees = {
#     "101": {"name": "Alice", "age": 30, "salary": 70000, "department": "HR"},
#     "102": {"name": "Bob", "age": 24, "salary": 48000, "department": "IT"},
#     "103": {"name": "Charlie", "age": 35, "salary": 90000, "department": "Finance"},
#     "104": {"name": "David", "age": 28, "salary": 53000, "department": "IT"},
#     "105": {"name": "Eve", "age": 40, "salary": 120000, "department": "Management"}
# }
#
# def filter_employees(employee):
#     # Функция возвращает True, если зарплата больше 50,000
#     return employee["salary"] > 50000
#
# # Применяем фильтр ко всем сотрудникам
# filtered_employees = list(filter(lambda emp: filter_employees(employees[emp]), employees))
# print("Сотрудники с зарплатой выше 50,000:")
# for emp_id in filtered_employees:
#     print(employees[emp_id])
#
# def sort_employees(employees, by="age"):
#     # Сортируем по заданному ключу ("age" или "salary")
#     return sorted(employees.values(), key=lambda x: x[by])
#
# # Сортируем по возрасту
# sorted_by_age = sort_employees(employees, by="age")
# print("\nСотрудники, отсортированные по возрасту:")
# for emp in sorted_by_age:
#     print(emp)
#
# def calculate_average(employees, department):
#     # Выбираем сотрудников из заданного отдела
#     dept_employees = [emp for emp in employees.values() if emp["department"] == department]
#     # Если сотрудников нет, возвращаем 0
#     if not dept_employees:
#         return 0
#     # Считаем среднюю зарплату
#     total_salary = sum(emp["salary"] for emp in dept_employees)
#     return total_salary / len(dept_employees)
#
# # Вычисляем среднюю зарплату в отделе IT
# average_salary_it = calculate_average(employees, "IT")
# print(f"\nСредняя зарплата в отделе IT: {average_salary_it}")
#

#!!! ВНИМАНИЕ :
# double = lambda x: x*2
# =
# def double(x):
		# return x * 2
#
# #Фильтрация
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x%2 == 0 and x>5) , my_list))
# #filter(x, y) это функция, которая под x принимает КАК фильтровать, а под y - ЧТО фильтровать
# print(new_list)
#
# #1
# names_of_philosophers = ["Kant", "Hegel", "Marx", "Wittgenstein", "Nietzsche", "Luhmann"]
# filtered_names_of_philosophers = list(filter(lambda x: len(x) > 5, names_of_philosophers))
# filtered_names_of_philosophers_new = sorted(filtered_names_of_philosophers)
# print(filtered_names_of_philosophers_new)
# #2
# zahlen = [1, 1, 2, 3, 5, 8, 13, 21]
# zahlen_cube = list(map(lambda x: x ** 2, zahlen))
# print(zahlen_cube)
# #3
# # words = ["Swiss", "Mascotte", "Paco Rabanne", "Fallout 4"]
# # strings_new = list(filter(lambda  x: x for x in words if x == "s", words))
# # print(strings_new)
# #4
# words = ["Swiss", "Mascotte", "Paco Rabanne", "Fallout 4"]
# words_new = list(map(lambda x: len(x), words))
# print(words_new)
# #5 reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
# from functools import reduce
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers_one = list(filter(lambda x: x % 2 == 0, numbers))
# numbers_two = reduce(lambda x, y: x + y, numbers_one)
# print(numbers_two)
#
# #1
# numbers = [1,2,3,4,5,6]
# numbers_new = list(filter(lambda x: (x%2 ==0), numbers))
# print(numbers_new)
# #2
# numbers = [1,2,3,4,5,6]
# numbers_new = list(map(lambda x: x**2, numbers))
# print(numbers_new)
# #3
# words = ['apple', 'banana', 'kiwi']
# words_new = sorted(words, key=lambda x: len(x))
# # list + lambda: Вы попытались использовать list(lambda x: ...),
# # но для сортировки нужен метод sorted,
# # и lambda передается в качестве аргумента key.
# print(words_new)
#
# #1
# lines = ["a10b", "c20", "30d"]
# # Извлекаем числа из строк, используя filter и lambda
# numbers = list(map(lambda x: int(''.join(filter(str.isdigit, x))), lines))
# result = sum(numbers)
# print(result)  # Ожидаемый результат: 60
#
# # 2
# strings = ["cat", "apple", "dog", "banana"]
# # Ожидаемый результат: "apple,banana"
# str_filtered = list(filter(lambda  x: len(x)>3, strings))
# # функция принимает значение итерируемого объекта в списке,
# # и возвращает его, если его длина более трёх
# print(",".join(str_filtered)) # при помощи функции .join() объединяем выделенные элементы списка
#
# #3
# nums = [1, 2, 3]
# nums_cube = dict(map(lambda x: (x, x**3), nums))
# print(nums_cube)  # Ожидаемый результат: {1: 1, 2: 8, 3: 27}


# def add_two_numbers(x,y):
#     return x + y
# result = add_two_numbers(3, 5)
# print(result)  # Должно вывести: 8
#
# def is_even(number):
#     if number %2 ==0:
#         return True
# print(is_even(4))
# print(is_even(7))
#
# def factorial(n):
#     if n < 1:
#         return "Факториал вычисляется для чисел больше или равных 1!"
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     return f"Факториал числа {n} это {factorial}."
#
# print(factorial(5))  # Должно вывести: Факториал числа 5 это 120.
# print(factorial(0))  # Должно вывести: Факториал вычисляется для чисел больше или равных 1!


# def count_vowels(stringy):
#     vowels = "aeiouy"  # Добавляем "y" к гласным
#     count = 0
#     for char in stringy:
#         if char.lower() in vowels:
#             count += 1
#     return count









