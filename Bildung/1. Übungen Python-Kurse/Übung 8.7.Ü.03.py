import json

freunde_liste = ["Anna", "Bernd", "Carla", "David", "Eva"]


try: # открываем обработку ошибок
    with open(".txt & .json/freunde.txt", "w") as file: # открываем файл текстовый в режиме записи
        json.dump(freunde_liste, file) # сохраняем в файл в режиме JSON файл
except Exception as e: # Исключение если что-то пошло не так
    print(f"Ein Fehler ist aufgetreten beim Speichern der Liste: {e}")


try:
    with open(".txt & .json/freunde.txt", "r") as file: # открываем файл для чтения
        geladene_liste = json.load(file) # так как файл в JSON, считываем данные через модуль JSON, присваивая переменну.ю
        print("Geladene Freunde Liste:", geladene_liste) # экранируем
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Laden der Liste: {e}")


try:
    with open(".txt & .json/freunde.txt", "r+") as file: # открываем с целью добавить
        freunde = json.load(file) # так как файл в JSON, считываем данные через модуль JSON
        freunde.append("Felix")  # Neuen Namen hinzufügen
        file.seek(0)  # Zurück zum Anfang der Datei gehen
        json.dump(freunde, file)
        file.truncate()  # Entfernt überschüssige Daten am Ende der Datei
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Aktualisieren der Liste: {e}")