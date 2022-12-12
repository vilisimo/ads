# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
#   Input: a = "11", b = "1"
#   Output: "100"

# Example 2:
#   Input: a = "1010", b = "1011"
#   Output: "10101"


# Constraints:
#   1 <= a.length, b.length <= 10^4
#   a and b consist only of '0' or '1' characters.
#   Each string does not contain leading zeros except for the zero itself.

class LookedUpSolution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        padded_a = a.zfill(max_length)
        padded_b = b.zfill(max_length)

        result = ''
        carry = 0
        for i in range(max_length):
            summed = carry
            summed += int(padded_a[~i])
            summed += int(padded_b[~i])

            result = str(summed % 2) + result
            carry = summed // 2

        return result if not carry else "1" + result


class WhileSolution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            summed = carry
            summed += int(a[i]) if i >= 0 else 0
            summed += int(b[j]) if j >= 0 else 0

            result = str(summed % 2) + result
            carry = summed // 2
            i -= 1
            j -= 1

        return result if not carry else "1" + result


class BuiltInSolution:
    def addBinary(self, a: str, b: str) -> str:
        summed = bin(int(a, 2) + int(b, 2))
        return summed[2:]
