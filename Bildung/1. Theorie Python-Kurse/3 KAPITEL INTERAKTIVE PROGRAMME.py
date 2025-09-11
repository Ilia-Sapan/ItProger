# 3.1 Das erste Python-Skript
print("Hallo")

# 3.2 EVA-Prinzip
name = input("Name: ")
gruß = "Hallo " + name + "!"
print(gruß)

# 3.3. Kommentare

# 3.4. Projekt: Volumenberechnung

#-----------------------------------------------------
#Dateiname: zylinder.py

print("Berechnung des Volumens eines Zylinders")
eingabe_h = input("Höhe in Meter: ")
eingabe_d = input("Durchmesser in Meter: ")
#Verarbeitung
h = float(eingabe_h)
d = float(eingabe_d)
volumen = (d/2)**2 * h
text = "Das Volumen beträgt " + str(volumen) + " Kubikmeter!"
print(text)