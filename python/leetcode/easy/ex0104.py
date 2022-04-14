# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.

# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: 3

# Example 2:
#   Input: root = [1,null,2]
#   Output: 2

# Constraints:
#   The number of nodes in the tree is in the range [0, 10^4].
#   -100 <= Node.val <= 100

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calculate(root, depth=0)

    def calculate(self, root: Optional[TreeNode], depth: int) -> tuple[int]:
        if not root:
            return depth

        current_depth = depth + 1
        left_depth = self.calculate(root.left, current_depth)
        right_depth = self.calculate(root.right, current_depth)

        return max(left_depth, right_depth)


class ImproveddRecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class InitialIterativeSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        depth = 0
        while stack:
            next_level = []
            while stack:
                node = stack.pop()
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            stack = next_level
            depth += 1

        return depth
