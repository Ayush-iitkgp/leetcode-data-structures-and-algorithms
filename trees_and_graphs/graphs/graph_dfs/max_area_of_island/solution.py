from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Start dfs from any node whose value is 1 and find the aread of the island from that node
        Similarly, do a DFS for each starting point and find the max of the area.
        Use seen set to avoid duplicate DFS
        """
        ans = 0
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows = len(grid)
        columns = len(grid[0])

        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < columns and grid[x][y] == 1

        def dfs(node):
            stack = list()
            area = 1
            stack.append(node)
            seen.add(node)
            while stack:
                x, y = stack.pop()
                # area += 1
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if isValid(new_x, new_y):
                        if (new_x, new_y) not in seen:
                            area += 1
                            stack.append((new_x, new_y))
                            seen.add((new_x, new_y))
                            # stack is
                            print(f" starting point is {node} and area {area}")
            print(f"area of the node starting with {node} is {area}")
            return area

        for i in range(rows):
            for j in range(columns):
                if (i, j) not in seen and grid[i][j] == 1:
                    ans = max(ans, dfs((i, j)))
        return ans
