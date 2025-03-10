from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            """Function that determines the minimum cost to reach until ith step"""
            if i == 0:
                return 0
            if i == 1:
                return 0
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
                return memo[i]

        n = len(cost)
        return dp(n)
        # print(result)
        # return ans
