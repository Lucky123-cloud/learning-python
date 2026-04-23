def reverse(n):
    reversed_number = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit

        n //= 10
    return reversed_number


print(reverse(252347))



def reverse2(n):
    return int(str(n)[::-1])


print(reverse2(654))
