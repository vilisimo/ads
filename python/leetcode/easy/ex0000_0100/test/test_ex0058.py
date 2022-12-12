import pytest

from leetcode.easy.ex0000_0100.ex0058 import InitialSolution


@pytest.mark.parametrize('input, expected', [
    ('Hello World', 5),
    ('   fly me   to   the moon  ', 4),
    ('luffy is still joyboy', 6),
    ('a sentence without whitespaces', 11),
    ('   a sentence   with white       spaces  ', 6),
    ('   a ', 1),
    ('a', 1),
])
def test_finds_length(input: str, expected: int):
    result = InitialSolution().lengthOfLastWord(input)
    assert result == expected
