class Vertex:
    """Lightweight vertex structure for a graph."""
    def __init__(self, x):
        """Do not call constructure directly. Use Graph's insert_vertex(x)."""
        self._val = x
    
    def value(self):
        """Return value associated with this vertex."""
        return self._val
    
    def __hash__(self): # allow vertext to be a map/set key
        return hash(id(self))

class Edge:
    """Lightweight edge structure for a graph."""
    def __init__(self, f, t, v):
        self._from = f # from
        self._to = t # to
        self._val = v
    
    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._from, self._to)
    
    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        return self._to if v is self._from else self._to
    
    def value(self):
        """Return value associate with this edge."""
        return self._val
    
    def __hash__(self): # allow edge to be a map/set key
        return hash((self._from, self._to))

class Graph:
    """"Representation of a simple graph using an adjacency map."""
    def __init__(self, directed=False):
        """Create an empty graph (undirected by default).
        
        Graph is directed if optional parameter is set to True.
        """
        self._outgoing = {}  # dict from [vertex] -> [vertex] -> [edge]
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing # directed if maps are distinct
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()
    
    def edge_count(self):
        """Return the number of edges in the graph."""
        # Count the number of outgoing edges
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to the resulting set
        return result
    
    def get_edge(self, u, v):
        """Return the edge from u to v, or None of not adjacent."""
        return self._outgoing[u].get(v)  # Get the outgoing edges of u, and pick v
    
    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    
    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e
    
    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    @classmethod
    def graph_from_matrix(cls, vertices, edges, directed=False):
        """Create a Graph from vertices and edges matrices.

        Args:
            vertices (list[list[int]]): vertice matrix
            edges (list[list[int]]): edge matrix
        """
        # TODO(P2): Check if the graph is directed based on the content of vertices
        g = Graph(directed)
        

# TODO(P1): Implement adjacent list constructor
# TODO(P1): Graph the matrix
        
