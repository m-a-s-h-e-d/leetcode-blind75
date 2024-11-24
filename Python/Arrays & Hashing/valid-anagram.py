# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if (len(s) != len(t)):
      return False

    letterCount = defaultdict(int)

    for char in s:
      letterCount[char] += 1

    for char in t:
      if char in letterCount and letterCount[char] > 0:
        letterCount[char] -= 1
      else:
        return False
    
    return True

# This is a funny solution that sorts the two strings
# Not a good solution as it requires O(nlogn) time

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
