# Implementirati Backtracking traženje u kombinaciji sa Forward checking tehnikom i Degree
# heuristikom za bojenje čvorova grafa sa tri boje (crvena, zelena i plava) tako da ni jedna dva
# susedna čvora nemaju istu boju


def oboji(graph, vrednosti):
    broj_stanja = 0
    moguce_boje = {x : [y for y in vrednosti] for x in graph.keys()}
    is_done = False

    obojeno = {x : None for x in graph.keys()}

    open_set = list()
    open_set.append((moguce_boje, obojeno, 0))
    
    while len(open_set) > 0 and not is_done:
        broj_stanja += 1
        #open_set.sort(key=lambda x: x[2])
        (trenutno_moguce, trenutno_obojeno, broj_obojenih) = open_set[-1]
        trenutni_cvor, broj_veza = None, 0
        for c in list(filter(lambda a: trenutno_obojeno[a] is None, trenutno_obojeno.keys())):
            # print(c, ", ", end="")
            if len(graph[c]) > broj_veza:
                trenutni_cvor = c
                broj_veza = len(graph[c])
        # print()
        open_set.remove(open_set[-1])
        if len(trenutno_moguce[trenutni_cvor]) == 0:
            continue

        for boja in trenutno_moguce[trenutni_cvor]:
            novo_moguce = {x : trenutno_moguce[x][:] for x in trenutno_moguce.keys()}
            novo_obojeno = {x : trenutno_obojeno[x] for x in trenutno_obojeno.keys()}
            next_is_valid = True
            # print("---------------------------------------")
            # print(boja)
            # print(novo_moguce)
            # print(trenutni_cvor)
            novo_moguce[trenutni_cvor].remove(boja)
            novo_obojeno[trenutni_cvor] = boja
            for c in graph[trenutni_cvor]:
                if boja in novo_moguce[c]:
                    novo_moguce[c].remove(boja)
                    if len(novo_moguce[c]) == 0 and novo_obojeno[c] is None:
                        next_is_valid = False
                        break
            # print(novo_moguce)
            # print(trenutni_cvor)
            # print(next_is_valid)
            if next_is_valid :
                if broj_obojenih + 1 == len(graph.keys()):
                    is_done = True;
                    obojeno = novo_obojeno.copy()
                    break
                open_set.append((novo_moguce, novo_obojeno, broj_obojenih+1))
        # print("*************************************************")

    for x in obojeno.keys():
        if obojeno[x] is None:
            return None
    return (obojeno, broj_stanja)

graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'D'],
    'C' : ['E', 'F'],
    'D' : ['A', 'B', 'E', 'F'],
    'E' : ['A', 'C'],
    'F' : ['C', 'E']
}

graph2 = {
    'A' : ['B', 'G'],
    'B' : ['A', 'G', 'E', 'C', 'H'],
    'C' : ['B', 'G', 'D'],
    'D' : ['F', 'G', 'C', 'E'],
    'E' : ['D', 'E', 'B'],
    'F' : ['G', 'D'],
    'G' : ['F', 'D', 'A', 'C'],
    'H' : ['B', 'E'],
}
vrednosti = ["crvena", "plava", "zelena"]

obojeni = oboji(graph2, vrednosti)
print(obojeni)