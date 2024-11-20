from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D', 'E'])
g.add_edge('C', ['A', 'D'])
g.add_edge('D', ['B', 'C'])
g.add_edge('E', ['B'])

bfs(g.graph, 'A')