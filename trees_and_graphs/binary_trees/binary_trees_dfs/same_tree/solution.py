from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        :param p:
        :param q:
        :return:
        """

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            """
            Checks if 2 subtrees rooted at node1 and node2 are same or not
            Two subtrees rooted at node1 and node2 are same if:
            1. node1.val == node2.val
            2. the left subtrees are same and the right subtrees are same

            The base condition:
            two empty trees are same
            one is empty but other is not empty then they are not same
            :param node1:
            :param node2:
            :return:
            """
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is None:
                return False
            elif node2 is not None and node1 is None:
                return False

            return node1.val == node2.val and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        # ans is dfs(root1, root2)
        return dfs(p, q)
