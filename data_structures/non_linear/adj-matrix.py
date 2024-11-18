class AdjMatrix:
    def __init__(self, size):
        self.graph = [[0 for j in range(size)] for i in range(size)]
        self.size = size

    def add_edge(self, vertex1, vertex2):
        has_edge = self.has_edge(vertex1, vertex2)
        if has_edge:
            print("Edge exists already.")
            return
        self.graph[vertex1][vertex2] = 1

    def remove_edge(self, vertex1, vertex2):
        if not self.has_edge(vertex1, vertex2):
            print("Edge doesn't exist.")
            return
        self.graph[vertex1][vertex2] = 0

    def dfs(self, start):
        pass

    def bfs(self, start):
        pass

    def has_edge(self, vertex1, vertex2):
        return self.graph[vertex1][vertex2] == 1

    def print_graph(self):
        for row in range(self.size):
            print(self.graph[row])

    def clear(self):
        pass
        # def add_vertex(self, vertex):
        #     pass

        # def remove_vertex(self, vertex):
        pass

    # def vertex_count(self):
    #     pass

    # def edge_count(self):
    #     pass

    # def neighbors(self):
    #     pass

    # def is_directed(self):
    #     pass


if __name__ == "__main__":
    graph = AdjMatrix(6)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 0)

    graph.print_graph()
