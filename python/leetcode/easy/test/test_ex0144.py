import pytest
from typing import Optional

from leetcode.easy.ex0144 import (
    ImprovedInitialStackSolution,
    ImprovedWhileLoopStackSolution,
    InitialRecursiveSolution,
    InitialStackSolution,
    TreeNode,
)


@pytest.mark.parametrize('root', [[], None])
def test_does_not_traverse_missing_tree(root: Optional[list]):
    assert InitialRecursiveSolution().preorderTraversal(root) == []
    assert InitialStackSolution().preorderTraversal(root) == []
    assert ImprovedInitialStackSolution().preorderTraversal(root) == []
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == []


def test_traverses_one_node_tree():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().preorderTraversal(root) == [1]
    assert InitialStackSolution().preorderTraversal(root) == [1]
    assert ImprovedInitialStackSolution().preorderTraversal(root) == [1]
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == [1]


def test_traverses_two_node_tree():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert InitialRecursiveSolution().preorderTraversal(root) == [1, 2]
    assert InitialStackSolution().preorderTraversal(root) == [1, 2]
    assert ImprovedInitialStackSolution().preorderTraversal(root) == [1, 2]
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == [1, 2]


def test_traverses_three_node_tree_without_branching():
    r11 = TreeNode(val=3)
    r01 = TreeNode(val=2, left=r11)
    root = TreeNode(val=1, right=r01)

    assert InitialRecursiveSolution().preorderTraversal(root) == [1, 2, 3]
    assert InitialStackSolution().preorderTraversal(root) == [1, 2, 3]
    assert ImprovedInitialStackSolution().preorderTraversal(root) == [1, 2, 3]
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == [1, 2, 3]


def test_traverses_three_node_tree_with_branching():
    left = TreeNode(val=2)
    right = TreeNode(val=3)
    root = TreeNode(val=1, left=left, right=right)

    assert InitialRecursiveSolution().preorderTraversal(root) == [1, 2, 3]
    assert InitialStackSolution().preorderTraversal(root) == [1, 2, 3]
    assert ImprovedInitialStackSolution().preorderTraversal(root) == [1, 2, 3]
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == [1, 2, 3]


def test_traverses_complicated_tree():
    l12 = TreeNode(val=5)
    l11 = TreeNode(val=4)
    l01 = TreeNode(val=2, left=l11, right=l12)
    r01 = TreeNode(val=3)
    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().preorderTraversal(root) == [1, 2, 4, 5, 3]
    assert InitialStackSolution().preorderTraversal(root) == [1, 2, 4, 5, 3]
    assert ImprovedInitialStackSolution().preorderTraversal(root) == [1, 2, 4, 5, 3]
    assert ImprovedWhileLoopStackSolution().preorderTraversal(root) == [1, 2, 4, 5, 3]
