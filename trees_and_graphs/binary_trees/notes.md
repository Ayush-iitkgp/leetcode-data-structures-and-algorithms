# Binary trees

## Nodes and graphs

### What is a graph?
1. A graph is a **collection** of **nodes** and **their pointers to other nodes**.
2. A `Linked List` is a also a graph.
3. A `Tree` is also a graph.

**Note:** Trees are less advanced topics than Graphs.

**Note:** A node in a graph is called `vertex` and a pointer in a graph is called `edge`. So basically, a graph is a collection of **nodes/vertices** and **pointers/edges**.

### What is a tree?
1. Like in a linked list where a **pointer** points to the **next** node, in a tree a **node's pointers** point to its **children**.
2. What is the start of a tree called?
   1. A start node of the linked list is called **head**.
   2. A start node of the tree is called **root**.
3. **Important:** In a tree, every node would have a parent except the `root` node.
4. **Important:** In a tree, each node **only has 1 parent** except of course the `root` node.

### What is a Binary Tree?
1. A binary tree is a tree where **each node has a maximum of 2 children**.
2. A node can have 0, 1 or 2 children but no more.
3. Also, every node (except the root) has exactly one parent.
4. **Note:** The children of a node in a binary tree are referred as `left` and `right` child but there is no difference between them when it comes to solving problems.

### Tree Terminology
#### Root Node
1. `root` node is a node at the top of the tree.
2. We can reach any other node of a tree from the root node
3. In Linked List, **head** was the input to most of the problem statements, similarly in Trees **root** will be the input to the problems.

#### Leaf Node
1. **Leaf Node:** It is a node in a tree with no child.

#### Depth of a Node
1. **Depth of a Node:** It tells us how far a node is from the `root`.
2. **A root node has depth 0.**
3. `Depth of a Child Node = Depth of the Parent Node + 1`

#### Subtree
1. **A subtree is a node and all of its descendants**.
2. The node is called the root of the subtree.
3. A subtree can be considered as a Tree with the chosen node as the root of the tree.
4. **Important:** Tree problems are solved using recursion.
5. **Note:** A subtree of a binary tree is also a binary tree.

#### Code Representation of a Tree
```python
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
```

**Note:** Like in Linked List problem, we are given the `head` of the linked list, similarly in a binary tree problem, we are given the `root` node as the input.
