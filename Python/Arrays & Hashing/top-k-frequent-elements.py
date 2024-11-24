# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequencyDict = dict()

    for num in nums:
      if num not in frequencyDict:
        frequencyDict[num] = 1
      else:
        frequencyDict[num] += 1

    buckets = [[] for i in range(len(nums) + 1)]
    for num in frequencyDict:
      frequency = frequencyDict[num]
      buckets[frequency].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
      for num in buckets[i]:
        res.append(num)
        if len(res) == k:
          return res
    
    return res