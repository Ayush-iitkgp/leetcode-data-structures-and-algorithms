from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """Start the DFS from node 0, and do not add the restricted noodes
        to the stack for visiting them later, keep track of all the nodes visited
        and return the final count
        """
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        print(f"graph is {graph}")

        # count = 0
        seen = set()
        stack = list()
        restricted_set = set(x for x in restricted)
        print(f"restricted_set is {restricted_set}")

        def dfs(node):
            count = 1
            stack.append(node)
            seen.add(node)
            while stack:
                for neighbor in graph[node]:
                    if neighbor in seen:
                        continue
                    if neighbor in restricted_set:
                        continue
                    count += 1
                    stack.append(neighbor)
                    seen.add(neighbor)
            return count

        return dfs(0)
