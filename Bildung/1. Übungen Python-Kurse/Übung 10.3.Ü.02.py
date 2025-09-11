# a
import os

def erstelle_datei(namen_textdatei, namen_verzeichnis):
    '''Erstellt eine neue Textdatei mit vorgegebenem Namen und Inhalt im spezifischen Verzeichnis.'''

    # Создаём папку, если её нет
    os.makedirs(namen_verzeichnis, exist_ok=True)

    # Полный путь к файлу
    ziel_datei = os.path.join(namen_verzeichnis, f"{namen_textdatei}.txt")

    # Текст для записи
    text = "I sebyvayu of crappy Raschke, knit cap and spizdiv plastic bag with nishtyak"

    # Создаём файл в указанной папке
    with open(ziel_datei, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Datei {ziel_datei} wurde erfolgreich erstellt!")


# Пример использования:
erstelle_datei("meine_datei", "mein_verzeichnis")

Aufgabe: Systemumgebung
Entwickle ein Python-Skript, das folgende Funktionen implementiert:

a) Erstelle eine Funktion erstelle_datei, die eine neue Textdatei mit einem vorgegebenen Namen und Inhalt in einem spezifischen Verzeichnis erstellt. Verwende dazu die with-Anweisung und stelle sicher, dass Fehler, wie z.B. fehlende Schreibberechtigungen, mit try und except abgefangen werden.

b) Implementiere eine Funktion listdir_filter, die alle Dateien eines Verzeichnisses auflistet, die eine bestimmte Dateiendung haben (z.B. .txt). Nutze dazu das Modul os und eine List Comprehension.

c) Schreibe eine Funktion umbenennen_dateien, die alle Dateien eines Verzeichnisses, die eine bestimmte Endung haben, umbenennt, indem sie ein Präfix hinzufügt. Verwende dazu das Modul os.

d) Entwickle eine Funktion json_speichern, die eine Liste von Dictionaries in eine Datei im JSON-Format speichert. Verwende dazu das Modul json.

e) Implementiere eine Funktion json_laden, die eine JSON-Datei liest und den Inhalt als Python-Objekt zurückgibt.

f) Erstelle eine Funktion regex_suche, die in allen .txt-Dateien eines Verzeichnisses nach einem regulären Ausdruck sucht und die Namen der Dateien zurückgibt, in denen die Suche erfolgreich war.

Für jede dieser Funktionen sollst du ein kurzes Beispiel für deren Aufruf und Verwendung schreiben.