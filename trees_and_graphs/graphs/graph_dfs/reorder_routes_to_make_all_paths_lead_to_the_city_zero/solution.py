from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        1. Assume that the graph is undirected this means that the entire undirected graph is connected
        2. construct an hashmap representing the graph
        3. Since the graph is connected, we can definitely say that all the nodes are accessible for any
        other nodes including node "0"
        4. Start DFS from node 0 in the undirected graph
        5. If the edge from exist from neighbor of 0 to node 0 than the swap is not required else
        it is required and hence increment the counter
        """
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            global ans
            print(f"current ans is {ans}")
            stack.append(node)
            while stack:
                node = stack.pop()
                seen.add(node)
                print(f"Node current being visited in {node}")
                for neighbor in graph[node]:
                    if neighbor in seen:
                        continue
                    if [neighbor, node] not in connections:
                        ans += 1
                    stack.append(neighbor)
        seen = set()
        global ans
        ans = 0
        stack = list()
        dfs(0)
        return ans
