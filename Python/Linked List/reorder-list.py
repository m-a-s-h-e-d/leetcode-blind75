# https://leetcode.com/problems/reorder-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # Need a slow pointer and a fast pointer to find the half-way point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        current = slow.next
        previous = slow.next = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

        # Now that second half is reversed we can slot them in the right place from the start
        current = head
        second = previous
        while second:
            temp1 = current.next
            temp2 = second.next
            current.next = second
            second.next = temp1
            current = temp1
            second = temp2

