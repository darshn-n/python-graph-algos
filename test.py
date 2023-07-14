import sys


def prim(adj_matrix):
    num_vertices = len(adj_matrix)
    key = [sys.maxsize] * num_vertices  # Initialize key values with infinite values
    parent = [-1] * num_vertices  # Initialize parent values with -1
    mst_set = [False] * num_vertices  # Initialize MST set

    # Start with the first vertex
    key[0] = 0  # Set the key value of the starting vertex as 0
    parent[0] = -1  # Set the parent of the starting vertex as -1

    for _ in range(num_vertices):
        # Find the vertex with the minimum key value from the vertices not yet included in the MST set
        min_key = sys.maxsize
        min_key_vertex = -1

        for v in range(num_vertices):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                min_key_vertex = v

        # Add the selected vertex to the MST set
        mst_set[min_key_vertex] = True

        # Update key values and parent values of the adjacent vertices
        for v in range(num_vertices):
            if (
                adj_matrix[min_key_vertex][v] > 0
                and not mst_set[v]
                and adj_matrix[min_key_vertex][v] < key[v]
            ):
                key[v] = adj_matrix[min_key_vertex][v]
                parent[v] = min_key_vertex

    return parent


# Example usage
adj_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

parent = prim(adj_matrix)

# Print the minimum spanning tree
for v in range(1, len(parent)):
    print(f"Edge: {parent[v]} - {v}")
