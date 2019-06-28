import math


class Kolo:
    promien = 0

    def __init__(self, r):
        self.promien = r

    def pole(self):
        return math.pi * self.promien ** 2


k1 = Kolo(5)
print(k1.pole())
