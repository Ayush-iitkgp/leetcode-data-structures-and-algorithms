# Stacks

* Stacks are **ordered collection** of elements where elements **are only added and removed from the same end**.
* Examples:
  * In real world, a stack of plates in the kitchen is an example of a stack since we can only add or remove the plate from the top of the pile.
  * In software world, a stack is the history of the current browser tab.
* A stack is a **LIFO (Last In, First Out)** where the last element placed is the first element to come out.
* **Q: How to implement stack in Python?**
* Ans: We use Python's list to implement stack
```python
stack = []
# Pushing into the stack. Time complexity O(1)
stack.append(elem)
# Peeking into the stack. Time complexity O(1)
elem = stack[-1]
# Popping from the stack. Time complexity O(1)
elem = stack.pop()
```
* Inserting into a stack is called **Pushing** and removing from the stack is called **Popping**.
* **Peeking** is looking at the elements at the top of the stack without popping it.
* **Important: In a stack, you can only add or remove elements from the top of the stack.**
* **Note:** Recursion is implemented using stack.

## How to identify if a problem can be solved using a Stack?
1. The problem statement would have a part where the **elements in the input are interacting with each other** such as:
   1. matching elements together
   2. querying some property such as "how far is the next largest element"
   3. evaluating a mathematical equation given as a string
   4. just comparing elements against each other
2. If the current element has to interact with the last element that was processed.
