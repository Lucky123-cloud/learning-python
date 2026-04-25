def merge(a, b):
    merged = a + b
    return list(dict.fromkeys(merged))
# if order is important


print(merge([1, 2, 3], [4, 5, 6]))

# OR

def merge2(a, b):
    return list(set(a + b)) 
# only if order is not Important

print(merge2([1, 2, 3], [4, 5, 6]))

# OR
def merge3(a, b):
    seen = set()
    result = []

    for num in a + b:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(merge3([1, 2, 3], [4, 5, 6]))