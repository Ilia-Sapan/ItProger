# #1
# import math
# sales_data = (5000, 6000, 4500, 7000, 8000, 5500, 6200, 7200)
# # Разделим данные на два полугодия
# first_half = sales_data[:4]  # Первые четыре элемента
# second_half = sales_data[4:]  # Последние четыре элемента
# # Вывод данных
# print("Данные за первые два квартала:", first_half)
# print("Данные за вторые два квартала:", second_half)
# # Средние значения
# med_1 = sum(first_half) / len(first_half)  # Среднее за первые два квартала
# med_2 = sum(second_half) / len(second_half)  # Среднее за вторые два квартала
# # Вывод результатов
# print("Средние продажи за первые два квартала:", round(med_1, 2))
# print("Средние продажи за вторые два квартала:", round(med_2, 2))
# #2
# year = int(input("Введите год: "))
# units_sold = int(input("Введите кол-во проданных ед. товара: "))
# price_per_unit =  int(input("Введите среднюю цену товара: "))
# revenue = units_sold * price_per_unit
# print(f"В {year} году было продано {units_sold} единиц товара по средней цене "
#       f"{price_per_unit}, что дало выручку {revenue}")
#
# #3
# number = 7.85
# log_base2 = 8
# angle = 30 #'(в градусах).
# #print(math.sqrt(16))          # Квадратный корень: 4.0
# #print(math.log(8, 2))         # Логарифм по основанию 2: 3.20
# #print(math.sin(math.radians(90)))  # Синус 90 градусов: 1.0
# #print(math.ceil(value))   # Результат: 6 идет к верхнему результату
# #print(math.floor(value))  # Результат: 5 идет к нижнему результату
#
# print(math.ceil(number))
# print(math.log(log_base2,2))
# print(round(math.sqrt(angle), 2))
#
# #4
# income_data = [48.5, 50.2, 47.8, 49.1, 51.0, 50.3]
# max_data = income_data[0]
# for data in income_data:
#       if data > max_data:
#             max_data = data
# print(f"Максимальный доход равен {round(max_data, 2)}")
# min_data = income_data[0]
# for data in income_data:
#       if data < min_data:
#             min_data = data
# print(f"Минимальный доход равен {round(min_data, 2)}")
#
# #5
# x = int(input("Введите число x: "))
# x += 5
# y = 2
# print(y**x)