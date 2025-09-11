# # # passwort.py
# # print("Bitte geben Sie Ihr Passwort ein!")
# # eingabe = input("Passwort: ")
# # if eingabe == "guido":
# #     print("Rasswort wurde erkannt.")
# #     print("Willkommen!")
# #
# # # kinokarte.py
# #
# # print('Willkommen im Kino! Bitte geben Sie Ihr Alter an!')
# # alter = int(input("Alter(Jahre); "))
# # if alter < 18:
# #     print("Dein Ticket kostet 5 Euro!")
# #     print('Viel Spaß!')
# # else:
# #     print("Dein Ticket kostet 8 Euro!")
# #     print('Viel Spaß!')
#
# #dialogprogramm.py
#
# print('Willkommen! Bitte stellen Sie Ihre Frage!')
# frage = input('Frage: ').lower()
# if 'wann' in frage:
#     thema = 'zum Liefertermin'
#     zuständig = 'Carla'
# elif 'rechnung' in frage:
#     thema = 'zum Rechnung'
#     zuständig = 'Tom'
# else:
#     thema = ''
#     zuständig = 'Kim'
# print('Vielen Dank für Ihre Frage ' + thema + '.')
# print(zuständig + ' hilft Ihnen gerne weiter.')
#
# # 4.2 Das Layout von Python-Programmen: Zeilen und Blöcke
#Block


# if x > 0:
#     pass # pass hilft Codeblöcke temporär leer zu lassen
# else:
#     x = - x
#
# # Zeilenstruktur
# satz = name + ' geht am ' + wochentag + \
# ' ins Kino.'

# Du kannst mehrere physische Zeilen durch
# einen Backslash \
# zu einer logischen Zeile
# verbinden.

# farben = {'rot',
#           'gelb',
#           'grün'}
#
# print('Der Zylinder hat ein Volumen von',
#       volumen, 'm.')

# Am Ende jeder physischen Zeile –
# außer der letzten – muss dann ein Komma stehen

# 4.3 Bedingungen konstruieren
# gerade == % 2 == 0
#
# 5 < durchmesser < 10
# (5 < durchmesser) and (durchmesser < 10)



# obst.py
#Eingabe
# farbe = input("Farbe (rot, grün, gelb): ")
# durchmesser = float(input("Durchmesser in cm: "))
# stein = input("Hat die Frucht einen Stein (j, n): ") == "j"
# #Verarbeitung
# if (farbe == "gelb") and (durchmesser < 10):
#     frucht = "Zitrone"
# elif (farbe == "gelb") and (durchmesser >= 10):
#     frucht = "Grapefruit"
# elif (farbe in {'rot', 'grün'}) and \
#         (durchmesser <=5) and not stein:
#     frucht = "Traube"
# elif (farbe in {'rot', 'grün'}) and \
#         (5 < durchmesser < 15):
#     frucht = 'Apfel'
# elif (farbe == "rot") and stein:
#     frucht = "Kirsche"
# elif (farbe == "grün") and (durchmesser >=15):
#     frucht = "Wasserlemone"
# else:
#     frucht = "Unbekante Frucht"
# #Ausgabe
# print(f"Es handelt sich um folgende Frucht: {frucht}.")

# 4.4 Bedingte Wiederholung – while
# x = 1
# while x < 100:
#     print(x)
#     x *= 2
#
# summe = 0
# nr = 0
# eingabe = input("Zahl: ")
# while eingabe:
#     summe += float(eingabe)
#     nr +=1
#     eingabe = input("Zahl: ")
# print('Die Summe der ', nr, 'Zahlen ist', summe)
# planeten = {'Merkur', 'Venus', 'Erde',
#             'Mars', 'Jupiter', 'Saturn',
#             'Uranus', 'Neptun'}
# print('Zähle allen Planeten unseres Sonnensystems auf!')
# while planeten != set():
#     eingabe = input('Planet: ')
#     if eingabe in planeten:
#         planeten = planeten - {eingabe}
#         print('Richtig!')
#     else:
#         print(f"Soory, {eingabe} ist kein Planet!")
# print('Glückwunsch! Du hast alle Planete aufgezählt!')
#
# a = float(input("Zahl: "))
# genauigkeit = float(input("Genauigkeit: "))
# x_alt = (a+1)/2
# d = 10000
#
# while d > genauigkeit:
#     x_neu = x_alt - (x_alt**2 - a)/(2*x_alt)
#     d = abs(x_neu - x_alt) # abs() gab Absolutzahl, z.B. abs(-20) ist 20.
#     x_alt = x_neu
#
# print(f'Die Quadratwurzel aus {a} ist ungefähr {x_alt}.')


# 4.5. Iterationen - for

# listen = [1,2,3,4,5]
# for x in listen:
#     print(x, x**2)
#
# for i in range(3): # Mit range(n) kannst du eine n-malige Wiederholung programmieren:
#     print("Hoch!")

