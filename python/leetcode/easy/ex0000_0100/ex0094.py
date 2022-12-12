# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [1,3,2]
#
# Example 2:
#   Input: root = []
#   Output: []
#
# Example 3:
#   Input: root = [1]
#   Output: [1]

# Constraints:
#   The number of nodes in the tree is in the range [0, 100].
#   -100 <= Node.val <= 100

# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node: TreeNode, result: list[int]):
        if node.left: self.traverse(node.left, result)
        result.append(node.val)
        if node.right: self.traverse(node.right, result)


class StackSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, result = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
