import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

operacja1 = math.pow(a * b * c, 1 / 3)
print(operacja1)
operacja2 = math.log(a ** 3) + math.log10(d)
print(operacja2)
operacja3 = (math.sin(a)) ** 2 + (math.cos(a)) ** 2 + d / math.sqrt(d)
print(operacja3)
