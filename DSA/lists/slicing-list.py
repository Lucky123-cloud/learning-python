lst = [1, 2, 3, 4, 5]

a = lst[1:4] #[2, 3, 4]
b = lst[:3] #[1, 2, 3]
c = lst[::2] # step slicing -> [1, 3, 5]
d = lst[::1]
e = lst[::-1]
f = lst[::-2]

print("a", a)
print("b", b)
print("c", c)
print("d", d)
print("e", e)
print("f", f)