from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)

        count = 0
        for x in arr:
            if x + 1 in arr_set:
                count = count + 1
        return count
