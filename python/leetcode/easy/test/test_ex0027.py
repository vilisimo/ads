import pytest

from leetcode.easy.ex0027 import InitialSolution


@pytest.mark.parametrize('nums, val, expected', [
    ([3 ,2, 2, 3], 3, [2, 2]),
    ([3, 2, 2, 3, 4, 4], 3, [2, 2, 4, 4]),
    ([1, 2, 3, 4, 5], 2, [1, 3, 4, 5]),
    ([1], 2, [1]),
    ([1, 1], 1, []),
])
def test_removes(nums: list[int], val: int, expected: int):
    k = InitialSolution().removeElement(nums, val)

    result = sorted(nums[0:k])

    assert result == expected
