import pytest

from leetcode.easy.ex0101_0200.ex0171 import InitialSolution



@pytest.mark.parametrize('title, expected', [
    ('A', 1),
    ('B', 2),
    ('C', 3),
    ('Z', 26),
    ('AA', 27),
    ('AB', 28),
    ('ZA', 677),
    ('ZY', 701),
    ('AAB', 704),
])
def test_transforms_to_number(title: str, expected: int):
    assert InitialSolution().titleToNumber(title) == expected
