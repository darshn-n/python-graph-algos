import sys


def bellman_ford(graph, source):
    V = len(graph)
    dist = [sys.maxsize] * V
    dist[source] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != 0:
                    dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist


# Example usage:
graph = [
    [0, -1, 4, 0, 0],
    [0, 0, 3, 2, 2],
    [0, 0, 0, 0, 0],
    [0, 1, 5, 0, 0],
    [0, 0, 0, -3, 0],
]

source = 0
distances = bellman_ford(graph, source)

print("Shortest distances from source vertex", source)
for i, distance in enumerate(distances):
    print("Vertex", i, ":", distance)
