# Prim's Algorithm
# Practical Problem:
# Connect all university buildings using minimum cable length.

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5, 'E': 6},
    'D': {'B': 4, 'C': 5, 'E': 2},
    'E': {'C': 6, 'D': 2}
}

visited = set()
start = 'A'

visited.add(start)

mst = []
total_cost = 0

while len(visited) < len(graph):

    min_edge = None
    min_cost = float('inf')

    for u in visited:
        for v in graph[u]:

            if v not in visited and graph[u][v] < min_cost:
                min_cost = graph[u][v]
                min_edge = (u, v)

    u, v = min_edge

    visited.add(v)
    mst.append((u, v, min_cost))
    total_cost += min_cost


print("Minimum Cable Connections")
print("-------------------------")

for u, v, cost in mst:
    print(f"{u} - {v}: {cost} meters")

print("-------------------------")
print(f"Total Cable Required: {total_cost} meters")