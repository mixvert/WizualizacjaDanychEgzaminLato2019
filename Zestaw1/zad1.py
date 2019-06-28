import math

print("Program do obliczenia pierwiastków")
print("ax^2+bx+c=0")
# pobranie wartości z wejścia za pomocą funkcji input
# input daje string'a, więc wynik jest rzutowany na int'a
print("Podaj a")
a = int(input())
print("Podaj b")
b = int(input())
print("Podaj c")
c = int(input())
# przypadek kiedy a jest różne od zera
if a != 0:
    # obliczenie delty
    delta = b ** 2 - 4 * a * c
    # pierwiastki w zależności od delty
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Pierwiastki: " + str(x1) + " " + str(x2))
    elif delta == 0:
        x = -b / (2 * a)
        print("Pierwiastek: " + str(x))
    else:
        print("Brak pierwiastków")
else:
    if b != 0:
        x = -c / b
        print("Pierwiastek: " + str(x))
    else:
        if c == 0:
            print("równanie tożsamościowe")
        else:
            print("równanie sprzeczne")
