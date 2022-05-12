# Given the head of a singly linked list, reverse the list, and return the
# reversed list.

# Example 1:
#   Input: head = [1,2,3,4,5]
#   Output: [5,4,3,2,1]

# Example 2:
#   Input: head = [1,2]
#   Output: [2,1]

# Example 3:
#   Input: head = []
#   Output: []

# Constraints:
#   The number of nodes in the list is the range [0, 5000].
#   -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class InitialIterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev



class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node
