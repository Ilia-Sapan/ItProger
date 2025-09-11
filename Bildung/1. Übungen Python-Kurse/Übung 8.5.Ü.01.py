personen = [('Ilia', 30), ('Ellina', 30), ('Uliana', 24), ('Sasha', 31)]

def speichere_daten(tupels):
    try:
        tupels = dict(tupels)
        with open(".txt & .json/personen.txt", "w", encoding="utf-8") as file:
            for keys, values in tupels.items():
                file.write(f'{keys}: {values}\n')
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Speichern der Daten: {e}")

def lade_daten():
    try:
        personen_1 = []
        with open(".txt & .json/personen.txt", "r", encoding="utf-8") as file:
            for information in file:
                name, alter =  information.strip().split(': ')
                personen_1.append({'Name': name, 'Alter': int(alter)})
            return personen_1
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Speichern der Daten: {e}")
        return []


def main():
    personen = [('Ilia', 30), ('Ellina', 30), ('Uliana', 24), ('Sasha', 31)]
    speichere_daten(personen)
    geladene_daten = lade_daten()
    if geladene_daten:
        for person in geladene_daten:
            print(f"Name: {person['Name']}, Alter: {person['Alter']}")
    else:
        print("Keine Daten geladen.")

if __name__ == "__main__":
        main()



