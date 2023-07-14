import sys


def prim(graph, src):
    mst = []
    V = len(graph)
    visited = [False] * V
    dist = [sys.maxsize] * V

    dist[src] = 0

    for _ in range(V):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                mst.append((u, v))

    return mst


def min_distance(dist, visited):
    min_dist = sys.maxsize
    min_index = -1

    for v in range(len(dist)):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_index = v

    return min_index


# Example usage:
src = 0
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

# graph = [
#     [0, 4, 0, 0, 0],
#     [4, 0, 8, 0, 0],
#     [0, 8, 0, 7, 9],
#     [0, 0, 7, 0, 10],
#     [0, 0, 9, 10, 0],
# ]

mst = prim(graph, src)

print("Minimum Spanning Tree:")
for u, v in mst:
    print(u, "--", v)
