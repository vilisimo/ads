# Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.

# Example 1:
#   Input: head = [1,2,6,3,4,5,6], val = 6
#   Output: [1,2,3,4,5]

# Example 2:
#   Input: head = [], val = 1
#   Output: []

# Example 3:
#   Input: head = [7,7,7,7], val = 7
#   Output: []

# Constraints:
#   The number of nodes in the list is in the range [0, 10^4].
#   1 <= Node.val <= 50
#   0 <= val <= 50

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class InitialSolution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        if not head:
            return None

        prev, curr = head, head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return head


class DummyNodeSolution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)

        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
