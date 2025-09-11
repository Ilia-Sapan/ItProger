# Programmiere eine Funktion, die den euklidischen Abstand zwischen n-dimensionalen Tupeln berechnen kann

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]

def euklid(x, y):
    return sum((a - b) ** 2 for a, b in zip(x, y)) ** 0.5

print(euklid(x,y))