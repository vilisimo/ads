import pytest

from leetcode.easy.ex0201_0300.ex0202 import InitialSolution, TwoPointerSolution


@pytest.mark.parametrize('number, happy', [
    (32, True),
    (31, True),
    (19, True),
    (13, True),
    (1, True),
    (2, False),
    (4, False),
    (5, False),
    (99, False),
    (750, False),
])
def test_determines_happiness(number: int, happy: bool):
    assert InitialSolution().isHappy(number) == happy
    assert TwoPointerSolution().isHappy(number) == happy
