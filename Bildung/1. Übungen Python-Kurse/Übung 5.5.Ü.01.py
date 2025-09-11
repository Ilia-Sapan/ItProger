

#Die Umrechnungsformeln lauten: (C = (F - 32) * 5/9) und (F = C * 9/5 + 32).

# A
def temperature_umrechner(temperature, einheit = "c" ) :
    '''Die Funktion soll die Temperatur von Celsius in Fahrenheit umrechnen,
    wenn einheit den Wert 'C' hat,
    und von Fahrenheit in Celsius,
    wenn einheit den Wert 'F' hat'''
    if einheit == "c":
        # Celsius in Farenheit
        return temperature * 9  / 5 + 32
    elif einheit == "f":
        return  (temperature - 32) * 5 / 9
    else:
        raise ValueError ("Ungultige Einheit. Nur 'c' oder 'f' sind erlaubt")


# B
while True:
    try:
        eingabe = input("Bitte geben Sie die Temperatur ein (oder 'ende', um zu beenden): ")
        if eingabe.lower() == 'ende':
            print("Programm beendet. Auf Wiedersehen!")
            break

        temperatur = float(eingabe)
        einheit = input("Geben Sie die Einheit ein ('C' für Celsius, 'F' für Fahrenheit): ").lower()

        if einheit not in ['c', 'f']:
            print("Ungültige Einheit. Bitte geben Sie 'C' oder 'F' ein.")
            continue

        # Umrechnung
        umgerechnete_temperatur = temperatur_umrechner(temperatur, einheit)
        ziel_einheit = 'Fahrenheit' if einheit == 'c' else 'Celsius'
        print(f"Die umgerechnete Temperatur beträgt {round(umgerechnete_temperatur, 2)} Grad {ziel_einheit}.")

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")


