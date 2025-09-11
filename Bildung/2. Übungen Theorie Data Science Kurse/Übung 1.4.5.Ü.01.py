# Programmiere einen Code, der eine Liste von Zahlen mit der Simple-Feature-Methode skaliert.

a = [1,2,3,4,5,6,7,8,9,10]

def sfm(liste):
    return list(map(lambda x: x / max(liste), liste))
print(sfm(a))