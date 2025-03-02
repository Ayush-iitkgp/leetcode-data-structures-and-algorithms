from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        place = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[place] = nums[i]
                place = place + 1
            # print(nums)

        # print(place)
        for j in range(len(nums) - place):
            nums[len(nums) - j - 1] = 0
            # print(nums)

        # return nums
