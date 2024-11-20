from collections import deque


class AdjList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = self.build_graph()

    def build_graph(self):
        graph = {}
        for vertex in self.vertices:
            graph[vertex] = set()
        return graph

    def size(self):
        return len(self.vertices)

    def add_vertex(self, vertex):
        if vertex in self.graph:
            print("The vertex already exists.")
            return
        self.graph[vertex] = set()

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            print("The vertex doesn't exist.")
            return
        del self.graph[vertex]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            print("Vertex doesn't exist")
            return
        neighbors = self.neighbors(vertex1)

        if vertex2 in neighbors:
            print("Edges already exists.")
            return

        self.graph[vertex1].add(vertex2)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            print("Vertex doesn't exist")
            return
        neighbors = self.neighbors(vertex1)

        if vertex2 not in neighbors:
            print("Edges doesn't exists.")
            return

        self.graph[vertex1].remove

    def neighbors(self, vertex):
        neighbors = []
        for neighbor in self.graph[vertex]:
            neighbors.append(neighbor)

        return neighbors

    def dfs_recur(self, source):
        visited = set()

        def dfs(vertex):
            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(source)
        print()

    def dfs_iter(self, source):
        stack = [source]
        visited = set()

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
        print()

    def bfs(self, source):
        queue = deque([source])
        visited = set()

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=", ")
                visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
        print()

    def is_connected(self):
        visited = set()
        path = []

        def dfs(vertex):
            if vertex not in visited:
                path.append(vertex)
                visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(list(self.graph.keys())[0])
        return len(path) == self.size()

    def edge_count(self):
        count = 0

        for vertex in self.vertices:
            count += len(self.graph[vertex])

        return count

    def find_path(self, start, end):
        visited = set()
        path = []

        def dfs(current, target):
            path.append(current)
            visited.add(current)

            if current == target:
                return True

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    if dfs(neighbor, target):
                        return True

            path.pop()
            return False

        path_exists = dfs(start, end)

        return True if path_exists else False

    def is_cyclic(self):
        visited = set()
        path = set()

        def dfs(current, parent=None):
            path.add(current)
            visited.add(current)

            for neighbor in self.graph[current]:
                if current == parent:
                    continue
                if neighbor in path:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor, current):
                        return True

            path.pop()
            return False

        for vertex in self.vertices:
            if vertex not in visited:
                if dfs(vertex):
                    return True
                else:
                    return False

    def print_graph(self):
        for vertex, neighbor in self.graph.items():
            print(f"Vertex: {vertex}, Neighbors: {neighbor}")

    def clear(self):
        self.graph.clear()


if __name__ == "__main__":
    graph = AdjList(["A", "B", "C", "D", "E", "F"])
    graph.build_graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "C")
    graph.add_edge("F", "A")

    is_connected = graph.is_connected()
    edge_count = graph.edge_count()
    path_exists = graph.find_path("A", "E")
    cycle_exists = graph.is_cyclic()

    print(f"is_connected: {is_connected}")
    print(f"edge_count: {edge_count}")
    print(f"path_exists: {path_exists}")
    print(f"cycle_exists: {cycle_exists}")

    graph.dfs_recur("A")
    graph.dfs_iter("A")
    graph.bfs("A")
    graph.print_graph()
