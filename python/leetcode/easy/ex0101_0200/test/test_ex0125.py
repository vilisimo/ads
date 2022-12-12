import pytest

from leetcode.easy.ex0101_0200.ex0125 import InitialSolution, SolutionWithoutLoop


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
def test_recognizes_palindrome_in_solution_without_loops(chars: str, expected: bool):
    assert SolutionWithoutLoop().isPalindrome(chars) == expected
