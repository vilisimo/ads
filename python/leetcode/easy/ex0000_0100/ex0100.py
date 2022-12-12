# Given the roots of two binary trees p and q, write a function to check
# if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
# Example 1:
#   Input: p = [1,2,3], q = [1,2,3]
#   Output: true
#
# Example 2:
#   Input: p = [1,2], q = [1,null,2]
#   Output: false
#
# Example 3:
#   Input: p = [1,2,1], q = [1,1,2]
#   Output: false
#
# Constraints:
#   The number of nodes in both trees is in the range [0, 100].
#   -10^4 <= Node.val <= 10^4

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True

        stack_p, stack_q = [], []
        current_p, current_q = p, q
        while current_p and current_q or (stack_p and stack_q):
            while current_p and current_q:
                stack_p.append(current_p)
                stack_q.append(current_q)
                current_p = current_p.left
                current_q = current_q.left

            if (current_p and not current_q) or (not current_p and current_q):
                return False

            current_p = stack_p.pop()
            current_q = stack_q.pop()

            if current_p.val != current_q.val:
                return False

            current_p = current_p.right
            current_q = current_q.right

            if (current_p and not current_q) or (not current_p and current_q):
                return False

        return p and q


class RecursiveSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class DepthFirstSearchSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False

            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True
