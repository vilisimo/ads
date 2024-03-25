import pytest

from algorithms.math.fibonacci import recursive_fibonacci, memoized_fibonacci, iterative_fibonacci


# n - seqeuence size
@pytest.mark.parametrize('n, expected', [
  (1, [0]),
  (2, [0, 1]),
  (16, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]),
])
def test_produces_expected_sequence(n: int, expected: list[int]):
  assert recursive_fibonacci(n) == expected
  assert memoized_fibonacci(n) == expected
  assert iterative_fibonacci(n) == expected
