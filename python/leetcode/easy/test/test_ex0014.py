import pytest

from leetcode.easy.ex0014 import (
    HorizontalSolution, 
    VerticalSolution, 
    DivideAndConquerSolution, 
    MinMaxSolution,
    BinarySearchSolution,
)


@pytest.mark.parametrize('input, expected', [
    (["flower", "flow", "flight"], "fl"),
    (["dancing", "dane", "danger"], "dan"),
    (["zone", "zing"], "z"),
    (["egotist", "egocentric", "egomaniac"], "ego")
])
def test_finds_common_prefix(input: list[str], expected: str):
    result = HorizontalSolution().longestCommonPrefix(input)
    assert result == expected
    
    result = VerticalSolution().longestCommonPrefix(input)
    assert result == expected

    result = DivideAndConquerSolution().longestCommonPrefix(input)
    assert result == expected

    result = MinMaxSolution().longestCommonPrefix(input)
    assert result == expected

    result = BinarySearchSolution().longestCommonPrefix(input)
    assert result == expected


def test_returns_first_member_for_array_of_one():
    result = HorizontalSolution().longestCommonPrefix(["theonlyone"])
    assert result == "theonlyone"

    result = VerticalSolution().longestCommonPrefix(["theonlyone"])
    assert result == "theonlyone"

    result = DivideAndConquerSolution().longestCommonPrefix(["theonlyone"])
    assert result == "theonlyone"

    result = MinMaxSolution().longestCommonPrefix(["theonlyone"])
    assert result == "theonlyone"

    result = BinarySearchSolution().longestCommonPrefix(["theonlyone"])
    assert result == "theonlyone"


def test_returns_empty_string_for_no_matching_prefix():
    result = HorizontalSolution().longestCommonPrefix(["dog","racecar","car"])
    assert not result

    result = VerticalSolution().longestCommonPrefix(["dog","racecar","car"])
    assert not result

    result = DivideAndConquerSolution().longestCommonPrefix(["dog","racecar","car"])
    assert not result

    result = MinMaxSolution().longestCommonPrefix(["dog","racecar","car"])
    assert not result

    result = BinarySearchSolution().longestCommonPrefix(["dog","racecar","car"])
    assert not result


def test_searches_for_prefix_not_postfix():
    result = HorizontalSolution().longestCommonPrefix(["ball", "dodgeball"])
    assert not result

    result = VerticalSolution().longestCommonPrefix(["ball", "dodgeball"])
    assert not result

    result = DivideAndConquerSolution().longestCommonPrefix(["ball", "dodgeball"])
    assert not result

    result = MinMaxSolution().longestCommonPrefix(["ball", "dodgeball"])
    assert not result

    result = BinarySearchSolution().longestCommonPrefix(["ball", "dodgeball"])
    assert not result



def test_finds_one_letter_prefixes():
    result = HorizontalSolution().longestCommonPrefix(["abc", "ab", "a", "d"])
    assert not result

    result = VerticalSolution().longestCommonPrefix(["abc", "ab", "a", "d"])
    assert not result

    result = DivideAndConquerSolution().longestCommonPrefix(["abc", "ab", "a", "d"])
    assert not result

    result = MinMaxSolution().longestCommonPrefix(["abc", "ab", "a", "d"])
    assert not result

    result = BinarySearchSolution().longestCommonPrefix(["abc", "ab", "a", "d"])
    assert not result
