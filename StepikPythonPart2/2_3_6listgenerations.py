x = [-2, -1, 0, 1, 2]
y = []
for i in x:
    y.append(i * i)
print(y)
#list comprehantions
g = [i * i for i in x]
print(g)
h = [i * i for i in x if i > 0]
print(h)
p = [(x, y) for x in range(3) for y in range(3) if y >=x]
print(p)
z =[]
for x in range(3):
    for y in range(3):
        if y >= x:
            z.append((x, y))
print(z)
# замена скобок [] на () делает данную конструкцию генератором
p1 =((x, y) for x in range(3) for y in range(3) if y >=x)
print(p1)
print(next(p1))
print(next(p1))

