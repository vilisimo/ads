import pytest

from leetcode.easy.ex0242 import InitialSolution, ArraySolution, AlternativeArraySolution

initial_solver = InitialSolution()
array_solver = ArraySolution()
optimized_solver = AlternativeArraySolution()


@pytest.mark.parametrize("initial, potential, expected", [
    ("anagram", "nagaram", True),
    ("rat", "cat", False),
    ("ab", "ba", True),
    ("a", "a", True),
    ("bc", "abc", False),
    ("a", "ab", False),
    ("abc", "abd", False),
])
def test_initial_solver_recognizes_anagram(initial: str, potential: str, expected: bool):
    assert initial_solver.isAnagram(initial, potential) == expected


@pytest.mark.parametrize("initial, potential, expected", [
    ("anagram", "nagaram", True),
    ("rat", "cat", False),
    ("ab", "ba", True),
    ("a", "a", True),
    ("bc", "abc", False),
    ("a", "ab", False),
    ("abc", "abd", False),
])
def test_array_solver_recognizes_anagram(initial: str, potential: str, expected: bool):
    assert array_solver.isAnagram(initial, potential) == expected


@pytest.mark.parametrize("initial, potential, expected", [
    ("anagram", "nagaram", True),
    ("rat", "cat", False),
    ("ab", "ba", True),
    ("a", "a", True),
    ("bc", "abc", False),
    ("a", "ab", False),
    ("abc", "abd", False),
])
def test_optimized_solver_recognizes_anagram(initial: str, potential: str, expected: bool):
    assert optimized_solver.isAnagram(initial, potential) == expected
