# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hcf(self, a, b=0):
        if b == 0:
            return a
        return self.hcf(b, a % b)

    def insertGreatestCommonDivisors(self, head):
        # Corrected base case: if head is None or head.next is None, return head
        if head is None or head.next is None:
            return head

        # Calculate GCD of the current node and the next node
        temp = ListNode(self.hcf(head.val, head.next.val))

        # Insert the new node between the current and the next node
        temp.next = head.next
        head.next = temp

        # Recursively call the function for the next original node (skip the newly inserted node)
        self.insertGreatestCommonDivisors(temp.next)

        return head
