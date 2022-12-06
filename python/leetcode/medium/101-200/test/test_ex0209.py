import pytest

from ex0209 import InitialSolution


@pytest.mark.parametrize("target, nums, expected", [
    (7, [2,3,1,2,4,3], 2),
    (4, [1, 4, 4], 1),
    (11, [1,1,1,1,1,1,1,1], 0),
    (10, [10, 0, 0, 9, 1], 1),
    (10, [10], 1),
    (3, [2], 0),
    (1, [0], 0),
])
def test_initial_finds_subarray(target: int, nums: list[int], expected: int):
    result = InitialSolution().minSubArrayLen(target, nums)
    assert result == expected
