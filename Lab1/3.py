from itertools import *


def uredi(lista, broj, vrednost):

    rez = list(map(lambda x: x[1] + vrednost if x[0] <
               broj else x[1] - vrednost, list(enumerate(lista))))

    return rez


def spoji(l1, l2):
    return list(starmap(lambda x, y: (x, y, x + y), zip_longest(l1, l2, fillvalue=0)))


print(uredi([1, 2, 3, 4, 5], 3, 1))
print(spoji([1, 7, 2, 4], [2, 5, 2]))
