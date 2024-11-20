# https://leetcode.com/problems/two-sum/

from collections import defaultdict
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seenNum = defaultdict(int)
    solution = []

    for i in range(len(nums)):
      compliment = target - nums[i]
      if (compliment in seenNum):
        solution = [seenNum[compliment], i]
        return solution
      seenNum[nums[i]] = i
    
    return solution