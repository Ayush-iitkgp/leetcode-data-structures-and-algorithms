from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :param isConnected: 2D matrix
        :return: number of connected components in the graph
        Step 1: Build the adjacency list - normally we don't have to do build the adjacency list but in this
        case it is required
        Step 2: Start graph traversal through a node if the node is already visited do not revisit
        it else increment the counter start the graph
        traversal from that node
        """
        def build_graph(isConnected: List[List[int]]):
            graph = {}
            for i in range(len(isConnected)):
                for j in range(len(isConnected[0])):
                    if isConnected[i][j] == 1:
                        if i in graph:
                            graph[i].append(j)
                        else:
                            graph[i] = [j]
            return graph

        def dfs(node: int):
            stack = list()
            stack.append(node)
            # seen = set()
            while stack:
                current_node = stack.pop()
                seen.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in seen:
                        stack.append(neighbor)

        seen = set()
        count = 0
        graph = build_graph(isConnected)
        print(graph)
        for node in range(0, len(graph)):
            if node not in seen:
                count += 1
                dfs(node)
        return count
