from leetcode.easy.ex0000_0100.ex0001 import Solution


def test_finds_answer_with_two_numbers():
    answer = Solution().twoSum(nums=[1, 2], target=3)

    assert set(answer) == {0, 1}


def test_finds_answer_with_three_numbers():
    answer = Solution().twoSum(nums=[3,2,4], target=6)

    assert set(answer) == {1, 2}


def test_finds_answer_with_multiple_numbers():
    answer = Solution().twoSum(nums=[2,7,11,15], target=9)

    assert set(answer) == {0, 1}


def test_finds_answer_with_multiple_large_numbers():
    answer = Solution().twoSum(nums=[14921, 2903, 23833, 983201, 12344, 32324], target=1007034)

    assert set(answer) == {2, 3}
