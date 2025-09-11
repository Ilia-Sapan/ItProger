import pandas as pd  # Работа с таблицами (DataFrame)
from sklearn import linear_model  # Импортируем модуль для линейной регрессии

file = r"C:\Users\isapa\Desktop\DS Kurse\Kursmaterial für Übungen\K4.0026_2.0_2.3.2.Ü.01_Fish.csv"

df = pd.read_csv(file)
pd.set_option('display.max_rows', 5) # 2 первые, 2 последние, 1 промежуточная
print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\tВсе колонки и данные\n")
print(df)
print("------------------------------------------------------------------------------")
df_whitefish = df[df['Species'] == 'Whitefish']
print(df_whitefish)
print("------------------------------------------------------------------------------")
# Определяем независимые переменные (предикторы), вес, длина, высота рыбки!
X = df_whitefish[["Weight" , "Length"  , "Height" ]]
# Определяем зависимую переменную (целевая переменная)
y = df_whitefish['Width'] # Длина рыбки!
# Создаем модель линейной регрессии
regr = linear_model.LinearRegression()
#Обучаем модель на данных X
regr.fit(X,y)
# Предсказываем длину рыбки!
# Triff eine Vorhersage dazu, welche Breite ein Whitefish mit einem Gewicht von 233 Gramm, einer Länge von 20.3 Zentimetern und einer Höhe von 13.32 Zentimetern hat.
predicted_width = regr.predict([[233,20.3,13.32]])
print(predicted_width)