# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
  # Start with a length and a character for encoding (This will split the length and the actual encoded string)
  def encode(self, strs: List[str]) -> str:
    res = ''
    for s in strs:
      res += str(len(s)) + '#' + s
    return res

  # Now that the string is encoded, it can be read in the following pattern: NUMBER#STRING
  def decode(self, s: str) -> List[str]:
    strs = []
    i = 0

    while i < len(s):
      stringIndex = i
      while s[i] != "#":
        i += 1
      length = int(s[stringIndex:i])
      i += 1
      strs.append(s[i:i+length])
      i += length
    
    return strs