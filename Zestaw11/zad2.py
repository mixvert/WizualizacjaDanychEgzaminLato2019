def mnozenie(*args):
    wynik = 1
    for element in args:
        wynik = wynik * element

    return wynik


print(mnozenie(2, 3, 4, 5))
print(mnozenie(5))
print(mnozenie(1, 7, 0, 2))
