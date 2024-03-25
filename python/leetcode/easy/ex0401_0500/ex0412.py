# Given an integer n, return a string array answer (1-indexed) where:
#  - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#  - answer[i] == "Fizz" if i is divisible by 3.
#  - answer[i] == "Buzz" if i is divisible by 5.
#  - answer[i] == i (as a string) if none of the above conditions are true.
 
# Example 1:
#   Input: n = 3
#   Output: ["1","2","Fizz"]
#   Example 2:

# Input: n = 5
#   Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
#   Input: n = 15
#   Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


class InitialSolution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for idx in range(1, n + 1):
            if (idx % 3 == 0 and idx % 5 == 0):
                result.append("FizzBuzz")
            elif (idx % 3 == 0):
                result.append("Fizz")
            elif (idx % 5 == 0):
                result.append("Buzz")
            else:
                result.append(str(idx))
        return result


class NoModuloSolution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = [str(i + 1) for i in range(n)]
        fizz, buzz, fizzBuzz = "Fizz", "Buzz", "FizzBuzz"

        for i in range(2, n, 3):
            result[i] = fizz
        for i in range(4, n, 5):
            result[i] = buzz
        for i in range(14, n, 15):
            result[i] = fizzBuzz

        return result