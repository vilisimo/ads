from leetcode.easy.ex0145 import InitialRecursiveSolution, IterativeSolution, TreeNode


def test_returns_empty_list_for_null():
    assert InitialRecursiveSolution().postorderTraversal(None) == []
    assert IterativeSolution().postorderTraversal(None) == []


def test_returns_same_node_for_single_element_tree():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().postorderTraversal(root) == [1]
    assert IterativeSolution().postorderTraversal(root) == [1]


def test_returns_post_order_for_simple_three_level_tree():
    l11 = TreeNode(val=3)
    r01 = TreeNode(val=2, left=l11)
    root = TreeNode(val=1, right=r01)

    assert InitialRecursiveSolution().postorderTraversal(root) == [3, 2, 1]
    assert IterativeSolution().postorderTraversal(root) == [3, 2, 1]


def test_returns_post_order_for_simple_two_level_tree():
    l01 = TreeNode(val=3)
    r01 = TreeNode(val=2)
    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().postorderTraversal(root) == [3, 2, 1]
    assert IterativeSolution().postorderTraversal(root) == [3, 2, 1]


def test_returns_post_order_for_complex_deep_tree():
    l21 = TreeNode(val=8)
    l11 = TreeNode(val=4)
    l12 = TreeNode(val=5, left=l21)
    l01 = TreeNode(val=2, left=l11, right=l12)

    r22 = TreeNode(val=9)
    r11 = TreeNode(val=6, right=r22)
    r12 = TreeNode(val=7)
    r01 = TreeNode(val=3, left=r11, right=r12)

    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().postorderTraversal(root) == [4, 8, 5, 2, 9, 6, 7, 3, 1]
    assert IterativeSolution().postorderTraversal(root) == [4, 8, 5, 2, 9, 6, 7, 3, 1]
