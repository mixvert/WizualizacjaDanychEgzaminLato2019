import math


def funkcja(zdanie):
    # pomocniczy wektor przechowujący długości wyrazów w zdaniu
    dlugosci = [len(x) for x in zdanie.split()]
    # średnia z wartości na liście długosci
    srednia = sum(dlugosci) / float(len(dlugosci))
    # trik by mieć matematyczne zaokrąglenie
    srednia = math.floor(srednia + 0.5)
    return srednia


zd1 = "Ala ma kota"
print(funkcja(zd1))
zd2 = "Wlazł kotek na płotek"
print(funkcja(zd2))
zd3 = "Lorem ipsum dolor sit amet"
print(funkcja(zd3))
