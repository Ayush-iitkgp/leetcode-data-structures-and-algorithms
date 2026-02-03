from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        1. Create min heap
        2. Keep removing until if the size of the heap is greater than K
        3. At the end the element at the top of the heap is the Kth largest element
        """
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]
