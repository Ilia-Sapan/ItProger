# Aufgabe: Kontrollstrukturen
richtige_antworten = 0

frage_1 = input("In welchem Jahr wurde Niklas Luhmann geboren? \n"
                "Antwortmöglichkeiten: \n(a) 1908 \n(b) 1912 \n(c) 1927"
                "\nAntwort: ")

while frage_1 not in ["a", "b", "c"]:
    print("Deine Antwort ist nicht korrekt! Bitte wähle a, b oder c.")
    frage_1 = input("In welchem Jahr wurde Niklas Luhmann geboren? \n"
                    "Antwortmöglichkeiten: \n(a) 1908 \n(b) 1912 \n(c) 1927"
                    "\nAntwort: ")

if frage_1 == "c":
    richtige_antworten += 1


frage_2 = input("In welchem Jahr wurde Friedrich Nietzsche geboren? \n"
                "Antwortmöglichkeiten: \n(a) 1911 \n(b) 1865 \n(c) 1844"
                "\nAntwort: ")

while frage_2 not in ["a", "b", "c"]:
    print("Deine Antwort ist nicht korrekt! Bitte wähle a, b oder c.")
    frage_2 = input("In welchem Jahr wurde Friedrich Nietzsche geboren? \n"
                    "Antwortmöglichkeiten: \n(a) 1911 \n(b) 1865 \n(c) 1844"
                    "\nAntwort: ")

if frage_2 == "c":
    richtige_antworten += 1


frage_3 = input("In welchem Jahr wurde Georg Hegel geboren? \n"
                "Antwortmöglichkeiten: \n(a) 1770 \n(b) 1904 \n(c) 2012"
                "\nAntwort: ")

while frage_3 not in ["a", "b", "c"]:
    print("Deine Antwort ist nicht korrekt! Bitte wähle a, b oder c.")
    frage_3 = input("In welchem Jahr wurde Georg Hegel geboren? \n"
                    "Antwortmöglichkeiten: \n(a) 1770 \n(b) 1904 \n(c) 2012"
                    "\nAntwort: ")

if frage_3 == "a":
    richtige_antworten += 1


print(f"Du hast {richtige_antworten} von 3 Fragen richtig beantwortet.")

