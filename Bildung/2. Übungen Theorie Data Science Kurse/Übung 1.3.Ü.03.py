def mittelwert(liste):
    a = len(liste)
    b = 0
    for el in liste:
        if el == int(el) or el == float(el):
            b += el
    result = round(b / a, 2)
    return result





s = [2,2,3]
print(mittelwert(s))