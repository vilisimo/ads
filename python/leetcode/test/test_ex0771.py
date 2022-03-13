import unittest

from leetcode.ex0771 import Solution


class TestClass(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_jewels(self):
        result = self.solution.numJewelsInStones("", "ABC")
        assert result == 0
 
    def test_non_empty_jewels(self):
        result = self.solution.numJewelsInStones("AB", "AAACBBL")
        assert result == 5
 
    def test_mixed_case_jewels(self):
        result = self.solution.numJewelsInStones("aA", "aAAbbbb")
        assert result == 3


if __name__ == "__main__":
    unittest.main()