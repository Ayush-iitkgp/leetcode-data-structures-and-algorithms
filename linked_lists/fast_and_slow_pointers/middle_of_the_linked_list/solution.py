from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solved using slow and fast pointer approach
        when the fast is None, slow is at the middle of the linked list
        """
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # ans = []
        # while slow is not None:
        #     ans.append(slow.val)
        #     slow = slow.next

        # return ans

        # return slow.val
