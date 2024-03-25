import sys


def recursive_fibonacci(n: int) -> list[int]:
  def inner_fibonacci(n: int) -> list[int]:
    if n in {0, 1}:
      return n
    return inner_fibonacci(n-1) + inner_fibonacci(n-2)
  return [inner_fibonacci(i) for i in range(n)]


def memoized_fibonacci(n: int) -> list[int]:
  cache = {0: 0, 1: 1}

  def inner_fibonacci(n: int) -> list[int]:
    if n in cache:
      return cache[n]
    cache[n] = inner_fibonacci(n-1) + inner_fibonacci(n-2)
    return cache[n]

  return [inner_fibonacci(i) for i in range(n)]


def iterative_fibonacci(n: int) -> list[int]:
  def inner_fibonacci(n: int) -> list[int]:
    if n in {0, 1}:
      return n
    
    previous, current = 0, 1
    for _ in range(2, n + 1):
      previous, current = current, previous + current
    return current
  
  return [inner_fibonacci(i) for i in range(n)]


if __name__ == "__main__":
  n = int(sys.argv[1])
  print(f"recursive\t>>\t{recursive_fibonacci(n)}")
  print(f"memoized\t>>\t{memoized_fibonacci(n)}")
  print(f"iterative\t>>\t{iterative_fibonacci(n)}")