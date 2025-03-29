from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> int:
            """
            take a node and returns the smallest depth of the node
            """
            if node is None:
                return 0
            if node.right is None:
                return 1 + dfs(node.left)
            elif node.left is None:
                return 1 + dfs(node.right)
            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)
