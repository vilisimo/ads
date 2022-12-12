from leetcode.easy.ex0101_0200.ex0101 import InitialRecursiveSolution, InitialIterativeSolution, TreeNode


def test_recognizes_symmetric_tree_of_one_node():
    root = TreeNode(val=1)

    assert InitialRecursiveSolution().isSymmetric(root)
    assert InitialIterativeSolution().isSymmetric(root)


def test_recognizes_symmetric_tree_of_three_nodes():
    left = TreeNode(val=2)
    right = TreeNode(val=2)
    root = TreeNode(val=1, left=left, right=right)

    assert InitialRecursiveSolution().isSymmetric(root)
    assert InitialIterativeSolution().isSymmetric(root)


def test_recognizes_symmetric_tree_of_five_nodes():
    l11 = TreeNode(val=3)
    l01 = TreeNode(val=2, left=l11)

    r11 = TreeNode(val=3)
    r01 = TreeNode(val=2, right=r11)

    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().isSymmetric(root)
    assert InitialIterativeSolution().isSymmetric(root)


def test_recognizes_symmetric_tree_of_seven_nodes():
    l11 = TreeNode(val=3)
    l12 = TreeNode(val=4)
    l01 = TreeNode(val=2, left=l11, right=l12)

    r11 = TreeNode(val=4)
    r12 = TreeNode(val=3)
    r01 = TreeNode(val=2, left=r11, right=r12)

    root = TreeNode(val=1, left=l01, right=r01)

    assert InitialRecursiveSolution().isSymmetric(root)
    assert InitialIterativeSolution().isSymmetric(root)


def test_recognizes_asymmetric_tree_of_two_nodes():
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)

    assert not InitialRecursiveSolution().isSymmetric(root)
    assert not InitialIterativeSolution().isSymmetric(root)


def test_recognizes_asymmetric_tree_of_three_nodes_but_different_values():
    left = TreeNode(val=2)
    right = TreeNode(val=3)
    root = TreeNode(val=1, left=left, right=right)

    assert not InitialRecursiveSolution().isSymmetric(root)
    assert not InitialIterativeSolution().isSymmetric(root)


def test_recognizes_asymmetric_tree_of_five_nodes_same_values_but_different_structure():
    l11 = TreeNode(val=3)
    l01 = TreeNode(val=2, right=l11)

    r11 = TreeNode(val=3)
    r01 = TreeNode(val=2, right=r11)

    root = TreeNode(val=1, left=l01, right=r01)

    assert not InitialRecursiveSolution().isSymmetric(root)
    assert not InitialIterativeSolution().isSymmetric(root)
