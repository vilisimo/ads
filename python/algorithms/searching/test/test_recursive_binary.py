import pytest

from algorithms.searching.recursiveBinary import search
from helpers.contrived import Contrived


def test_invalid_collection():
  with pytest.raises(TypeError):
    search(collection=None, target=1)


def test_invalid_element():
    with pytest.raises(TypeError):
        search(collection=[1, 2, 3], target=None)


def test_empty_collection():
    actual = search(collection=[], target=1)

    assert actual == -1


def test_non_existent_element():
    numbers = [1, 2, 3, 4]
    actual = search(collection=numbers, target=5)

    assert actual == -1


def test_basic_search():
    numbers = [1, 2, 3, 4]
    actual = search(collection=numbers, target=3)

    assert actual == 2


def test_cornercase_low():
    numbers = [1, 2, 3, 4]
    actual = search(collection=numbers, target=1)

    assert actual == 0


def test_cornercase_high():
    numbers = [3, 11, 27, 41]
    actual = search(collection=numbers, target=41)

    assert actual == 3


def test_tuples():
    numbers = (1, 4, 99, 101)
    actual = search(collection=numbers, target=4)

    assert actual == 1


def test_repeating_numbers():
    numbers = [1, 3, 3, 6]
    actual = search(collection=numbers, target=3)

    assert actual == 1


def test_letters():
    letters = ['a', 'c', 'f', 'j', 'r']
    actual = search(collection=letters, target='j')

    assert actual == 3


def test_custom_objects():
    items = [Contrived("a", 1), Contrived("b", 2), Contrived("c", 3)]
    actual = search(collection=items, target=Contrived("b", 2))

    assert actual == 1
