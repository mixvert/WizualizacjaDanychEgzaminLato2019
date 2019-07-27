rok = int(input())


def funkcja(x):
    if x % 4 == 0 and x % 100 != 0:
        print("rok przestępny")
    elif x % 400 == 0:
        print("rok przestępny")
    else:
        print("rok nie jest przestępny")


funkcja(rok)
print("rok 2000")
funkcja(2000)
