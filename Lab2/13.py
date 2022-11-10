from functools import *
from itertools import *


def skupi(l1):
    # uzima svaku listu i sledecu da bi njihove elemente dodao, ne uzima samo poslednju
    return list(starmap(lambda i, x: list(starmap(lambda a, b: a+b, zip_longest(x, l1[i+1], fillvalue=0))), enumerate(l1[:-1])))


print(skupi([[1, 3, 5], [2, 4, 6], [1, 2], [0, 0, 1]]))
