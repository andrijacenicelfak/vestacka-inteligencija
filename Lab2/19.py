from functools import *
from itertools import *


def brojanje(strUlaz: str):
    return reduce(lambda a, b: a+1 if b > 1 else a, (starmap(lambda a, b: len(list(b)), groupby(strUlaz))), 0)


print(brojanje("aatesttovii"))
