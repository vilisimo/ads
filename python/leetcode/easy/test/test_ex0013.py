import pytest

from leetcode.easy.ex0013 import InitialSolution, ImprovedSolution


@pytest.mark.parametrize('roman, expected', [
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('V', 5),
    ('VI', 6),
    ('VII', 7),
    ('VIII', 8),
    ('IX', 9),
    ('X', 10),
])
def test_converts_to_integer_up_to_ten_including(roman: str, expected: int):
    assert InitialSolution().romanToInt(roman) == expected
    assert ImprovedSolution().romanToInt(roman) == expected


@pytest.mark.parametrize('roman, expected', [
    ('XII', 12),
    ('XIV', 14),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('C', 100),
    ('CX', 110),
    ('CD', 400),
    ('D', 500),
    ('DC', 600),
    ('CM', 900),
    ('M', 1000),
    ('MC', 1100),

])
def test_converts_large_numbers(roman: str, expected: int):
    assert InitialSolution().romanToInt(roman) == expected
    assert ImprovedSolution().romanToInt(roman) == expected


@pytest.mark.parametrize('roman, expected', [
    ('MCMXCIV', 1994),
    ('LVIII', 58),
    ('III', 3),
])
def test_covers_indicated_test_cases(roman: str, expected: str):
    assert InitialSolution().romanToInt(roman) == expected
    assert ImprovedSolution().romanToInt(roman) == expected
