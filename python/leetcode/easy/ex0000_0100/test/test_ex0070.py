import pytest

from leetcode.easy.ex0000_0100.ex0070 import LookedUpSolution


@pytest.mark.parametrize('input, expected', [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
])
def test_calculates_ways(input: int, expected: int):
    result = LookedUpSolution().climbStairs(input)
    assert result == expected
