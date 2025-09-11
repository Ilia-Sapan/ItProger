# Словари
# number = {4 : 3} # Словари в фигурных скобках, {x: y}, x - ключ, y - значение
# print(number[4]) # Обращение по ключу к значению
#
# new_word = {(5, 6): 4} # В качестве ключа могу использовать кортежи
#
# country = {"Code": "RU", "name": "Russia", "Population": 144}
# print(country["Population"]) # Обращаюсь к значению по ключу

# country = dict(code = "RU", name = "Russia", Population = 144) #можно создать через dict()
# # print(country["name"])
# # for key in country: # Для одного элемента выводятся ТОЛЬКО КЛЮЧИ СПЕРВА
# #     print(key)
# # for key, value in country.items(): # Для КЛЮЧА и ЗНАЧЕНИЯ идет функция .items()
# #     print(key, " - ", value) # Выводим всё
# print(country.get("name")) # метод .get()
# country.pop("name") # удаляет ключ
# country.popitem() # удаляет последний ключ в словаре
# print(country.keys()) # выводит .keys() только ключи
# print(country.values()) # выводит .values() только значения
# print(country.items()) # выводит и ключ, и значение
#
# country["code"] = "None" # Замена значения при помощи ключа
# print(country)
#
# person = {
#
#     "user_1": {
#         "first_name" : "Ilya",
#         "second_name" : "Sapan",
#         "age": 30,
#         "adress": ("Düsseldorf", "Kölner Straße", "217", "40227"),
#         "education": "PhD."
#     },
#     "user_2" : {
#
#     }
#
# }
# print(f"PLZ ist {person["user_1"]["adress"][3]}.")
#
# #1. Создание и работа с вложенными словарями
#
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
# print(f"Возраста всех персон. Итак. Тимур это {users["Timur"]["age"]} лет, Илья это {users["Ilya"]["age"]} лет, "
#       f"Эллина это {users["Ellina"]["age"]} лет, Иван"
#       f" это {users["Ivan"]["age"]} лет.")
#
# users["Ilya"]["hobby"] = "Books" # Добавляем ключ хобби со значением
# print(users["Ilya"])
#
# # 4. Обратный словарь
# country = input("Введите страны через запятую: ")  # Пример ввода: "Russia, Germany, France"
# town = input("Введите города через запятую: ")  # Пример ввода: "Moscow, Berlin, Paris"
#
# # Разделяем строки на списки
# country_list = country.split(", ")
# town_list = town.split(", ")
#
# # Создаём словарь из пар (город → страна)
# town_country = dict(zip(town_list, country_list))
#
# # Печатаем результат
# print("Словарь город → страна:", town_country)
#
# # Обратный словарь (страна → город)
# country_town = {v: k for k, v in town_country.items()}
# print("Словарь страна → город:", country_town)










