def funkcja(napis):
    napis = napis.replace('a', '$')
    napis = napis.replace('e', '$')
    napis = napis.replace('i', '$')
    napis = napis.replace('o', '$')
    napis = napis.replace('u', '$')
    napis = napis.replace('y', '$')
    return napis


print(funkcja("informatyka"))
