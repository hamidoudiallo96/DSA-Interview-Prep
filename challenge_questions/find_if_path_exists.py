# Grokking Graph Problem 2: Number of Provinces (medium)

from collections import defaultdict


def build_graph(n, edges):
    graph = defaultdict(set)

    for vertex1, vertex2 in edges:
        graph[vertex1].add(vertex2)
        graph[vertex2].add(vertex1)

    return graph


class Solution:
    def valid_path(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        # base case
        if n <= 1:
            return start == end

        graph = build_graph(n, edges)
        visited = set()

        def dfs(current):
            if current == end:
                return True

            visited.add(current)

            for neighbor in graph[current]:
                if neighbor == end:
                    return True
                elif neighbor not in visited and dfs(neighbor):
                    return True

            return False

        return dfs(start)


if __name__ == "__main__":
    sol = Solution()
    print(sol.valid_path(4, [[0, 1], [1, 2], [2, 3]], 0, 3))  # true
    print(sol.valid_path(4, [[0, 1], [2, 3]], 0, 3))  # false
    print(sol.valid_path(5, [[0, 1], [3, 4]], 0, 4))  # false
