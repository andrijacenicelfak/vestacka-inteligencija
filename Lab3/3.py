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
listaNivoa = nivoUGrafu(graph, 'A')
for i in listaNivoa:
    print(i)
