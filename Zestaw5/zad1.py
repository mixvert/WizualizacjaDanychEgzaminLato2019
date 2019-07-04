def funkcja(lista):
    minlen = 1000
    minstr = ""
    for elem in lista:
        if len(elem) <= minlen:
            minlen = len(elem)
            minstr = elem

    return minstr


print(funkcja(["Ala", "ma", "kota"]))
print(funkcja(["Ala", "ma", "ko"]))
