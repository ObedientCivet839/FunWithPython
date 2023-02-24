from graph import DirectedGraph

class GraphSearch():
    def __init__(self, graph: DirectedGraph):
        self.graph = graph
    
    def BFS(self, startVertex):
        # Create a list (queue) to store all vertices for BFS
        queue = [startVertex]
        res = []

        visited = set()
        visited.add(startVertex)

        while queue:
            v = queue.pop(0)
            res.append(v)

            for n in self.graph.neighbors[v]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
        return res
