#-------------------------------------------
# Dateiname: Taschenrechner.py
# Das ist Python-Programm,
# das als Taschenrechner für einfache mathematische Operationen
# (Addition, Subtraktion, Multiplikation, Division) fungiert.
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 17.01.2025, 10:22 AM
#-------------------------------------------

# Wir machen die Funktion
def taschenrechner():
    while True:
        # Wir fordern einen benutzerdefinierten Vorgang an, indem wir die Antwort in Kleinbuchstaben übersetzen
        benutzerfrage_operation = input("Willkommen beim Programm „Rechner - Python!“.\n"
                                  "Bitte wählen Sie die gewünschte Operation durch Eingabe eines Buchstabens aus:\n"
                                  "'A' für Addition, 'S' für Subtraktion, 'M' für Multiplikation, 'D' für Division.\n"
                                  "Sie haben die Wahl: ").lower()


        while benutzerfrage_operation not in ["a", "s", "m", "d"]:
            print("Bitte wählen Sie die Buchstaben A, S, M oder D!")
            benutzerfrage_operation = input("Willkommen beim Programm „Rechner - Python!“.\n"
                                            "Bitte wählen Sie die gewünschte Operation durch Eingabe eines Buchstabens aus:\n"
                                            "'A' für Addition, 'S' für Subtraktion, 'M' für Multiplikation, 'D' für Division.\n"
                                            "Sie haben die Wahl: ").lower()
        if benutzerfrage_operation in ["a", "s", "m", "d"]:
            try:
                # Wir beantragen die erste Nummer
                benutzerfrage_zahl_1 = float(input("Großartig, jetzt geben Sie die erste Zahl ein: "))
                # Wir beantragen die zweite Nummer
                benutzerfrage_zahl_2 = float(input("Gut, geben Sie nun die zweite Zahl ein: "))
                if benutzerfrage_operation == "a":
                    print(f"Resultat ist {benutzerfrage_zahl_1 + benutzerfrage_zahl_2}")
                elif benutzerfrage_operation == "s":
                    print(f"Resultat ist {benutzerfrage_zahl_1 - benutzerfrage_zahl_2}")
                elif benutzerfrage_operation == "m":
                    print(f"Resultat ist {benutzerfrage_zahl_1 * benutzerfrage_zahl_2}")
                elif benutzerfrage_operation == "d":
                    print(f"Resultat ist {benutzerfrage_zahl_1 / benutzerfrage_zahl_2}")
            except ZeroDivisionError: # Behandlung von Fehlern bei der Division durch Null
                print("Man kann nicht durch Null dividieren!")
            except ValueError: # Behandlung von Eingabefehlern
                print("Geben Sie die richtigen Werte ein!")
            finally:
                print("Danke!Tschüß!")
# Starten einen Funktion
taschenrechner()














