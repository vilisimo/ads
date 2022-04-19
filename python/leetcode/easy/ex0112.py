# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Example 1:
#   Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: true
#   Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
#   Input: root = [1,2,3], targetSum = 5
#   Output: false
#   Explanation: There two root-to-leaf paths in the tree:
#       (1 --> 2): The sum is 3.
#       (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
#   Input: root = [], targetSum = 0
#   Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.


# Constraints:
#   The number of nodes in the tree is in the range [0, 5000].
#   -1000 <= Node.val <= 1000
#   -1000 <= targetSum <= 1000

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InitialRecursiveSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
           return False

        target = targetSum - root.val

        if target == 0 and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)



class InitialIterativeDfsSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right and value == targetSum:
                return True
            if node.right:
                stack.append((node.right, node.right.val + value))
            if node.left:
                stack.append((node.left, node.left.val + value))

        return False


class InitialIterativeBfsSolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, value = queue.popleft()
            if not node.left and not node.right and value == targetSum:
                return True
            if node.right:
                queue.append((node.right, node.right.val + value))
            if node.left:
                queue.append((node.left, node.left.val + value))

        return False
