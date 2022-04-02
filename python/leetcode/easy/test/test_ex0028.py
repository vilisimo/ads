import pytest

from leetcode.easy.ex0028 import BuiltInSolution, NoBuiltInSolution


@pytest.mark.parametrize('haystack, needle, expected', [
    ("hello", "ll", 2),
    ("aaaaaaa", "a", 0),
    ("42839 18", " ", 5),
    ("verylongstring", "long", 4),
    ("aaaaaaa", "bba", -1),
    ("a", "aa", -1),
    ("aaaa", "aaa", 0),
])
def test_finds_index_of_a_string(haystack: str, needle: str, expected: int):
    result = BuiltInSolution().strStr(haystack, needle)
    assert result == expected

    result = NoBuiltInSolution().strStr(haystack, needle)
    assert result == expected
