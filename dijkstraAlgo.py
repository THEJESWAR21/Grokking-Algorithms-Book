def main(graph, costs, parents, visited):
    node = find_lowest_cost_node(costs, visited)

    while node is not None:
        cost = costs[node] 
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        visited.append(node)
        node = find_lowest_cost_node(costs, visited)

def find_lowest_cost_node(costs, visited):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in visited:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

def print_shortest_path(start, target, costs, parent):
    if costs[target] == float('inf'):
        print(f"No path found from {start} to {target}")
        return

    print(f"Shortest Distance to {target}: {costs[target]}")

    path =[]
    current = target
    while current is not None:
        path.append(current)
        current = parents.get(current)

    path.reverse()
    print("Path Taken:", " -> ".join(path))

if __name__ == "__main__":
    infinity = float('inf')
    graph = {
        'A': {'B': 6, 'C': 2},
        'B': {'D': 1},
        'C': {'B': 3, 'D': 5},
        'D': {},
    }

    costs = {
        'B' : 6,
        'C' : 2,
        'D' : infinity

    }

    parents = {
        'A': None,
        'B': 'A',
        'C': 'A',
        'D': None
    }

    visited = []

    main(graph, costs, parents, visited)

    print("-- Final Shortest Distance From A ---")
    for node, distance in costs.items():
        print(f"Distance to {node}: {distance}")

    print("\n--- Detailed Path to Destination 'D' ---")
    print_shortest_path('A', 'D', costs, parents)

