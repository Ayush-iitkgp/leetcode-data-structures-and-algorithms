from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Notes: Directed acyclic graphs can also be considered as a Tree problem.
        Usually, a DAG would involve calculating Indegree of nodes
        The solution is to find set of nodes that have InDegree 0 since any other node
        which has indegree more than 0 can be reached by any other node.
        """
        indegree = [0] * n
        for x, y in edges:
            indegree[y] += 1
        print(f"Indegree of nodes in the graph is {indegree}")
        ans = [i for i, x in enumerate(indegree) if x == 0]
        return ans
