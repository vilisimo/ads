from leetcode.easy.ex0112 import (
    TreeNode,
    InitialRecursiveSolution,
    InitialIterativeDfsSolution,
    InitialIterativeBfsSolution,
)


def test_returns_false_for_none_input():
    root = None

    assert not InitialRecursiveSolution().hasPathSum(root, 0)
    assert not InitialIterativeDfsSolution().hasPathSum(root, 0)
    assert not InitialIterativeBfsSolution().hasPathSum(root, 0)


def test_returns_false_for_single_node_and_correct_value():
    root = TreeNode(val=3)

    assert InitialRecursiveSolution().hasPathSum(root, root.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val)


def test_returns_false_for_single_node_and_different_value():
    root = TreeNode(val=3)

    assert not InitialRecursiveSolution().hasPathSum(root, root.val + 1)
    assert not InitialIterativeDfsSolution().hasPathSum(root, root.val + 1)
    assert not InitialIterativeBfsSolution().hasPathSum(root, root.val + 1)


def test_returns_false_for_two_level_balanced_tree():
    right = TreeNode(val=3)
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left, right=right)

    assert not InitialRecursiveSolution().hasPathSum(root, 5)
    assert not InitialIterativeDfsSolution().hasPathSum(root, 5)
    assert not InitialIterativeBfsSolution().hasPathSum(root, 5)


def test_returns_false_for_simple_right_tree_when_root_already_has_requested_value():
    right = TreeNode(val=2)
    root = TreeNode(val=1, right=right)

    assert not InitialRecursiveSolution().hasPathSum(root, 1)
    assert not InitialIterativeDfsSolution().hasPathSum(root, 1)
    assert not InitialIterativeBfsSolution().hasPathSum(root, 1)


def test_returns_false_for_simple_left_tree_when_root_already_has_requested_value():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert not InitialRecursiveSolution().hasPathSum(root, 1)
    assert not InitialIterativeDfsSolution().hasPathSum(root, 1)
    assert not InitialIterativeBfsSolution().hasPathSum(root, 1)


def test_returns_true_for_simple_tree_when_root_has_value_but_child_has_zero():
    left = TreeNode(val=0)
    root = TreeNode(val=1, left=left)

    assert InitialRecursiveSolution().hasPathSum(root, 1)
    assert InitialIterativeDfsSolution().hasPathSum(root, 1)
    assert InitialIterativeBfsSolution().hasPathSum(root, 1)


def test_returns_true_for_skewed_tree():
    l21 = TreeNode(val=3)
    l11 = TreeNode(val=2, left=l21)
    root = TreeNode(val=1, left=l11)

    assert InitialRecursiveSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val + l11.val + l21.val)


def test_returns_true_for_balanced_tree():
    l22 = TreeNode(val=4)
    l21 = TreeNode(val=3)
    l11 = TreeNode(val=2, left=l21, right=l22)

    r22 = TreeNode(val=8)
    r21 = TreeNode(val=6)
    r11 = TreeNode(val=4, left=r21, right=r22)

    root = TreeNode(val=1, left=l11, right=r11)

    assert InitialRecursiveSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val + l11.val + l21.val)


def test_returns_true_when_multiple_paths_exist():
    l22 = TreeNode(val=4)
    l21 = TreeNode(val=3)
    l11 = TreeNode(val=2, left=l21, right=l22)

    r22 = TreeNode(val=4)
    r21 = TreeNode(val=3)
    r11 = TreeNode(val=2, left=r21, right=r22)

    root = TreeNode(val=1, left=l11, right=r11)

    assert InitialRecursiveSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val + l11.val + l21.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val + l11.val + l21.val)


def test_returns_true_for_complex_tree():
    l32 = TreeNode(val=2)
    l31 = TreeNode(val=7)
    l21 = TreeNode(val=11, left=l31, right=l32)
    l11 = TreeNode(val=4, left=l21)

    r31 = TreeNode(val=1)
    r22 = TreeNode(val=4, right=r31)
    r21 = TreeNode(val=13)
    r11 = TreeNode(val=8, left=r21, right=r22)

    root = TreeNode(val=5, left=l11, right=r11)

    assert InitialRecursiveSolution().hasPathSum(root, root.val + l11.val + l21.val + l32.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val + l11.val + l21.val + l32.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val + l11.val + l21.val + l32.val)


def test_handles_negative_numbers():
    l32 = TreeNode(val=8)
    l31 = TreeNode(val=9)
    l21 = TreeNode(val=7, left=l31, right=l32)
    l11 = TreeNode(val=6, left=l21)

    r32 = TreeNode(val=-9)
    r22 = TreeNode(val=5, right=r32)
    r21 = TreeNode(val=-3)
    r11 = TreeNode(val=-2, left=r21, right=r22)

    root = TreeNode(val=1, left=l11, right=r11)

    assert InitialRecursiveSolution().hasPathSum(root, root.val + r11.val + r22.val + r32.val)
    assert InitialIterativeDfsSolution().hasPathSum(root, root.val + r11.val + r22.val + r32.val)
    assert InitialIterativeBfsSolution().hasPathSum(root, root.val + r11.val + r22.val + r32.val)
