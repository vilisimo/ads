import pytest

from leetcode.easy.ex0121 import InitialSolution, MinMaxSolution, TwoPointersSolution



@pytest.mark.parametrize('days, expected', [
    ([], 0),
    ([1], 0),
    ([2], 0),
    ([1, 2], 1),
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 2, 2], 0),
    ([2, 2, 3], 1),
    ([3, 2, 3], 1),
    ([2, 4, 1], 2),
    ([4, 6, 1, 5, 8], 7),
])
def test_chooses_best_day(days: list[int], expected: int):
    assert InitialSolution().maxProfit(days) == expected
    assert MinMaxSolution().maxProfit(days) == expected
    assert TwoPointersSolution().maxProfit(days) == expected
