import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans

# Генерация случайных данных (100 точек)
X = [random.randint(1, 100) for _ in range(100)]
Y = [random.randint(1, 100) for _ in range(100)]
data = list(zip(X, Y))  # Объединяем координаты в кортежи

# Обучение моделей K-Means с 3 и 4 кластерами
kmeans3 = KMeans(n_clusters=3, random_state=42)
kmeans3.fit(data)

kmeans4 = KMeans(n_clusters=4, random_state=42)
kmeans4.fit(data)

# Получаем центроиды кластеров
centroids_3 = kmeans3.cluster_centers_
centroids_4 = kmeans4.cluster_centers_

# Создаём 3 графика
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# График с 3 кластерами
ax1.scatter(X, Y, c=kmeans3.labels_, cmap="viridis")
ax1.scatter(centroids_3[:, 0], centroids_3[:, 1], c="red", marker="X", s=200, label="Центроиды")
ax1.set_title("График 3 кластеров")
ax1.legend()

# График с 4 кластерами
ax2.scatter(X, Y, c=kmeans4.labels_, cmap="plasma")
ax2.scatter(centroids_4[:, 0], centroids_4[:, 1], c="red", marker="X", s=200, label="Центроиды")
ax2.set_title("График 4 кластеров")
ax2.legend()

# # График центроидов (их расположение)
# ax3.scatter(centroids_3[:, 0], centroids_3[:, 1], c="blue", marker="o", s=150, label="Центроиды (3 кластера)")
# ax3.scatter(centroids_4[:, 0], centroids_4[:, 1], c="red", marker="X", s=150, label="Центроиды (4 кластера)")
# ax3.set_title("Центроиды кластеров")
# ax3.legend()

plt.show()
