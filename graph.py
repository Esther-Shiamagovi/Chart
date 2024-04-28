
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def __str__(self):
        return str(self.graph)
    
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
print("Graph as an adjacency list:")
print(g)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.graph])
    
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("Graph as an adjacency matrix:")
print(g)


class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def __str__(self):
        return str(self.graph)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
print("Graph as an adjacency list:")
print(g)
