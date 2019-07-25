# zadanie ma bardzo wiele sposobów na rozwiązanie

# I sposób
import math

lista = [2, 34, 55]
wynik = 0
for x in lista:
    wynik = wynik * (10 ** (round(math.log10(x)))) + x

print(wynik)
