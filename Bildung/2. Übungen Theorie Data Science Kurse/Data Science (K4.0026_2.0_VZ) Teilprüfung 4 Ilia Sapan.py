#-------------------------------------------
# Dateiname: Teilprüfung_4.py
# Autor: Ilia Sapan
# Data Science (K4.0026_2.0_VZ)
# Matrikelnummer
# 399644000031193700
# Letzte Änderung: 21.03.2025
#-------------------------------------------
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Erstellen von 2D-Daten mit 3 Clustern (300 Punkte, 2 Merkmale)
X = np.concatenate([
    np.random.normal(loc=-2, scale=1, size=(100, 2)),  # Cluster 1 (Mittelwert -2)
    np.random.normal(loc=3, scale=1, size=(100, 2)),   # Cluster 2 (Mittelwert 3)
    np.random.normal(loc=7, scale=1, size=(100, 2))    # Cluster 3 (Mittelwert 7)
])

# Liste zur Speicherung der Trägheit (WCSS - Within-Cluster Sum of Squares)
inertia = []

# K-Means für verschiedene Clusteranzahlen (K=1 bis K=10)
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)  # Verwenden von K-Means++
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)  # Speichern der Trägheit

# Zeichnen des Elbow-Diagramms
plt.plot(range(1, 11), inertia, marker='o', linestyle='-')
plt.title("Elbow-Methode")
plt.xlabel("Anzahl der Cluster (K)")
plt.ylabel("Trägheit (WCSS)")
plt.show()
