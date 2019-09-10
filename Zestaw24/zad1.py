def funkcja(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 3 * funkcja(n - 2)


print(funkcja(6))
