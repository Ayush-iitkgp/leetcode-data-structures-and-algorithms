from math import sqrt
from typing import List
from heapq import heappop, heappush


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x*x + y*y)

        heap = []

        for point in points:
            heappush(heap, (-distance(point[0], point[1]), point[0], point[1]))

            if len(heap) > k:
                heappop(heap)

        return [[h[1], h[2]] for h in heap]
