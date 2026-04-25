def freqElem(lst):
    freq = {}

    for n in lst:
        freq[n] = freq.get(n, 0) + 1
    return freq


print(freqElem([2, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8]))