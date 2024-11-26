# https://leetcode.com/problems/minimum-window-substring/

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    # Initial setup for O(1) access on the required characters
    tHash = dict()

    for char in t:
      if char not in tHash:
        tHash[char] = 0
      tHash[char] += 1

    # Setup for finding the shortest substring with O(1) access on the character count
    currentShortestSubstring = ""
    matchCount = 0
    requiredCount = len(tHash.keys())
    windowHash = dict()

    for key in tHash.keys():
      windowHash[key] = 0

    # Iterate through and find all substrings matching, while shrinking left upon finding all t chars
    left = 0
    for right, char in enumerate(s):
      if char in tHash:
        windowHash[char] += 1
        if windowHash[char] == tHash[char]:
          matchCount += 1
        while matchCount == requiredCount:
          currentString = s[left:right+1]
          if currentShortestSubstring == "" or len(currentString) < len(currentShortestSubstring):
            currentShortestSubstring = currentString
          if s[left] in windowHash:
            windowHash[s[left]] -= 1
          if s[left] in tHash and windowHash[s[left]] < tHash[s[left]]:
            matchCount -= 1
          left += 1
    
    return currentShortestSubstring