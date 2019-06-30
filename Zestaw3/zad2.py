import math

print("Podaj a")
a = float(input())
print("Podaj b")
b = float(input())
print("Podaj c")
c = float(input())

operacja1 = (a ** 2 + math.sin(b)) / (math.e ** c)
print(operacja1)
operacja2 = math.atan(b * c ** 2)
print(operacja2)
operacja3 = math.log(c, a)
print(operacja3)
