graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {},
}

costs = graph['A']
neighbors = graph['B']
current = graph.get('A')

print(current)
# print(costs)
# print(neighbors)
