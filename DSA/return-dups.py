def dups(lst):
    freq = {}

    for n in lst:
        freq[n] = freq.get(n, 0) + 1

    return [num for num, count in freq.items() if count > 1]
    

print(dups([2, 1, 3, 4, 2, 3, 5, 4, 3, 4]))

# OR

def dups2(lst):
    seen = set()
    duplicates = set()

    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(dups2([2, 1, 3, 4, 2, 3, 5, 4, 3, 4]))