import pytest

from leetcode.easy.ex0101_0200.ex0169 import (
    BoyerMooreVotingSolution,
    BuiltInSolution,
    HashMapSolution,
    SortingSolution,
)


@pytest.mark.parametrize('elements, expected', [
    ([1], 1),
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1, 1, 1, 2, 2, 2, 2], 2),
    ([3, 3, 3, 3, 2, 2, 1], 3),
    ([1, 2, 3, 1, 2, 3, 2, 2], 2),
    ([1, 2, 2, 2, 3, 1, 4, 2], 2),
])
def test_finds_majority_element(elements: list[int], expected: int):
    assert BuiltInSolution().majorityElement(elements) == expected
    assert HashMapSolution().majorityElement(elements) == expected
    assert SortingSolution().majorityElement(elements) == expected
    assert BoyerMooreVotingSolution().majorityElement(elements) == expected
