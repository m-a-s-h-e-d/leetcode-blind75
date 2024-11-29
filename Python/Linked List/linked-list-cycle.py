# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    # With a slow and fast pointer, the fast pointer will have
    # finished two iterations once the slow pointer finishes the first
    # In the case of a cycle
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True

    return False