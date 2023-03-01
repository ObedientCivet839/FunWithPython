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
        self._outgoing = {}
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
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    
