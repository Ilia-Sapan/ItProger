
#a, b
from random import randint
from math import sqrt

if __name__ == '__main__':
    def erzeuge_zufallszahlen_liste(n):
        '''Funktion, die eine Liste mit
        n zufälligen ganzen Zahlen zwischen
        1 und 100 zurückgibt.'''
        return [randint(1, 100) for _ in range(n)]

    def berechne_wurzeln(liste):
        '''Funktion, die für jede Zahl in der übergebenen
        Liste die Quadratwurzel berechnet und die Wurzeln gibt.'''
        return [round(sqrt(x), 3) for x in liste]

    def sortiere_und_erzeuge_tupel(liste):
        ''' Funktion, die Liste von Quadratwurzeln aufsteigend sortiert
        und ein Tupel aus (Originalzahl, Quadratwurzel)
        für jede Zahl in der ursprünglichen Liste erzeugt.'''
        return sorted((x, round(sqrt(x), 3)) for x in liste)

    def erstelle_dictionary(tupel_liste):
        '''Funktion, wobei der Schlüssel die Originalzahl
        und der Wert die Quadratwurzel ist.
        Gib dieses Dictionary zurück.'''
        return {x: wurzel for x, wurzel in tupel_liste}

    def main(n):
        result_1 = erzeuge_zufallszahlen_liste(n)  # Zufällige Zahlen
        result_2 = berechne_wurzeln(result_1)  # Quadratwurzeln berechnen
        result_3 = sortiere_und_erzeuge_tupel(result_1)  # Sortierte Tupel
        result_4 = erstelle_dictionary(result_3)  # Dictionary erstellen
        return result_1, result_2, result_3, result_4

    # Hauptprogramm
    print(main(10))
