from functools import reduce


def operacija(l1, func):
    return list(map(lambda t: reduce(func, t), l1))


def objedini(l1):
    return list(map(lambda x: {x: None} if type(x) in (int, float) else {x[0]: list(map(lambda z: z[1], filter(lambda y: y[0] > 0, enumerate(list(x)))))}, l1))


print(operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y))
print(objedini([(1), (3, 4, 5), (7), (1, 4, 5), (6, 2, 1, 3)]))
