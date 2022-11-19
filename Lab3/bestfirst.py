import queue


def best_first(graph, start, end):
    if start is end:
        return [start]
    pqueue = queue.PriorityQueue(len(graph))
    visited = set()
    prev = dict()
    prev[start] = None
    visited.add(start)
    pqueue.put((graph[start][0], start))
    found = False
    while (not found) and (not pqueue.empty()):
        node = pqueue.get()  # (H, CVOR)
        for dest in graph[node[1]][1]:
            prev[dest] = node[1]
            if dest is end:
                found = True
                break
            visited.add(dest)
            pqueue.put((graph[dest][0], dest))
    path = list()
    if found:
        path.append(end)
        prev_node = prev[end]
        while prev_node is not None:
            path.append(prev_node)
            prev_node = prev[prev_node]
        path.reverse()
    return path


graph = {
    'A': (9, ['B', 'C']),
    'B': (6, ['D', 'E']),
    'C': (7, ['F', 'G']),
    'D': (4, ['H']),
    'E': (8, ['G', 'I']),
    'F': (3, ['J']),
    'G': (4, ['J']),
    'H': (4, []),
    'I': (3, ['J']),
    'J': (0, [])
}

print(best_first(graph, 'A', 'J'))
