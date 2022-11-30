from termcolor import cprint
from functools import reduce


def ima_u_tabli(tabla, domina):
    pronadjene = list()
    for i in range(4):
        for j in range(4):
            if domina[0] == tabla[i][j] and domina[1] == tabla[i][j+1]:
                pronadjene.append(((i, j), False))
    for i in range(3):
        for j in range(5):
            if domina[0] == tabla[i][j] and domina[1] == tabla[i+1][j]:
                pronadjene.append(((i, j), True))
    return pronadjene


def rekurzivno(tabla, domine, koraci=list(), i=0):
    if len(domine) == 0:
        return (True, koraci)
    for trenutno in domine:
        lokacije = ima_u_tabli(tabla, trenutno)
        if (len(lokacije) == 0):
            continue
        for lokacija in lokacije:
            nova_tabla = [x[:] for x in tabla]
            nova_tabla[lokacija[0][0]][lokacija[0][1]] = 'x'
            if not lokacija[1]:
                nova_tabla[lokacija[0][0]][lokacija[0][1]+1] = 'x'
            else:
                nova_tabla[lokacija[0][0]+1][lokacija[0][1]] = 'x'
            domine_za_prosledjivanje = list(filter(lambda a : a != (trenutno[1], trenutno[0]) and a != trenutno, domine[:]))
            novi_koraci = [*koraci, (trenutno, lokacija),]
            moguce = rekurzivno(nova_tabla, domine_za_prosledjivanje, novi_koraci, i+1)
            if moguce[0]:
                return (True, moguce[1])
    return (False, None)


tabla = [
    [2, 3, 2, 2, 2],
    [3, 0, 3, 0, 0],
    [3, 0, 3, 1, 1],
    [0, 1, 1, 1, 2]
]
domine = [
    (3, 3), (3, 2), (3, 1), (3, 0),
    (2, 3), (2, 2), (2, 1), (2, 0),
    (1, 3), (1, 2), (1, 1), (1, 0),
    (0, 3), (0, 2), (0, 1), (0, 0)
]

print(rekurzivno(tabla, domine))
