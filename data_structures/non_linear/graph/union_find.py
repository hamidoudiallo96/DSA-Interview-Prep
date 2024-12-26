class UnionFind:
    def __init__(self, size: int):
        self.parent = self.make_set(size)
        self.rank = [1] * size
        self.count = size

    def make_set(self, vertex_count: int):
        return [x for x in range(vertex_count)]

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int):
        vertex1 = self.find(x)
        vertex2 = self.find(y)

        if vertex1 == vertex2:
            return

        if self.rank[vertex1] > self.rank[vertex2]:
            self.parent[vertex2] = self.parent[vertex1]
            self.rank[vertex1] += 1
        else:
            self.parent[vertex1] = self.parent[vertex2]
            self.rank[vertex2] += 1

        self.count -= 1


def main():
    edges = [[0, 2], [1, 4], [1, 5], [2, 3], [2, 7], [4, 8], [5, 8]]

    number_of_edges = 9
    union_find = UnionFind(number_of_edges)

    for vertex1, vertex2 in edges:
        union_find.union(vertex1, vertex2)

    print(f"Number of Connected Components is {union_find.count}.")


if __name__ == "__main__":
    main()
