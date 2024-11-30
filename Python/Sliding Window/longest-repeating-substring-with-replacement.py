# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    currentMax = 0
    
    left = 0
    maxfreq = 0
    for right in range(len(s)):
      count[s[right]] = 1 + count.get(s[right], 0)
      maxfreq = max(maxfreq, count[s[right]])

      while (right - left + 1) - maxfreq > k:
        count[s[left]] -= 1
        left += 1
      currentMax = max(currentMax, right - left + 1)

    return currentMax