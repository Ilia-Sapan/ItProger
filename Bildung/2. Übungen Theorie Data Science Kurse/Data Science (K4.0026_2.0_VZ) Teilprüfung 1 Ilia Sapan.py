#-------------------------------------------
# Dateiname: Python_Programm.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 27.02.2025
#-------------------------------------------

import pandas as pd # Importieren Pandas-Bibliothek

file = r"txt & others/K4.0026_2.0_1.4.4.Ü.01_dirtydata.csv"  # Geben den lokalen Pfad zu der Datei

data_file = pd.read_csv(file) # Öffnen dieser Datei mit read_csv()

# 1. Ersetze in Spalten mit numerischen Werten die leeren Zellen durch den Mittelwert.

change_mittelwert_kunden = data_file['Kunden'].mean() # Berechnen den Mittelwert in der Spalte "Kunden"

change_mittelwert_min = data_file['MinKauf'].mean() # Berechnen den Mittelwert in der Spalte "MinKauf"

change_mittelwert_max = data_file['MaxKauf'].mean() # Berechnen den Mittelwert in der Spalte "MaxKauf"

# in NaN durch den Mittelwert ersetzen

data_file.fillna({'Kunden': round(change_mittelwert_kunden)},  inplace=True)

data_file.fillna({'MinKauf': round(change_mittelwert_min)},  inplace=True)

data_file.fillna({'MaxKauf': round(change_mittelwert_max)},  inplace=True)

# 2. Korrigiere die Datumsangaben (einheitliches Format, fehlende Angaben löschen).

# Konvertiert die Spalte "Datum" in das Datumsformat und korrigiert die Fehler.

data_file["Datum"] = pd.to_datetime(data_file["Datum"], errors="coerce")
# Füllen Sie fehlende Werte mit dem vorherigen Datum auf.

data_file["Datum"] = data_file["Datum"].ffill()
# Bei der Korrektur treten doppelte Daten auf, die wir aber nicht entfernen können, also bearbeiten wir sie manuell.

data_file.loc[22, "Datum"] = pd.to_datetime("2020-12-22")

data_file.loc[26, "Datum"] = pd.to_datetime("2020-12-26")

# 3. Bearbeite falsche Werte (Ausreißer aus den Daten).

# In der Spalte "Dauer" wurde nur ein falscher Wert festgestellt, so dass wir diesen durch Griffe ersetzen können
data_file.loc[7, 'Dauer'] = 45

# Füllen wir die Lücken mit dem Mittelwert aus!

change_mittelwert_dauer = data_file['Dauer'].mean() # Berechnen den Mittelwert in der Spalte "Dauer"

# in NaN durch den Mittelwert ersetzen

data_file.fillna({'Dauer': round(change_mittelwert_dauer)},  inplace=True)


data_file.to_csv("cleaned_data.csv", index=False)
print(data_file)