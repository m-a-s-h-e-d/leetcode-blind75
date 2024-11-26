# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    remainingSteps = len(nums) - 1
    
    for i in range(len(nums) - 2, -1, -1):
      if i + nums[i] >= remainingSteps:
        remainingSteps = i

    return remainingSteps == 0