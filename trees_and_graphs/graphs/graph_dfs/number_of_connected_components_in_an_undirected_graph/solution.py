from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Similar to number of provinces
        """
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        count = 0
        stack = list()

        def dfs(node):
            stack.append(node)
            seen.add(node)
            while stack:
                node = stack.pop()

                for neighor in graph[node]:
                    if neighor in seen:
                        continue
                    stack.append(neighor)
                    seen.add(neighor)

        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count
