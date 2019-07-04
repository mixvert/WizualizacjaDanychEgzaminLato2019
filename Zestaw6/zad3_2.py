# II sposób
import itertools

result = map(''.join, itertools.product('abcdefghijklmnopqrstuvwyz', repeat=3))
for elem in result:
    print(elem)
