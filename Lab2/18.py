from re import *


def brojevi(strUlaz: str):
    return list(map(lambda x: int(x), findall(r'(\d+)', strUlaz)))


print(brojevi("42+10=52;10*10=100"))
