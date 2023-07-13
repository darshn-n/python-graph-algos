import sys


def prim(graph, V):
    mst = []
    visited = [False] * V
    key = [sys.maxsize] * V

    key[0] = 0

    for _ in range(V):
        u = min_key(key, visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                mst.append((u, v))

    return mst


def min_key(key, visited):
    min_val = sys.maxsize
    min_index = -1

    for v in range(len(key)):
        if not visited[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index


# Example usage:
V = 5
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]


mst = prim(graph, V)

print("Minimum Spanning Tree:")
for u, v in mst:
    print(u, "--", v)