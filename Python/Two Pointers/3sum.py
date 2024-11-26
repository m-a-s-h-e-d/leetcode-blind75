# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []

    # First, sort the numbers to make them easier to work with
    sortedNums = sorted(nums)
    
    # Go through all the integers to find a pair that add to 0
    for i, n in enumerate(sortedNums):
      # Once this index gets past 0, triplets can no longer be formed, as the numbers are all greater than 0
      if n > 0:
        break

      # If same as previous checked integer, skip it
      if i > 0 and n == sortedNums[i - 1]:
        continue

      # Iterate the rest of the numbers to find the pair that fit
      left = i + 1
      right = len(sortedNums) - 1
      while left < right:
        threeSum = n + sortedNums[left] + sortedNums[right]
        if threeSum < 0:
          left += 1
        elif threeSum > 0:
          right -= 1
        else:
          res.append([n, sortedNums[left], sortedNums[right]])
          left += 1
          right -= 1
          while left < right and sortedNums[left] == sortedNums[left - 1]:
            left += 1

    return res
