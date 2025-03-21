from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we need to add a dummy node at the start of the linked list so head and tail removals are handled.
        Use fast and slow pointers to reach to the node previous to the node that has to be removed.
        Return dummy.head
        """
        if not head:
            return None
        dummy = ListNode(0, head)
        slow = fast = dummy
        for i in range(n + 1):
            print(i)
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        print(slow.val)

        slow.next = slow.next.next if slow.next else None

        return dummy.next
