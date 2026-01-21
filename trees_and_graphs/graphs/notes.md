# Graphs

**Q: What is a Graph?**

**Ans:** A graph is a collection of nodes and connections between those nodes.

**Note:** Nodes are also called **Vertices** and the connections between nodes are also called as **Edges**.

## Graph terminology

* An Edge can be directed or undirected in a graph.
* A **directed edge** means that we can only traverse in **one** direction where as an **undirected edge** means that we can traverse in both the directions.
* In pictorial representation, a directed edges will be an **arrow (-->)** between nodes.
* In pictorial representation, an undirected edge will be **straight line (--)** between nodes.
* **Node's Indegree**: Number of edges that can be used to reach the node (vertex).
* **Node's Outdegree**: Number of edges that can be used to leave the node (vertex).
* **Neighbors**: A node's neighbor is a **collection of nodes** that can be reached from it.
* A graph can be **cyclic** or **acyclic**.

**Q: What is a connected component in a Graph?**

**Ans:** A connected component is a Graph is a **collection of Vertices (nodes)** that are connected to each other via edges.

## How are graphs given in algorithm problems?
* In Linked List related problems, **head** of the linked list is given as the input.
* In Tree related problems, **root** of the tree is given as the input.
* In Graph related problems, only the information related to the Graph is given so the **first step is to represent the graph in the code**.
* **Important:** In graph related problems, the problem statement **would not mention that the input is the Graph**.
* **Note:** Usually, we will label the nodes (vertices) of the graph from _0 to n-1_ when representing the graph in the code.

### First way to represent a Graph in Input of the Problem Statement: Array of Edges
* In this format, a Graph will be represented as the 2D array with 2 columns and number of rows is equal to number of edges.
* Each element of the array will be in the format `[x, y]` which represents that **there is an edge from vertx x to vertex y**.
* In this input format, we can't directly start the Graph traversal, we need a **pre-processing** (named `build_graph`) step before graph traversal.
* In the pre-processing step, **we construct a HashMap (named graph)** where graph[x] is a list of nodes that can be accessed from node x.
* Example: Input is `edges = [[0, 1], [1, 2], [2, 0], [2, 3]]`
```python
def build_graph(edges):
    """
    It's a pre-processing step where we build and return a hashmap named "graph" that represent
    all the nodes reachable from the keys in the hashmap
    """
    graph = {}
    for x, y in edges:
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]

    return graph
```

### Second way to represent a Graph in the Input of the Problem Statement: Adjacency List
* If the input of the problem statement is adjacency list, the nodes of the graph will **definitely** be numbered from **0 to n-1**.
*  Also, the input would be 2-D integer array named `graph`.
* `graph[i]` **represents all the outgoing connection from node i.**
* If the input is the adjacency list, we can access all the neighbors of a given node i via `graph[i]`.
* **Note:** **We do not need pre-processing step in this kind of input.**

### Third way to represent a Graph in the Input of the Problem Statement: Adjacency Matrix
* In this input format, the nodes will again be numbered  from **0 to n-1**.
* **In this format, the input will be 2D array of size n*n named graph**
* If `graph[i][j] == 1` then there is an outgoing edge from `node i` to `node j`.
* When the input is adjacency matrix then we can traverse the graph in 2 ways:
* In the first way, we can use the Input matrix directly to traverse the graph - **this is the preferred method.**
* In the second way, we can pre-process the input and construct the hashmap as we did for the array of edges as the input and then use this hashmap for the graph traversal.

### Fourth (and last) way to represent a Graph in the Input of the Problem Statement: Matrix
* Here also, the input will be a 2D matrix.
* Here the **nodes are not numbered** from 0 to n-1.
* This way of representing the graph **is not very intuitive.**
* **But this is the most common way to represent a graph.**
* In this input format, each square in the 2D matrix represents a node.
* In this input, the edges of the graph are determined by the problem statement not by the input.

## Code differences between graphs and trees
* Tree has an start point called **root** node but a graph does not have an explicit start point, the start point depends on the problem statement.
* In Tree Problems, the input Tree is given
* But in the graph related problems, we will have to first create the graph using **hashmap**.
* When traversing a Tree, we had to only traverse the left and the right node from a specific node
* But in the graph, **we will have to use a loop to traverse the neighbors of a node** since it can have any number of neighbors.
* When performing Tree traversal, we are always guaranteed that we won't be visiting the same node again.
* But in the Graph traversal, we can visit the same node (vertex again), hence we need to avoid it since we want to visit a node only once.

**Q:How to avoid visiting a node multiple times in Graph traversal?**
**Ans:** We need **to keep a `set` (named `seen`) of visited nodes** and before we visit the node, we must check if the node is already in the set,
if it is then we don't  visit the node else add it to the set and then we visit the node.

**Q: Which node should be the starting point of the Graph Traversal?**
**Ans:** It will depend upon the problem statement.
