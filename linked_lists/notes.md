# Linked lists

* Linked lists are **also ordered collection of elements** just like arrays.
* Linked lists use **pointers** whereas arrays do not use it.
* Linked lists are also used to implement other data structures.

**Q: What is a Node?**

**Ans:** A Node is an object that **contains more than one piece of data** like integer or string.

**Note 1:** Linked lists are implemented using **Node**.

**Note 2:** A Node in a linked list contains a `value` and a `next` pointer which points to the next element in the linked list.

**Note 3:** A Node in Python is an instance of a class as defined below.

**Example of a Node in a Linked List in Python:**
```
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
```

**Note 4:** A Node at the start of the linked list is called **head**.

**Note 5:** You can only access all the elements of the linked list from head. So, **always keep reference to the head**.

### Advantages and disadvantages compared to arrays
**Important: All the problems that involve linked list will have linked list as part of the input.**
#### Advantages
1. We can add or remove element from a linked list in O(1) at position `i` provided we have reference to the **node before at position `i-1`** the element that needs to be removed.
2. Linked lists do not have fixed size whereas arrays have initial size allocated ot it.

#### Disadvantages
1. You can only access an element in the list in O(n) whereas in array, it can be performed in O(1).

### Linked list Operations
#### 1. Assignment (=)
a. **In Python, a variable points to the reference/address of an object in the memory.**

b. In the assignment operation below:
```
prev.next = node.next
```
`prev.next` on the left of the assignment operator refers to the arrow pointer in the Linked List where as `node.next` to the right of the assignment operator refers to the Linked List **Node**.


#### 2. Chaining .next
a. When you have multiple `.next`, for example `head.next.next`, everything before the last `next` refers to a node in the linked list.
#### 3. Traversal
Linked list traversal is done using **while loop**. For example:
```
while head is not None:
    head = head.next
```

### Types of linked lists
#### 1. Singly linked list
1. Most common kind linked list.
2. In this linked list, each node has:
   1. a `value`
   2. the **pointer** to the next element, this pointer is usually called `next`.
3. In this linked list, we can only **move forward**.
4. **In this linked list, to add or remove element at index `i`, we need the reference to the element at index `i-1`.**
5. How to delete an element at index `i` in the singly linked list?
   1. We need reference to the prev element.
   2. `prev.next = prev.next.next`
   3. **Important:** When removing an element from the linked list, always add a node before the head of the linked list.
6. How to add an element at index `i` in the linked list?
   1. We need reference to the `prev_node` element and `new_node`
   2. `new_node.next = prev_node.next.next`
   3. `prev_node.next = new_node`

#### 2. Doubly linked list
1. In this linked list, each node has:
   1. `value`
   2. the pointer to the **next node** called `next`
   3. the pointer to the **previous node** called `prev`
2. In this linked list, we can **move forward and backward**.
3. **In this linked list, to add or remove element at index `i`, we need the reference of the element at index `i` itself.**
4. How to delete an element at index `i`?
   1. We need reference to the current element in the linked list.
   2. We need to extract `prev_node` and `next_node`
   3. `prev_node = curr.prev` and `next_node = curr.next`
5. How to add an element at index `i`?
   1. We need reference to the current element in the linked list.
   2. We only need to extract `prev_node`
   3. `prev_node = curr.prev`

#### 3. Doubly linked list with sentinel nodes
1. Sentinel nodes are at the end of the doubly linked list and

#### Dummy pointers
1. Dummy pointers are used so that we keep the `head` of the linked list intact because
it is only with head we can traverse a linked list.
2. How to initialize a dummy pointer?
```
dummy = head
```
3. Now, use `dummy` to traverse the linked list instead of using `head`.
