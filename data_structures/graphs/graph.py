# TODO(P1): UndirectedGraph

# TODO(P2): WeightedGraph

# TODO(P3): Use Generics

class DirectedGraph():
    def __init__(self):
        # Map from a vertex to its neighbors (as adjacency lists)
        self.neighbors = {}

    def __str__(self):
        res = ""
        for v in self.neighbors.keys():
            res += str(v) + " -> " + ", ".join([str(n) for n in self.neighbors[v]]) + "\n"
        return res

    def addEdge(self, a, b):
        # Add a new edge from a to b
        if a in self.neighbors:
            self.neighbors[a].append(b)
        else:
            self.neighbors[a] = [b]
