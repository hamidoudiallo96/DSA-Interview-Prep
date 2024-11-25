from collections import deque


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

    def dfs_recur(self, source):
        visited = set()

        def dfs(vertex):
            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in range(self.size - 1, -1, -1):
                if self.graph[vertex][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        dfs(source)

    def dfs_iter(self, source):
        stack = [source]
        visited = set()

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in range(self.size - 1, -1, -1):
                if self.graph[vertex][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    def bfs(self, source):
        queue = deque([source])
        visited = set()

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in range(self.size):
                if self.graph[vertex][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)

    def has_edge(self, vertex1, vertex2):
        return self.graph[vertex1][vertex2] == 1

    def print_graph(self):
        for row in range(self.size):
            print(self.graph[row])

    def neighbors(self, vertex):
        neighbors = []

        for neighbor in range(self.size):
            if self.graph[vertex][neighbor] == 1:
                neighbors.append(neighbor)

        return neighbors

    def is_connected(self):
        visited = set()

        def dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)

            if vertex in visited:
                return True

            for neighbor in range(self.size - 1, -1, -1):
                if self.graph[vertex][neighbor] == 1:
                    dfs(neighbor)

        return dfs(0) or False


if __name__ == "__main__":
    graph = AdjMatrix(6)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(4, 2)
    graph.add_edge(5, 0)
    graph.print_graph()

    print("Depth First Search Iter")
    graph.dfs_iter(0)
    print("\nDepth First Search Recur")
    graph.dfs_recur(0)

    print("\nBreadth First Search")
    graph.bfs(0)
    print()

    print(graph.neighbors(2))
    print(graph.is_connected())
