# Heaps

* Heap is a data structure that is an implementation of the **priority queue**.
* **Question: What is a Priority Queue?**
* **Ans:** It is also a abstract data structure (like stacks and queues) where each element has a priority that
determines its order of service.
* **Note:** Like how Stack is an abstract data structure and List (in Python) implements it, similarly Priority Queue is an abstract data structure and Heap is used to implement it.

## Time Complexity of Heap Data Structure Operations
* Add an element O(log n)
* Remove the minimum element O(log n)
* Find the minimum element O(1)

**Note:** There are 2 types of Heaps:
1. **Min Heap:** A heap configured to find/remove the minimum element
2. **Max Heap:** A heap configured to find/remove the maximum element.

## How is a heap implemented?
* **Important:** All the programming languages have a **built-in** data type called Heap.
* The most important way to implement a Heap is called **Binary Heap** that uses an array.
* A Binary Heap implements a Binary Tree with only an array.
* Each element in the array is equivalent to a Node in a Tree.
* **The smallest element in the Tree is the root.**
* The following property is maintained at every node: _if A is the parent of B, then `A.val <= B.val`_
* And the binary tree must be the complete tree.
* **Important:** The children of the element at index `i` in the array are at indices `2i+1` and `2i+2` of the array.

**Note 1:** An existing array can be converted to heap in `O(n)` time.
**Note 2:** Using a heap can reduce the time complexity of a problem from `O(n**2)` to `O(n long n)`.
**Note 3:** **We should heap when we want to find maximum or minimum of something repeatedly.**

## Interface guide
* Python provides **min heap** using `heapq` module.
* **Note:** To solve problems in Python that require max heap, multiply the input by -1.
* Create a heap from the array
```python
from heapq import heapify
nums = [1, 2, 3]
heapify(nums) # Now nums is a min heap and this operation is O(n) time complexity
```
* Push an element to the heap
```python
from heapq import heapify, heappush
heap = [1, 2, 4]
heapify(heap)
heappush(heap, 5)
```
* Find the minimum element in the heap, length of the heap and print the elements in the heap in the sorted order
```python
from heapq import heapify
heap = [4, 5, 1]
heapify(heap)
min_element = heap[0] # returns the min element in the queue
lenght = len(heap) # returns the lenght of the queue
# The numbers will be printed in sorted order
while heap:
    print(heapq.heappop(heap))
```
