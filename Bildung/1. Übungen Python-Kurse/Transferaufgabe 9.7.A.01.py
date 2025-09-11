import json
import re

FILE_1 = r'C:\Users\isapa\PycharmProjects\itProger\WEITERBILDUNG\Übungen\.txt & .json\example.txt'
# a)
# try:
#     with open(FILE_1, 'r', encoding="utf-8") as file:
#         reading = file.read()
#         print(reading)
# except FileNotFoundError as e:
#     print(f'Tschuldigung, aber Ihre File hat {e}...')
# except Exception as e:
#     print(f'Ooops... File hat {e}.')
# else:
#     print('Alles erledigt!')
# b)
# with open(FILE_1, 'r', encoding="utf-8") as file:
#     text = file.read()  # Считываем всё содержимое файла
#     result = re.findall(r'[A-Z][a-z]*', text)  # Ищем слова с заглавной буквы
#     print(result)
# c)
import re
def woerte_zahl(file_input):
    result_dict = {}  # Обычный словарь для хранения слов и их частот

    with open(file_input, 'r', encoding="utf-8") as file:
        text = file.read()

        # Находим все слова, начинающиеся с заглавной буквы
        words = re.findall(r'[A-Z][a-z]*', text)

        # Подсчитываем количество каждого слова
        for word in words:
            if word in result_dict:
                result_dict[word] += 1  # Если слово уже в словаре, увеличиваем счетчик
            else:
                result_dict[word] = 1  # Если слово еще нет в словаре, добавляем его с начальным счетчиком 1

    return result_dict
result = woerte_zahl(FILE_1)
print(result)
#d)
with open('.txt & .json/daten.json', 'w', encoding="utf-8") as file:
    x = json.dump(result,file, indent=4)
    print(x)
