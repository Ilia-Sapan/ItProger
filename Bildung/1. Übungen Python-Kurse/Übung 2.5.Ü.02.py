# Aufgabe: Datentypen

# A
a = 42 # int
b = 33.3 # float
c = 33 + 1j # complex
d = "Hello, World" # str
e = (1,2,3,4,5) # tuple
f = [1,2,3,4,5] # list
g = {1,2,3} #set

# B

print(f"Der Datentyp von a ist: {type(a)}")
print(f"Der Datentyp von b ist: {type(b)}")
print(f"Der Datentyp von c ist: {type(c)}")
print(f"Der Datentyp von d ist: {type(d)}")
print(f"Der Datentyp von e ist: {type(e)}")
print(f"Der Datentyp von f ist: {type(f)}")
print(f"Der Datentyp von g ist: {type(g)}")

# C

b = str(b) # Konvertierung in einen Datentyp str
print(b)

# D
neues_list = [f[0], f[1], e[-1]]
print(neues_list)

# E
g.add(4)
print(g)