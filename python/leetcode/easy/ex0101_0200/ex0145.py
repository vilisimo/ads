# Given the root of a binary tree, return the postorder traversal
# of its nodes' values.

# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [3,2,1]

# Example 2:
#   Input: root = []
#   Output: []

# Example 3:
#   Input: root = [1]
#   Output: [1]

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)

        return result

    def traverse(self, node: Optional[TreeNode], result: list[int]) -> None:
        if not node:
            return

        self.traverse(node.left, result)
        self.traverse(node.right, result)
        result.append(node.val)


class IterativeSolution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        current, pre = root, None
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack[-1]
            if not current.right or current.right == pre:
                result.append(current.val)
                stack.pop()
                pre = current
                current = None
            else:
                current = current.right

        return result
