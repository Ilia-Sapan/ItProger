from PIL.ImageFile import ERRORS

einkaufsliste = ['Apple', 'Banana', 'Kiwi', 'Melon', 'Sandwich']
def einkauf_hinzufuegen(kauflisten):
    for i in range(3):
        produkt = input('Geben Sie bitte Lebensmittel ein: ')
        if produkt not in kauflisten:
            kauflisten.append(produkt)
        else:
            print('Lebensmittel bereits in der Liste!')
    return kauflisten


try:
    with open('.txt & .json/einkaufsliste.txt', 'w') as datei:
        for lebensmittel in einkaufsliste:
            datei.write(lebensmittel + '\n')
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
try:
    with open('.txt & .json/einkaufsliste.txt', 'r') as datei:
        inhalt = datei.readlines()
        print("Einkaufsliste:")
        for lebensmittel in inhalt:
            print(lebensmittel.strip())
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Lesen der Datei: {e}")

