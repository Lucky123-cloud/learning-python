def firstNoneReapting(lst):
    freq = {}

    for num in lst:
        freq[num] = freq.get(num, 0) + 1
        
    for num in lst:
        if freq[num] == 1:
            return num

    return None

print(firstNoneReapting([2, 1, 1, 1, 3, 4, 5, 6]))