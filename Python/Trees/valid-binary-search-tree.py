# https://leetcode.com/problems/validate-binary-search-tree/

import collections

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True

    minVal = float("-inf")
    maxVal = float("inf")
    queue = collections.deque([(root, minVal, maxVal)])
    
    while queue:
      node, left, right = queue.popleft()
      if not (left < node.val < right):
        return False
      if node.left:
        queue.append((node.left, left, node.val))
      if node.right:
        queue.append((node.right, node.val, right))

    return True
