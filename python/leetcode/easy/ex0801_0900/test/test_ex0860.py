from leetcode.easy.ex0801_0900.ex0860 import InitialSolution

import pytest


@pytest.mark.parametrize("notes, expected", [
    ([5], True),
    ([5, 5], True),
    ([5, 10], True),
    ([5,5,5,10,20], True),
    ([5,5,10,10,20], False),
    ([10, 5], False),
    ([5, 10, 5, 10], True),
    ([5, 10, 5, 10, 20], False),
    ([5, 10, 5, 10, 5, 5, 5, 20], True),
    ([5, 10, 5, 20], True),
    ([5, 5, 5, 5, 20, 10], True),
])
def test_determines_if_change_can_be_given(notes: list[int], expected: bool):
    assert InitialSolution().lemonadeChange(notes) == expected
