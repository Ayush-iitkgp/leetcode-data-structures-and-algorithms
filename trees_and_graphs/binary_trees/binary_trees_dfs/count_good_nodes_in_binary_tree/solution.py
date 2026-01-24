# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest_value):
            """
            returns number of good nodes starting from node where largest_value is larget_value
            input:
            node: current node
            largest_value: largest value until the current node
            """
            if node is None:
                return 0

            if node.val >= largest_value:
                ans = 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                ans = dfs(node.left, largest_value) + dfs(node.right, largest_value)
            # print("ans is: ")
            # print(ans)
            return ans

        return dfs(root, float("-inf"))
