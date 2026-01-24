from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. Build the hashmap representing the graph
        2. Build the array that has inward connections for each vertex
        3. Initiate the queque with the vertices that have 0 inward connections
        4. Iterate until the queue is empty and add to the topological sort array
        5. If the length of the array is total number of vertices then the topological sort is
        possible else not possible.
        """

        graph = defaultdict(list)
        inward = [0] * numCourses

        for x, y in prerequisites:
            graph[y].append(x)
            inward[x] += 1

        queue = deque()
        for i in range(numCourses):
            if inward[i] == 0:
                queue.append(i)

        print(f"Hashmap representation of the graph is {graph}")
        print(f"starting queue is {queue}")

        # Apply DFS
        topological_sort_order = []
        while queue:
            vertex = queue.popleft()
            topological_sort_order.append(vertex)
            for neighbor in graph[vertex]:
                inward[neighbor] -= 1
                if inward[neighbor] == 0:
                    queue.append(neighbor)

        print(f"Topological sort order of the graph is {topological_sort_order}")
        return len(topological_sort_order) == numCourses
