from termcolor import cprint
from functools import reduce
import queue


def ima_u_tabli(tabla, domina):
    pronadjene = list()
    for i in range(4):
        for j in range(4):
            if domina[0] == tabla[i][j] and domina[1] == tabla[i][j + 1] :
                pronadjene.append(((i, j), False, False))
    for i in range(4):
        for j in range(4):
            if domina[1] == tabla[i][j] and domina[0] == tabla[i][j + 1] :
                pronadjene.append(((i, j), False, True))
    for i in range(3):
        for j in range(5):
            if domina[0] == tabla[i][j] and domina[1] == tabla[i + 1][j] :
                pronadjene.append(((i, j), True, False))
    for i in range(3):
        for j in range(5):
            if domina[1] == tabla[i][j] and domina[0] == tabla[i + 1][j] :
                pronadjene.append(((i, j), True, True))

    return (len(pronadjene),  domina, pronadjene)

def postavi_u_tabli(tabla, potez):
    nova_tabla = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(len(tabla)):
        for j in range(len(tabla[0])):
            nova_tabla[i][j] = tabla[i][j]
    (i,j) = potez[0]
    if(potez[1]):
            nova_tabla[i][j] = 'x'
            nova_tabla[i+1][j] = 'x'
    else:
        nova_tabla[i][j] = 'x'
        nova_tabla[i][j+1] = 'x'

    return nova_tabla

def make_tuple(tabla):
    return reduce(lambda a, b: (*a, reduce(lambda x, y: (*x, y), b, tuple())), tabla, tuple())

def make_list(tabla):
    return reduce(lambda a, b: [*a, reduce(lambda x, y: [*x, y], b, tuple())], tabla, tuple())

def pronadji_put(tabla, domine):
    open_set = list()
    kraj = False
    svi_koraci = list()
    open_set.append((10, tabla, domine, list()))
    while len(open_set) > 0 and not kraj:
        (nova_tabla, nove_domine, heur, potezi, koraci) = (None, None, 9999, None, None)
        broj_poteza = 10
        open_set.sort(key=lambda a : a[0])
        domina = None
        index = -1
        for i in range(len(open_set)):
            (bp, nt, ds, k) = open_set[i]
            if(len(ds) == 0):
                continue
            heuristics = ima_u_tabli(nt, ds[0])
            if nova_tabla is None or heuristics[0] < heur:
                domina = ds[0]
                nova_tabla = nt
                nove_domine = ds[1:]
                heur = heuristics[0]
                potezi = heuristics[2]
                koraci = k
                broj_poteza = bp
                index = i
        open_set.remove(open_set[index])
        for p in potezi:
            ntabla = postavi_u_tabli(nova_tabla, p)
            novi_koraci = koraci[:]
            novi_koraci.append((domina, p))
            open_set.append((broj_poteza-1, ntabla, nove_domine, novi_koraci))
            if( len(novi_koraci)== 10):
                kraj = True
                svi_koraci = novi_koraci

    return svi_koraci

tabla = [
    [2, 3, 2, 2, 2],
    [3, 0, 3, 0, 0],
    [3, 0, 3, 1, 1],
    [0, 1, 1, 1, 2]
]
domine = [
    (3, 3), (3, 2), (3, 1), (3, 0),
    (2, 2), (2, 1), (2, 0),
    (1, 1), (1, 0),
    (0, 0)
]
print(pronadji_put(tabla, domine))