# https://leetcode.com/problems/binary-tree-level-order-traversal/

import collections

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    queue = collections.deque()
    queue.append(root)

    while queue:
      n = len(queue)
      level = []
      for _ in range(n):
        node = queue.popleft()
        if node:
          level.append(node.val)
          queue.append(node.left)
          queue.append(node.right)
      if level:
        res.append(level)

    return res
