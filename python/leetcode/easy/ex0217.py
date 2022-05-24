# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

# Example 1:
#   Input: nums = [1,2,3,1]
#   Output: true

# Example 2:
#   Input: nums = [1,2,3,4]
#   Output: false

# Example 3:
#   Input: nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true

# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9

from typing import List


class InitialSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


class SortingSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx-1] == nums[idx]:
                return True
        return False
