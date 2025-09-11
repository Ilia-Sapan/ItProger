from random import randint
from math import *
# a
random_number = randint(1, 10)  # Случайное число от 1 до 10
print(random_number)
# b
def calculate_quadrat(x):
    return pow(x,2)
# c
if random_number > 5:
    print(calculate_quadrat(random_number))
elif random_number <=5:
    print(f"Die Zahl {random_number} ist kleiner oder gleich als fünf!")

# d
for i in range(1,random_number+1):
    print(i)