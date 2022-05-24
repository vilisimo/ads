import pytest

from leetcode.easy.ex0217 import InitialSolution, SortingSolution


@pytest.mark.parametrize('array, expected', [
    ([], False),
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 1], True),
    ([1], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
])
def test_recognizes_duplicate(array: list[int], expected: bool):
    assert InitialSolution().containsDuplicate(array) == expected


@pytest.mark.parametrize('array, expected', [
    ([], False),
    ([3, 1, 2, 4], False),
    ([2, 1, 3, 1], True),
    ([1], False),
    ([2, 1, 1, 3, 1, 3, 3, 4, 4, 2], True),
])
def test_recognizes_duplicate_with_sorted_solution(array: list[int], expected: bool):
    assert SortingSolution().containsDuplicate(array) == expected
