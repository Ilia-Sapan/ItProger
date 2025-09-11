import matplotlib.pyplot as plt
import sklearn
import pandas as pd
import random
from random import seed

from IPython.core.pylabtools import figsize
from sklearn.cluster import KMeans

X = [random.randint(1,100) for i in range(100)]
Y = [random.randint(1,100) for j in range(100)]

data = list(zip(X,Y))

print(data)

kmeans3 = KMeans(n_clusters=3)
kmeans3.fit(data)
kmeans4 = KMeans(n_clusters=4)
kmeans4.fit(data)

fig, (ax1, ax2) = plt.subplots(1,2,figsize = (10,4))

ax1.scatter(X,Y, c = kmeans3.labels_)
ax1.set_title('График трёх кластеров')
ax1.legend()

ax2.scatter(X,Y, c = kmeans4.labels_)
ax2.set_title('График четырех кластеров')
ax2.legend()

plt.show()