def main(graph):
    ...


if __name__ == "__main__":
    graph = {
        'A': {'B': 6, 'C': 2},
        'B': {'D': 1},
        'C': {'B': 3, 'D': 5},
        'D': {},
    }
    main(graph)

