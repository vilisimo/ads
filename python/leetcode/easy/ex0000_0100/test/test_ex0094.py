from leetcode.easy.ex0000_0100.ex0094 import TreeNode, InitialRecursiveSolution, StackSolution


def test_traverses_one_element():
    root = TreeNode(val=1)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [1]

    result = StackSolution().inorderTraversal(root)
    assert result == [1]


def test_traverses_tree_with_left_child():
    child = TreeNode(val=2)
    root = TreeNode(val=1, left=child)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [2, 1]

    result = StackSolution().inorderTraversal(root)
    assert result == [2, 1]


def test_traverses_tree_with_right_child():
    child = TreeNode(val=2)
    root = TreeNode(val=1, right=child)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [1, 2]

    result = StackSolution().inorderTraversal(root)
    assert result == [1, 2]


def test_traverses_tree_with_both_children():
    left = TreeNode(val=2)
    right = TreeNode(val=3)
    root = TreeNode(val=1, left=left, right=right)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [2, 1, 3]

    result = StackSolution().inorderTraversal(root)
    assert result == [2, 1, 3]


def test_traverses_tree_with_long_right_branch():
    child = TreeNode(val=3)
    parent = TreeNode(val=2, left=child)
    root = TreeNode(val=1, right=parent)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [1, 3, 2]

    result = StackSolution().inorderTraversal(root)
    assert result == [1, 3, 2]


def test_traverses_tree_with_long_left_branch():
    child = TreeNode(val=3)
    parent = TreeNode(val=2, left=child)
    root = TreeNode(val=1, left=parent)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [3, 2, 1]

    result = StackSolution().inorderTraversal(root)
    assert result == [3, 2, 1]


def test_traverses_complex_tree():
    c4 = TreeNode(val=8)
    c3 = TreeNode(val=7)
    p2 = TreeNode(val=6, left=c3, right=c4)

    gc1 = TreeNode(val=5)
    c2 = TreeNode(val=4, left=gc1)
    c1 = TreeNode(val=3)
    p1 = TreeNode(val=2, left=c1, right=c2)

    root = TreeNode(val=1, left=p1, right=p2)

    result = InitialRecursiveSolution().inorderTraversal(root)
    assert result == [3, 2, 5, 4, 1, 7, 6, 8]

    result = StackSolution().inorderTraversal(root)
    assert result == [3, 2, 5, 4, 1, 7, 6, 8]


