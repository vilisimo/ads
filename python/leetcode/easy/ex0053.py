# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
#   Input: nums = [1]
#   Output: 1

# Example 3:
#   Input: nums = [5,4,-1,7,8]
#   Output: 23

# Constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# Follow up: If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.

from typing import List


class O2nSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                curr_sum = nums[i-1] + nums[i]
                nums[i] = curr_sum
        return max(nums)



class KadanesSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        max_sum = 0

        for i in range(len(nums)):
            if max_sum < 0:
                max_sum = 0

            max_sum = max_sum + nums[i]
            max_so_far = max(max_so_far, max_sum)

        return max_so_far


class DivideAndConquerSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.max_sub(nums, start=0, end=len(nums) - 1)

    def max_sub(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]

        mid = (start + end) // 2

        left = self.max_sub(nums=nums, start=start, end=mid)
        right = self.max_sub(nums=nums, start=mid + 1, end=end)
        center = self.max_center(nums=nums, left=start, center=mid, right=end)

        return max(left, right, center)

    def max_center(self, nums: List[int], left: int, center: int, right: int) -> int:
        left_sum = float('-inf')
        left_total = 0
        for i in range(center, left - 1, -1):
            left_total += nums[i]
            left_sum = max(left_total, left_sum)

        right_sum = float('-inf')
        right_total = 0
        for i in range(center + 1, right + 1):
            right_total += nums[i]
            right_sum = max(right_total, right_sum)

        return max(left_sum, left_sum + right_sum, right_sum)
