
import queue


def breadt_first(graph, start, end):
    if (start is end):
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found = False
    while (not found) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        for dest in graph[node]:
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found = True
                    break
                visited.add(dest)
                queue_nodes.put(dest)
    path = list()
    if found:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['G', 'I'],
    'F': ['J'],
    'G': ['J'],
    'H': [],
    'I': ['J'],
    'J': []
}

print(breadt_first(graph, 'A', 'G'))
