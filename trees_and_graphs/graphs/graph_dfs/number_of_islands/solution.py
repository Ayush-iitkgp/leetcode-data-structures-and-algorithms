from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(x: int, y: int) -> bool:
            # print(x, y)
            return 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == "1"

        def dfs(row: int, col: int) -> None:
            # seen = set()
            stack = list()
            stack.append((row, col))
            while stack:
                node = stack.pop()
                seen.add((node[0], node[1]))
                # print(node[0], node[1])
                for dx, dy in directions:
                    x, y = node[0] + dx, node[1] + dy
                    if isValid(x, y) and (x, y) not in seen:
                        stack.append((x, y))
            # print(row, col, seen)

        seen = set()
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    count += 1
        return count
