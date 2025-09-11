

FILE_P = r"/WEITERBILDUNG/Übungen/.txt & .json/products.txt"

import re


def berechne_mwst(preis):
    return preis * 1.19  # Calculate and return price with VAT


def ist_gueltiger_preis(preis):
    try:

        float(preis)  # Attempt to convert to float

        return True

    except ValueError:

        return False


def ist_gueltiger_name(name):
    return bool(re.match(r'^[\w\s]+$', name))


produkte = []

try:

    with open(FILE_P, 'r') as file:

        next(file)  # Skip the header line

        for line in file:

            produkt, preis_str = line.strip().split(',')

            if not ist_gueltiger_preis(preis_str):
                print(f"Warnung: Ungültiger Preis für {produkt}. Überspringe Produkt.")

                continue

            if not ist_gueltiger_name(produkt):
                print(f"Warnung: Ungültiger Produktname '{produkt}'. Überspringe Produkt.")

                continue

            preis = float(preis_str)

            produkte.append((produkt, preis, berechne_mwst(preis)))

    with open('produkte_mit_mwst.txt', 'w') as file:

        file.write('Produkt,Preis,MwSt\n')

        for produkt in produkte:
            file.write(f"{produkt[0]},{produkt[1]:.2f},{produkt[2]:.2f}\n")



except IOError:

    print("Fehler beim Lesen der Datei.")
