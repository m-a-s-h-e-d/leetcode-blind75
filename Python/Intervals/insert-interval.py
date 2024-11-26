# https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0
    n = len(intervals)
    res = []

    # Get the left side
    while i < n and intervals[i][1] < newInterval[0]:
      res.append(intervals[i])
      i += 1

    # Find place to insert new interval
    while i < n and newInterval[1] >= intervals[i][0]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1
    res.append(newInterval)

    # Get the right side
    while i < n:
      res.append(intervals[i])
      i += 1

    return res
          