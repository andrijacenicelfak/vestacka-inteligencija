from functools import *


def test(testStr: str):
    rez = list(map(lambda x: chr(x) if (x >= 65 and x <= 90) or (x >= 97 and x <= 122) or (
        x >= 48 and x <= 57) else "\\u" + hex(x)[2:].zfill(4), map(lambda x: ord(x), testStr)))
    return reduce(lambda a, b: a+b, rez)


print(test("Otpornost 10Ω."))
