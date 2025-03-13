from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Step 1: Create a map with the frequency of each number
        Step 2: Initialize ans = -1 and iterate through the map, if frequency is equal to 1, answer is
        max of current element and previous answer
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        array = []
        for k in count:
            if count[k] == 1:
                array.append(k)

        if len(array) == 0:
            return -1
        array = sorted(array)
        print(array)
        return array[-1]
        # return sorted(array)
