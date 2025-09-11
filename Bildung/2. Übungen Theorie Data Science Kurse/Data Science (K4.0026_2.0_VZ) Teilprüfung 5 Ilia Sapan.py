#-------------------------------------------
# Dateiname: Teilprüfung_5.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer
# 399644000031193700
# Letzte Änderung: 26.03.2025
#-------------------------------------------

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Koordinaten der Punkte
x = [4, 6, 9, 4, 3, 11, 12, 6, 10, 12]
y = [22, 18, 25, 16, 16, 24, 24, 22, 21, 21]

# Punktdaten in (x, y)-Tupel umwandeln
data = list(zip(x, y))

# Hierarchisches Clustering mit Ward-Methode
linked = linkage(data, method='ward')

# Zwei nebeneinander stehende Plots vorbereiten
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Punktwolke
ax1.scatter(x, y, color='green')
ax1.set_title('Punktdaten')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.grid(True)

# Plot 2: Dendrogramm
# Zeichnen des Dendrogramms
# orientation='top' - Platzierung von oben nach unten
# distance_sort='ascending' - Sortierung nach Entfernung beim Zusammenführen
# show_leaf_counts=True - zeigt die Anzahl der Elemente im Cluster an
dendrogram(linked, orientation='top', distance_sort='ascending', show_leaf_counts=True, ax=ax2)

# Überschrift und Achsenbeschriftung


ax2.set_title('Dendrogramm : Agglomerative Clustering')
ax2.set_xlabel('Punktnummer')
ax2.set_ylabel('Verschmelzungsabstand')
ax2.grid(True)

plt.tight_layout()
plt.show()
