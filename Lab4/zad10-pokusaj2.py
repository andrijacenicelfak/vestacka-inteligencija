from termcolor import cprint
from functools import reduce
import queue


def ima_u_tabli(tabla, domina):
    pronadjene = list()
    # for i in range(4):
    #     for j in range(4):
    #         if domina[0] == tabla[i][j] and domina[1] == tabla[i][j + 1] :
    #             pronadjene.append(((i, j), False, False))
    # for i in range(4):
    #     for j in range(4):
    #         if domina[1] == tabla[i][j] and domina[0] == tabla[i][j + 1] :
    #             pronadjene.append(((i, j), False, True))
    # for i in range(3):
    #     for j in range(5):
    #         if domina[0] == tabla[i][j] and domina[1] == tabla[i + 1][j] :
    #             pronadjene.append(((i, j), True, False))
    # for i in range(3):
    #     for j in range(5):
    #         if domina[1] == tabla[i][j] and domina[0] == tabla[i + 1][j] :
    #             pronadjene.append(((i, j), True, True))
    for i in range(4):
        for j in range(5):
            if j < 4:
                if domina[0] == tabla[i][j] and domina[1] == tabla[i][j + 1]:
                    pronadjene.append(((i, j), False, False))
                if domina[1] == tabla[i][j] and domina[0] == tabla[i][j + 1]:
                    pronadjene.append(((i, j), False, True))
            if i < 3:
                if domina[0] == tabla[i][j] and domina[1] == tabla[i + 1][j]:
                    pronadjene.append(((i, j), True, False))
                if domina[1] == tabla[i][j] and domina[0] == tabla[i + 1][j]:
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

def pronadji_put(tabla, domine, use_heuristics=True):
    broj_proverenih_stanja = 0
    open_set = list()
    kraj = False
    svi_koraci = list()
    open_set.append((10, tabla, domine, list()))
    open_set.sort(key=lambda a : a[0])
    while len(open_set) > 0 and not kraj:
        broj_proverenih_stanja += 1
        (nova_tabla, nove_domine, heur, potezi, koraci) = (None, None, 9999, None, None)
        broj_poteza = 10
        domina = None
        index = -1
        for i in range(len(open_set)):
            (bp, nt, ds, k) = open_set[i]
            if(len(ds) == 0):
                continue
            trenutno = None
            trenutna_domina = None
            if use_heuristics:
                trenutno = ima_u_tabli(nt, ds[0])
                trenutna_domina = ds[0]

                for j in ds[1:]:
                    t2 = ima_u_tabli(nt, j)
                    if trenutno[0] > t2[0]:
                        trenutno = t2
                        trenutna_domina = j
            else:
                trenutna_domina = ds[0]
                trenutno = ima_u_tabli(nt, trenutna_domina)

            trenutne_domine = list(filter(lambda a: a != trenutna_domina, ds))
            if nova_tabla is None or trenutno[0] < heur:
                domina = trenutna_domina
                nova_tabla = nt
                nove_domine = trenutne_domine
                heur = trenutno[0]
                potezi = trenutno[2]
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
    return (svi_koraci, broj_proverenih_stanja)


def stampaj_tablu_po_koracima(koraci, broj_prolaza):
    poredjana_tabla = [[('_', False)]*5 for i in range(4)]

    for korak in koraci:
        kord = korak[1][0]
        domina = korak[0]
        poredjana_tabla[kord[0]][kord[1]] = (domina[0], True)
        if korak[1][1]:
            poredjana_tabla[kord[0]+1][kord[1]] = (domina[1], True)
        else:
            poredjana_tabla[kord[0]][kord[1]+1] = (domina[1], True)
        for i in range(len(poredjana_tabla)):
            for j in range(len(poredjana_tabla[0])):
                if poredjana_tabla[i][j][1]:
                    cprint(poredjana_tabla[i][j][0],
                           color="blue", attrs=['bold'], end=' ')
                else:
                    print(poredjana_tabla[i][j][0], end=' ')
                poredjana_tabla[i][j] = (poredjana_tabla[i][j][0], False)
            print('\n', end='')
        print('\n', end='')
    print(koraci)
    print("Broj stanja : ", broj_prolaza)

tabele = list()

tabele.append([
            [2, 3, 2, 2, 2],
            [3, 0, 3, 0, 0],
            [3, 0, 3, 1, 1],
            [0, 1, 1, 1, 2]
            ])
tabele.append([
            [2, 3, 3, 0, 0],
            [2, 1, 3, 1, 0],
            [2, 0, 2, 1, 0],
            [3, 3, 1, 2, 1]
            ])
tabele.append([
            [2, 3, 3, 0, 0],
            [2, 1, 3, 0, 0],
            [2, 1, 1, 2, 0],
            [3, 3, 1, 2, 1]
            ])
tabele.append([
            [2, 3, 2, 2, 2],
            [3, 0, 0, 3, 0],
            [3, 0, 3, 1, 1],
            [0, 1, 1, 1, 2]
            ])

tabele.append([
            [3, 0, 1, 3, 0],
            [3, 2, 1, 0, 1],
            [2, 2, 3, 1, 0],
            [1, 2, 2, 3, 0]
            ])
domine = [
    (3, 3), (3, 2), (3, 1), (3, 0),
    (2, 2), (2, 1), (2, 0),
    (1, 1), (1, 0),
    (0, 0)
]
(koraci, broj_prolaza) = pronadji_put(tabele[0], domine)
stampaj_tablu_po_koracima(koraci, broj_prolaza)

ukupno_prolaza = 0

for tabela in tabele:
    (koraci, broj_prolaza) = pronadji_put(tabela, domine)
    ukupno_prolaza += broj_prolaza

print("Sa heuristikom srednji broj predjenih stanja : ", int(ukupno_prolaza/len(tabele)))

ukupno_prolaza = 0

for tabela in tabele:
    (koraci, broj_prolaza) = pronadji_put(tabela, domine, False)
    ukupno_prolaza += broj_prolaza

print("Bez heuristikom srednji broj predjenih stanja : ", int(ukupno_prolaza/len(tabele)))
