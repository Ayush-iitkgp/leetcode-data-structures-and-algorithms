# Fast and slow pointers
* It is one of the methods of solving problems related to a linked list
* This method is very similar to the two pointers approach used in the array related problems.
* Here, we initialize 2 pointers that don't move at the same node. Instead:
  * First pointer named `fast` can move at the faster speed than the `slow` pointer. Both pointers start at `head`.
  * First pointer named `fast` can begin at some node away from the `slow` pointer.
* **Important:When `fast` pointers move at 2x speed the `slow` pointer, the condition for while loop is as follows:**
```
slow = fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
```

## Examples
1. **Find the middle of the linked list:** Given the head of a linked list with an odd number of nodes head,
return the value of the node in the middle.
2. **Linked List Cycle:** Given the head of a linked list, determine if the linked list has a cycle.
   * If the linked list has a cycle, then `fast` and `fast.next` would never be `None`.
   * Also, at some point of time, the `fast` and the `slow` pointer would point to the same node.
3. **Given the head of a linked list and an integer k, return the `kth` node from the end.**
   1. Let's assume that the length of the linked list in N
   2. If you start `fast` from `Kth node` and slow from `head`
   3. When fast reaches `tail`, we have done **N-K** iteration, hence `slow` is at **N-Kth node from the head which is Kth node from the tail**.
