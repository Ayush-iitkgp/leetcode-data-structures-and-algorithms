class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dp(i):
            """total number of ways to reach the i-th stair"""
            if i == 1:
                return 1
            elif i == 2:
                return 2

            if i in mem:
                return mem[i]

            mem[i] = dp(i - 1) + dp(i - 2)
            return mem[i]

        ans = dp(n)
        return ans
