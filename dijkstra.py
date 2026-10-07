# Dijkstra's Algorithm
# Practical Problem:
# Find the shortest route from location A to all other locations.

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

# Set initial distance as infinity
distance = {}

for node in graph:
    distance[node] = float('inf')

# Distance from A to A is 0
distance['A'] = 0

visited = set()

while len(visited) < len(graph):

    current = None
    min_distance = float('inf')

    # Find the unvisited node with minimum distance
    for node in graph:

        if node not in visited and distance[node] < min_distance:
            min_distance = distance[node]
            current = node

    visited.add(current)

    # Update distances of neighbouring nodes
    for neighbor in graph[current]:

        new_distance = distance[current] + graph[current][neighbor]

        if new_distance < distance[neighbor]:
            distance[neighbor] = new_distance


print("Shortest Distances from A")
print("-------------------------")

for node in distance:
    print(f"A -> {node}: {distance[node]}")