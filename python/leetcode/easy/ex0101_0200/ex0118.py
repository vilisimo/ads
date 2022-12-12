# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:

# Input: numRows = 5
#   Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
#   Input: numRows = 1
#   Output: [[1]]

# Constraints:
#   1 <= numRows <= 30

from typing import List


class InitialSolution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            appendable = [1] * (i + 1)
            for j in range(1, len(appendable) - 1):
                appendable[j] = result[i-1][j-1] + result[i-1][j]
            result.append(appendable)

        return result


# Looked up the formula
class InitialFormulaSolution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append(self.pascal(i))

        return result

    # Look up here: https://stackoverflow.com/a/15580400/4543382
    def pascal(self, n: int):
        result = [1]
        for i in range(n):
            line = (result[i] * (n - i) // (i + 1))
            result.append(line)
        return result
