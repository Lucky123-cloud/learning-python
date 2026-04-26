def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]