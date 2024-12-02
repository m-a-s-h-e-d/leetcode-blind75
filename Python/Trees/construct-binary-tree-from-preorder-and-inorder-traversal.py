# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Use a hashmap to store the value indices for O(1) lookup time
    indices = {val: index for index, val in enumerate(inorder)}

    self.preorder_index = 0
    def dfs(left, right) -> Optional[TreeNode]:
      if left > right:
        return None

      root_val = preorder[self.preorder_index]
      self.preorder_index += 1
      root = TreeNode(root_val)
      mid = indices[root_val]
      root.left = dfs(left, mid - 1)
      root.right = dfs(mid + 1, right)
      return root
    
    return dfs(0, len(inorder) - 1)
  