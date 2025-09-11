print("Начнем, господа! Вот разница температур: ")
temperatures = [-3, -8, 5, 1, 12, -6, 0]
temperatures_difference = ((max(temperatures)) - (min(temperatures)))
print(f"Минимальная температура {min(temperatures)} градусов.")
print(f"Максимальная температура {max(temperatures)} градусов.")
print(f"Разница температуры составляет {temperatures_difference} градусов.")

print("Господа, а теперь поиграем в разницу чисел... \n")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
difference_num1_num_2 = num_2 - num_1
print(f" {num_2} - {num_1} = {difference_num1_num_2}")
print("Число по модулю: ", abs(difference_num1_num_2))

print("Господа, а теперь поиграем в степени! \n")
number_1 = int(input("Введите основание степени: "))
number_2 = int(input("Введите показатель степени: "))
print(f"\nЧисло в основании {number_1} в степени {number_2} равно {pow(number_1, number_2)}.")

one = (int(input("Число первое: ")))
two = (int(input("Число второе: ")))
three = (int(input("Число третье: ")))
four = (int(input("Число четвертое: ")))
one_four = (one, two, three, four)
print(f"{one} {two} {three} {four}")
print("Максимальное число: ", max(one_four))
print("Минимальное число: ", min(one_four))
print("Модуль разницы между максимумом и минимумом:", abs(max(one_four)-min(one_four)))
print("Квадрат модуля равен:", pow((abs(max(one_four)-min(one_four))), 2))

