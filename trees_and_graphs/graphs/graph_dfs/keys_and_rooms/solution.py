from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Start dfs traversal from node 0, if after the dfs all the nodes have been
        visited then we can say that all the rooms can be unlocked else not
        """
        graph = defaultdict(list)
        # print(rooms)

        for i in range(len(rooms)):
            print(i)
            for x in rooms[i]:
                graph[i].append(x)

        print(f"graph is {graph}")
        stack = []
        seen = set()

        def dfs(node):
            stack.append(node)
            # seen.add(node)
            while stack:
                print(f"current stack is {stack}")
                print(f"current seen is {seen}")
                node = stack.pop()
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    stack.append(neighbor)
        dfs(0)
        return len(seen) == len(rooms)
