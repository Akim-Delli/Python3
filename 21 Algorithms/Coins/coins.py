__author__ = 'adelli'

from functools import reduce

def change(data, total):
    data.sort(key=int)
    return reduce(lambda l, x: l + [(divmod(l[-1][0], int(x))[1], divmod(l[-1][0], int(x))[0], x)], reversed((data)), [(total,0, 0)])[1:]


def calculateChange(changeCoins, amount):
    for element in change(changeCoins, amount):
        if element[1] !=0 : print('{} coins of {}'.format(element[1], element[2]))

calculateChange([1, 3, 5, 10, 50], 2458)
