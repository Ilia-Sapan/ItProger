# Aufgabe: Kontrollstrukturen
#
# Dieses Skript fragt die Stimmung des Benutzers ab und reagiert entsprechend.
# Es wiederholt sich, bis der Benutzer das Programm explizit beendet.

while True:  # Die Schleife stellt sicher, dass das Programm wiederholt wird, bis der Benutzer es beenden möchte.
    # a) Frage den Benutzer nach seiner aktuellen Stimmung
    stimmung = input("Wie ist deine aktuelle Stimmung? (z.B. 'glücklich', 'traurig', 'müde'): ").strip().lower()

    # b) Überprüfe die Eingabe des Benutzers und reagiere entsprechend
    if stimmung == "glücklich":
        # Wenn der Benutzer "glücklich" eingibt, wird eine positive Nachricht ausgegeben.
        print("Es ist toll zu hören, dass du glücklich bist!")
    elif stimmung == "traurig":
        # Wenn der Benutzer "traurig" eingibt, wird eine tröstende Nachricht ausgegeben.
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")
    elif stimmung == "müde":
        # Wenn der Benutzer "müde" eingibt, wird eine Empfehlung zum Ausruhen gegeben.
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")
    else:
        # Für alle anderen Eingaben wird eine Standardnachricht ausgegeben.
        print("Interessant! Ich weiß nicht viel über diese Stimmung.")

    # c) Frage den Benutzer, ob er das Programm beenden möchte
    beenden = input("Möchtest du das Programm beenden? (Ja/Nein): ").strip().lower()
    if beenden == "ja":
        # Wenn der Benutzer "Ja" eingibt, wird die Schleife beendet.
        print("Programm wird beendet. Auf Wiedersehen!")
        break
    elif beenden == "nein":
        # Wenn der Benutzer "Nein" eingibt, wird die Schleife fortgesetzt.
        print("Okay, lass uns weitermachen!")
    else:
        # Wenn der Benutzer etwas anderes eingibt, wird die Eingabe ignoriert und die Schleife wiederholt sich.
        print("Ungültige Eingabe. Das Programm wird fortgesetzt.")