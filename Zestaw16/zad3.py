import math


class Rakieta:
    a = 0
    b = 0

    def __init__(self):
        self.a = 0
        self.b = 0

    def przesun(self, x, y):
        self.a = self.a + x
        self.b = self.b + y

    def pozycja(self):
        print("pozycja " + str(self.a) + " " + str(self.b))

    def odleglosc(self, druga):
        return math.sqrt((druga.a - self.a) ** 2 + (druga.b - self.b) ** 2)


r1 = Rakieta()
r1.przesun(4, 5)
r1.pozycja()
r2 = Rakieta()
r2.przesun(2, 3)
r2.pozycja()
print(r1.odleglosc(r2))
