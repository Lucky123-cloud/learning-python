def isTriangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

print(isTriangle(3, 4, 5))


def isTriangle2(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2]

print(isTriangle(3, 4, 5))