def isPalindrome(n):
    return n == int(str(n)[::-1])

print(isPalindrome(121))

def isPalindrome2(n):
    reversed_number = 0
    original = n

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10

    return original == reversed_number

print(isPalindrome2(121))