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

    def DFS(self, startVertex):
        # Create a list (stack) to store all vertices for BFS
        stack = [startVertex]
        res = []

        visited = set()
        visited.add(startVertex)

        while stack:
            # remove from the end of the list (i.e. top of the stack)
            v = stack.pop()
            res.append(v)

            for n in self.graph.neighbors[v]:
                if n not in visited:
                    # append to the end of the list (i.e. top of the stack)
                    stack.append(n)
                    visited.add(n)
        return res

    def detectCycle(self):
        visited = set()
        for v in self.graph.neighbors.keys():
            if self.detectCycleHelper(v, visited):
                return True
        return False

    def detectCycleHelper(self, v, visited):
        """Detects if there is a cycle includes node v."""
        if v in visited:
            return True
        visited.add(v)
        if v in self.graph.neighbors:
            for n in self.graph.neighbors[v]:
                if self.detectCycleHelper(n, visited):
                    return True
                visited.remove(n)
        return False
