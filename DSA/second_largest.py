def secondLargest(lst):
    lst = sorted(lst)
    lst = list(set(lst))
    lst = lst[::-1]
    return(lst[1])


print(secondLargest([3, 4, 1, 2, 6, 7, 8, 1, 2]))
