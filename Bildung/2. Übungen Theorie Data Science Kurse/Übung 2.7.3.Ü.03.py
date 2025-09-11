import pandas as pd
import matplotlib.pyplot as plt


file = r"C:\Users\isapa\Desktop\DS Kurse\gini_data.csv"
df = pd.read_csv(file)
print(df.to_string())

x_splits = [0.4, 0.8, 1.1, 1.3, 2, 2.4, 2.8]

y_splits = [0.8, 1.2, 1.8, 2.1, 2.4, 2.7, 2.9]

def gini_impurity(data):
    """Вычисляет Gini impurity по меткам классов."""
    total = len(data)
    if total == 0:
        return 0
    score = sum((data.count(label)/total)**2 for label in set(data))
    return 1 - score

print(gini_impurity(df['Kategorie'].tolist()))

colors = {'rot': 'red', 'blau': 'blue', 'gruen': 'green'}
# Создаём scatter plot
plt.figure(figsize=(6,6))
for category in df['Kategorie'].unique():
    subset = df[df['Kategorie'] == category]
    plt.scatter(subset['X'], subset['Y'], label=category, color=colors[category])

# Добавляем подписи
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Разделение точек по категориям")
# plt.legend()
# plt.grid(True)
# plt.show()

# Функция для вычисления Gini Gain
def gini_gain(split_variable, split_value, dataframe):
    """
    Вычисляет Gini Gain после разбиения данных по указанной переменной и порогу.
    - split_variable: индекс столбца для разбиения (0 - X, 1 - Y)
    - split_value: пороговое значение разбиения
    - dataframe: исходные данные
    """

    # Преобразуем DataFrame в список списков для удобства работы
    datalist = dataframe.values.tolist()

    # Извлекаем категории классов из DataFrame
    kategorien = dataframe['Kategorie'].values.tolist()

    # Общее количество элементов в выборке
    sample_size = len(kategorien)

    # Вычисляем Gini impurity перед разбиением
    impurity_before = gini_impurity(kategorien)

    # Создаём два списка для данных, которые пойдут в левый и правый узел
    A = []  # Левый узел (<= split_value)
    B = []  # Правый узел (> split_value)

    # Разбиваем данные по указанному порогу
    for j in range(len(datalist)):
        tupel = datalist[j]  # Берём одну строку данных
        if tupel[split_variable] < split_value:  # Если значение меньше порога
            A.append(tupel)  # Отправляем в левый узел
        else:
            B.append(tupel)  # Отправляем в правый узел

    # Создаём списки категорий для левого и правого узлов
    A_list = [element[2] for element in A]  # Извлекаем только метки классов из A
    B_list = [element[2] for element in B]  # Извлекаем только метки классов из B

    # Вычисляем Gini impurity после разбиения
    impurity_A = gini_impurity(A_list)
    impurity_B = gini_impurity(B_list)

    # Вычисляем взвешенный Gini impurity после разбиения
    gini_split = (len(A) / sample_size) * impurity_A + (len(B) / sample_size) * impurity_B

    # Вычисляем Gini Gain (насколько impurity уменьшился)
    gini_gain_value = impurity_before - gini_split

    return gini_gain_value  # Возвращаем Gini Gain

for i in range(0, len(x_splits)):
    print(gini_gain(0, x_splits[i], df))

for i in range(0, len(x_splits)):
    print(gini_gain(1, y_splits[i], df))