import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Координаты точек
x = [4, 6, 9, 4, 3, 11, 12, 6, 10, 12]
y = [22, 18, 25, 16, 16, 24, 24, 22, 21, 21]

# Объединяем данные в список точек (x, y)
data = list(zip(x, y))

methods = ['ward', 'average', 'complete', 'single']

# Создаем фигуру с 4 осями (одна строка, 4 столбца)
fig, axes = plt.subplots(1, 4, figsize=(10, 5))

# Для каждого метода строим дендрограмму в отдельной оси
for ax, method in zip(axes, methods):
    linked = linkage(data, method=method)
    dendrogram(linked, orientation='top', distance_sort='ascending', show_leaf_counts=True, ax=ax)
    ax.set_title(f'Methode: {method}')
    ax.set_xlabel('Punktnummer')
    ax.set_ylabel('Verschmelzungsabstand')
    ax.grid(True)

plt.tight_layout()
plt.show()
