# I sposób
import string

litery = string.ascii_lowercase
for elem1 in litery:
    for elem2 in litery:
        for elem3 in litery:
            print(elem1 + elem2 + elem3)
