from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        diameter of a binary tree = max(diameter of all the subtrees)
        diameter of a subtree = left height(depth) of the subtree + right height(depth) of the subtree
        """
        diameter_array = []

        def dfs(node):
            """
            returns depth of a tree and also appends the diameter of the node to the diameter_array
            """
            if node is None:
                diameter_array.append(0)
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            diameter_node = left_depth + right_depth
            diameter_array.append(diameter_node)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return max(diameter_array)
