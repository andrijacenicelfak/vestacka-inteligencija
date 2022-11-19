
import queue


def planinarenje(graph, start, end):
    if (start is end):
        return [start]
    prev = dict()
    prev[start] = None
    stack = queue.LifoQueue(len(graph))
    stack.put(start)
    visited = set()
    visited.add(start)
    found = False
    while (not found) and (not stack.empty()):
        node = stack.get()
        destinations = list()
        for dest in graph[node][1]:
            destinations.append((graph[dest][0], dest))
        for dest in sorted(destinations, reverse=True):
            if dest[1] not in visited:
                prev[dest[1]] = node
                if dest[1] is end:
                    found = True
                    break
                visited.add(dest[1])
                stack.put(dest[1])
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
print(planinarenje(graph, 'A', 'J'))
