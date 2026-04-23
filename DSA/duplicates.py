def duplicate(n):
    freq = {}

    for num in n:
        freq[num] = freq.get(num, 0) + 1

    return freq

print(duplicate([1, 2, 2, 3, 3, 4, 4, 4, 5, 6]))