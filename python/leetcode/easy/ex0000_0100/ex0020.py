# Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.

# Example 1:
#   Input: s = "()"
#   Output: true

# Example 2:
#   Input: s = "()[]{}"
#   Output: true

# Example 3:
#   Input: s = "(]"
#   Output: false

# Constraints:

# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        stack = []
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            else:
                if not stack or pairs[stack.pop()] != bracket:
                    return False

        return not stack
