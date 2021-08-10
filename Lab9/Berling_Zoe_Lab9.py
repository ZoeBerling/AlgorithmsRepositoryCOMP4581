"""Zoe Berling Algorithms Lab 9 Greedy Shortest Path and MST"""

# Dijkstra's shortest path greedy algorithm
# Find the min priority vertex from the list of given vertices
# Each vertex in the form of a list with priority as the first
# element returns the min vertex and removes it from the list
def extractMin(verts):
    minIndex = 0
    for v in range(1,len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)
# Dijkstra's shortest path algorithm
def shortest(g, start):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    vertsToProcess[start][1] = 0  # change starting vertex

    # Start with an empty list of processed edges
    vertsProcessed = []
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        vertsProcessed.append(u)
        # print("to process:",vertsToProcess)
        # print(" processed:",vertsProcessed)
    # Examine all potential verts remaining
        for v in vertsToProcess:
        # Only care about the ones that are adjacent to u
            if g[u[0]][v[0]] > 0:
            # Update the distances if necessary
                if u[1] + g[u[0]][v[0]] < v[1]:
                    v[1] = u[1] + g[u[0]][v[0]]
    print(vertsProcessed)

# Prim's Algorithm
# Create a list of edges that form the minimum
def MST(g, start):
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    vertsToProcess[start][1] = -1 # change starting vertex

    # print(f'vertstoproces{vertsToProcess}')
    # Start with an empty list of processed edges
    #  vertsProcessed = []
    q = []

    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        #  vertsProcessed.append(u)
        q.append([u[0], u[-1]])  # take only last result
        # print("to process:", vertsToProcess)
        # print(" processed:", vertsProcessed)

        # Examine all potential verts remaining
        for v in vertsToProcess:
            # Only care about the ones that are adjacent to u
            if g[u[0]][v[0]] > 0:
                # Update the distances if necessary
                if g[u[0]][v[0]] < v[1]:
                    v[1] = g[u[0]][v[0]]
                    v.append(u[0])

    print(q)

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels:
# 2
# / \
# 3---1--7
# |\ |
# 4 | 0--6
# \|/
# 5
graph = [[0, 7, 0, 0, 0, 10, 15, 0],
[7, 0, 12, 5, 0, 0, 0, 9],
[0, 12, 0, 6, 0, 0, 0, 0],
[0, 5, 6, 0, 14, 8, 0, 0],
[0, 0, 0, 14, 0, 3, 0, 0],
[10, 0, 0, 8, 3, 0, 0, 0],
[15, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 0, 0, 0, 0, 0, 0]]
shortest(graph, 0)
shortest(graph, 2)
MST(graph, 0)
MST(graph, 7)
MST(graph, 4)