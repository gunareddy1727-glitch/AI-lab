from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS Traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("\nDFS Traversal:")

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# -------- USER INPUT --------
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("\nEnter starting node: ")

# -------- PRINT GRAPH --------
print("\nGraph (Adjacency List):")
for node in graph:
    print(f"{node} -> {' '.join(graph[node]) if graph[node] else 'None'}")

# -------- RUN --------
bfs(graph, start)
dfs(graph, start)
