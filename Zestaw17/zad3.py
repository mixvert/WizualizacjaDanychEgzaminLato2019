import math


def pole(a, b, c, d):
    p = (a + b + c + d) / 2
    return math.sqrt((p - a) * (p - b) * (p - c) * (p - d))


print(pole(3, 4, 3, 4))
