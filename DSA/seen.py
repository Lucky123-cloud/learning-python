num = [1, 2, 3, 3, 4, 4, 5, 6]

seen = set()

for n in num:
    if n in seen:
        print("first duplicate: ", n)
        break
    seen.add(n)

