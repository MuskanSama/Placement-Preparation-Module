# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        # Initialize the two pointers
        first = dummy
        second = dummy

        # Move the first pointer n+1 nodes ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node by adjusting the pointers
        second.next = second.next.next

        # Return the head of the modified list (excluding the dummy node)
        return dummy.next
        