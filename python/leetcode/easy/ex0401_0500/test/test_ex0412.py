from leetcode.easy.ex0401_0500.ex0412 import InitialSolution, NoModuloSolution


def test_n_1():
    result = InitialSolution().fizzBuzz(1)
    assert result == ["1"]

    result = NoModuloSolution().fizzBuzz(1)
    assert result == ["1"]

def test_n_2():
    result = InitialSolution().fizzBuzz(2)
    assert result == ["1", "2"]

    result = NoModuloSolution().fizzBuzz(2)
    assert result == ["1", "2"]

def test_n_3():
    result = InitialSolution().fizzBuzz(3)
    assert result == ["1","2","Fizz"]

    result = NoModuloSolution().fizzBuzz(3)
    assert result == ["1","2","Fizz"]

def test_n_5():
    result = InitialSolution().fizzBuzz(5)
    assert result == ["1","2","Fizz","4","Buzz"]

    result = NoModuloSolution().fizzBuzz(5)
    assert result == ["1","2","Fizz","4","Buzz"]

def test_n_15():
    result = InitialSolution().fizzBuzz(15)
    assert result == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    result = NoModuloSolution().fizzBuzz(15)
    assert result == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
