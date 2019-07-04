def suma_cyfr(liczba):
    liczba = str(liczba)
    suma = 0
    for elem in liczba:
        suma = suma + int(elem)

    return suma


print(suma_cyfr(3004))
print(suma_cyfr(12345))
