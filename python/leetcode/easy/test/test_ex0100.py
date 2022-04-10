import pytest

from leetcode.easy.ex0100 import TreeNode, InitialSolution, RecursiveSolution, DepthFirstSearchSolution


def test_recognizes_same_short_trees():
    l1 = TreeNode(val=2)
    r1 = TreeNode(val=3)
    root1 = TreeNode(val=1, left=l1, right=r1)
    l2 = TreeNode(val=2)
    r2 = TreeNode(val=3)
    root2 = TreeNode(val=1, left=l2, right=r2)

    assert InitialSolution().isSameTree(root1, root2)
    assert RecursiveSolution().isSameTree(root1, root2)
    assert DepthFirstSearchSolution().isSameTree(root1, root2)


def test_recognizes_one_missing():
    root1 = None
    root2 = TreeNode(val=1)

    assert not InitialSolution().isSameTree(root1, root2)
    assert not RecursiveSolution().isSameTree(root1, root2)
    assert not DepthFirstSearchSolution().isSameTree(root1, root2)


def test_recognizes_null_trees():
    assert InitialSolution().isSameTree(None, None)
    assert RecursiveSolution().isSameTree(None, None)
    assert DepthFirstSearchSolution().isSameTree(None, None)


def test_recognizes_same_values_but_different_tree():
    r1 = TreeNode(val=2)
    root1 = TreeNode(val=1, right=r1)
    l2 = TreeNode(val=2)
    root2 = TreeNode(val=1, left=l2)

    assert not InitialSolution().isSameTree(root1, root2)
    assert not RecursiveSolution().isSameTree(root1, root2)
    assert not DepthFirstSearchSolution().isSameTree(root1, root2)

def test_recognizes_same_values_and_order_but_different_structure():
    l02 = TreeNode(val=1)
    l01 = TreeNode(val=2, left=l02)
    root1 = TreeNode(val=3, left=l01)

    l2 = TreeNode(val=1)
    r2 = TreeNode(val=3)
    root2 = TreeNode(val=2, left=l2, right=r2)

    assert not InitialSolution().isSameTree(root1, root2)
    assert not RecursiveSolution().isSameTree(root1, root2)
    assert not DepthFirstSearchSolution().isSameTree(root1, root2)


def test_recognizes_totally_different_trees():
    r2 = TreeNode(val=1)
    r1 = TreeNode(val=2, right=r2)
    root1 = TreeNode(val=3, right=r1)

    l2 = TreeNode(val=1)
    l1 = TreeNode(val=2, left=l2)
    root2 = TreeNode(val=3, left=l1)

    assert not InitialSolution().isSameTree(root1, root2)
    assert not RecursiveSolution().isSameTree(root1, root2)
    assert not DepthFirstSearchSolution().isSameTree(root1, root2)
