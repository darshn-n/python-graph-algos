import sys


def dijkstra(graph, source):
    V = len(graph)
    dist = [sys.maxsize] * V
    dist[source] = 0
    visited = [False] * V

    for _ in range(V):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


def min_distance(dist, visited):
    V = len(dist)
    min_dist = sys.maxsize
    min_index = -1

    for v in range(V):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_index = v

    return min_index


# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

source = 0
distances = dijkstra(graph, source)

print("Shortest distances from source vertex", source)
for i, distance in enumerate(distances):
    print("Vertex", i, ":", distance)
