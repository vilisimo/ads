from leetcode.easy.ex0701_0800.ex0771 import Solution


def test_empty_jewels():
    result = Solution().numJewelsInStones("", "ABC")
    assert result == 0

def test_non_empty_jewels():
    result = Solution().numJewelsInStones("AB", "AAACBBL")
    assert result == 5

def test_mixed_case_jewels():
    result = Solution().numJewelsInStones("aA", "aAAbbbb")
    assert result == 3
