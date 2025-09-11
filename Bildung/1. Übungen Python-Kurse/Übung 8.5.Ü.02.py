# a
# Liste von Tupeln
studenten = [
        ("Anna Müller", 123456, "Informatik"),
        ("Bernd Schmidt", 654321, "Maschinenbau"),
        ("Carla Weber", 112233, "BWL"),
        ("Daniel Fischer", 445566, "Physik"),
        ("Elena Wagner", 778899, "Medizin")
    ]
def speichere_daten(x):
    '''Die Funktion speichert diese Daten
    in einer Textdatei namens studentendaten.txt.'''
    try: # Nutzen Konstruktion try-except für der Bearbeitung von Ausnahmen
        with open('.txt & .json/studentendaten.txt', 'w', encoding='utf-8') as file: # Öffnen die Datei zum Schreiben
            for el in studenten: # Bedingungen
                nm, mn, sg = el # Drei Elemente in Tuple bzw.
                file.write(f'Name: {nm}, '
                           f'Matrikelnummer: {mn}, '
                           f'Studiengang: {sg}\n') # Schreiben in File dieser Daten
    except Exception as e: # Wenn Ausnahmen
        print(f"Ein Fehler ist aufgetreten beim Speichern der Daten: {e}")
def lade_daten():
    '''die Funktion, die gespeicherten Daten
    aus der Datei studentendaten.txt
    liest und als Liste von Dictionaries zurückgibt'''
    try:
        studenten_dictionary = [] # bauen neue Wörtebuch, es ist leer
        with open('.txt & .json/studentendaten.txt', 'r', encoding='utf-8') as file: # Öffnen die Datei zum lesen
            for information in file:
                #   Trennen Sie die Daten in der Textdatei durch Kommas
                nm, mn, sg = information.strip().split(', ')
                # Schöpfen Dictionary, eingeben key: value
                # Trennen Sie weiter durch Doppelpunkte, was notwendig ist [1].
                studenten_new = {
                    'Name': nm.split(': ')[1],
                    'Matrikelnummer': mn.split(': ')[1],
                    'Studiengang': sg.split(': ')[1]
                }
                studenten_dictionary.append(studenten_new)
            return studenten_dictionary
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Speichern der Daten: {e}")
        return []

print(lade_daten())