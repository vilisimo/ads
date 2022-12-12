# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.

# Example 1:
#   Input: x = 4
#   Output: 2

# Example 2:
#   Input: x = 8
#   Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

# Constraints:
#   0 <= x <= 2^31 - 1

class InitialSolution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = start + (end - start) // 2
            square = mid * mid
            if square > x:
                end = mid - 1
            elif square < x:
                start = mid + 1
            else:
                return mid

        return end
