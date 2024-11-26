from typing import List


class Solution:
    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        visited = set()
        province_count = 0

        def dfs(current):
            visited.add(current)

            for neighbor in range(n):
                if is_connected[current][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                dfs(city)
                province_count += 1

        return province_count


def main():
    g1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    g2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    sol1 = Solution().find_circle_num(g1)  # 2 connected components
    sol2 = Solution().find_circle_num(g2)  # 3 connected components

    print(f"Solution1: {sol1}, Solution2: {sol2}")


if __name__ == "__main__":
    main()
