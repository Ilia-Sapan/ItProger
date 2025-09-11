# 2.1 Literale und die Funktion type()
print(type(1)) # <class 'int'> ganze Zahl
print(type(1.0)) # <class 'float'> Gleitkommazahl
print(type(12+3j)) # <class 'complex'> Komplexe Zahlen
print(type("Sie sagte 'Danke' und ging hinaus")) # <class 'str'> Zeichenkette
# 2.2 Die Python-Typ-Hierarchie
print(bin(19)) # Die Funktion bin() liefert zu einer Dezimalzahl die Python-Binärdarstellung: 0b10011
print(hex(421)) # Mit der Funktion hex() kannst du die Hexadezimaldarstellung einer ganzen Zahl ermitteln: 0x1a5
# Tupel (tuple)
person = ("Anne", 2001)
# Liste (list)
primzahlen = [1, 2, 3, 4, 5] # Im Unterschied zu Strings und Tupeln kann man eine Liste verändern:
s = [3, 7, 13]
s[0] = 5
print(s)
# Menge (set)
menge = {1,2,3}
# Dictionary (dict)
d = {'Sun': 'Sonnen', 'Moon': 'Mond', 'Star': 'Stern'}
# Wahrheitswerte – der Datentyp bool
print(bool(22)) # True
print(bool(0)) # False

#NoneType
a = print()
print(a) # None
b = None
print(b) # None

# Test auf Vorkommen
print("I" in "Team") # False
print(1 in {1,2,4}) # True

#Anzahl der Items
#Die Standartfunktion len() liefert die Größe einer Kollektion
print(len("Python")) # 6
print(len([1,2])) # 2

#Index
farben = ("rot", "gelb", "grün")
print(farben[1]) # gelb

#Konkatenation
print((1,2,3,4)+(5,6,7)) # (1, 2, 3, 4, 5, 6, 7)

# 2.5 Objekte eines Typs erzeugen – Casting

print(int(12.3)) # 12
print(str([1,2,3])) # [1, 2, 3]
print(list("Sonne")) # ['S', 'o', 'n', 'n', 'e']
print(set("abaac")) # {'a', 'c', 'b'} Diplikate einfernt

