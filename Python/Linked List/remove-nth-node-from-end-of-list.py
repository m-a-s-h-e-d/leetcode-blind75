# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head

        # Constraints 1 <= n <= sz, so you don't need to check if the index fits
        
        # Move fast ahead by n nodes so the difference between fast and slow is n
        for i in range(0, n):
            fast = fast.next

        # Move fast to the end of the list
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # Remove slow by setting previous to slow.next
        if slow == head:
            head = head.next
        else:
            prev.next = slow.next

        return head