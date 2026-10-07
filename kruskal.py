# Kruskal's Algorithm
# Practical Problem:
# Connect all company offices with minimum network cost.

edges = [
    ('A', 'B', 4),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 2),
    ('C', 'D', 4),
    ('C', 'E', 5),
    ('D', 'E', 2)
]

# Sort edges according to cost
edges.sort(key=lambda x: x[2])

# Initially, every node is its own parent
parent = {}

for u, v, cost in edges:
    parent[u] = u
    parent[v] = v


# Find the root parent of a node
def find(node):

    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


# Join two different sets
def union(u, v):

    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        parent[root_v] = root_u
        return True

    return False


mst = []
total_cost = 0

# Select edges
for u, v, cost in edges:

    if union(u, v):
        mst.append((u, v, cost))
        total_cost += cost


print("Minimum Cost Network")
print("--------------------")

for u, v, cost in mst:
    print(f"{u} - {v}: {cost}")

print("--------------------")
print(f"Total Network Cost: {total_cost}")