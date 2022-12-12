from leetcode.easy.ex0101_0200.ex0110 import TreeNode, InitialRecursiveSolution


def test_considers_none_to_be_balanced():
    root = None

    assert InitialRecursiveSolution().isBalanced(root)


def test_considers_tree_of_one_node_balanced():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().isBalanced(root)


def test_considers_tree_of_two_nodes_balanced():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert InitialRecursiveSolution().isBalanced(root)


def test_considers_tree_of_three_nodes_balanced():
    left = TreeNode(val=2)
    right = TreeNode(val=3)
    root = TreeNode(val=1, left=left, right=right)

    assert InitialRecursiveSolution().isBalanced(root)


def test_considers_skewed_three_node_tree_unabalanced():
    l21 = TreeNode(val=3)
    l11 = TreeNode(val=2, left=l21)
    root = TreeNode(val=1, left=l11)

    assert not InitialRecursiveSolution().isBalanced(root)


def test_considers_skewed_five_node_tree_to_be_balanced():
    l21 = TreeNode(val=3)
    l11 = TreeNode(val=2, left=l21)
    r21 = TreeNode(val=5)
    r11 = TreeNode(val=4, right = r21)
    root = TreeNode(val=1, left=l11, right=r11)

    assert InitialRecursiveSolution().isBalanced(root)


def test_considers_complex_skewed_tree_unbalanced():
    r32 = TreeNode(val=4)
    l31 = TreeNode(val=4)
    l22 = TreeNode(val=3)
    l21 = TreeNode(val=3, left=l31, right=r32)
    l11 = TreeNode(val=2, left=l21, right=l22)
    r11 = TreeNode(val=2)
    root = TreeNode(val=1, left=l11, right=r11)

    assert not InitialRecursiveSolution().isBalanced(root)
