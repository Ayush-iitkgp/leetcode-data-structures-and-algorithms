from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Start the BFS from (0, 0) and keep incrementing the count until you reach (n-1, n-1)
        Keep the seen set to ensure not visiting the same node again.
        """
        rows = columns = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1,), (-1, -1)]

        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < columns and grid[x][y] == 0

        print(f"rows is {rows} and columns is {columns}")

        def bfs(x, y, shortest_length):
            if grid[x][y] == 1:
                return -1
            queue = deque()
            # shortest_length = 1
            queue.append((x, y, shortest_length))
            seen = set()
            seen.add((x, y))

            while queue:
                # print(f"queue is {queue}")
                # print(f"seen is {seen}")
                x, y, shortest_length = queue.popleft()
                if x == rows-1 and y == columns-1:
                    return shortest_length
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if isValid(new_x, new_y):
                        if (new_x, new_y) in seen:
                            continue
                        else:
                            seen.add((new_x, new_y))
                            queue.append((new_x, new_y, shortest_length + 1))

            return -1

        return bfs(0, 0, 1)
