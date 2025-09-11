import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Данные
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0,0,0,0,0,0,1,1,1,1,1,1])

# Визуализация данных
plt.scatter(X, y)

# Создаём и обучаем логистическую регрессию
logr = linear_model.LogisticRegression()
logr.fit(X, y)

# Делаем предсказание для 1.46
predicted = logr.predict(np.array([[1.46]]))
print(f"Предсказанный класс для 1.46: {predicted[0]}")

# Вывод коэффициентов модели
log_odds = logr.coef_[0]
odds = np.exp(log_odds)
print("Log-odds:", log_odds)
print("Odds ratio:", odds)

# Показываем график
plt.show()

def probability(logr, X):  # Определяем функцию, которая вычисляет вероятность класса 1 (злокачественная опухоль)
    argument = logr.coef_ * X + logr.intercept_  # Вычисляем log-odds (логарифм шансов): b0 + b1 * X
    exponential = np.exp(-argument)  # Применяем экспоненциальную функцию к -log-odds, это часть сигмоиды
    probability = 1 / (1 + exponential)  # Завершаем вычисление сигмоидной функции, получаем вероятность класса 1
    return probability  # Возвращаем вероятность, что опухоль злокачественная (p(y=1))

print(probability(logr, np.array([1.46]).reshape(-1,1)))
# Передаём в функцию модель logr и значение X=1.46 (размер опухоли)
# numpy.array([1.46]).reshape(-1,1) → Преобразуем число в 2D-массив (требуется для работы sklearn)
# Выводим вероятность того, что опухоль злокачественная

