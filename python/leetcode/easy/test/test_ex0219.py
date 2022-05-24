import pytest

from leetcode.easy.ex0219 import InitialSolution, SlidingWindowSolution


@pytest.mark.parametrize('array, k, expected', [
    ([1, 1], 1, True),
    ([1, 1], 0, False),
    ([1, 1, 1], 1, True),
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
    ([1, 2, 3, 1, 2, 1], 2, True),

])
def test_recognizes_duplicate(array: list[int], k: int, expected: bool):
    assert InitialSolution().containsNearbyDuplicate(array, k) == expected
    assert SlidingWindowSolution().containsNearbyDuplicate(array, k) == expected
