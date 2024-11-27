# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    current = head

    while current is not None:
      nextNode = current.next
      current.next = previous
      previous = current
      current = nextNode
    
    return previous