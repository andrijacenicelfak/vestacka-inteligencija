def numlista(lista):
    return list(filter(lambda x: type(x) in (int, float), lista))


def spojidict(l1, l2):
    kraca = l1 if len(l1) < len(l2) else l2
    duza = l1 if len(l1) >= len(l2) else l2
    minusi = ['-'] * (len(duza) - len(kraca))
    kraca.extend(minusi)
    rez = list(map(lambda x, y: {'prvi': x, 'drugi': y}, l1, l2))
    return rez


print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))
print(spojidict([1, 7, 2, 4], [2, 5, 2]))
