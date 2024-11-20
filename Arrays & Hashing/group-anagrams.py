# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagramDict = dict()

    for anagram in strs:
      currentValue = 1
      for char in anagram:
        currentValue *= ord(char)
      if currentValue not in anagramDict:
        anagramDict[currentValue] = [anagram]
      else:
        anagramDict[currentValue].append(anagram)

    result = []
    for key in anagramDict:
      result.append(anagramDict[key])
    
    return result