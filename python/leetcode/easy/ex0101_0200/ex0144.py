# Given the root of a binary tree, return the preorder
# traversal of its nodes' values.

# Input: root = [1,null,2,3]
#   Output: [1,2,3]

# Example 2:
#   Input: root = []
#   Output: []

# Example 3:
#   Input: root = [1]
#   Output: [1]

# Constraints:
#   The number of nodes in the tree is in the range [0, 100].
#   -100 <= Node.val <= 100

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)

        return result

    def traverse(self, node: Optional[TreeNode], result: list[int]) -> List[int]:
        if not node:
            return

        result.append(node.val)
        self.traverse(node.left, result)
        self.traverse(node.right, result)


class InitialStackSolution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack, result = [], []
        while stack or current:
            while current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            current = stack.pop()
            current = current.right

        return result


class ImprovedInitialStackSolution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack, result = [], []
        while stack or current:
            while current:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            current = stack.pop()

        return result


class ImprovedWhileLoopStackSolution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if not node:
                continue

            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return result
