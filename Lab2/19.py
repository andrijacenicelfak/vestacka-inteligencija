from functools import *
from itertools import *


def brojanje(strUlaz: str):
    rez = list(strUlaz)
    return max(starmap(lambda a, b: len(list(b)), groupby(strUlaz)))


print(brojanje("aatestttovi"))
