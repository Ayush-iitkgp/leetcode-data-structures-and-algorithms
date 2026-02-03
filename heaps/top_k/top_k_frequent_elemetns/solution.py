from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Store the elements and their frequency in the hashmap
        2. Create a min-heap and start pushing the elements based on their frequency
        3. If after pushing the element the length of the heap is greater than K then
        remove the element with the minimum frequency
        """
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        heap = []  # Initialize an empty heap

        for key, value in counter.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)

        return [y for x, y in heap]
