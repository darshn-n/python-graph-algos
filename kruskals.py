def kruskal(graph):
    V = len(graph)
    mst = []
    edges = []

    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]

    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            mst.append(edge)
            union(parent, u, v)

    return mst


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, i, j):
    parent[find(parent, j)] = find(parent, i)


# Example usage:
# graph = [
#     [0, 4, 0, 0, 0],
#     [4, 0, 8, 0, 0],
#     [0, 8, 0, 7, 9],
#     [0, 0, 7, 0, 10],
#     [0, 0, 9, 10, 0],
# ]

# graph = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0],
# ]


graph = [
    [0, 1, 2, 0],
    [1, 0, 3, 2],
    [2, 3, 0, 1],
    [0, 2, 1, 0],
]
mst = kruskal(graph)

print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} \t{weight}")
