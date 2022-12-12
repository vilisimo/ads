import pytest

from leetcode.easy.ex0000_0100.ex0066 import InitialSolution, IterativeOnesComplimentSolution, IterativeReadableSolution


@pytest.mark.parametrize('input, expected', [
	([1,2,3], [1,2,4]),
	([4,3,2,1], [4,3,2,2]),
	([1, 0], [1, 1]),
	([8], [9]),
	([9], [1,0]),
	([3,9], [4,0]),
	([3,9], [4,0]),
])
def test_increments_integer(input: list[int], expected: list[int]):
	result = InitialSolution().plusOne(input)
	assert result == expected


@pytest.mark.parametrize('input, expected', [
	([1,2,3], [1,2,4]),
	([4,3,2,1], [4,3,2,2]),
	([1, 0], [1, 1]),
	([8], [9]),
	([9], [1,0]),
	([3,9], [4,0]),
	([3,9], [4,0]),
])
def test_iterative_ones_compliment_addition(input: list[int], expected: list[int]):
	result = IterativeOnesComplimentSolution().plusOne(input)
	assert result == expected


@pytest.mark.parametrize('input, expected', [
	([1,2,3], [1,2,4]),
	([4,3,2,1], [4,3,2,2]),
	([1, 0], [1, 1]),
	([8], [9]),
	([9], [1,0]),
	([3,9], [4,0]),
	([3,9], [4,0]),
])
def test_iterative_readable_addition(input: list[int], expected: list[int]):
	result = IterativeReadableSolution().plusOne(input)
	assert result == expected
