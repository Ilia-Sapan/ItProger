#-------------------------------------------
# Dateiname: Teilprüfung_2.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 04.03.2025
#-------------------------------------------

import math
import pandas as pd
import numpy as np
file = r"txt & others/K4.0026_2.0_1.5.C.01_ProjectData.xlsx"
data_file_1 = pd.read_excel(file, sheet_name="Tabellenblatt1")
data_file_2 = pd.read_excel(file, sheet_name="Tabellenblatt2")
# print(data_file_1)
# print(data_file_2)

print('---------------------------------------------------------------------------------------------------------')
# 1.0. Bestimme den Informationsgewinn der einzelnen Features mit Bezug auf die Klasse „Draussen Essen”.
target_col = "Draussen Essen"
def entropy( column ):
    """Entropie-Berechnungsfunktion"""
    probs = column.value_counts(normalize=True)  # Wie viel teilen
    return -sum(probs * np.log2(probs))  # Entropie-Formel
def conditional_entropy( df , feature , target ):
    """Funktion zur Berechnung der bedingten Entropie H(D|A)"""
    grouped = df.groupby(feature)[target]  # Gruppierung nach Merkmal
    weighted_entropy = sum((len(group) / len(df)) * entropy(group) for _, group in grouped)
    return weighted_entropy
def information_gain(df , feature , target ):
    """IG-Berechnungsfunktion"""
    return entropy(df[target]) - conditional_entropy(df, feature, target)
# Wir erhalten eine Liste aller Merkmale (außer der Zielvariablen)
features = [col for col in data_file_1.columns if col != target_col]
ig_values = {feature: information_gain(data_file_1, feature, target_col) for feature in features}
# Resultäten
print(pd.DataFrame(ig_values.items(), columns=['Features', 'Informationsgewinn']))
print('---------------------------------------------------------------------------------------------------------')
# 2.0. Bestimme den Informationsgewinn der einzelnen Features mit Bezug auf die Klasse „Aussenverkauf”.
# Da die Daten numerisch sind, müssen sie zuerst kategorisiert werden.

# 2.1. Die Windgeschwindigkeit kann in verschiedene Stärken eingeteilt werden.

def windkategorie ( staerken ):
    if 1 <= staerken <= 5:
        return "1-5 km/h"
    elif 6 <= staerken <= 11:
        return "6-11 km/h"
    elif 12 <= staerken <= 19:
        return "12-19 km/h"

# Fügen Wir eine neue Kategorie hinzu
data_file_2['Windkategorie'] = data_file_2['Windgeschwindigkeit'].apply(windkategorie)

def temperkategorie ( grad ):
    if grad <= 18:
        return "kalt"
    elif 18 <= grad <= 28:
        return "mild"
    elif grad >= 28:
        return "heiss"

data_file_2['Wahrnehmung'] = data_file_2['Temperatur'].apply(temperkategorie)
# print(data_file_2[['Temperatur', 'Wahrnehmung']])

# 2.2. Teile die Luftfeuchtigkeit in die folgenden Kategorien ein

def luftfeuchtigkeitkategorie( daten ):
    if daten >= 5:
        return "hoch"
    elif daten < 5:
        return "niedrig"

data_file_2['Luftfeuchtigkeitniveau'] = data_file_2['Luftfeuchtigkeit'].apply(luftfeuchtigkeitkategorie)
# print(data_file_2[['Luftfeuchtigkeit', 'Luftfeuchtigkeitniveau']])

# 2.3. den Mittelwert aller Features.
print('---------------------------------------------------------------------------------------------------------')
temperatur_mittel = data_file_2['Temperatur'].mean()
luftfeuchtigkeit_mittel = data_file_2['Luftfeuchtigkeit'].mean()
windgeschwindigkeit_mittel = data_file_2['Windgeschwindigkeit'].mean()

print(f'Durchschnittlicher Wert bei\nTemperatur - {temperatur_mittel:.2f} Grad,\nLuftfeuchtigkeit - {luftfeuchtigkeit_mittel:.2f} g/m3, '
      f'\nWindgeschwindigkeit - {windgeschwindigkeit_mittel:.2f} km/h.')

# 2.4. den Median aller Features.
print('---------------------------------------------------------------------------------------------------------')
temperatur_med =  data_file_2['Temperatur'].median()
luftfeuchtigkeit_med =  data_file_2['Luftfeuchtigkeit'].median()
windgeschwindigkeit_med = data_file_2['Windgeschwindigkeit'].median()


print(f'Median bei\nTemperatur - {temperatur_med:.2f} Grad,\nLuftfeuchtigkeit - {luftfeuchtigkeit_med:.2f} g/m3, '
      f'\nWindgeschwindigkeit - {windgeschwindigkeit_med:.2f} km/h.')

# 2.5. die Standardabweichung aller Features.
print('---------------------------------------------------------------------------------------------------------')
standarts = data_file_2.drop(columns=['Aussenverkauf', 'Windkategorie','Luftfeuchtigkeitniveau','Wahrnehmung']).std()
print(f'Die Standardabweichung aller Features ist \t\n{standarts}.')

# die Korrelation zwischen Luftfeuchtigkeit und Temperatur.
korr_l_t = data_file_2[['Luftfeuchtigkeit', 'Temperatur']].corr()
print(f'die Korrelation zwischen Luftfeuchtigkeit und Temperatur ist: \t\n{korr_l_t}')
# die Korrelation zwischen Windgeschwindigkeit und Luftfeuchtigkeit.
korr_w_l = data_file_2[['Windgeschwindigkeit', 'Luftfeuchtigkeit']].corr()
print(f'die Korrelation zwischen Windgeschwindigkeit und Luftfeuchtigkeit ist: \t\n{korr_w_l}')
# die Korrelation zwischen Windgeschwindigkeit und Temperatur.
korr_w_t = data_file_2[['Windgeschwindigkeit', 'Temperatur']].corr()
print(f'die Korrelation zwischen Windgeschwindigkeit und Temperatur ist: \t\n{korr_w_t}')


print('---------------------------------------------------------------------------------------------------------')
target_col_2 = "Aussenverkauf"

features = [col for col in data_file_2.columns if col != target_col_2]
ig_values = {feature: information_gain(data_file_2, feature, target_col_2) for feature in features}
print(pd.DataFrame(ig_values.items(), columns=['Features', 'Informationsgewinn']))

















