# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]).

# Find two lines that together with the x-axis form a container, such that
# the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.

# Example 2:
#   Input: height = [1,1]
#   Output: 1

# Constraints:
#   n == height.length
#   2 <= n <= 10^5
#   0 <= height[i] <= 10^4

from typing import List


class InitialSolution:
    def maxArea(self, height: List[int]) -> int:
        head, tail = 0, len(height) - 1
        area = 0
        while head < tail:
            w = tail - head
            h = min(height[head], height[tail])
            area = max(area, w * h)
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        return area
