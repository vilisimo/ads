# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:
#   Input: strs = ["flower","flow","flight"]
#   Output: "fl"

# Example 2:
#   Input: strs = ["dog","racecar","car"]
#   Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


# Reference material:
# - https://afteracademy.com/blog/longest-common-prefix
# - https://www.geeksforgeeks.org/longest-common-prefix-using-binary-search/


from typing import List


# Initial
class HorizontalSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        candidate = strs[0]
        for word in strs:
            if not candidate:
                return ''
            for i in range(len(candidate), -1, -1):
                candidate = candidate[:i]
                if word.startswith(candidate):
                    break

        return candidate


class VerticalSolution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            if not strs:
                return ""

            for charIdx in range(len(strs[0])):
                char = strs[0][charIdx]
                for arrIdx in range(len(strs)):
                    # charIdx starts from 0, so when it is > 0, it means 
                    # that we've already found at least 1 common letter
                    if charIdx == len(strs[arrIdx]) or strs[arrIdx][charIdx] != char:
                        return strs[0][0:charIdx]
            return strs[0]


class DivideAndConquerSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return self.lcp(strs, 0, len(strs) - 1)
        
    def lcp(self, strs: List[str], start: int, end: int) -> str:
        if start == end:
            return strs[start]

        mid = (start + end) // 2
        leftside = self.lcp(strs, start, mid)
        rightside = self.lcp(strs, mid + 1, end)
        common = self.sharedPrefix(leftside, rightside)
        
        return common

    def sharedPrefix(self, left: str, right: str) -> str:
        shortest = min(len(left), len(right))
        for i in range(shortest):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:shortest]


class MinMaxSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_s = min(strs)
        max_s = max(strs)

        for i in range(len(min_s)):
            if min_s[i] != max_s[i]:
                return min_s[0:i]

        return min_s


class BinarySearchSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        start = 0
        end = len(min(strs, key=len))

        while start <= end:
            mid = (start + end) // 2
            candidate = strs[0][0:mid]

            if self.is_shared(strs, prefix=candidate):
                start = mid + 1
            else:
                end = mid - 1

        return strs[0][0:end]

    def is_shared(self, strs: List[str], prefix: str) -> str:
        for word in strs:
            if not word.startswith(prefix):
                return False
        return True