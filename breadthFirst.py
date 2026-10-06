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
                visted.append(neighbour)
                queue.append(neighbour)

print("Following is the Breath First Search")
bfs(visted, graph , "You")
