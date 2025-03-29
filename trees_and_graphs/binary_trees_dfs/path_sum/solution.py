from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], currentSum: int) -> bool:
            """
            return true if the there is a path starting from the node and ending at leaf that has
            sum equal to the targetSum
            :param node: tree node
            :param currentSum: sum of the node's values from the root to the current node (excluding the current node)
            :return:
            """
            if node is None:
                return False

            # if both children are null, then the node is a leaf
            if node.left is None and node.right is None:
                return (currentSum + node.val) == targetSum

            left_tree = dfs(node.left, currentSum + node.val)
            right_tree = dfs(node.right, currentSum + node.val)
            return left_tree or right_tree

        return dfs(root, 0)
