#-------------------------------------------
# Dateiname: Teilprüfung_3.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer
# 399644000031193700
# Letzte Änderung: 11.03.2025
#-------------------------------------------

'''Diese Datei wurde von der Kaggle-Plattform
und der Worldometer-Website
(https://www.worldometers.info/demographics/life-expectancy/#countries-ranked-by-life-expectancy)
für die Analyse, Polynome und Kreuzvalidierung übernommen.'''

'''Ich habe versucht, den Zusammenhang zwischen der Rangfolge 
eines Landes und seiner allgemeinen Lebenserwartung zu analysieren.'''


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import KFold, cross_val_score

# Wir wollen die Lebenserwartung basierend auf dem Länder-Ranking vorhersagen
# Datei laden
file = r"C:\Users\isapa\Desktop\life_expectancy.csv"
df = pd.read_csv(file)

# Mikronesien erscheint anomal. Setzen wir den Wert auf 72.9 Jahre, wie im Internet gefunden.
df.loc[df["Country"] == "Micronesia", "Sum of Life Expectancy  (both sexes)"] = 72.9

# Sortieren nach Lebenserwartung (absteigend)
df = df.sort_values(by="Sum of Life Expectancy  (both sexes)", ascending=False)

# Eine "Ranking"-Spalte hinzufügen, um die Länder von 1 bis zur Anzahl der Zeilen zu nummerieren
df["Ranking"] = range(1, len(df) + 1)

# Relevante Spalten auswählen
df = df[["Country", "Sum of Life Expectancy  (both sexes)", "Ranking"]]

# Für np.polyfit wird ein 1D-Array benötigt
X_polyfit = df['Ranking'].values
# Für Modelle in scikit-learn wird ein 2D-Array benötigt
X_cv = df['Ranking'].values.reshape(-1, 1)
y = df['Sum of Life Expectancy  (both sexes)']

# Modelle, berechnet mit np.polyfit (1D-Array wird verwendet)
my_modell_1 = np.poly1d(np.polyfit(X_polyfit, y, 1))
my_modell_2 = np.poly1d(np.polyfit(X_polyfit, y, 2))
my_modell_3 = np.poly1d(np.polyfit(X_polyfit, y, 3))
my_modell_4 = np.poly1d(np.polyfit(X_polyfit, y, 4))

# Erzeugen eines gleichmäßig verteilten Satzes von x-Werten für die Plots (1D-Array)
my_line = np.linspace(df["Ranking"].min(), df["Ranking"].max(), 200)

plt.scatter(X_polyfit, y, color="red", label="Daten", s=1)  # Streudiagramm der Daten
plt.plot(my_line, my_modell_1(my_line), label='Grad 1')       # Kurve für Modell 1. Grades
plt.plot(my_line, my_modell_2(my_line), label='Grad 2')       # Kurve für Modell 2. Grades
plt.plot(my_line, my_modell_3(my_line), label='Grad 3')       # Kurve für Modell 3. Grades
plt.plot(my_line, my_modell_4(my_line), label='Grad 4')       # Kurve für Modell 4. Grades

plt.xlabel("Ranking")                 # Beschriftung der X-Achse
plt.ylabel("Life Expectancy")         # Beschriftung der Y-Achse
plt.title("Abhängigkeit der Lebenserwartung vom Länderranking")
plt.gca().invert_xaxis()              # X-Achse invertieren
plt.legend()                        # Legende hinzufügen


# Einrichtung der Kreuzvalidierung
falt_zahl = 5                        # Daten in 5 Teile aufteilen
falt_zahl_fold = KFold(n_splits=falt_zahl, shuffle=True, random_state=42)

# Liste der Polynomgrade
degrees = [1, 2, 3, 4]

# Dictionary zur Speicherung der Ergebnisse (mittlerer quadratischer Fehler)
mqf_results = {}

# Schleife zur Modellbewertung mittels Kreuzvalidierung
for degree in degrees:
    modell = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    mqf_punkte = -cross_val_score(modell, X_cv, y, cv=falt_zahl_fold, scoring='neg_mean_squared_error')
    mqf_results[degree] = np.mean(mqf_punkte)

print('-------------------------------------------------------------------------------------')
# Ausgabe der Ergebnisse
for degree, mqf in mqf_results.items():
    print(f'Polynom {degree}. Grades: mittlerer MQF = {mqf:.2f}')

# Suchen niedrigste Polinomwerte
min_mqf = min(mqf_results.values())
besser_degree = next(key for key, value in mqf_results.items() if value == min_mqf)
print(f"Die beste Polynom ist Grad {besser_degree} mit mittlerem MQF: {min_mqf:.2f}")
print('-------------------------------------------------------------------------------------')
print(df)
print('-------------------------------------------------------------------------------------')
plt.show()