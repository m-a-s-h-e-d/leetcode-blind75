# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    left = 0
    currentMax = 0

    for right in range(len(s)):
      while s[right] in charSet:
        charSet.remove(s[left])
        left += 1
      charSet.add(s[right])
      currentMax = max(currentMax, right - left + 1)
    
    return currentMax