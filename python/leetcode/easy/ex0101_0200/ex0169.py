# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
#   Input: nums = [3,2,3]
#   Output: 3

# Example 2:
#   Input: nums = [2,2,1,1,1,2,2]
#   Output: 2

# Constraints:
#   n == nums.length
#   1 <= n <= 5 * 104
#   -10^9 <= nums[i] <= 10^9

from typing import List
from collections import Counter, defaultdict


class BuiltInSolution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return counter.most_common(1)[0][0]


class HashMapSolution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        majority = float('-inf')
        for element in nums:
            counts[element] += 1
            if counts[element] > counts[majority]:
                majority = element

        return majority


class SortingSolution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class BoyerMooreVotingSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for element in nums:
            if count == 0:
                candidate = element
            count += 1 if element == candidate else -1
        return candidate
