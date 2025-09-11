import pandas as pd

# DataFrame() для создания столбцов и строк.
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)
print("________________________________________________________________________________________")
df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(df)
print("________________________________________________________________________________________")

df = pd.DataFrame({'Ellina': ['Swimming', 'Gym'], 'Ilia': ['Wrestling', 'Gym']})
print(df)
print("________________________________________________________________________________________")

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']) # Добавляем индекс
print(df)
print("________________________________________________________________________________________")
# Series() для создания столбцовых данных

df = pd.Series([1, 2, 3, 4, 5])
print(df)

print("________________________________________________________________________________________")
df = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(df)



wine_reviews = pd.read_csv("    ../input/wine-reviews/winemag-data-130k-v2.csv")
wine_reviews.shape
wine_reviews.head()
# index_col позволяет убрать ненужные индексы
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()