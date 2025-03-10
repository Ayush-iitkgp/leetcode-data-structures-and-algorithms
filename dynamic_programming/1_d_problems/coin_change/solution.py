from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dp(i):
            """fewest coin needed to make sum equal to i"""
            if i == 0:
                return 0
            elif i < min(coins):
                return -1
            elif i in coins:
                return 1

            if i in mem:
                return mem[i]

            ans = -1
            for k in coins:
                if dp(i - k) != -1:
                    ans = min(dp(i - k), ans) if ans != -1 else dp(i - k)
            mem[i] = 1 + ans if ans != -1 else -1
            return mem[i]

        ans = dp(amount)
        print(mem)
        return ans
