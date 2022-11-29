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


def poredjaj_domine(tabla, domine):

    poredjana_tabla = [[('_', False)]*len(tabla[0]) for i in range(len(tabla))]
    print("Po kojim vrednostima treba da se radju domine:")
    for t in tabla:
        print(t)
    print('\n')
    koraci = list()
    (moguce, koraci) = rekurzivno(tabla, domine, koraci)
    if not moguce:
        print("Nema resenja!")
    else : 
        for korak in koraci:
            kord = korak[1][0]
            domina = korak[0]
            poredjana_tabla[kord[0]][kord[1]] = (domina[0], True)
            if korak[1][1] :
                poredjana_tabla[kord[0]+1][kord[1]] = (domina[1], True)
            else:
                poredjana_tabla[kord[0]][kord[1]+1]= (domina[1], True)
            for i in range(len(poredjana_tabla)):
                for j in range(len(poredjana_tabla[0])):
                    if poredjana_tabla[i][j][1]:
                        cprint(poredjana_tabla[i][j][0],color="blue", attrs=['bold'] ,end=' ')
                    else:
                        print(poredjana_tabla[i][j][0], end=' ')
                    poredjana_tabla[i][j] = (poredjana_tabla[i][j][0], False)
                print('\n', end='')
            print('\n', end='')
                    
                        
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
