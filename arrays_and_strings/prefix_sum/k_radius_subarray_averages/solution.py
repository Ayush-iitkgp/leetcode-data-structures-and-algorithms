from typing import List
import math


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        prefix_sum = [0] * length
        prefix_sum[0] = nums[0]
        for i in range(1, length):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        avgs = [0] * length
        for i in range(length):
            if i - k < 0 or i + k >= length:
                avgs[i] = -1
            else:
                avgs[i] = math.floor((prefix_sum[i + k] - prefix_sum[i - k] + nums[i - k]) / (2 * k + 1))
        return avgs
