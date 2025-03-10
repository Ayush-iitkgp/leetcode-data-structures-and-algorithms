# 1D Problems

### Examples:
1. **House Robbers: Can't rob 2 consecutive houses together.**
   1. Function defines: **_Maximum amount earned till ith house._**.
   2. It could include the ith house or exclude it.
   3. Recurrence relation is: `dp(i) = max(num[i] + dp(i-2), dp(i-1))`
2. **Length of the Longest Increasing Subsequence**
    1. Function defines: Length of the longest subsequences including the **ith** element.
    2. Recurrence relation is: `dp(i) = 1 + max(dp(j) such that j < i and nums[j] < nums[i]) `
3. **Solving Questions With Brainpower**
4. **Climbing Stairs**: Find total number of ways to reach the top
   1. Function is: **Total number of ways to reach the i-th stair**
   2. Recurrence relation is: `dp(i) = dp (i-1) + dp(i-2)`
5. **Min Cost Climbing Stairs:** Given an array of cost, find the minimum cost to climb stairs
   1. Function is: **Minimum cost to pay to reach i-th stair**
   2. Recurrence relation is: `dp(i) = min(cost[i-2]+dp(i-2), cost[i-1]+dp(i-1))`
