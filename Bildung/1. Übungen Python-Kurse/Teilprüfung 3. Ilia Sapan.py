#-------------------------------------------
# Dateiname: Python_Programm.py
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_8.7.A.01)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 31.01.2025, 09:02 AM
#-------------------------------------------
import json
FILE_T = '.txt & .json/NAMEN.txt'
FILE_J = '.txt & .json/NAMEN.json'
def namens(textfile)->list:
    '''Die Funktion, die eine Liste von
    Namen aus einer Textdatei liest. '''
    nur_namens = [] # Wir erstellen eine Liste zur weiteren Bearbeitung
    try: # Wir öffnen try-except Blocke für der Bearbeitung Fehler
        with open(textfile, 'r', encoding='utf-8') as file: # Wir öffnen Textdatei mit with-Anweisung
            for line in file:
                name = line.split(", ")[0] # Wir trennen die Zeichenfolge durch ein Komma und nehmen das erste Element.
                nur_namens.append(name) # Wir fügen Namens in der Liste hinzu
            return nur_namens # Wir geben Liste zurück
    except Exception as e:
        print(f'\nFehler entdeckt!')
        return []
# Speichern als JSON
def namens_json(funktion):
    '''Die Funktion, die eine Liste von
        Namen in JSON-Format speichert'''
    try: # Wir öffnen try-except Blocke für der Bearbeitung Fehler
        with open(FILE_J, 'w', encoding='utf-8') as file: # Wir öffnen JSON-FILE für der Schreibung Namensdatei
            json.dump(funktion, file, indent=4) #
    except Exception as e:
        print(f'\nFehler entdeckt!')
    finally:
        print("Daten erfolgreich in JSON gespeichert!\n"
              "Sie finden sie in der Datei 'NAMEN.json'.")
# Aufruf einer JSON-Verarbeitungsfunktion,
# die als Argument eine andere Funktion hat,
# die eine Textdatei verarbeitet:
# namens_json(namens(FILE_T))

# Benutzeroberfläche:


while True:
    print('----------------------------------------------------------------------------------------------------')
    print('\t\t\t\t\t\t\tHerzlich willkommen!\n'
          'Mit diesem Programm können Sie Namen aus einer '
          'Textdatei übernehmen und in das JSON-Format konvertieren.')
    print('----------------------------------------------------------------------------------------------------')
    print('\t\t\t\t!!! Wir möchten Sie darauf Aufmerksam machen,\n'
          '\t\t\t\tdass Datei soll dabei so strukturiert sein,\n'
          '\t\t\t\tdass jeder Name in einer neuen Zeile steht, nach Komma !!!')
    print('----------------------------------------------------------------------------------------------------')
    options = int(input('Wählen Sie den gewünschten Vorgang:\n'
                    '1. Namen holen.\n'
                    '2. Namen in JSON-Format konvertieren.\n'
                        'Zahl: '))

    while options not in [1,2]:
        print('Bitte, oder 1, oder 2!')
        options = int(input('Wählen Sie den gewünschten Vorgang:\n'
                                '1. Namen holen.\n'
                                '2. Namen in JSON-Format konvertieren.\n'
                                'Zahl: '))

    if options == 2:
        try:
            pfad_file = input('Bitte kopieren Sie den Absolute Pfad zu Ihrer Textdatei und fügen Sie ihn hier ein.\n'
                              'Pfad: ')
            file_text = fr'{pfad_file}'
            namens_json(namens(file_text))
        except ValueError as e:
            print(f"Das ist {e}! Geben Sie die richtigen Werte ein!")
    elif options == 1:
        try:
            pfad_file = input('Bitte kopieren Sie den Absolute Pfad zu Ihrer Textdatei und fügen Sie ihn hier ein.\n'
                              'Pfad: ')
            file_text = fr'{pfad_file}'
            print(f"Namen-Liste: {namens(file_text)}")
        except ValueError as e:
            print(f"Das ist {e}! Geben Sie die richtigen Werte ein!")
            # Möglichkeit, das Programm zu beenden
    beenden = input("Möchten Sie das Programm beenden? (Ja/Nein): ").lower()
    if beenden == "nein":
        continue
    elif beenden == "ja":
        break

