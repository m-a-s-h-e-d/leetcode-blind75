# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import Optional, List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    newHead = ListNode()
    current = newHead

    while list1 and list2:
      if list1.val < list2.val:
        current.next = list1
        list1 = list1.next
      else:
        current.next = list2
        list2 = list2.next
      current = current.next

    if list1:
      current.next = list1
    elif list2:
      current.next = list2

    return newHead.next

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)

    if n == 0:
      return None

    for i in range(1, len(lists)):
      lists[i] = Solution.mergeTwoLists(lists[i-1], lists[i])
    
    return lists[-1]