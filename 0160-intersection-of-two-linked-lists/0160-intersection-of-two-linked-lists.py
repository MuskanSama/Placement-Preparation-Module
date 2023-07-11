# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1

        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getLength(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
