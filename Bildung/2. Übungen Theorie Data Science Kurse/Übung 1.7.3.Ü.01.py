liste = [[1,2,3],[6,5,3,3],[54,3]]

list_neu = []
for elements in liste:
    a = sum(elements)
    list_neu.append(a)
print(list_neu)

def q_a(items):
    for item in items:
        result = 0
        for item2 in item:
            result += item2
        print(result)
    pass

print(q_a(liste))