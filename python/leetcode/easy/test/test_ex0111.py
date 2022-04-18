from leetcode.easy.ex0111 import (
    TreeNode,
    InitialRecursiveSolution,
    ImprovedRecursiveSolution,
    InitialIterativeSolution,
)


def test_finds_depth_when_no_nodes_given():
    assert InitialRecursiveSolution().minDepth(None) == 0
    assert ImprovedRecursiveSolution().minDepth(None) == 0
    assert InitialIterativeSolution().minDepth(None) == 0


def test_finds_depth_of_one():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().minDepth(root) == 1
    assert ImprovedRecursiveSolution().minDepth(root) == 1
    assert InitialIterativeSolution().minDepth(root) == 1


def test_finds_depth_of_two_when_no_other_subtrees_present():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert InitialRecursiveSolution().minDepth(root) == 2
    assert ImprovedRecursiveSolution().minDepth(root) == 2
    assert InitialIterativeSolution().minDepth(root) == 2


def test_finds_depth_of_two_when_longer_tree_exists():
    l11 = TreeNode(val=3)
    l01 = TreeNode(val=2, left=l11)
    r01 = TreeNode(val=4)
    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().minDepth(root) == 2
    assert ImprovedRecursiveSolution().minDepth(root) == 2
    assert InitialIterativeSolution().minDepth(root) == 2


def test_finds_depth_when_subtrees_are_the_same():
    left = TreeNode(val=3)
    right = TreeNode(val=2)
    root = TreeNode(val=1, left=left, right=right)

    assert InitialRecursiveSolution().minDepth(root) == 2
    assert ImprovedRecursiveSolution().minDepth(root) == 2
    assert InitialIterativeSolution().minDepth(root) == 2


def test_finds_depth_of_complex_tree():
    r12 = TreeNode(val=7)
    r11 = TreeNode(val=15)
    r01 = TreeNode(val=20, left=r11, right=r12)
    l01 = TreeNode(val=9)
    root = TreeNode(val=3, left=l01, right=r01)

    assert InitialRecursiveSolution().minDepth(root) == 2
    assert ImprovedRecursiveSolution().minDepth(root) == 2
    assert InitialIterativeSolution().minDepth(root) == 2


def test_finds_depth_of_skewed_tree():
    l41 = TreeNode(val=5)
    l31 = TreeNode(val=4, left=l41)
    l21 = TreeNode(val=3, left=l31)
    l11 = TreeNode(val=2, left=l21)
    root = TreeNode(val=1, left=l11)

    assert InitialRecursiveSolution().minDepth(root) == 5
    assert ImprovedRecursiveSolution().minDepth(root) == 5
    assert InitialIterativeSolution().minDepth(root) == 5
