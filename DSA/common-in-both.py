def common_elements(a, b):
    return list(set(a) & set(b))


# OR

def common_elements2(a, b):
    b_set = set(b)
    result = []

    for num in a:
        if num in b_set and num not in result:
            result.append(num)
    return result

print(common_elements([3, 1, 2, 2], [2, 3, 4]))
print(common_elements2([3, 1, 2, 2], [2, 3, 4]))