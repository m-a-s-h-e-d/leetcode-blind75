# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
  def maxArea(self, heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    currentMax = 0

    while (left < right):
      volume = min(heights[left], heights[right]) * (right - left)
      currentMax = volume if volume > currentMax else currentMax
      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1
    
    return currentMax
