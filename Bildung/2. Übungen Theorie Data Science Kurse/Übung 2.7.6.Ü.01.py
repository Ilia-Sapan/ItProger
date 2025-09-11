
import pandas as pd
import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Einlesen der Daten / Читаем данные

df = pd.read_csv(r"C:\Users\isapa\Desktop\hiring_data.csv")
# print(df.to_string())
# print(df['Uni'].unique())

# Vorbereiten der Daten
d = {'Oxford': 0, 'Harvard': 1, 'ETH': 2}
df['Uni'] = df['Uni'].map(d)

d = {'YES': 1, 'NO': 0}
df['Hire'] = df['Hire'].map(d)
print(df.to_string())



# Trennung der Feature Spalten von der target-Spalte

features = ['Age', 'Experience', 'Rank', 'Uni']
X = df[features]
y = df['Hire']

# Jetzt kommt der eigentliche Decision Tree Klassifizierer

dtree = DecisionTreeClassifier()
dtree.fit(X,y)

# Получаем глубину и листья решений
tree_depth = dtree.get_depth()
num_leaves = dtree.get_n_leaves()

# Вывод результатов
print(f"Глубина дерева: {tree_depth}")
print(f"Количество листьев: {num_leaves}")


tree.plot_tree(dtree, feature_names=features)

plt.show()



