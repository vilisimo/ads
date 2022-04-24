import pytest

from leetcode.easy.ex0136 import BitSolution


@pytest.mark.parametrize('numbers, expected', [
    ([1, 1, 2, 2, 3], 3),
    ([1], 1),
    ([1, 2, 2], 1),
    ([2, 1, 2], 1),
    ([3, 2, 1, 2, 3], 1),
    ([4, 1, 2, 1, 2], 4),
    ([-4, -1, -2, -1, -2], -4),
    ([-4, -1, -2, 1, -1, -2, 1], -4),
])
def test_finds_number(numbers: list[int], expected: int):
    assert BitSolution().singleNumber(numbers) == expected
