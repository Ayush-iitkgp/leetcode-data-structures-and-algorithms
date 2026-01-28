# Graph BFS

Most of the graph problems can be solved using both DFS and BFS. However, there are some problems where using BFS is better than using DFS:
1. In trees, BFS was better when we were concerned with tree levels.
2. In graphs, **BFS is better when we are asked to find the shortest path**.

* **BFS on a graph always visits nodes according to their distance from the starting point(node/vertex).**

* **Important:** In a graph, there are **multiple ways** to reach a vertex from the starting vertex. However, when you reach the vertex using BFS, it is guaranteed that it is the shortest path from the starting vertex.

* Important: To implement BFS, we will use a **queue (iteratively) instead**.
```python
from collections import deque
queue = deque()
queue.add(root)
while queue:
    # do something
```
