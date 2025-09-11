#-------------------------------------------
# Dateiname: Bücherei.py
# Software zur Verwaltung von Büchereien
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 24.01.2025, 10:29 AM
#-------------------------------------------

if __name__ == "__main__":
    # Hier wird die Datenbank von Bibliotheken gegeben
    buecherei_datenbank = [
        {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
        {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
        {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
    ]
    def buchsuche(titel, autor=None):
        """Die Funktion, die Bücher nach Titel und optional nach Autor sucht"""
        # Wir schaffen eine relevante Buchliste
        relevant_books = [elements for elements in buecherei_datenbank if elements["Titel"] == titel]
        # Bedingungen, wenn ein Autorname vorhanden ist
        if autor is not None:
            relevant_books = [book for book in relevant_books if book["Autor"] == autor]
        for elements in relevant_books:
            for keys, values in elements.items():
                print(f"{keys} - {values}")
    def fuege_buch_hinzu(titel, autor, jahr):
        '''Die Funktion, die neue Büche hinzufügt'''
        # Wir wandeln die Liste in das Wörtebuch um
        bueche = dict(Titel = titel, Autor = autor, Jahr = int(jahr))
        # Wir fügen neues Buch in das Wörtebuchliste hinzu
        buecherei_datenbank.append(bueche)
        return buecherei_datenbank
    def buecher_nach_jahr(jahr):
        '''Die Funktion, die alle Bücher zurückgibt, die in einem bestimmten Jahr veröffentlicht wurden.'''
        # Wir machen Bedingungen und iterieren
        return list(filter(lambda buch: buch["Jahr"] == jahr, buecherei_datenbank))
    def zeige_datenbank(lists):
        '''Die Funktion, die die den aktuellen Inhalt der Bücherei-Datenbank in einer formatierten Ausgabe anzeigt. '''
        print("Die folgenden Bücher sind in unserer Bibliothek vorhanden:\n")
        for elements in lists:
            for keys, values in elements.items():
                print(f"{keys} - {values}")
while True:
    antwort = input(
        "Guten Tag! Wir freuen uns, Sie in SHEK-Bibliothek begrüßen zu dürfen!\n "
        "Welchen Dienst möchten Sie nutzen?\n"
        "(S)uchen Sie ein Buch im Katalog nach Titel/Autor.\n"
        "(H)inzufügen eines neuen Buches zum Katalog.\n"
        "Suche nach einem Buch nach (E)rscheinungsjahr.\n"
        "(K)atalog ansehen.\n"
        "Bitte geben Sie den Buchstaben in Klammern ein, um die gewünschte Funktion zu wählen: ").upper()
    while antwort not in ["S", "H", "E", "K"]:
        print("Bitte wählen Sie die Buchstaben  S, H, E oder K!")
        antwort = input(
            "Guten Tag! Wir freuen uns, Sie in  SHEK-Bibliothek begrüßen zu dürfen!\n "
            "Welchen Dienst möchten Sie nutzen?\n"
            "(S)uchen Sie ein Buch im Katalog nach Titel/Autor.\n"
            "(H)inzufügen eines neuen Buches zum Katalog.\n"
            "Suche nach einem Buch nach (E)rscheinungsjahr.\n"
            "(K)atalog ansehen.\n"
            "Bitte geben Sie den Buchstaben in Klammern ein, um die gewünschte Funktion zu wählen: ").upper()
    if antwort in ["S", "H", "E", "K"]:
        try:
            if antwort == "S":
                titel_nutz = input("Geben Sie bitte das Titel ein: ")
                autor_nutz = input("Geben Sie bitte Autornamen ein: ")
                print(buchsuche(titel=titel_nutz, autor=autor_nutz))
            elif antwort == "H":
                titel_nutz = input("Geben Sie bitte das Titel ein: ")
                autor_nutz = input("Geben Sie bitte Autornamen ein: ")
                jahr_nutz = input("Geben Sie bitte Jahr ein: ")
                print(fuege_buch_hinzu(titel_nutz, autor_nutz, jahr_nutz))
            elif antwort == "E":
                jahr_nutz = int(input("Geben Sie bitte Jahr ein: "))
                print(buecher_nach_jahr(jahr=jahr_nutz))
            elif antwort == "K":
                print(zeige_datenbank(buecherei_datenbank))
        except ValueError:
            print("Geben Sie die richtigen Werte ein!")
        # Möglichkeit, das Programm zu beenden
        beenden = input("Möchten Sie das Programm beenden? (Ja/Nein): ").lower()
        if beenden == "ja":
            print("Vielen Dank für Ihren Besuch in der SCHEK-Bibliothek! Auf Wiedersehen!")
            break

