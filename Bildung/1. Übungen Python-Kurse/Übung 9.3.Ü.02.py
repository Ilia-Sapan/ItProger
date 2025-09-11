import json

FILE_1 = r"C:\Users\isapa\PycharmProjects\itProger\WEITERBILDUNG\Übungen\.txt & .json\tagebuch.txt"

# try:
#     with open(FILE_1, 'r', encoding='utf-8') as file: # Открываем файл с текстом
#         text = file.read() # присваиваем переменной задачу читать текст
#         print(text.count("домой")) #Вставляем нужное
# except FileNotFoundError:
#     print("\nFehler: Die Datei 'beispiel.txt' wurde nicht gefunden.")
# except Exception as e:
#     print(f"\nEin unerwarteter Fehler ist aufgetreten: {e}")

# FILE_1 = r"C:\Users\isapa\PycharmProjects\itProger\WEITERBILDUNG\Übungen\.txt & .json\tagebuch.txt"
#
# def count_word_occurrences(text, word):
#     words = text.lower().split()  # Приводим к нижнему регистру и разбиваем по пробелам
#     return words.count(word.lower())  # Подсчёт точных вхождений слова
#
# try:
#     with open(FILE_1, 'r', encoding='utf-8') as file:
#         text = file.read()
#         word_to_find = "домой"  # Искомое слово
#         count = count_word_occurrences(text, word_to_find)
#         print(f"Das Wort '{word_to_find}' kommt {count} Mal im Text vor.")
# except FileNotFoundError:
#     print("\nFehler: Die Datei 'tagebuch.txt' wurde nicht gefunden.")
# except Exception as e:
#     print(f"\nEin unerwarteter Fehler ist aufgetreten: {e}")



import json


def zaehle_wort(text, wort):
    return text.lower().count(wort.lower())


def ersetze_wort(text, alt, neu):
    return text.replace(alt, neu)


def teile_in_saetze(text):
    return text.split('.')


def speichere_als_json(dateiname, daten):
    with open(dateiname, 'w', encoding='utf-8') as file:
        json.dump(daten, file, ensure_ascii=False, indent=4)


try:
    with open('tagebuch.txt', 'r', encoding='utf-8') as file:
        inhalt = file.read()
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
else:
    wort_vorkommen = zaehle_wort(inhalt, 'traurig')
    print(f"Das Wort 'traurig' kommt {wort_vorkommen} Mal vor.")

    aktualisierter_text = ersetze_wort(inhalt, 'traurig', 'glücklich')

    with open('tagebuch_neu.txt', 'w', encoding='utf-8') as neue_datei:
        neue_datei.write(aktualisierter_text)

    saetze = teile_in_saetze(aktualisierter_text)
    speichere_als_json('tagebuch_saetze.json', saetze)