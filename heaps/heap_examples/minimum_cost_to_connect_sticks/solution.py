from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        1. Create min heap from the sticks array
        2. Pop 2 minimum and then push the sum of them
        3. Do it until the length of the heap is 1
        """
        heap = sticks
        heapify(heap)
        cost = 0
        while len(heap) > 1:
            first_min = heappop(heap)
            second_min = heappop(heap)
            cost = cost + first_min + second_min
            heappush(heap, first_min + second_min)

        return cost
