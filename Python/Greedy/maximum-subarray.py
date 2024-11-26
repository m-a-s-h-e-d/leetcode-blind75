# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    current = 0
    currentMax = nums[0]

    for num in nums:
      if current < 0:
        current = 0
      current += num
      currentMax = max(current, currentMax)

    return currentMax