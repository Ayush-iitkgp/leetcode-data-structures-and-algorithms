from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The approach is to initialize
        1. a slow pointer at head
        2. a fast pointer at head.next
        3. if slow.val == fast.val, move the fast to the next and delete the node at slow and move the
        4. iterate until fast is not at the end of the linked list
        """
        if not head:
            return head
        slow = head
        fast = head.next

        while fast is not None:
            if slow.val == fast.val:
                # curr = fast
                fast = fast.next
                slow.next = slow.next.next
                # print(slow.val)
            else:
                slow = slow.next
                fast = fast.next
        return head
