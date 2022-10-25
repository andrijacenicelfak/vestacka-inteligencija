def uredi(lista, broj, vrednost):

    rez = list(map(lambda x: x[1] + vrednost if x[0] <
               broj else x[1] - vrednost, list(enumerate(lista))))

    return rez


def spoji(l1, l2):
    kraca = l1 if len(l1) < len(l2) else l2
    duza = l1 if len(l1) >= len(l2) else l2
    nule = [0] * (len(duza) - len(kraca))
    kraca.extend(nule)

    rez = list(
        map(
            lambda x, y:
                (x[1], y, x[1] + y) if x[0] == len(l1)-1 else (x[1] if x[1] <
                                                               y else y, x[1] if x[1] > y else y, x[1]+y), list(enumerate(l1)), l2
        )
    )

    return rez


print(uredi([1, 2, 3, 4, 5], 3, 1))
print(spoji([1, 7, 2, 4], [2, 5, 2]))
