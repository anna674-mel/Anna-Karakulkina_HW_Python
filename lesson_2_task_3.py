from math import ceil


def square(a):
    return ceil(a*a)


a = float(input('Введите длину стороны квадрата: '))


print(f'Округленная в большую сторону площадь квадрата - {square(a)}')
