from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr):
            """
            Represents a current subarray that is the permutation of the input array
            """
            if len(curr) == len(nums):
                # print(curr)
                ans.append(curr[:])
                print(ans)
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        print(f"{ans=}")
        return ans
