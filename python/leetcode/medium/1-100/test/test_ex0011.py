import pytest

from ex0011 import InitialSolution


@pytest.mark.parametrize("input, expected", [
	([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
	([1, 1], 1),
	([8, 7, 2, 2, 1, 7, 5], 35),
	([2, 2], 2),
	([1, 6, 8, 10, 3, 4, 5], 25),
])
def test_calculates_area(input: list[int], expected: int):
	assert InitialSolution().maxArea(input) == expected