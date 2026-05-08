#  Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is,n = mi for some
# integer i,andFalse otherwise.

def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


def is_multiple2(n, m):
    return n % m == 0


print(is_multiple(10, 5))
print(is_multiple(10, 3))
print(is_multiple2(10, 5))