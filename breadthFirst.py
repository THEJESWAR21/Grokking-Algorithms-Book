from collections import deque

graph = {
    'You': ["Alice", "Bob", "Claire"],
    'Bob': ["Anuj", "Peggy"],
    'Alice': ["Peggy"],
    'Claire': ["Thom", "Jonny"],
    'Anuj': [],
    'Peggy': [],
    'Thom': [],
    'Jonny': [],
}

visted = [] # To Prevent infinite loops
queue = [] # FIFO

def bfs(visted, graph, node):
    visted.append(node)
    queue.append(node) 

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visted:
                if neighbour == "Jonny":
                    visted.append(neighbour)
                    
                else:
                    visted.append(neighbour)
                    queue.append(neighbour)

# print("Following is the Breath First Search")
# bfs(visted, graph , "You")

def bfs_path(graph, start, target):
    # check if both start and target exist
    if start not in graph or target not in graph:
        return None

    if start == target:
        return [start]

    queue = deque([start])

    parent_map = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = parent_map[current]
            return path[::-1] # Reverse the path to get Start -> Target


        for neighbour in graph[current]:
            if neighbour not in parent_map:
                parent_map[neighbour] = current
                queue.append(neighbour)

    return None

start_node = "You"
target_node = "Jonny"

shortest_path = bfs_path(graph, start_node, target_node)
print(f"Shortest Path from {start_node} to {target_node}: {shortest_path}")

