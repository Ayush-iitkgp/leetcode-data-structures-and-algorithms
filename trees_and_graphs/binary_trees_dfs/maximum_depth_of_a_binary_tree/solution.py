from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            """
            This function returns the maximum depth of a binary tree when the node is the root of the binary tree.

            :param node: node of the binary tree
            :return: maximum number of nodes from the root node to the leaf node.
            """
            # Step 1: Handle the base case
            if node is None:
                return 0

            # Step 2: Call the recursive function on the children
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            if left_depth > right_depth:
                if node.left is not None:
                    print(node.left.val)
                # print(f"ans is: {node.left.value if  else 5}")
            else:
                if node.right is not None:
                    print(node.right.val)
                # print(f"ans is: {node.right.value if node.right is not None else 5}")

            # Step 3: Perform some logic at the current node
            max_depth = 1 + max(left_depth, right_depth)

            # Step 4: Return the answer
            return max_depth

        max_depth = depth(root)
        # print(max_depth)
        return max_depth
