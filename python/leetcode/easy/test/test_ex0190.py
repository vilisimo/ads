import pytest

from leetcode.easy.ex0190 import (
    BitwiseOperationsSolution,
    ExpandedSolution,
    InitialSolution,
    BitwiseOrSolution,
)


@pytest.mark.parametrize("bits, expected", [
    (43261596, 964176192),
    (4294967293, 3221225471),
])
def test_reverses_bits(bits: int, expected: int):
    assert InitialSolution().reverseBits(bits) == expected
    assert ExpandedSolution().reverseBits(bits) == expected
    assert BitwiseOperationsSolution().reverseBits(bits) == expected
    assert BitwiseOrSolution().reverseBits(bits) == expected
