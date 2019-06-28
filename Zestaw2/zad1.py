# wersja 1
def funkcja(arg):
    return list(set(arg))


# wersja 2
def funkcja2(arg):
    return list(dict.fromkeys(arg))


# wersja 3
def funkcja3(arg):
    temp = []
    for elem in arg:
        if elem not in temp:
            temp.append(elem)
    return temp


test = [34, 12, -3, 4, 5, 5, 12, -3]
print(type(test))
test = funkcja(test)
print(type(test))

test2 = [34, 12, -3, 4, 5, 5, 12, -3]
print(type(test2))
test2 = funkcja2(test2)
print(type(test2))

test3 = [34, 12, -3, 4, 5, 5, 12, -3]
print(type(test3))
test3 = funkcja3(test3)
print(type(test3))
