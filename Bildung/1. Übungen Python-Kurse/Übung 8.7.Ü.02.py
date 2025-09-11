import json

alter = 30
hobbies = ['Bueche', 'Mathematik', 'Philosophie']
favorite_colours = ('gelb', 'weiss', 'gruen')

# Вывод хобби
for hobbie in hobbies:
    print(f'Eines meiner Hobbies ist: {hobbie}.')

def jahre_bis_rente(x) -> str:
    alt_rente = 65
    return f'Bis zur Rente {alt_rente - x} Jahre.'

try:
    daten = []  # Создаём список для всех записей

    for hobbie, colour in zip(hobbies, favorite_colours):
        daten.append({"Hobbies": hobbie, "Favorite Colours": colour})  # Добавляем в список

    # Записываем список в JSON-файл
    with open('.txt & .json/persoenliche_daten.json', 'w') as file:
        json.dump(daten, file, indent=4)

    print('Ready!')

except Exception as e:
    print(f"Scheiße! Das ist {e}!!!")
