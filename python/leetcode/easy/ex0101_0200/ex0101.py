# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
# Example 1:
#   Input: root = [1,2,2,3,4,4,3]
#   Output: true
#
# Example 2:
#   Input: root = [1,2,2,null,3,null,3]
#   Output: false
#
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
#   -100 <= Node.val <= 100
#
# Follow up: Could you solve it both recursively and iteratively?

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == root.right:
            return True
        return self.check(root.left, root.right)

    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)


class InitialIterativeSolution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False

            stack.append((l.left, r.right))
            stack.append((l.right, r.left))

        return True
