import math
n = 7
ar = [1,2,1,2,1,3,2]
# result = 3
def sockMerchant(n, ar):
    a = {}
    for el in ar:
        a[el] = ar.count(el)
    b = []
    for values in a.values():
        if values >= 2:
            c = values / 2
            b.append(c)
        b = list(map(lambda x: math.floor(x), b))
    return sum(b)




print(sockMerchant(n,ar))


n2 = 9
ar2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(n2,ar2))