# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

# Example 1:

# Input: rowIndex = 3
#   Output: [1,3,3,1]

# Example 2:
#   Input: rowIndex = 0
#   Output: [1]

# Example 3:
#   Input: rowIndex = 1
#   Output: [1,1]

# Constraints:
#   0 <= rowIndex <= 33

from typing import List


class InitialSolution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex <= 0:
            return result

        for i in range(1, rowIndex + 1):
            current = [1] * (i + 1)
            for j in range(1, len(current) - 1):
                current[j] = result[j-1] + result[j]
            result = current

        return result


# row 1
# [1] ->
# [0, 1]
# [1, 0]
# =
# [1, 1]


# row 2
# [1, 1] ->
# [0, 1, 1]
# [1, 1, 0]
# =
# [1, 2, 1]

# row 3
# [1, 2, 1] ->
# [0, 1, 2, 1]
# [1, 2, 1, 0]
# =
# [1, 3, 3, 1]
class ZipSolution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for _ in range(rowIndex):
            result = [x + y for x, y in zip([0] + result, result + [0])]

        return result


class IterationSolution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for outer in range(2, rowIndex + 1):
            for inner in range(outer - 1, 0, -1):
                result[inner] += result[inner-1]

        return result



# Formula here: https://stackoverflow.com/a/15580400/4543382
# C(n,k+1) = C(n,k) * (n-k) / (k+1)
class FormulaSolution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for k in range(rowIndex):
            number = result[k] * (rowIndex - k) // (k + 1)
            result.append(number)

        return result
