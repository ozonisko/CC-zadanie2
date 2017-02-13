from collections import defaultdict, deque
import sys


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination] + matrix[0]  # must add first element coz its not an edge
    # return visited[destination] + matrix[0], list(full_path) # optional list of nodes


def make_graph(n_size, full_matrix):
    size = n_size
    matrix2 = full_matrix
    graph = Graph()
    for node in range(1, len(matrix2) + 1):  # nodes names 1, 2, 3 ...
        graph.add_node(node)
    for node in range(1, len(matrix2) + 1):
        if node % size:  # adding horizontal edges
            graph.add_edge(node, node + 1, matrix2[node])
        if node <= len(matrix2) - size:  # adding vertical edges
            graph.add_edge(node, node + size, matrix2[node + size - 1])
    print(shortest_path(graph, 1, len(matrix2)))


if __name__ == '__main__':
    matrix = []
    n = None
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            data = file.readlines()
        data = [x.strip().split(',') for x in data]
        counter = - 1
        for line in data:
            if counter <= 0:
                if counter == 0:  # the matrix has all rows
                    matrix = list(map(int, matrix))
                    make_graph(n, matrix)  # send complete matrix to compute shortest path
                matrix = list()  # cleaning
                counter = int(line[0])  # how many rows in matrix
                n = counter  # copy number of rows to send to the function
            else:
                matrix.extend(line)  # matrix is extended by rows of values
                counter -= 1
        matrix = list(map(int, matrix))
        make_graph(n, matrix)
    else:
        print("There is no input file to process.")
