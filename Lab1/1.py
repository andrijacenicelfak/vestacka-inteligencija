def parni(list):
    i = 0
    for x in list:
        if x % 2 == 0:
            i += 1
    return i


def poredak(lista1, lista2):
    kraca = lista1 if len(lista1) < len(lista2) else lista2
    duza = lista1 if len(lista1) >= len(lista2) else lista2
    nule = [0] * (len(duza) - len(kraca))
    kraca.extend(nule)
    rez = []

    for i in range(len(lista1)):
        rez.append(
            (lista1[i], lista2[i], 'Jeste' if lista2[i] >= lista1[i]*2 else 'Nije'))

    return rez


print(parni([1, 4, 5, 2, 8, 2]))
print(poredak([1, 7, 2, 4], [2, 5, 2]))
