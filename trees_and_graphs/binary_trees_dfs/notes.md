# Binary trees - DFS

**Q: What is a tree traversal?**

**Ans:** Tree traversal is a method of accessing all the nodes of a tree starting from the root of the tree.

**Q: How is Tree traversal achieved?**

**Ans:** We perform tree traversal using **recursion**. Whereas linked list traversal was performed using `while` loop.

**Q: How many types of tree traversal are there?**

**Ans:** There are 2 types of tree traversal:
1. Depth First Search (DFS)
2. Breadth First Search (BFS)

**Note:** Depth First Search (DFS) can be performed using 3 ways:
1. **preorder:** `Root node -> Left node -> Right node`
2. **inorder:** `Left node -> Root node -> Right node`
3. **postorder:** `Left node -> Right node -> Root node`

**Note:** A DFS problem related to binary tree can be solved using any one of the 3 ways.

## Depth-first search (DFS)
1. In DFS, we pick a branch of the tree and traverse it until it reaches the leaf node.
2. Once we are at the leaf node, we perform **backtracking** to find the branch of the tree that has not been explored yet.
3. Because we need to perform **backtracking**, we implement DFS using **recursion**.
4. **Note:** DFS can also be performed using `stack` data structure.

### Code for DFS
```python
def dfs(node):
    if node is None:
        return

    # Visit the left node
    dfs(node.left)
    # Visit the right node
    dfs(node.right)
    # then return
    return
```
