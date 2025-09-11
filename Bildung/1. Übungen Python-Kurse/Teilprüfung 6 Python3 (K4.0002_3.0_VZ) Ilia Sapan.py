#-------------------------------------------
# Dateiname: Online-Buchladens.py
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 21.02.2025. Start: 09:15 AM, Ende: 13:24
#-------------------------------------------
import customtkinter
class Buch:
    '''Die Klasse Buch mit den Attributen
    titel, autor, kategorie und preis.'''

    def __init__(self, titel, autor, kategorie, preis): # Klassenparameter festlegen
        '''Konstruktor, der die Klassenparameter initialisiert'''
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self)->str: # ein Objekt einer Klasse als String dargestellt werden soll
        '''Konstruktor, der Klassenparameter als String zurückgibt'''
        return (f'Titel: {self.titel}'
                f'\nAutor: {self.autor}'
                f'\nKategorie: {self.kategorie}'
                f'\nPreis: {self.preis}')
class Buchladen:
    '''Eine Klasse, die eine Liste
    von Büchern speichert, sie
    hinzufügt und den Preis nachschlägt'''

    def __init__(self): # Ein neues Klassenbuch initialisieren
        '''Die Funktion initialisiert den Beginn der Klasse'''
        self.inventar = []

    def buch_hinzu(self, buch): # Buch hinzufügen, und Buch ist ein Object von Klasse "Buch"
        '''Funktion zum Hinzufügen eines Buches zur Liste'''
        self.inventar.append(buch)

    def get_inventar_kategorie(self, kategorie):
        '''Funktion zum Durchsuchen von Büchern und Hervorheben ihrer Kategorien'''
        return [buch for buch in self.inventar if buch.kategorie == kategorie]

    def gesamte_summe(self, buecher):
        '''Funktion, die zahlt des Gesamtpreises einer Buchauswahl'''
        return sum(buch.preis for buch in buecher)

    def __str__(self): # ein Objekt einer Klasse als String dargestellt werden soll
        '''Konstruktor, der Klassenparameter als String zurückgibt'''
        return "\n".join(f"{buch.titel} by {buch.autor}: {buch.preis}" for buch in self.inventar)

# Obkekten Buch-Klasse
buch1 = Buch("Der kleine Prinz", "Antoine de Saint-Exupéry", "Roman", 15.99)
buch2 = Buch("Die unendliche Geschichte", "Michael Ende", "Roman", 12.99)
buch3 = Buch("Sapiens: Eine kurze Geschichte der Menschheit", "Yuval Noah Harari", "Sachbuch", 19.99)
buch4 = Buch("Die Physik des Bewusstseins", "Giulio Tononi", "Wissenschaft", 24.99)

# Obkekt Buchladen-Klasse
buchladen = Buchladen()

# Büche hinzufügen
buchladen.buch_hinzu(buch1)
buchladen.buch_hinzu(buch2)
buchladen.buch_hinzu(buch3)
buchladen.buch_hinzu(buch4)

# Bücher nach Kategorien suchen
romane = buchladen.get_inventar_kategorie("Roman")
sachbuecher = buchladen.get_inventar_kategorie("Sachbuch")

# Drücken Resultat
print("Romane im Buchladen:")
for buch in romane:
    print(buch)

print("\nSachbücher im Buchladen:")
for buch in sachbuecher:
    print(buch)

# Zahlen Gesamtpreis
gesamtpreis = buchladen.gesamte_summe(romane)
print(f"\nGesamtpreis der Romane: {gesamtpreis} Euro")