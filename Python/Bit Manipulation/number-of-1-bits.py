# https://leetcode.com/problems/number-of-1-bits/

class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
      if 1 & n:
        count += 1
      n >>= 1
    return count