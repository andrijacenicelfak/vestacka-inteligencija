# Napisati funkciju koja određuje visinu stabla traženja (broj nivoa u stablu traženja), a za algoritam obilaska grafa po širini, koje se formira za zadati polazni čvor i zadati graf.
import queue


def depth(graph, start):
    kompletni_putevi = []
    nekompletni_putevi = queue.Queue(-1)
    nekompletni_putevi.put([start])
    while not nekompletni_putevi.empty():
        put = nekompletni_putevi.get()
        poslednji = put[-1]
        potencijalni = graph[poslednji]
        if len(potencijalni) < 1:
            kompletni_putevi.append(put)
        else:
            for cvor in potencijalni:
                if cvor not in put:
                    nput = [*put, cvor]
                    nekompletni_putevi.put(nput)
                else:
                    nput = (*put,)
                    if (nput not in kompletni_putevi):
                        kompletni_putevi.append(nput)
    return max(map(lambda x: len(x)-1, kompletni_putevi))


zadati_graf = {
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
print(depth(zadati_graf, 'A'))
