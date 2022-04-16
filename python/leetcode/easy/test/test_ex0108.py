from leetcode.easy.ex0108 import TreeNode, InitialRecursiveSolution, ImprovedRecursiveSolution


def test_builds_tree_from_one_element():
    elements = [1]

    result = InitialRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 1
    assert not result.left
    assert not result.right

    result = ImprovedRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 1
    assert not result.left
    assert not result.right


def test_builds_tree_from_two_elements():
    elements = [1, 2]

    result = InitialRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 2
    assert result.left.val == 1
    assert not result.left.left
    assert not result.left.right
    assert not result.right

    result = ImprovedRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 2
    assert result.left.val == 1
    assert not result.left.left
    assert not result.left.right
    assert not result.right



def test_builds_tree_from_three_elements():
    elements = [1, 2, 3]

    result = InitialRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3
    assert not result.left.left
    assert not result.left.right
    assert not result.right.left
    assert not result.right.right

    result = ImprovedRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3
    assert not result.left.left
    assert not result.left.right
    assert not result.right.left
    assert not result.right.right


def test_builds_tre_from_multiple_elements():
    elements = [-10,-3,0,5,9]

    result = InitialRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 0
    assert result.left.val == -3
    assert result.left.left.val == -10
    assert result.right.val == 9
    assert result.right.left.val == 5

    result = ImprovedRecursiveSolution().sortedArrayToBST(elements)
    assert result.val == 0
    assert result.left.val == -3
    assert result.left.left.val == -10
    assert result.right.val == 9
    assert result.right.left.val == 5
