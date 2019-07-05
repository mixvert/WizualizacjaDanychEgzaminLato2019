def gwiazdki(n):
    for j in range(1, n + 1):
        for k in range(1, j + 1):
            print("*", end="")

        print("")
    for j in range(n - 1, 0, -1):
        for k in range(1, j + 1):
            print("*", end="")

        print("")


gwiazdki(5)
