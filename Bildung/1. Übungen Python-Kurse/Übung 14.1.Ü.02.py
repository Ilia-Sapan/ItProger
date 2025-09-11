
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel  # Setzt den Titel des Buches
        self.autor = autor  # Setzt den Autor des Buches
        self.ausgeliehen = False  # Standardmäßig wird das Buch nicht ausgeliehen

    def ausleihen(self):
        if self.ausgeliehen:
            print("Buch bereits ausgeliehen")  # Wenn das Buch schon ausgeliehen ist
        else:
            self.ausgeliehen = True  # Setzt das Attribut 'ausgeliehen' auf True
            print(f"{self.titel} wurde ausgeliehen.")  # Gibt eine Bestätigung aus

    def zurueckgeben(self):
        if not self.ausgeliehen:
            print("Buch war nicht ausgeliehen")  # Wenn das Buch nicht ausgeliehen ist
        else:
            self.ausgeliehen = False  # Setzt das Attribut 'ausgeliehen' auf False
            print(f"{self.titel} wurde zurückgegeben.")  # Gibt eine Bestätigung aus

    def status(self):
        status = "ausgeliehen" if self.ausgeliehen else "verfügbar"
        print(f"Titel: {self.titel}, Autor: {self.autor}, Status: {status}")  # Gibt den Status des Buches aus

# Beispiel der Anwendung
buch1 = Buch("Der Steppenwolf", "Hermann Hesse")
buch1.status()  # Ausgabe des Status
buch1.ausleihen()  # Buch ausleihen
buch1.status()  # Ausgabe des Status nach dem Ausleihen
buch1.zurueckgeben()  # Buch zurückgeben
buch1.status()  # Ausgabe des Status nach der Rückgabe

