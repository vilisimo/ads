from leetcode.easy.ex0101_0200.ex0118 import InitialSolution, InitialFormulaSolution


def test_returns_one_array_for_one_level():
    result = InitialSolution().generate(1)
    assert result == [[1]]

    result = InitialFormulaSolution().generate(1)
    assert result == [[1]]


def test_returns_two_arrays_for_two_levels():
    result = InitialSolution().generate(2)
    assert result == [[1], [1, 1]]

    result = InitialFormulaSolution().generate(2)
    assert result == [[1], [1, 1]]


def test_returns_three_arrays_for_three_levels():
    result = InitialSolution().generate(3)
    assert result == [[1], [1, 1], [1, 2, 1]]

    result = InitialFormulaSolution().generate(3)
    assert result == [[1], [1, 1], [1, 2, 1]]


def test_returns_four_arrays_for_four_levels():
    result = InitialSolution().generate(4)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    result = InitialFormulaSolution().generate(4)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]


def test_returns_five_arrays_for_five_levels():
    result = InitialSolution().generate(5)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    result = InitialFormulaSolution().generate(5)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_returns_six_arrays_for_six_levels():
    result = InitialSolution().generate(6)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

    result = InitialFormulaSolution().generate(6)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
