import pytest

from leetcode.easy.ex0104 import (
    InitialRecursiveSolution,
    ImproveddRecursiveSolution,
    InitialIterativeSolution,
    TreeNode,
)



def test_null_tree():
    assert InitialRecursiveSolution().maxDepth(None) == 0
    assert InitialIterativeSolution().maxDepth(None) == 0
    assert ImproveddRecursiveSolution().maxDepth(None) == 0

def test_single_level_tree():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().maxDepth(root) == 1
    assert InitialIterativeSolution().maxDepth(root) == 1
    assert ImproveddRecursiveSolution().maxDepth(root) == 1


def test_two_level_tree():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert InitialRecursiveSolution().maxDepth(root) == 2
    assert InitialIterativeSolution().maxDepth(root) == 2
    assert ImproveddRecursiveSolution().maxDepth(root) == 2


def test_two_level_symmetrical_tree():
    left = TreeNode(val=2)
    right = TreeNode(val=3)
    root = TreeNode(val=1, left=left, right=right)

    assert InitialRecursiveSolution().maxDepth(root) == 2
    assert InitialIterativeSolution().maxDepth(root) == 2
    assert ImproveddRecursiveSolution().maxDepth(root) == 2


def test_multi_level_tree():
    l01 = TreeNode(val=2)

    r11 = TreeNode(val=4)
    r12 = TreeNode(val=5)
    r01 = TreeNode(val=3, left=r11, right=r12)

    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().maxDepth(root) == 3
    assert InitialIterativeSolution().maxDepth(root) == 3
    assert ImproveddRecursiveSolution().maxDepth(root) == 3


def test_multi_level_balanced_tree():
    l11 = TreeNode(val=7)
    l12 = TreeNode(val=6)
    l01 = TreeNode(val=5, left=l11, right=l12)

    r11 = TreeNode(val=4)
    r12 = TreeNode(val=3)
    r01 = TreeNode(val=2, left=r11, right=r12)

    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().maxDepth(root) == 3
    assert InitialIterativeSolution().maxDepth(root) == 3
    assert ImproveddRecursiveSolution().maxDepth(root) == 3
