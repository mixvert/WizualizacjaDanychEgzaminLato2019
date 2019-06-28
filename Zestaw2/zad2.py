def sumdigits(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + sumdigits(number // 10)


print(sumdigits(34512))
