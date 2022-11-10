from functools import *


def broj(strBroj: str):
    strBroj = strBroj.upper()
    return reduce(lambda a, b: a + (ord(b[1]) - (48 if ord(b[1]) <= 57 else 55))*(16 ** (5 - int(b[0]))), enumerate(strBroj[1:]), 0)


print(broj("#FA0EA0"))
