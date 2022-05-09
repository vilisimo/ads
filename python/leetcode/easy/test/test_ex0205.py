import pytest

from leetcode.easy.ex0205 import DictSetSolution, LengthComparisonSolution, ArraySolution


@pytest.mark.parametrize('s, t, expected', [
    ('foo', 'bar', False),
    ('egg', 'add', True),
    ('a', 'b', True),
    ('aaabba', 'cccddc', True),
    ('paper', 'title', True),
    ('tiger', 'tiger', True),
    ('rhino', 'tiger', True),
    ('car', 'baa', False),
])
def test_recognizes_isomorphic_string(s: str, t: str, expected: bool):
    assert DictSetSolution().isIsomorphic(s, t) == expected
    assert LengthComparisonSolution().isIsomorphic(s, t) == expected
    assert ArraySolution().isIsomorphic(s, t) == expected
