if __name__ == "__main__":

    import json # импортируем модуль json
    FILENAME = ".txt & .json/contacts.json"  # назначаем имя файла, в котором будут сохранены данные
    def speichere_daten(name, nummer, email): # создаем функцию, которая принимает данные
        kontakt_datei = {
            "Name": name,
            "Nummer": nummer,
            "Email": email } #  Создаём словарь 'kontakt' с данными, которые принимает функция
        try: # Пытаемся открыть файл и загрузить существующие данные
            with open(FILENAME, "r+") as file: # открываем файл для чтения и записи с модулем r+
                daten = json.load(file)  # Загружаем JSON-данные в переменную `daten`
                daten.append(kontakt_datei) # Добавляем новый контакт в список
                file.seek(0) # перемещаем курсор в начало файла (чтоб записывал с первой строчки)
                json.dump(daten, file, indent=4) # сохраняем, грамотно разделяем 4-мя пробелами
        except (FileNotFoundError, json.JSONDecodeError):
            with open(FILENAME, 'w') as file: # Открываем "kontakte.json" в режиме записи ('w'), создавая новый файл.
                json.dump([kontakt_datei], file, indent=4) # Записываем список с одним контактом:
            print("Neue Datei wurde erstellt, da keine vorhanden war.")
    def laden_kontakte():
        '''Функция, считывает сохраненные данные о контактах
        из файла JSON и возвращает их в виде списка словарей'''
        try:
            with open(FILENAME, 'r') as file:
                str_kontakten = json.load(file)
                print(str_kontakten)
        except (FileNotFoundError, json.JSONDecodeError):
            print('Ooops... Etwa nicht so...')
    def main():
        while True:
            print('Guten Tag! Geben Sie bitte Name, Nummer und E-Mail!')
            name = input('Name: ')

            try:
                nummer = int(input('Nummer: '))  # Проверка, что номер - число
            except ValueError:
                print("Fehler: Nummer muss eine Zahl sein!")
                continue

            email = input('E-Mail: ')

            # Frage den Benutzer, ob er das Programm beenden möchte
            beenden = input("Möchtest du das Programm beenden? (Ja/Nein): ").strip().lower()
            if beenden == "ja":
                print("Programm wird beendet. Auf Wiedersehen!")
                break
            elif beenden == "nein":
                speichere_daten(name, nummer, email)  # Сохраняем данные
                print(laden_kontakte())  # Выводим список контактов


    # Hauptprogramm starten
    main()
