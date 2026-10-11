def main(graph, costs, parents, visted):
    node = find_lowest_cost_node(costs) # Find the node with the lowest cost

    # if all nodes are visted node becomes None 
    while node is not None:
        # Find the cost and neighbor of that node
        cost = costs[node] 
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        visted.append(node)
        node = find_lowest_cost_node(costs)
        print(node)

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in visted:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


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

    visted = []

    main(graph, costs, parents, visted)

