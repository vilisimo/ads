import pytest

from leetcode.easy.ex0168 import Solution


@pytest.mark.parametrize('number, expected', [
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (26, 'Z'),
    (27, 'AA'),
    (28, 'AB'),
    (677, 'ZA'),
    (701, 'ZY'),
    (704, 'AAB'),
])
def test_converts_to_column(number: int, expected: str):
    assert Solution().convertToTitle(number) == expected
