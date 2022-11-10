from functools import *
from itertools import starmap


def brojanje(strUlaz: str):
    rez = list(strUlaz)
    rez2 = [(reduce(lambda a, b: a, enumerate(rez), 0))
            for i in range(len(rez))]
    return max(rez2)


print(brojanje("aatesttovi"))
