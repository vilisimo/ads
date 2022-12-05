# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to
# C's strstr() and Java's indexOf().



# Example 1:
#   Input: haystack = "hello", needle = "ll"
#   Output: 2

# Example 2:
#   Input: haystack = "aaaaa", needle = "bba"
#   Output: -1

# Constraints:
#   1 <= haystack.length, needle.length <= 10^4
#   haystack and needle consist of only lowercase English characters.

class BuiltInSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class NoBuiltInSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        hc, nc = len(haystack), len(needle)

        for idx in range(hc - nc + 1):
            for nidx in range(nc):
                if idx + nidx >= hc or haystack[idx + nidx] != needle[nidx]:
                    break
            else:
                return idx

        return -1
