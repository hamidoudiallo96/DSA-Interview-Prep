# LC 547. Number of Provinces
# Union-Find Implementation
from typing import List


class UnionFind:
    def __init__(self, vertex_count):
        self.parent = self.make_set(vertex_count)
        self.rank = [1] * vertex_count
        self.count = vertex_count

    def make_set(self, vertex_count):
        return [x for x in range(vertex_count)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        node1 = self.find(x)
        node2 = self.find(y)

        if node1 == node2:
            return

        if self.rank[node1] > self.rank[node2]:
            self.parent[node2] = self.parent[node1]
            self.rank[node1] += 1
        else:
            self.parent[node1] = self.parent[node2]
            self.rank[node2] += 1

        self.count -= 1


class Solution:
    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        uf = UnionFind(len(is_connected))

        for i in range(len(is_connected)):
            for j in range(len(is_connected)):
                if is_connected[i][j] == 1:
                    uf.union(i, j)

        return uf.count


def main():
    g1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    g2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    sol1 = Solution().find_circle_num(g1)  # 2 connected components
    sol2 = Solution().find_circle_num(g2)  # 3 connected components

    print(f"Solution1: {sol1}, Solution2: {sol2}")


if __name__ == "__main__":
    main()
