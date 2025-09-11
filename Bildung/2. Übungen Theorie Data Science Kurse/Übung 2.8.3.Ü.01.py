import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

# Читаем данные из CSV файла
df = pd.read_csv(r"C:\Users\isapa\Desktop\hiring_data.csv")
# df.to_string() можно использовать для вывода всего DataFrame, если нужно проверить данные
# print(df.to_string())
# print(df['Uni'].unique())

# Преобразуем категориальные признаки в числовые
# Для колонки 'Uni' задаём отображение: Oxford → 0, Harvard → 1, ETH → 2
uni_map = {'Oxford': 0, 'Harvard': 1, 'ETH': 2}
df['Uni'] = df['Uni'].map(uni_map)

# Для колонки 'Hire' задаём отображение: YES → 1, NO → 0
hire_map = {'YES': 1, 'NO': 0}
df['Hire'] = df['Hire'].map(hire_map)

# Выводим преобразованный DataFrame для проверки
print(df.to_string())

# Определяем признаки (features) и целевую переменную (target)
features = ['Age', 'Experience', 'Rank', 'Uni']
X = df[features]   # Матрица признаков (все входные данные)
y = df['Hire']     # Целевая переменная (результат найма)

# Создаём модель дерева решений (Decision Tree Classifier)
dtree = DecisionTreeClassifier()

# Обучаем модель на данных: X (признаки) и y (метки)
dtree.fit(X, y)

# Предсказываем класс для нового кандидата с параметрами:
# Age = 40, Experience = 10, Rank = 7, Uni = Harvard (код 1)
prediction = dtree.predict([[40, 10, 7, 1]])

# Получаем характеристики обученного дерева
tree_depth = dtree.get_depth()       # Глубина дерева (количество уровней)
num_leaves = dtree.get_n_leaves()      # Количество листьев (конечных узлов)

# Выводим полученные характеристики дерева
print(f"Глубина дерева: {tree_depth}")
print(f"Количество листьев: {num_leaves}")

# Интерпретируем предсказание: если предсказание равно 1, значит "YES" (нанят), иначе "NO"
if prediction == [1]:
    print("Прогноз принятия: да")
else:
    print("Прогноз принятия: нет")

# Визуализируем дерево решений
plt.figure(figsize=(12, 8))  # Устанавливаем размер графика
plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True)
plt.show()

# Создаём модель случайного леса (Random Forest Classifier)
rf_model = RandomForestClassifier()

# Обучаем случайный лес на тех же данных
rf_model.fit(X, y)

# Предсказываем класс для того же нового кандидата
rf_prediction = rf_model.predict([[40, 10, 7, 1]])

# Интерпретируем предсказание случайного леса
if rf_prediction == [1]:
    print("Прогноз принятия (Random Forest): да")
else:
    print("Прогноз принятия (Random Forest): нет")
