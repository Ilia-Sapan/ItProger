import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def a():
    print("________________________________________")

file = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial Case Studies\K4.0026_2.0_2.C.01_Salaries.csv"
df = pd.read_csv(file)

# Очистка данных
a()
print(df.to_string())
a()
print(f'Количество пропусков: \n{df.isna().sum()}')
a()
print(f'Количество дубликатов: {df.duplicated().sum()}')

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print(f'Количество дубликатов после очистки: {df.duplicated().sum()}')
print(f'Количество пропусков после очистки: \n{df.isna().sum()}')

# Замена пропуска на среднее значение
df_position = df[df['Position'] == 'Junior Consultant']
mean_salary = df_position['Salary'].mean()

if 79 in df.index:  # Проверяем, есть ли индекс 79
    df.loc[79, 'Salary'] = int(round(mean_salary))

a()

# Разделение данных
X = df[['Level']]
Y = df['Salary']

# Визуализация точек
plt.scatter(X, Y, alpha=0.5, s=50, color="green", linewidths=3, label="Real Data")
plt.xlabel('Level')
plt.ylabel('Salary')

# Линейная регрессия
linreg = LinearRegression()
linreg.fit(X, Y)
Y_pred_linear = linreg.predict(X)

# Полиномиальная регрессия
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
lin_reg_poly = LinearRegression()
lin_reg_poly.fit(X_poly, Y)

# Сортируем X перед визуализацией полинома
X_sorted = np.sort(X, axis=0)
Y_pred_poly_sorted = lin_reg_poly.predict(poly.transform(X_sorted))

# Визуализация
plt.plot(X, Y_pred_linear, color='black', label='Linear Regression')
plt.plot(X_sorted, Y_pred_poly_sorted, color="red", linewidth=2, label="Polynomial Regression (deg=4)")
plt.legend()
plt.show()
