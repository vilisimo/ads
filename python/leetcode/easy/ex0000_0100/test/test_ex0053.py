import pytest


from leetcode.easy.ex0000_0100.ex0053 import O2nSolution, KadanesSolution, DivideAndConquerSolution


@pytest.mark.parametrize('input, expected', [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
    ([-1], -1),
    ([5, 2, -20, 3, -1, 2], 7),
    ([1, 0, 3, 22, -1, 3, -1, -3, 3, 1, 0], 28)
])
def test_finds_largest_sum(input: list[int], expected: int):
    result = O2nSolution().maxSubArray(input)
    assert result == expected


# Previous solution modifies array, hence new test
@pytest.mark.parametrize('input, expected', [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1], -1),
    ([5, 2, -20, 3, -1, 2], 7),
    ([1, 0, 3, 22, -1, 3, -1, -3, 3, 1, 0], 28)
])
def test_immutable_solutions(input: list[int], expected: int):
    result = KadanesSolution().maxSubArray(input)
    assert result == expected

    result = DivideAndConquerSolution().maxSubArray(input)
    assert result == expected
