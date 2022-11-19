from itertools import starmap
import queue


def nivoUGrafu(graph, start):
    red = queue.PriorityQueue(-1)
    red.put((0, start))
    nivoi = dict()
    nivoi[start] = 0
    while not red.empty():
        node = red.get()
        sledeci = graph[node[1]]
        for next in sledeci:
            if nivoi.get(next) is None or nivoi[next] > nivoi[node[1]]+1:
                nivoi[next] = nivoi[node[1]]+1
                red.put((nivoi[start], next))
    return map(lambda x: (x, nivoi[x]), nivoi.keys())


def cvoroviHeuristika(graph, start):
    return starmap(lambda x, y: (x, len(graph) - y), nivoUGrafu(graph, start))


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['A', 'B'],
    'D': ['C', 'E', 'F'],
    'E': ['G', 'H', 'A'],
    'F': ['B', 'C', 'D'],
    'G': ['E', 'H'],
    'H': ['J'],
    'J': []
}

listaCvorovaHeuristika = cvoroviHeuristika(graph, 'A')
for i in listaCvorovaHeuristika:
    print(i)
