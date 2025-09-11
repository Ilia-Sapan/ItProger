# a
import os
FILE_VERZ = r"C:\Users\isapa\Desktop\ORDNER FÜR OS SYS"
def erstelle_verzeichnis(verzeichnisnamen):
    '''Die Funktion soll mithilfe des os-Moduls überprüfen,
     ob das Verzeichnis bereits existiert.'''
    return print(os.path.exists(verzeichnisnamen)) # Возвращает True or False

# erstelle_verzeichnis(FILE_VERZ) # True



# b
def speichere_text_in_datei(dateinamen, speicher_text):
    '''Die Funktion soll den Text in der angegebenen Datei speichern.'''
    try:
        with open(dateinamen, 'w+', encoding='utf-8') as file:
            file_neu = file.write("\n" + speicher_text.upper())
            print(file_neu)
    except FileNotFoundError:
        print('Entschuldigung, aber die Datei wurde nicht gefunden... ')
    except ValueError:
        print('Entschuldigung, aber etwas nicht korrekt...')
    else:
        print('Gut gemacht!')
FILE_1 = ".txt & .json/texttexttext.txt"
texttext = "I sebyvayu of crappy Raschke, knit cap and spizdiv plastic bag with nishtyak"
# speichere_text_in_datei(FILE_1, texttext)

# c
def lese_datei(dateinamen):
    try:
        with open(dateinamen, 'r+', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('Entschuldigung, aber die Datei wurde nicht gefunden... ')
    except ValueError:
        print('Entschuldigung, aber etwas nicht korrekt...')
# print(lese_datai(FILE_1))

# d
DOC = r"C:\Users\isapa\Desktop\Научная литература (политология, социология, философия)"
DOC_1 = r"C:\Users\isapa\Desktop\Литература для исследования серых зон"
def liste_dateien_in_verzeichnis(verzeichnis):
    return "\n".join(os.listdir(verzeichnis))
# print(liste_dateien_in_verzeichnis(DOC_1))

# e
FILE_VERZ = r"C:\Users\isapa\Desktop\ORDNER FÜR OS SYS"
dateiname = os.path.join(FILE_VERZ, "texttexttext.txt")
text = "I sebyvayu of crappy Raschke, knit cap and spizdiv plastic bag with nishtyak"


erstelle_verzeichnis(FILE_VERZ)
speichere_text_in_datei(dateiname, text)
lese_datei(dateiname)
liste_dateien_in_verzeichnis(FILE_VERZ)