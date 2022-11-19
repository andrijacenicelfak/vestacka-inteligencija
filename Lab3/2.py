import queue


def disjuktni_putevi(graph, start, end):
    nekompletni_putevi = queue.Queue(-1)
    nekompletni_putevi.put([start])
    kompetni_putevi = []
    while not nekompletni_putevi.empty():
        put = nekompletni_putevi.get()
        poslednji = put[-1]
        if poslednji is end:
            kompetni_putevi.append((*put,))
        else:
            potencijalni = graph[poslednji]
            if len(potencijalni) > 0:
                for cvor in potencijalni:
                    if cvor not in put:
                        nekompletni_putevi.put([*put, cvor])
    # prikaz za sve puteve
    for i in kompetni_putevi:
        print(i)
    return len(kompetni_putevi)


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'A', 'B'],
    'D': ['C', 'E', 'F'],
    'E': ['G', 'H', 'A'],
    'F': ['B', 'C', 'D'],
    'G': ['E', 'F', 'H'],
    'H': ['J'],
    'J': []
}

print(disjuktni_putevi(graph, 'A', 'F'))
