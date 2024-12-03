# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    if not nums:
      return 0
    
    n = len(nums)
    
    if n == 1:
      return nums[0]

    # 0th index acts as a placeholder for previous max
    # While 1st index considers whether or not the previous value was higher
    money = [0] * n
    money[0] = nums[0]
    money[1] = max(nums[0], nums[1])

    for i in range(2, n):
      money[i] = max(money[i - 1], nums[i] + money[i - 2])

    return money[-1]
  