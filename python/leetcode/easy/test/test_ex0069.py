import pytest

from leetcode.easy.ex0069 import InitialSolution


@pytest.mark.parametrize('input, expected', [
    (0, 0),
    (1, 1),
    (4, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (15, 3),
    (33, 5),
    (99, 9),
])
def test_finds_square_root(input: int, expected: int):
    result = InitialSolution().mySqrt(input)
    assert result == expected
