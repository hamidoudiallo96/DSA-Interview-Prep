from collections import deque
from typing import List


class Solution:
    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        visited = set()
        province_count = 0

        def bfs(city):
            queue = deque()
            queue.append(city)
            while queue:
                city = queue.popleft()
                visited.add(city)
                for neighbor in range(n):
                    if is_connected[city][neighbor] == 1 and neighbor not in visited:
                        queue.append(neighbor)

        for i in range(n):
            if i not in visited:
                province_count += 1
                bfs(i)

        return province_count


def main():
    g1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    g2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    sol1 = Solution().find_circle_num(g1)  # 2 connected components
    sol2 = Solution().find_circle_num(g2)  # 3 connected components

    print(f"Solution1: {sol1}, Solution2: {sol2}")


if __name__ == "__main__":
    main()
