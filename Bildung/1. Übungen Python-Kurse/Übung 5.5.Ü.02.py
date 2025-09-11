#
# def geld_umrechner(menge, waehrung):
#     ''' Python-Programm, das eine Funktion namens umrechner enthält '''
#     if waehrung == "USD":
#         return menge
#     elif waehrung == "EUR":
#         return menge * 1.1
#     elif waehrung == "GPB":
#         return menge * 1.1 * 0.9
#     else:
#         raise ValueError ("Ungultige Einheit. Nur 'USD', 'GPB' oder 'EUR' sind erlaubt")
#
#
# while True:
#     # menge = float(input("Sum: "))
#     # waehrung = str(input("GPB, EUR oder USD: "))
#     # print(geld_umrechner(menge, waehrung))
#     try:
#         eingabe = input("Bitte geben Sie die Summe ein (oder 'ende', um zu beenden): ")
#         if eingabe.lower() == 'ende':
#             print("Programm beendet. Auf Wiedersehen!")
#             break
#
#         menge = float(eingabe)
#         waehrung = input("Geben Sie die Waehrung ein (GPB, EUR oder USD): ").upper()
#
#         if waehrung not in ['GPB', 'EUR', 'USD']:
#             print("Ungültige Waehrung. Bitte geben Sie GPB, EUR oder USD.")
#             continue
#
#         # Umrechnung
#         umgerechnete_geld = geld_umrechner(menge, waehrung)
#         if waehrung == 'USD':
#             ziel_waehrung = 'USD'
#         elif  waehrung == "GPB":
#             ziel_waehrung = "GPB"
#         else:
#             ziel_waehrung == "EUR"
#         print(f"Die umgerechnete Temperatur beträgt {round(geld_umrechner)} Grad {ziel_waehrung}.")
#
#     except ValueError:
#         print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
#
def umrechner(betrag, waehrung="USD"):
    if waehrung == "USD":
        return betrag * 1.1
    elif waehrung == "GBP":
        return betrag * 0.9
    else:
        return None


while True:
    print("Währungsumrechner: EUR zu USD oder GBP")
    betrag = float(input("Bitte geben Sie den Betrag in EUR ein, den Sie umrechnen möchten: "))
    waehrung = input(
        "Bitte geben Sie die Währung ein, in die Sie umrechnen möchten (USD/GBP). Drücken Sie Enter für USD: ").upper()

    if waehrung not in ["USD", "GBP", ""]:
        print("Die angegebene Währung wird nicht unterstützt.")
    else:
        ergebnis = umrechner(betrag, waehrung)
        if ergebnis is not None:
            print(f"Umrechnungsergebnis: {ergebnis:.2f} {waehrung}")
        else:
            print("Es gab ein Problem mit der Währungsumrechnung.")

    weiter = input("Möchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").lower()
    if weiter != "ja":
        print("Programm beendet.")
        break
