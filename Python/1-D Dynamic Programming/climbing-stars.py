# https://leetcode.com/problems/climbing-stairs/

class Solution:
  def climbStairs(self, n: int) -> int:
    dp = [-1] * n
    # First two steps have 1 and 2 ways to reach respectively
    dp[0] = 1
    if n == 1:
      return dp[0]
    dp[1] = 2

    for i in range(2, n):
      dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]
