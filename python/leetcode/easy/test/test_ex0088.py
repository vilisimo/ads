import pytest

from leetcode.easy.ex0088 import InitialPlusLookedUpSolution


@pytest.mark.parametrize('nums1, m, nums2, n, expected', [
    ([0], 0, [1], 1, [1]),
    ([0, 0], 0, [1, 2], 2, [1, 2]),
    ([1], 1, [], 0, [1]),
    ([1, 2], 2, [], 0, [1, 2]),
    ([2, 2, 0], 2, [2], 1, [2, 2, 2]),
    ([1, 3, 0], 2, [2], 1, [1, 2, 3]),
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([], 0, [], 0, []),
    ([2, 0], 1, [1], 1, [1, 2]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([0, 3, 0, 0, 0], 2, [-1, 2, 3], 3, [-1, 0, 2, 3, 3]),
    ([-1, 0, 0, 0], 1, [-2, -1, 0], 3, [-2, -1, -1, 0]),
    ([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6, [-1, 0, 0, 1, 1, 1 ,2, 3, 3]),
])
def test_merges_arrays(nums1: list[int], m: int, nums2: list[int], n: int, expected: list[int]):
    InitialPlusLookedUpSolution().merge(nums1, m, nums2, n)

    assert nums1 == expected
