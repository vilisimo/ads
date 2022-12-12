import pytest

from leetcode.easy.ex0000_0100.ex0067 import LookedUpSolution, BuiltInSolution, WhileSolution


@pytest.mark.parametrize('a, b, expected', [
    ('11', '1', '100'),
    ('1010', '1011', '10101'),
    ('100101', '10101', '111010'),
    ('1010', '11', '1101'),
])
def test_adds_binary_numbers(a: str, b: str, expected: str):
    result = LookedUpSolution().addBinary(a, b)
    assert result == expected

    result = BuiltInSolution().addBinary(a, b)
    assert result == expected

    result = WhileSolution().addBinary(a, b)
    assert result == expected
