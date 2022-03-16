# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Example 1:
#   Input: x = 121
#   Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
#   Input: x = -121
#   Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
#   Input: x = 10
#   Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# Constraints:

# -2^31 <= x <= 2^31 - 1


# Follow up: Could you solve it without converting the integer to a string?

class StringSolution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        # Alternatively, we could just take the string and iterate over
        # it from start and end until the indices meet, or start > end.
        reversed = number[::-1]
        return number == reversed


class InitialSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        last_digit = x % 10
        digits = [last_digit]
        while x // 10:
            x = x // 10
            next_digit = x % 10
            digits.append(next_digit)

        start = 0
        end = len(digits) - 1
        while start <= end:
            if digits[start] != digits[end]:
                return False
            start +=1
            end -= 1
        return True


class HalfNumberSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10

        return x == rev or x == rev // 10
