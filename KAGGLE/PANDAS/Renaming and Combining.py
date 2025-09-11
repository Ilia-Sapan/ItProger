from kaggle_utils import load_kaggle_dataset
import pandas as pd

reviews = load_kaggle_dataset('atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024')
print(reviews.info())

print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t        Переименование колонки      \n")
reviews.rename(columns={'Age': 'Alt'}, inplace=True)
print(reviews.head())
print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t        Переименование индекса    \n")
reviews.rename(index = {0 : 'Erste', 1 : 'Zweite'}, inplace=True)
print(reviews.head())
print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t    Задает имена осей    \n")
reviews.rename_axis("Country", axis='rows', inplace=True)
print(reviews.head())
print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t        Комбинирование    \n")
canadian_youtube = pd.read_csv(r"C:\Users\isapa\PycharmProjects\itProger\KAGGLE\PANDAS\data\extracted\CAvideos.csv")
british_youtube = pd.read_csv(r"C:\Users\isapa\PycharmProjects\itProger\KAGGLE\PANDAS\data\extracted\DEvideos.csv")
pd.concat([canadian_youtube, british_youtube])
print("------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t        Код выполняет левое соединение (left join) двух DataFrame по общему мульти‑индексу    \n")
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')

# например

import pandas as pd

# Создаём два DataFrame
canadian = pd.DataFrame({
    'title': ['A', 'B'],
    'trending_date': ['2021-01-01', '2021-01-01'],
    'views': [100, 200]
}).set_index(['title', 'trending_date'])

british = pd.DataFrame({
    'title': ['A', 'C'],
    'trending_date': ['2021-01-01', '2021-01-01'],
    'likes': [10, 30]
}).set_index(['title', 'trending_date'])

# Левое соединение
result = canadian.join(british, lsuffix='_CAN', rsuffix='_UK')

print(result)
