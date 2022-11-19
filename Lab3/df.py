
import queue


def depth_first(graph, start, end):
    if start == end:
        rez = list()
        rez.append(start)
        return rez
    stack = queue.LifoQueue(len(graph))
    visited = set()
    prev = dict()
    prev[start] = None
    visited.add(start)
    stack.put(start)
    found = False

    while (not found) and (not stack.empty()):
        node = stack.get()
        for dest in graph[node]:
            prev[dest] = node
            if dest is end:
                found = True
                break
            visited.add(dest)
            stack.put(dest)
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

print(depth_first(graph, 'A', 'J'))
