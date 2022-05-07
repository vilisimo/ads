import pytest

from leetcode.easy.ex0191 import BrianKerninghansSolution, InitialSolution


@pytest.mark.parametrize('number, expected', [
    (0, 0),
    (1, 1),
    (7, 3),
    (11, 3),
    (128, 1),
    (6768133, 10),
    (43261596, 12),
    (4294967293, 31),
])
def test_calculates_hamming_weight(number: int, expected: int):
    assert InitialSolution().hammingWeight(number) == expected
    assert BrianKerninghansSolution().hammingWeight(number) == expected
