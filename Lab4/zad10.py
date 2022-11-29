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


def rekurzivno(tabla, domine, koraci, i=0):
    if len(domine) == 0:
        return (True, koraci)
    #(trenutno, nove_domine) = (domine[0], [*domine[1:]])
    #print(len(domine))
    #print(koraci)
    for trenutno in domine:
        #print("Depth", i)
        #print("Domina", trenutno)
        # for t in tabla:
        #     print(t)
        # print('\n')
        lokacije = ima_u_tabli(tabla, trenutno)
        if (len(lokacije) == 0):
            continue
        for lokacija in lokacije:
            # print(lokacija)
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


def poredjaj_domine(tabla, domine):

    poredjana_tabla = [[None]*len(tabla) for i in range(len(tabla[0]))]

    print("Po kojim vrednostima treba da se radju domine:")
    for t in tabla:
        print(t)
    print("Pocetna tabla:")
    for t in poredjana_tabla:
        print(t)
    koraci = list()
    (moguce, koraci) = rekurzivno(tabla, domine, koraci)
    if not moguce:
        print("Nema resenja!");
    return koraci


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

print(poredjaj_domine(tabla, domine))
