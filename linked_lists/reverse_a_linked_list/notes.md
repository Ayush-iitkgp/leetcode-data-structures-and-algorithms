# Reverse a linked List

**Very Important:** If `node.next` is to the left of the assignment (=) operator, it refers
to the **pointer (->)**. And if `node.next` is to the right of it, it refers to the **node**

## How to reverse a linked list
1. Start with `prev = None`
2. Start with `curr = head`
3. Iterate `while curr is not None`
   1. Extract **next node** as `next_node = curr.next`
   2. Move curr.next pointer to point to prev as `curr.next = prev`
   3. Now, prev is current as `prev = curr`
   4. Now, move current to the next_node as `curr = next_node`
   5. **Important:** At the end of each loop, **there will be no pointer between** `prev` and `curr`
4. Return `prev` as it is the new `head` of the reversed linked list.
