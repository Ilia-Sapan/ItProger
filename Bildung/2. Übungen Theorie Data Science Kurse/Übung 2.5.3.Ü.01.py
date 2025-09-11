import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

datum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
luftfeuchtigkeit = [72, 61, 84, 58, 90, 68, 38, 34, 30, 46, 88, 53, 32, 89, 30]
draußen_gäste = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1]

# Объединяю списки "день" и "влажность". Теперь каждая точка данных имеет две характеристики: день и влажность.
daten = list(zip(datum,luftfeuchtigkeit))


# Создаю модель KNN (K-nearest-neighbors) на пяти ближайших соседях
knn = KNeighborsClassifier(n_neighbors=5)


# Теперь я обучаю модель на данных (координаты -> "гости на улице")
# Этот шаг необходим для того, чтобы модель могла "узнать" структуру твоих данных.
# Запомнив обучающие примеры, алгоритм сможет оценить,
# насколько похожи новые данные на уже известные и
# сделать предсказание на основе голосования ближайших соседей (здесь 5 ближайших).
knn.fit(daten,draußen_gäste)

# Координаты новой точки, которую нужно классифицировать
new_datum = 16
new_luftfeuchtigkeit = 60

# Записываем новую точку в виде списка кортежей (так требует sklearn)

new_point = [(new_datum,new_luftfeuchtigkeit)]

# Предсказываем класс новой точки
prediction = knn.predict(new_point)

print(prediction)

plt.scatter(datum + [new_datum], luftfeuchtigkeit + [new_luftfeuchtigkeit], c=draußen_gäste + [prediction[0]])
# Рисуем график снова, включая новую точку, цвет зависит от предсказанного класса

plt.text(x=new_datum - 1.7, y=new_luftfeuchtigkeit - 0.7, s=f"new point, class: {prediction[0]}")
# Подписываем новую точку на графике (сдвигаем текст немного влево и вниз)

plt.show()
# Показываем итоговый график с новой точкой
