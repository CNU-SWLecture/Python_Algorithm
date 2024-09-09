a = 1
print(id(a))
print(id(1))

c = [10, 100, a]
print(c)
print(id(c))

print(id(c[0]))
print(id(c[1]))
print(id(c[2]))