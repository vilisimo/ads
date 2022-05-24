# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and
# abs(i - j) <= k.

# Example 1:
#   Input: nums = [1,2,3,1], k = 3
#   Output: true

# Example 2:
#   Input: nums = [1,0,1,1], k = 1
#   Output: true

# Example 3:
#   Input: nums = [1,2,3,1,2,3], k = 2
#   Output: false

# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9
#   0 <= k <= 10^5

from typing import List


class InitialSolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for idx, num in enumerate(nums):
            if num in indices and abs(indices[num] - idx) <= k:
                return True
            indices[num] = idx
        return False


class SlidingWindowSolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        candidates = set()
        for idx, num in enumerate(nums):
            if idx > k:
                candidates.remove(nums[idx-k-1])

            if num in candidates:
                return True

            candidates.add(num)

        return False
