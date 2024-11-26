# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
      return False
    
    stack = []

    for char in s:
      n = len(stack)
      if char == '{' or char == '[' or char == '(':
        stack.append(char)
      elif n < 1:
        return False
      elif char == '}':
        if stack[n - 1] != '{':
          return False
        stack.pop(n - 1)
      elif char == ']':
        if stack[n - 1] != '[':
          return False
        stack.pop(n - 1)
      elif char == ')':
        if stack[n - 1] != '(':
          return False
        stack.pop(n - 1)
    
    return len(stack) == 0
      