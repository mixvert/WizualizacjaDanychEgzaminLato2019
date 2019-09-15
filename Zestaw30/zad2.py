def funkcja(lista):
    ile = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            ile = ile + 1
    return ile


print(funkcja([3, 4, 5, 6, 1, 2]))
