# A
def berechne_durchschnitt(zahlliste):
    if not zahlliste:  # Prüft, ob die Liste leer ist
        return None
    for zahl in zahlliste:
        zahl += zahl
        mid = zahl / len(zahlliste)
    return mid



nuumbeerss = [1, 2, 3, 4]
print(f"Durchschnittswert ist {berechne_durchschnitt(nuumbeerss)}.")


