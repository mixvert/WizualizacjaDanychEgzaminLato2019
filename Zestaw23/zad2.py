def funkcja(lista):
    wynik = 0
    for i in range(len(lista)):
        wynik = wynik + lista[i]

    return wynik


print(funkcja([3, 4, 5]))
