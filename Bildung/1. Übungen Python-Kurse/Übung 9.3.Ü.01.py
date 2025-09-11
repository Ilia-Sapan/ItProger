import json

text = "Hier ist ein Beispieltext mit einem Emoji: \U0001F600 und einem Zeilenumbruch\nHier ist der zweite Teil des Textes, der {0} enthält."
print(text)

try:
    with open('.txt & .json/example.txt', 'r', encoding='utf-8') as file:
        reading = file.read()
        print(reading)
except Exception as e:
    print(f'Das ist{e}')

data = {'Name': 'Ilia', 'Age': 30}
def json_speichern(obj):
    try:
        with open ('.txt & .json/data_001.json', 'w') as file:
            obj = json.dump(obj, file, indent= 4)
    except Exception as e:
        print(f'Das ist{e}')

json_speichern(data)