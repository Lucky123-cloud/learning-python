num = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
freq = {}


for n in num:
    if n % 2 == 0:
        freq[n] = freq.get(n, 0) + 1
        count += 1

print(count)
print(freq)
print(list(set(num)))
