from functools import reduce
import queue

# vraca udaljenost svih cvorova od end


def heuristika_udaljenost(graph, end):
    heuristika = dict()
    heuristika[end] = 0

    poseceni = set()
    poseceni.add(end)

    red = queue.Queue(len(graph))
    red.put(end)

    while not red.empty():
        node = red.get()
        for (duzina, sledeci) in graph[node]:
            if heuristika.get(sledeci) is None or heuristika[sledeci] > heuristika[node]+duzina:
                heuristika[sledeci] = heuristika[node]+duzina
                red.put(sledeci)

    return heuristika


def heuristika(graph, g1, g2):
    d1 = heuristika_udaljenost(graph, g1)
    d2 = heuristika_udaljenost(graph, g2)

    print(d1)
    print(d2)

    # d = reduce(lambda a, b: {*a, b: min(d1[b], d2[b])}, graph.keys(), dict())
    for key in graph.keys():
        graph[key] = (d1[key] if d1[key] < d2[key] else d2[key], graph[key])
    return graph


graph = {
    'A': [(4, 'B'), (2, 'D'), (3, 'C'), (7, 'F')],
    'B': [(4, 'A'), (4, 'D'), (6, 'E')],
    'C': [(3, 'A'), (5, 'F')],
    'D': [(2, 'A'), (4, 'B'), (2, 'F'), (2, 'G')],
    'E': [(6, 'B'), (2, 'G')],
    'F': [(5, 'C'), (7, 'A'), (2, 'D')],
    'G': [(2, 'E'), (2, 'D')]
}
print(heuristika(graph, 'A', 'D'))
