from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        1. Construct the graph hashmap
        2. Start the dfs from source vertex and if at the end of the dfs destination
        vertex is part of the seen set then there is a path from source to destination
        """
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        stack = list()
        seen = set()

        def dfs(source, destination):
            if source == destination:
                return True
            print(f"dfs stating from the node {source}")
            stack.append(source)
            seen.add(source)
            while stack:
                # print(f"current stack is {stack}")
                # print(f"current see is {seen}")
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor == destination:
                        return True
                    if neighbor in seen:
                        continue
                    stack.append(neighbor)
                    seen.add(neighbor)
            return False
        return dfs(source, destination)
