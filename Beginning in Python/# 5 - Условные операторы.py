# # Условные операторы
#
# user_data = int(input("Введите число: ")) #Создаем переменную
# if user_data > 0: # Создаем условие, если число user_data больше нуля, то тогда...
#     print("Hallochen!") #...пишем "Hallochen" (срабатывает код под отступом перед print())
#     if user_data > 23:
#         print("---") # cрабатывает только после второго условия, т.к. отступ под вторым if
#     elif user_data == 5:
#         print( "It's five!!")
# print("abcdef") # Срабатывает без условий, т.к. без отступа
#
# isHappy = True
# if isHappy and user_data == 6: # если isHappy это True вместе с тем, что user_data = 6 верно, то...
#     print("user is happy so so6")
# elif isHappy or user_data == 4: #если isHappy это True ИЛИ... то...
#     print("Now!")
# isHappy = False
# if not isHappy:
#     print("Yeah, Buddy!")
#
# #Тернарные операторы
#
# data = input()
# number = 5 if data == "Five" else 0 #Условия в одну строку

# #1 Четное или нечетное
# zahl = int(input("Geben Sie Zahl ein: "))
# if zahl %2==0:
#     print("Diese Zahl ist geradezahl!")
# else:
#     print("Diese Zahl ist nicht geradezahl!")
#
# #2 Vergleich der Zahlen
#
# zahl_1 = int(input("Geben Sie Zahl ein: "))
# zahl_2 = int(input("Geben Sie Zahl ein: "))
#
# if zahl_1 > zahl_2:
#     print("Die erste Zahl größe als zweite Zahl!")
# elif zahl_2 > zahl_1:
#     print("Die zweite Zahl größe als erste Zahl!")
# else:
#     print("Sie sind gleiche!")
#
# # Temperature
#
# temperature = int(input("WIe viel Grad drausen Heute ist: "))
# if temperature > 30:
#     print("Hitze!")
# elif temperature > 0 and temperature <30:
#     print("Ganz normal!")
# else:
#     print("Oh, na ja, so schlimm!")

#Rabatt
#
# price = int(input("Price ist: "))
# if price > 1000:
#     print(f"Heute Price ist {price} Euro, und Sie haben Rabatt 10%")
# elif price > 500 or price < 1000 or price == 1000:
#     print(f"Heute Price ist {price} Euro, und Sie haben Rabatt 5%")
# else:
#     print(f"Heute Price ist {price} Euro, und Sie haben keine Rabatt! Tschüß!")

# 5 Einfaches Menu
#
# wahl = input("Was wollen Sie? Kaffe, Tea oder Saft? Bitte: ")
# if wahl == "Kaffe":
#     print("Sie habe Kaffe gewählt!")
# elif wahl == "Saft":
#     print("Sie habe Saft gewählt!")
# elif wahl == "Tea":
#     print("Sie habe Tea gewählt!")
# else:
#     print("Tschuldigung, aber Ihre Wahl nicht exsitiert!")

#Schaltjahr
#
# jahr = int(input("Welches Jahr wählen Sie: "))
# if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
#     print("Dieses Jahr ist ein Schaltjahr!")
# else:
#     print("Dieses Jahr ist kein Schaltjahr!")

# #Calculator
# number_1 = int(input("Bitte geben Sie erste Zahl: "))
# number_2 = int(input("Bitte geben Sie zweite Zahl: "))
# operator = input("Bitte geben Sie das Operator +, -, * oder / ein: ")
# if operator == "+":
#     print(number_1 + number_2)
# elif operator == "*":
#     print(number_1 * number_2)
# elif operator == "/":
#     print(number_1 / number_2)
# elif operator == "-":
#     print(number_1 - number_2)
# else:
#     print("Fehler: unbekannte operator")

#Rank
#
# points = int(input("Geben Sie bitte Points ein: "))
# if points >= 90 and points <= 100:
#     print("Perfect!")
# elif points >= 70 and points <= 89:
#     print("Gut!")
# elif points >= 50 and points <= 69:
#     print("Normal!")
# elif points >= 0 and points <= 49:
#     print("Schlecht!")
# print("Dank!")

#Triangle
# side_1 = int(input("Введите первую сторону треугольника: "))
# side_2 = int(input("Введите вторую сторону треугольника: "))
# side_3 = int(input("Введите третью сторону треугольника: "))
# if (side_1 + side_2) > side_3:
#     print("Треугольник возможен!")
# else:
#     print("Нереально, чувак!")