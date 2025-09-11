from scipy.cluster.vq import kmeans

from kaggle_utils import load_kaggle_dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mpl_toolkits.mplot3d import Axes3D


df = load_kaggle_dataset('vjchoudhary7/customer-segmentation-tutorial-in-python')
# print("------------------------------------------------------------------------")
# print(df.head())
# print("------------------------------------------------------------------------")
# print(df.shape)
# print("------------------------------------------------------------------------")
# print('Verlorene Daten')
# missing_values = df.isnull().sum()
# print(missing_values)
# print("------------------------------------------------------------------------")

# X = df['Annual Income (k$)']
# y = df['Spending Score (1-100)']
#
# data = list(zip(X,y))
# # print(data)
#
# # plt.scatter(X,y, s = 20, c = 'green')
# # plt.xlabel('Annual Income (k$)')
# # plt.ylabel('Spending Score(1-100')
# # plt.title('Steuerdiagramme')
# # plt.show()



# Объединяем два признака в пары, как в исходном примере
X = df['Annual Income (k$)']
y = df['Spending Score (1-100)']
data = list(zip(X, y))

# inertia = []  # для WCSS
# silhouette_scores = []  # для силуэтного коэффициента
#
# # Перебираем количество кластеров от 2 до 10 (1 кластер не подходит для силуэтного коэффициента)
# for k in range(2, 11):
#     kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
#     kmeans.fit(data)
#
#     inertia.append(kmeans.inertia_)  # сохраняем инерцию
#     score = silhouette_score(data, kmeans.labels_)  # вычисляем силуэтный коэффициент
#     silhouette_scores.append(score)
#
# # Построение графика для инерции (Elbow Method)
# plt.figure(figsize=(12, 5))
# plt.subplot(1, 2, 1)
# plt.plot(range(2, 11), inertia, marker="o", linestyle="-")
# plt.title("Elbow Method")
# plt.xlabel("Количество кластеров (K)")
# plt.ylabel("Trägheit (WCSS)")
#
# # Построение графика для силуэтного коэффициента
# plt.subplot(1, 2, 2)
# plt.plot(range(2, 11), silhouette_scores, marker="o", linestyle="-", color='green')
# plt.title("Silhouette Score")
# plt.xlabel("Количество кластеров (K)")
# plt.ylabel("Silhouette Score")
#
# plt.tight_layout()
# plt.show()

# kmeans5 = KMeans(n_clusters=5, random_state=42)
# kmeans5.fit(data)
#
# plt.scatter(X,y, c = kmeans5.labels_, cmap='viridis')
# plt.title('Steuerdiagramme mit 5 Klusters')
# plt.xlabel('Annual Income (k$)')
# plt.ylabel('Spending Score(1-100')
# plt.title('')
# plt.show()

# 3D scatter plot
X = df['Annual Income (k$)']
y = df['Spending Score (1-100)']
z = df['Age']
data_new = list(zip(X,y,z))
kmeans5 = KMeans(n_clusters=5, random_state=42)
kmeans5.fit(data_new)
labels = kmeans5.labels_

# 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(X, y, z, c=labels, cmap='viridis')
ax.set_title('Steuerdiagramme mit 5 Klusters')
ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.set_zlabel('Age')

plt.show()