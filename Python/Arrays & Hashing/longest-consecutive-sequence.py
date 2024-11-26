# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    longestSequence = 0
    seenNumbers = set()

    # Convert the array into a hash set for O(1) lookup
    for num in nums:
      if num not in seenNumbers:
        seenNumbers.add(num)

    # Search for the beginning of sequences by finding the smallest integers
    for num in seenNumbers:
      if num - 1 not in seenNumbers:
        currentNum = num + 1
        while currentNum in seenNumbers:
          currentNum += 1
        if currentNum - num > longestSequence:
          longestSequence = currentNum - num
    
    return longestSequence
