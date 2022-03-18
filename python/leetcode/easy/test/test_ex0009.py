import pytest

from leetcode.easy.ex0009 import StringSolution, InitialSolution, HalfNumberSolution


@pytest.mark.parametrize('number', [121, 222, 0, 1, 123454321])
def test_verifies_palindrome_integer(number: int):
    assert StringSolution().isPalindrome(number)
    assert InitialSolution().isPalindrome(number)
    assert HalfNumberSolution().isPalindrome(number)


@pytest.mark.parametrize('number', [-999, -1, 10, 112, -121])
def test_recognizes_non_palindrome_integer(number: int):
    assert not StringSolution().isPalindrome(number)
    assert not InitialSolution().isPalindrome(number)
    assert not HalfNumberSolution().isPalindrome(number)
