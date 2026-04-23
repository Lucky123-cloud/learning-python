def sumOfDigits(n):
    total = 0
    n = abs(n)

    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sumOfDigits(123))


def suming(n):
    return sum(int(d) for d in str(abs(n)))

print(suming(345))