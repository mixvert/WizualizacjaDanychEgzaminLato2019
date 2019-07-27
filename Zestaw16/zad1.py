# uwaga, wykonanie skryptu może długo trwać
def funkcja(n, m):
    if m == 0:
        return 0
    if n >= m > 0:
        return n - m + funkcja(n - 1, m) + funkcja(n, m - 1)
    else:
        return funkcja(m, n)


print(funkcja(44, 22))
