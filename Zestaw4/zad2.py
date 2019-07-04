def funkcja(*args):
    return max(args) - min(args)


print(funkcja(2, 3, 4, 4, -2, 8, 10))
print(funkcja(2, 3))
print(funkcja(5))
print(funkcja(1, 2, -3, 40))
