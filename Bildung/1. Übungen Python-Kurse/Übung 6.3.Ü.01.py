import random
import math


zahl = random.randint(1, 100)


def quadratwurzel(z):
    return math.sqrt(z)

if zahl > 50:
    print(f"Quadratwurzel von {zahl} ist {quadratwurzel(zahl)}")
else:
    print("Zahl ist 50 oder kleiner")


for i in range(1, 6):
    print(f"Quadratwurzel von {i} ist {quadratwurzel(i)}")