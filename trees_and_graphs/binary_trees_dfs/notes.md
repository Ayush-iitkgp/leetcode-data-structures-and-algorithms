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

### Steps to solve a DFS Problem using Recursion
1. Define the state variables and the function definition.
   1. First state variable is usually the `node`.
   2. Second state variable would depend upon the problem statement.
2. Write the base case. Usually `node == null` is the base case.
   1. Also, sometimes **the leaf node** is the base case as well.
3. Perform **some logic** at the current node. The logic would depend upon the problem statement.
4. Call the DFS function with the `left` and the `right` node
5. Return the answer

**Important Note:** Step 2 and step 3 can change their orders depending upon the problem statement.

**Note 2:** It's also possible that the logic happens between calling the dfs on the left and the dfs on the right depending on the problem statement.

### Solving Binary Tree DFS Problems using Iteration
1. We need to use `stack` data structure for it.
2. We will always perform **preorder DFS** when using iteration.
3. We start by adding `root` of the tree to the stack before starting the iteration.
4. Iterate until the stack is empty:
   1. Pop the element from the stack
   2. Perform the logic
   3. Add the left child to the stack
   4. Add the right child to the stack

### Time and Space Complexity of Binary Tree Problems
1. Time complexity is usually O(n) where n is the number of nodes present in the tree.
It is O(n) because we visit the nodes only once.
2. The space complexity is usually O(n) as well.
