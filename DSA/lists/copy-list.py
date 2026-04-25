a = [1, 2, 3]

b = a # same reference

c = a.copy() # safe copy

print(a)
print(b)
print(c)

c = a + b
print(c)
print(b)
print(a)

b = b + c
print(a)
print(b)

a = c + b
print(a)
print(b)
