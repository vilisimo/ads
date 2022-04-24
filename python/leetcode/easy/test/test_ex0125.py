import pytest

from leetcode.easy.ex0125 import InitialSolution


@pytest.mark.parametrize("chars, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("amanaplanacanalpanama", True),
    ("race a car", False),
    ("sedek uzu kedes", True),
    ("arbaabra", True),
    ("", True),
    (" ", True),
    ("l", True),
    ("fortune", False),
    ("karnmrak", False),
])
def test_recognizes_palindrome(chars: str, expected: bool):
    assert InitialSolution().isPalindrome(chars) == expected
