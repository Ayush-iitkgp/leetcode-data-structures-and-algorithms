from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        ans = None
        for right in range(len(nums)):
            curr = curr + nums[right]
            while curr - nums[left] >= target:
                curr = curr - nums[left]
                left = left + 1
            if curr >= target:
                ans = right - left + 1 if not ans else min(ans, right - left + 1)
        return ans if ans else 0
