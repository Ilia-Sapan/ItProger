import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Импорт для работы с 3D графиками
import random  # если требуется для генерации случайных чисел (не используется в этом примере)

from pydantic_core.core_schema import model_field
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Настройка pandas для устранения предупреждений по даункастингу
pd.set_option('future.no_silent_downcasting', True)

# Загрузка данных из CSV-файла
file = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial Case Studies\K4.0026_2.0_3.C.01_MobilePhone.csv"
df = pd.read_csv(file)

# Пример структуры DataFrame:
#   battery_power         int_memory      frontcamermegapixels  blue  Price Range  ...
#   1043                16              5                     1     h
#   841                 8               7                     1     m
#   ...

# Заменяем значения в столбце Price Range: h -> 1, m -> 2, l -> 3
new_signe = {'h': 1, 'm': 2, 'l': 3}
df['Prise Range'] = df['Price Range'].replace(new_signe)

# # Подготовка данных для графиков
# X_1 = df['battery_power']
# Y_1 = df['int_memory']
#
# X_2 = df['frontcamermegapixels']
# Y_2 = df['blue']
#
# X_3 = df['int_memory']
# Y_3 = df['frontcamermegapixels']
#
# X_4 = df['battery_power']
# Y_4 = df['blue']
# Z_4 = df['frontcamermegapixels']
#
# X_5 = df['battery_power']
# Y_5 = df['frontcamermegapixels']
#
# # Создаем фигуру, в которой первые три подграфика - 2D, а четвертый - 3D
# fig = plt.figure(figsize=(16, 4))
#
# # Первый 2D график
# ax1 = fig.add_subplot(151)  # Расположение: 1-я позиция из 4
# ax1.scatter(X_1, Y_1, alpha=0.3, s=15, color='b')
# ax1.set_title('Battery Power и Internal Memory')
# ax1.set_xlabel('Battery Power')
# ax1.set_ylabel('Internal Memory')
#
# # Второй 2D график
# ax2 = fig.add_subplot(152)
# ax2.scatter(X_2, Y_2, alpha=0.4, s=15, color='r')
# ax2.set_title('Frontkamera-Megapixel и Bluetooth')
# ax2.set_xlabel('Frontkamera-Megapixel')
# ax2.set_ylabel('Bluetooth')
#
# # Третий 2D график
# ax3 = fig.add_subplot(153)
# ax3.scatter(X_3, Y_3, alpha=0.5, s=15, color='g')
# ax3.set_title('Internal Memory и Frontkamera-Megapixel')
# ax3.set_xlabel('Internal Memory')
# ax3.set_ylabel('Frontkamera-Megapixel')
#
# # Четвертый график - 3D scatter plot
# ax4 = fig.add_subplot(154, projection='3d')
# ax4.scatter(X_4, Y_4, Z_4, alpha=0.5, s=15, color='m')
# ax4.set_title('3D-Scatter: Battery Power, Bluetooth, Frontkamera-Megapixel')
# ax4.set_xlabel('Battery Power')
# ax4.set_ylabel('Bluetooth')
# ax4.set_zlabel('Frontkamera-Megapixel')
#
# # Пятый график - 2D график
# ax5 = fig.add_subplot(155)
# ax5.scatter(X_5, Y_5, alpha=0.5, s=15, color='black')
# ax5.set_title('Battery Power und Frontkamera-Megapixel')
# ax5.set_xlabel('Battery Power (mAh)')
# ax5.set_ylabel('Frontkamera-Megapixel (megapixel)')
#
#
# plt.tight_layout()  # Автоматическая корректировка отступов
# plt.show()

X = np.array(df[['battery_power', 'frontcamermegapixels']])
y = np.array(df['Price Range'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

# Логистическая регрессия
model = LogisticRegression()
model.fit(X,y)
y_pred = model.predict(X_test)

# Дерево решений
model_1 = DecisionTreeClassifier()
model_1.fit(X,y)
y_pred_1 = model.predict(X_test)

# Случайный лес
model_2 = RandomForestClassifier()
model_2.fit(X,y)
y_pred_2 = model.predict(X_test)

print(f'Точность модели логистической регрессии равна {accuracy_score(y_test,y_pred):.2f}')
print(f'Точность модели деревья решений равна {accuracy_score(y_test,y_pred_1):.2f}')
print(f'Точность модели случайного леса равна {accuracy_score(y_test,y_pred_2):.2f}')

# Вычисление точностей
acc_lr = accuracy_score(y_test, y_pred)
acc_dt = accuracy_score(y_test, y_pred_1)
acc_rf = accuracy_score(y_test, y_pred_2)

# Визуализация точностей с помощью столбчатой диаграммы
models = ['Лог. регрессия', 'Дерево решений', 'Случ. лес']
accuracies = [acc_lr, acc_dt, acc_rf]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracies, color=['blue', 'green', 'orange'])
plt.ylim(0, 1)
plt.ylabel('Точность')
plt.title('Сравнение точности моделей')
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from IPython.core.pylabtools import figsize
# from matplotlib.pyplot import figure
# from scipy import stats
# import random
#
# from sklearn.metrics import accuracy_score  # Для вычисления точности
# from sklearn.neighbors import KNeighborsClassifier  # KNN-классификатор
# from mpl_toolkits import mplot3d  # Для 3D-визуализации
#
# # *******************************
# # Подготовка данных
# # *******************************
#
# # Загрузка CSV-файла с данными
# file = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial Case Studies\K4.0026_2.0_3.C.01_MobilePhone.csv"
# df = pd.read_csv(file)
#
# # Преобразуем DataFrame в список (если нужно для других целей, но далее работаем с исходным df)
# data = df.values.tolist()
#
# # *******************************
# # Извлечение интересующих столбцов в виде списков
# # *******************************
# battery_power = df['battery_power'].tolist()  # Емкость батареи
# bluetooth = df['blue'].tolist()  # Наличие Bluetooth
# dual_sim = df['dual_sim'].tolist()  # Dual SIM
# frontcameramegapixels = df['frontcamermegapixels'].tolist()  # Количество мегапикселей фронтальной камеры
# pricerange = df['Price Range'].tolist()  # Ценовой диапазон (в виде строк)
# internal_memory = df['int_memory'].tolist()  # Объем внутренней памяти
#
# # *******************************
# # Визуализация данных
# # *******************************
# # Преобразование ценового диапазона в числовые значения:
# # Если 'h' - присваиваем 2, если 'm' - присваиваем 1, иначе (например, 'l') - 0.
# new_pricerange = []
# for i in range(0, len(pricerange)):
#     if pricerange[i] == 'h':
#         new_pricerange.append(2)
#     elif pricerange[i] == 'm':
#         new_pricerange.append(1)
#     else:
#         new_pricerange.append(0)
#
# # 2D визуализация: создаем 3 графика с использованием темного стиля
# with plt.style.context('dark_background'):
#     fig, ax = plt.subplots(1, 3, figsize=(15, 5))
#
#     # Первый график: Battery Power vs Internal Memory
#     ax[0].scatter(battery_power, internal_memory, c=new_pricerange)
#     ax[0].legend()
#     ax[0].set_xlabel('Battery Power')
#     ax[0].set_ylabel('Internal Memory')
#     ax[0].set_title('')
#
#     # Второй график: Bluetooth vs Front Camera Megapixel
#     ax[1].scatter(bluetooth, frontcameramegapixels, c=new_pricerange)
#     ax[1].legend(loc='center')
#     ax[1].set_xlabel('Bluetooth')
#     ax[1].set_ylabel('Front Camera Megapixel')
#     ax[1].set_title('')
#
#     # Третий график: Front Camera Megapixel vs Internal Memory
#     ax[2].scatter(frontcameramegapixels, internal_memory, c=new_pricerange)
#     ax[2].legend()
#     ax[2].set_xlabel('Front Camera Megapixel')
#     ax[2].set_ylabel('Internal Memory')
#     ax[2].set_title('')
#
# # 3D визуализация: строим 3D scatter plot
# with plt.style.context('dark_background'):
#     figure = plt.figure()
#     ax3d = plt.axes(projection='3d')
#     ax3d.scatter(frontcameramegapixels, bluetooth, battery_power, c=new_pricerange)
#     ax3d.set_xlabel('Front Camera Megapixels')
#     ax3d.set_ylabel('Bluetooth')
#     ax3d.set_zlabel('Battery Power')
#     ax3d.set_yticks([0, 1])
#     ax3d.set_yticklabels(['no', 'yes'])
#     ax3d.set_xticks([0, 1, 2])
#     ax3d.set_xticklabels(['low', 'medium', 'high'])
#
# # *******************************
# # Разделение данных на обучающую и тестовую выборки
# # *******************************
# # Здесь данные разбиваются вручную (80% - обучение, 20% - тест)
# train_battery = battery_power[:int(0.8 * len(battery_power))]
# train_front = frontcameramegapixels[:int(0.8 * len(frontcameramegapixels))]
# train_labels = new_pricerange[:int(0.8 * len(new_pricerange))]
#
# test_battery = battery_power[int(0.8 * len(battery_power)):]
# test_front = frontcameramegapixels[int(0.8 * len(frontcameramegapixels)):]
# test_labels = new_pricerange[int(0.8 * len(new_pricerange)):]
#
# # *******************************
# # K-Nearest Neighbors анализ
# # *******************************
# # Объединяем обучающие признаки в кортежи (каждый объект представляется парой: Battery Power и Front Camera Megapixels)
# train_data = list(zip(train_battery, train_front))
#
# # Инициализируем KNN с 5 соседями
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(train_data, train_labels)  # Обучаем модель на обучающих данных
#
# # *******************************
# # Тестирование модели и вычисление точности предсказаний
# # *******************************
# # Получаем предсказания для тестовой выборки
# # Сначала объединяем тестовые признаки в список кортежей
# test_data = list(zip(test_battery, test_front))
# predictions = knn.predict(test_data)
#
# # Вычисляем точность предсказаний с помощью accuracy_score
# accuracy = accuracy_score(test_labels, predictions)
# print(f'Точность модели KNN: {accuracy:.2f}')
#
# # Выводим предсказания для каждого тестового примера
# for i in range(len(test_battery)):
#     print('Предсказанная класс:', predictions[i], 'Правильная класс:', test_labels[i])
#
# plt.show()
