import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Исходные данные
data = {
    "Person": ["Anton", "Bernd", "Klaus"],
    "Körpergroße": [170, 180, 190],
    "Schuhgröße": [42, 44, 43]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Признаки и целевая переменная
X = df[['Körpergroße']]
y = df['Schuhgröße']

# Модель линейной регрессии
model = LinearRegression()
model.fit(X, y)

# Предсказания для графика
X_fit = np.linspace(X.min(), X.max(), 100)
y_fit = model.predict(X_fit)

# Визуализация данных и линии регрессии
plt.scatter(X, y, color='blue', label='Данные')
plt.plot(X_fit, y_fit, color='red', linewidth=2, label='Линейная регрессия')

# Оформление графика
plt.xlabel('Körpergroße (см)')
plt.ylabel('Schuhgröße')
plt.title('Линейная регрессия: Schuhgröße от Körpergroße')
plt.legend()

# Показать график
plt.show()
