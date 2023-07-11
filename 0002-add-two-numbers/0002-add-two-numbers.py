# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # Dummy node to hold the result
        current = dummy  # Pointer to the current node in the result
        carry = 0  # Carry to be added in the next iteration

        while l1 or l2:
            # Get the values of the current nodes or 0 if the nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits along with the carry
            total = val1 + val2 + carry

            # Update the carry and create a new node with the sum digit
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next nodes in the input lists and the result list
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next

        # If there's a remaining carry, add a new node with the carry
        if carry > 0:
            current.next = ListNode(carry)

        # Return the head of the result list (excluding the dummy node)
        return dummy.next
