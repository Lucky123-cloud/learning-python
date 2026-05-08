def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result



def factors2(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i



print(factors(12))
print(list(factors2(12)))