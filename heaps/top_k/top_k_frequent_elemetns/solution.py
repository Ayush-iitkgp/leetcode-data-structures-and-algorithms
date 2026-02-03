from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            1. Convert the input to the max heap at each step
            2. Take the first 2 elements in the heap
            3. get the result of the smash at each step and add the result to the heap if not destroyed
        """

        heap = [-stone for stone in stones]  # converted to negative since we need the max heap
        print(f"Negative of the input {heap=}")
        heapify(heap)
        while len(heap) > 1:
            print(f"heap is {heap}")
            first = abs(heappop(heap))
            second = abs(heappop(heap))
            print(f"first element of the heap is {first}")
            print(f"second element of the heap is {second}")
            if second == first:
                continue
            else:
                heappush(heap, -abs(first-second))

        print(f"current heap is {heap}")

        if len(heap) == 1:
            return abs(heap[0])
        else:
            return 0
