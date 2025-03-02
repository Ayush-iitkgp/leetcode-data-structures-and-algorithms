from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        answer = [0] * len(nums)
        j = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                answer[j] = nums[left] * nums[left]
                left = left + 1
            else:
                answer[j] = nums[right] * nums[right]
                right = right - 1
            j = j - 1
            # print(answer)
        # print(answer)
        return answer

