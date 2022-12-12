import pytest

from leetcode.easy.ex0000_0100.ex0035 import InitialSolution


@pytest.mark.parametrize('input, target, expected', [
    ([1, 2, 3, 4], 2, 1),
    ([1, 2], 2, 1),
    ([1, 2], 1, 0),
    ([1], 0, 0),
    ([1, 5, 9, 11, 22, 48], 22, 4),
])
def test_finds_existing_number(input: list[int], target: int, expected: int):
    result = InitialSolution().searchInsert(input, target)

    assert result == expected


@pytest.mark.parametrize('input, target, expected', [
    ([1, 2, 3, 4], 5, 4),
    ([1, 2], 0, 0),
    ([9, 11], 10, 1),
    ([12, 42, 78, 199], 77, 2),
    ([1, 5, 9, 11, 22, 48], 29, 5),
])
def test_finds_missing_number(input: list[int], target: int, expected: int):
    result = InitialSolution().searchInsert(input, target)

    assert result == expected
