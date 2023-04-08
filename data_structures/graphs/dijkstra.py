# Dijkstra's Algorithm in Python

# TODO: Define a Graph class with weighted directed edge using matrix
# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

## My attempt

def dijkstra(start):
    # starting point (just an index)
    # Number of vertices = N
    N = len(vertices)
    # create 2 matrices to store shortest path from point i to point j
    dist = [1e7 for i in range(N)]
    prev = [None for i in range(N)]
    queue = []
    for i in range(N):
        queue.append(i)  # add i to queue
    # set distant from the starting point to 0
    dist[start] = 0
    
    # TODO(P1): Use weighted heap
    def next_vertex(queue, dist):
        # get the vertex (index) with the shortest distance
        closest = 0
        min_dist = 1e7  # TODO(P2): Use inf
        for i in queue:
            if dist[i] < min_dist:
                min_dist = dist[i]
                closest = i
        return closest

    while queue:  # while queue is not empty
        # get the vertex (index) with the shortest distance
        u = next_vertex(queue, dist)
        # print('queue:', queue)
        # print('u:', u)
        # print('dist:', dist)
        # print('prev:', prev)
        queue.remove(u) # remove the item
        # get neighbors of u
        for v in range(N):
            if vertices[u][v] == 1:
                # only look at remaining nodes
                if v in queue:
                    # print('v:', v)
                    temp_dist = dist[u] + edges[u][v]
                    if temp_dist < dist[v]:
                        dist[v] = temp_dist
                        prev[v] = u
    print('dist:', dist)
    print('prev:', prev)

# Solution:
# https://www.programiz.com/dsa/dijkstra-algorithm

if __name__ == "__main__":
    dijkstra(0)
