# Aufgabe: EVA-Prinzip, Kommentare


# A
nummer_a = 3.5 # float
nummer_b = 23 # int
nummer_c = 13j # complex
nummer_d = "33" # str

# B
listen = [nummer_a, nummer_b, nummer_c]
for x in listen:
    print(type(x))

#C
nummer_d = float(nummer_d)

# D
number_1 = input("Geben Sie erste Zahl ein: ")
number_2 = input("Geben Sie zweite Zahl ein: ")
number_zusammen = str(number_2 + " und " + number_1) # umwandeln
print(number_zusammen)