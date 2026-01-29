from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        columns = len(maze[0])

        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < columns and maze[x][y] == "."

        def isBorder(x, y):
            return x == 0 or x == rows - 1 or y == 0 or y == columns - 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(x, y):
            steps = 0
            seen = set()
            seen.add((x, y))
            queue = deque()
            queue.append((x, y, steps))
            while queue:
                # print(f"queue is {queue}")
                # print(f"seen is {seen}")
                x, y, steps = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    # print(f"new_x is {new_x} and new_y is {new_y}")
                    if isValid(new_x, new_y) and (new_x, new_y) not in seen:
                        if isBorder(new_x, new_y):
                            return steps + 1
                        seen.add((new_x, new_y))
                        queue.append((new_x, new_y, steps + 1))

            return -1
            # return steps

        return bfs(entrance[0], entrance[1])

# maze = [["+","+","+"],[".",".","."],["+","+","+"]]
# entrance = [1,0]
# print(Solution().nearestExit(maze, entrance))
