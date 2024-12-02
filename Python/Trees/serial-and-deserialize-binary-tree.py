# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Codec:
  
  # Encodes a tree to a single string.
  def serialize(self, root: Optional[TreeNode]) -> str:
    res = []

    def dfs(root):
      if not root:
        res.append("N")
      else:
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    dfs(root)

    return ",".join(res)

  # Decodes your encoded data to tree.
  def deserialize(self, data: str) -> Optional[TreeNode]:
    vals = data.split(",")
    self.i = 0

    def dfs():
      if vals[self.i] == "N":
        self.i += 1
        return None
      node = TreeNode(int(vals[self.i]))
      self.i += 1
      node.left = dfs()
      node.right = dfs()
      return node

    return dfs()
