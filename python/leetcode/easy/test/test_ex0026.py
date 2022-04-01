import pytest

from leetcode.easy.ex0026 import InitialSolution, ImprovedSolution


@pytest.mark.parametrize('input, expected', [
    ([1], [1]),
    ([1, 1, 2], [1, 2]),
    ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([-100, 11, 22, 99], [-100, 11, 22, 99]),
    ([1, 1, 1, 1], [1]),
    ([1, 2, 2, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 2], [1, 2]),
])
def test_removes_duplicates(input: list[int], expected: int):
    k = InitialSolution().removeDuplicates(input)

    assert len(expected) == k
    assert input[:len(expected)] == expected

    k = ImprovedSolution().removeDuplicates(input)

    assert len(expected) == k
    assert input[:len(expected)] == expected

