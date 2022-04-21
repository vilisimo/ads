import pytest

from typing import List

from leetcode.easy.ex0119 import FormulaSolution, InitialSolution, IterationSolution, ZipSolution


@pytest.mark.parametrize('row, expected', [
    (0, [1]),
    (1, [1, 1]),
    (2, [1, 2, 1]),
    (3, [1, 3, 3, 1]),
    (4, [1, 4, 6, 4, 1]),
    (5, [1, 5, 10, 10, 5, 1]),
])
def test_returns_correct_row(row: int, expected: List[int]):
    assert InitialSolution().getRow(row) == expected
    assert FormulaSolution().getRow(row) == expected
    assert ZipSolution().getRow(row) == expected
    assert IterationSolution().getRow(row) == expected
