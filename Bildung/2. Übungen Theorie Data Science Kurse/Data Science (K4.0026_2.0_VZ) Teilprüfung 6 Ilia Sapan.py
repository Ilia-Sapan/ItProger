#-------------------------------------------
# Dateiname: Teilprüfung_6.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer: 399644000031193700
# Letzte Änderung: 01.04.2025
#-------------------------------------------

# Import der notwendigen Bibliotheken
import pandas as pd                  # für die Arbeit mit tabellarischen Daten
import numpy as np                   # für Arrays und numerische Berechnungen
import matplotlib.pyplot as plt      # für die Visualisierung von Bildern

# 1. Laden der Daten aus einer CSV-Datei
dateipfad = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial für Übungen\K4.0026_2.0_3.5.Ü.01_mnist_data.csv"  # Pfad zur Datei (r = raw string, damit Backslashes nicht interpretiert werden)
df = pd.read_csv(dateipfad, header=None)  # CSV-Datei ohne Kopfzeile einlesen

# 2. Umwandlung des DataFrame in eine Liste von Listen
# Jede Zeile wird so aussehen: [Label, Pixel_1, Pixel_2, ..., Pixel_784]
daten_liste = df.values.tolist()

# === 3. Visualisierung der ersten 4 Bilder auf einem einzigen Canvas ===
fig, achsen = plt.subplots(1, 4, figsize=(10, 5))  # Erstelle eine Figur mit 4 Unterplots (horizontal angeordnet)

# Durchlauf der ersten 4 Zeilen des Datensatzes
for i in range(4):
    label = daten_liste[i][0]                        # Label (die dargestellte Ziffer)
    pixelwerte = daten_liste[i][1:]                  # Nur die Pixelwerte
    bild = np.array(pixelwerte).reshape(28, 28)      # Umwandlung der Liste in ein 28x28 Bild

    achsen[i].imshow(bild, cmap="gray")              # Zeichne das Bild in Graustufen
    achsen[i].set_title(f"Ziffer: {label}")           # Füge einen Titel mit dem Label hinzu
    achsen[i].axis("off")                            # Entferne die Achsen für eine saubere Darstellung

# === 4. Anzeige des finalen Canvas mit den Bildern ===
plt.tight_layout()     # Optimiert das Layout, damit sich Beschriftungen nicht überlappen
plt.show()             # Zeige die Abbildung

# Aufteilen der Eingangsdaten in Labels und Merkmale
label_list = []     # Liste zur Speicherung der Klassenlabels (erste Spalte der Daten)
data_list = []      # Liste zur Speicherung der eigentlichen Merkmale (alle Spalten außer der ersten)

# Durchlauf durch jedes Element der Eingangsdaten
for element in daten_liste:
    label_list.append(element[0])   # Die erste Spalte enthält das Klassenlabel
    data_list.append(element[1:])   # Die restlichen Werte sind die Merkmale

# Aufteilen der Daten in Trainings- und Testdatensätze
# 80% für das Training – die ersten 8000 Einträge
# 20% für den Test – alle Einträge nach den ersten 8000
training_labels = label_list[:8000]   #  Labels für das Training
training_data = data_list[:8000]      #  Daten für das Training
test_labels = label_list[8000:]       #  Labels für den Test
test_data = data_list[8000:]          #  Daten für den Test

#  Skalierung der Datenwerte in den Bereich [0.01, 1.0]
# Dies ist für neuronale Netze oft notwendig (z.B. arbeitet die Sigmoid-Funktion nicht gut mit Werten [0, 255])
# Formel: Normalisierung in [0,1] → Skalierung in [0,0.99] → Verschiebung um +0.01
training_data = (np.asarray(training_data)/255 * 0.99) + 0.01  # Normalisierung der Trainingsdaten
test_data = (np.asarray(test_data)/255 * 0.99) + 0.01          # Normalisierung der Testdaten

# Grundparameter des neuronalen Netzwerks
imput_nodes = 784       # Anzahl der Eingabeneuronen (Pixel)
hidden_nodes = 100      # Anzahl der Neuronen in der versteckten Schicht
output_nodes = 10       # Anzahl der Ausgabeneuronen (Klassen von 0 bis 9)
learning_rate = 0.3     # Lernrate

# Gewichtinitialisierung (Zufallswerte von -0.5 bis 0.5)
# Gewichtsmatrix von der Eingabe- zur versteckten Schicht
w_input_hidden = np.random.rand(hidden_nodes, imput_nodes) - 0.5
# Gewichtsmatrix von der versteckten zur Ausgabeschicht
w_hidden_output = np.random.rand(output_nodes, hidden_nodes) - 0.5

# Sigmoid-Funktion (Aktivierungsfunktion)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Forward-Pass-Funktion (Testfunktion)
def test(input_vector, w_ih, w_ho):
    # Umwandlung des Eingabevektors in ein 2D-Array (Spaltenvektor)
    inputs = np.array(input_vector, ndmin=2).T

    # Berechnung der Eingaben für die versteckte Schicht
    hidden_inputs = np.dot(w_ih, inputs)
    hidden_outputs = sigmoid(hidden_inputs)

    # Berechnung der Eingaben für die Ausgabeschicht
    final_inputs = np.dot(w_ho, hidden_outputs)
    final_outputs = sigmoid(final_inputs)

    return final_outputs

# Teste die Funktion mit dem ersten Testdateneintrag und gebe den Ausgabeverktor aus
output = test(test_data[0], w_input_hidden, w_hidden_output)
print(output)
