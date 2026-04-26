def removeDups(lst):
    seen = set()

    for n in lst:
        if n in seen:
            print(f"{n} is in seen already")
            return
        else:
            seen.add(n)
    return list(seen)


print(removeDups([1, 2, 3, 4, 5, 6]))