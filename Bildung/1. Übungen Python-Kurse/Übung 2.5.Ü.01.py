# A

a = 33 # int
b = 33.3 # float
c = 33 + 1j # complex
d = "Hello, World" # str
e = (1,2,3,4,5) # tuple
f = [1,2,3,4,5] # list
g = {1,2,3} #set

#B

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#C

a_float = float(a)
a_string = str(a)
print(a_float)
print(a_string)

#D

neue_liste = f[:-3]
print(neue_liste)
if f[-1] not in neue_liste:
    neue_liste.append(f[:-1])
print(neue_liste)

# E
g.add(4)
g.add(5)
print(g)

