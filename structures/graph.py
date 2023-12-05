class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.graph and to_node in self.graph:
            self.graph[from_node].append(to_node)
        else:
            print("Invalid edge")

    def display(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))
