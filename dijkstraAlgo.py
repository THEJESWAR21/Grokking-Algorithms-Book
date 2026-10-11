def main(graph, costs, parents, visited):
    # Find the Lowest Cost Node : C
    node = find_lowest_cost_node(costs, visited)

    while node is not None:
        cost = costs[node] # Return the Cost of the Node : 2
        neighbors = graph[node] # Returns all Neigbours like ['B': 3, 'D': 5]

        for n in neighbors.keys(): # ['B', 'D']
            new_cost = cost + neighbors[n] # 2 + 3 = 5
            if costs[n] > new_cost: # 3 > 5
                costs[n] = new_cost # Replace the Cost of that node
                parents[n] = node # Replace the parent 
        visited.append(node) # Keep track of visited Nodes
        node = find_lowest_cost_node(costs, visited) # Find the next Node

def find_lowest_cost_node(costs, visited):
    lowest_cost = float("inf") # Infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node] # Return the value of costs
        if cost < lowest_cost and node not in visited:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

def print_shortest_path(start, target, costs, parent):
    if costs[target] == float('inf'):
        print(f"No path found from {start} to {target}")
        return

    print(f"Shortest Distance to {target}: {costs[target]}") # Return the Shortest Distance to Target

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parents.get(current) # Get the Neighbors and append it 

    path.reverse() # Reverse the String to go from Start to Target
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
