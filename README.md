# Graph Algorithms in Python

This contains Python implementations of three important graph algorithms:

- Prim's Algorithm
- Kruskal's Algorithm
- Dijkstra's Algorithm

The algorithms are demonstrated using practical real-life problems.

## Algorithms and Applications

| Algorithm            | Purpose               | Real-Life Application                                |
| -------------------- | --------------------- | ---------------------------------------------------- |
| Prim's Algorithm     | Minimum Spanning Tree | Connecting university buildings with minimum cable   |
| Kruskal's Algorithm  | Minimum Spanning Tree | Connecting company offices with minimum network cost |
| Dijkstra's Algorithm | Shortest Path         | Finding the shortest route between locations         |

---

## 1. Prim's Algorithm

### Problem

A university wants to connect all of its buildings using network cables. The goal is to connect every building while using the minimum total cable length.

### Concept

Prim's Algorithm constructs a Minimum Spanning Tree (MST). It starts from a selected vertex and repeatedly selects the minimum-weight edge that connects a visited vertex to an unvisited vertex.

### File

`prims.py`

### Sample Result

```text
Minimum Cable Connections
-------------------------
A - B: 2 meters
B - C: 1 meters
B - D: 4 meters
D - E: 2 meters
-------------------------
Total Cable Required: 9 meters
```

### Time Complexity

```text
O(V²)
```

---

## 2. Kruskal's Algorithm

### Problem

A company wants to connect all of its offices through a network. Each possible connection has a different installation cost. The goal is to connect every office with minimum total cost.

### Concept

Kruskal's Algorithm constructs a Minimum Spanning Tree by sorting all edges according to their weights and selecting the smallest edge that does not create a cycle.

### File

`kruskal.py`

### Sample Result

```text
Minimum Cost Network
--------------------
B - C: 1
B - D: 2
D - E: 2
A - C: 3
--------------------
Total Network Cost: 8
```

### Time Complexity

```text
O(E log E)
```

---

## 3. Dijkstra's Algorithm

### Problem

A person wants to travel from location A to other locations using roads with different distances. The goal is to find the shortest possible distance from location A.

### Concept

Dijkstra's Algorithm finds the shortest distance from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

### File

`dijkstra.py`

### Sample Result

```text
Shortest Distances from A
-------------------------
A -> A: 0
A -> B: 3
A -> C: 2
A -> D: 8
A -> E: 10
```

### Time Complexity

```text
O(V²)
```

---

## Comparison

| Feature                        | Prim's         | Kruskal's      | Dijkstra's    |
| ------------------------------ | -------------- | -------------- | ------------- |
| Main purpose                   | MST            | MST            | Shortest Path |
| Finds minimum total connection | Yes            | Yes            | No            |
| Finds shortest route           | No             | No             | Yes           |
| Weighted graph                 | Yes            | Yes            | Yes           |
| Negative edge weights          | Not relevant   | Can handle     | No            |
| Common application             | Network design | Network design | GPS / Routing |

---

## How to Run

Make sure Python 3 is installed.

### Prim's Algorithm

```bash
python prims.py
```

### Kruskal's Algorithm

```bash
python kruskal.py
```

### Dijkstra's Algorithm

```bash
python dijkstra.py
```

---

## Project Structure

```text
alg/
│
├── prims.py
├── kruskal.py
├── dijkstra.py
└── README.md
```

---

## Technologies Used

- Python 3
- Graph Algorithms
- Data Structures

## Author

**Nidhi**

Computer Science and Engineering Student
