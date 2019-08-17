def funkcja(n):
    if n == 0 or n == 1:
        return 1
    else:
        return 4 * funkcja(n - 1) + 5


print(funkcja(19))
