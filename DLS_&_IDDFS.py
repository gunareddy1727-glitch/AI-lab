def dls(graph, node, goal, depth, visited):
    if node == goal:
        return True
    if depth == 0:
        return False

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False


def iddfs(graph, start, goal):
    # Dynamic max depth → number of nodes (safe upper bound)
    max_depth = len(graph)

    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        visited = set()
        if dls(graph, start, goal, depth, visited):
            return True

    return False


# -------- USER INPUT --------
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# -------- RUN --------
if iddfs(graph, start, goal):
    print("Goal found!")
else:
    print("Goal not found.")
