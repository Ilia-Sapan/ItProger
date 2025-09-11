#-------------------------------------------
# Dateiname: Kundenfeedback.py
# ein Python-Programm, das eine Textdatei mit Kundenfeedback aus verschiedenen Ländern analysiert.
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Erste Änderung: 07.02.2025, 07:46 AM
# # Letzte Änderung: 07.02.2025, ___
#-------------------------------------------
FEEDBACK_FILE = ".txt & .json/feedback.txt"
# a
def oeffnen_datei(file_textdatei)-> str :
    '''Die Funktion liest Textdatei, die Kundenkommentare
    in verschiedenen Sprachen enthält'''

    # Wir öffnen die Datei mit dem Modul r.
    # Und encoding="utf-8" wird uns beim Lesen helfen
    try:
        with open(file_textdatei, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
    except Exception as e:
        print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
    else:
        print("Operation erfolgreich abgeschlossen!  \U0001F60A")
    return content # Wir geben aus dem Textdatei der Text
# b
def rueckrufdatum(file_textdatei)-> list :
    '''Die Funktion liest Textdatei, und alle Datumsangaben
    im Format DD.MM.YYYY aus dem Text zu extrahiert
    und speichert diese in einer Liste.'''

    #Wir importieren Bibliothek re
    from re import findall

    # Wir öffnen die Datei mit dem Modul r.
    # Und encoding="utf-8" wird uns beim Lesen helfen
    try:
        with open(file_textdatei, "r", encoding="utf-8") as file:
            text = file.read()

            # Regulärer Ausdruck für die Suche nach Daten im Format TT.MM.JJJJJ

            datum = findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)
    except FileNotFoundError:
        print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
    except Exception as e:
        print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
    else:
        print("Operation erfolgreich abgeschlossen!  \U0001F60A")

    return datum # Wir geben aus dem Text eine Liste von Daten auf Anfrage und Bedingungen zurück
# c
def wie_oft_jedes_datum(ergebnis_dat)-> dict:
    '''Die Funktion, die zahlt, wie oft jedes Datum vorkommt,
    und speichere die Ergebnisse in einem Dictionary'''
    try:
        # Wir öffnen leere Dictionary
        datum_dict = {}
        for datum in ergebnis_dat:
            datum_zahl = ergebnis_dat.count(datum) # Die Anzahl bestimmter Daten aus der Liste in eine Variable „ziehen“.
            datum_dict[datum] = datum_zahl # Wir machen in Dictionary 'key-value'
        return datum_dict # z.B. print(wie_oft_jedes_datum(rueckrufdatum(FEEDBACK_FILE)))
    except FileNotFoundError:
        print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
    except Exception as e:
        print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
    else:
        print("Operation erfolgreich abgeschlossen!  \U0001F60A")
# d
def wort_gut(file_textdatei) -> list:
    '''Die Funktion, die identifiziert das Wort
    "exzellent" in beliebiger Groß-
    oder Kleinschreibung enthalten und gibt das ganze Satz zurück.'''
    import re
    try:
        with open(file_textdatei, "r", encoding="utf-8") as file:
            content = file.read().lower()  # Der gesamte Text wird klein geschrieben
            exzellent_list = [] # Wir schöpfen leere Liste
            words = ["eccellente", "exzellent", "excellent"] # Wötre, die suchen wir

            # Den Text in Zeilen aufteilen und durch Datums und Satzzeichen trennen
            # Patterns: lookbehind mit Punkt (\.) und Abstand (\s)
            # oder (|) lookbehind mit unserem Datum in der darüber liegenden Funktion
            sentences = re.split(r'(?<=\.\s)|(?<=\n\d{2}\.\d{2}\.\d{4})', content)

            # Wir prüfen
            for sentence in sentences:
                if any(word in sentence for word in words):
                    exzellent_list.append(sentence.strip())

        return exzellent_list
    except FileNotFoundError:
        print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
    except Exception as e:
        print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
    else:
        print("Operation erfolgreich abgeschlossen!  \U0001F60A")
# e
import json
datum_gefund = wie_oft_jedes_datum(rueckrufdatum(FEEDBACK_FILE)) # Dictionary
komment_gefund = wort_gut(FEEDBACK_FILE) # List

# Wir speichern die Daten in dem JSON-Format

try:
    with open(".txt & .json/datums_vorkommen.json", "w", encoding="utf") as file:
        json.dump(datum_gefund, file, indent=4)
except FileNotFoundError:
    print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
except Exception as e:
    print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
else:
    print("Operation erfolgreich abgeschlossen!  \U0001F60A")

try:
    with open(".txt & .json/exzellente_feedbacks.json", "w", encoding="utf") as file:
        json.dump(komment_gefund, file, indent=5)
except FileNotFoundError:
    print("Es tut mir leid, die Datei wurde nicht gefunden.   \U0001F622")
except Exception as e:
    print(f"Sorry, aber es gibt ein Fehler: {e}...  \U0001F622")
else:
    print("Operation erfolgreich abgeschlossen!  \U0001F60A")
