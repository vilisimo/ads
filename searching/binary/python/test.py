import unittest
from binarySearch import search

class TestBinarySearch(unittest.TestCase):

    def test_invalid_collection(self):
        with self.assertRaises(TypeError):
            search(collection=None, target=1)

    def test_invalid_element(self):
        with self.assertRaises(TypeError):
            search(collection=[1, 2, 3], target=None)

    def test_empty_collection(self):
        actual = search(collection=[], target=1)

        self.assertEqual(-1, actual)

    def test_non_existent_element(self):
        numbers = [1, 2, 3, 4]
        actual = search(collection=numbers, target=5)

        self.assertEqual(-1, actual)

    def test_basic_search(self):
        numbers = [1, 2, 3, 4]
        actual = search(collection=numbers, target=3)

        self.assertEqual(2, actual)

    def test_cornercase_low(self):
        numbers = [1, 2, 3, 4]
        actual = search(collection=numbers, target=1)

        self.assertEqual(0, actual)

    def test_cornercase_high(self):
        numbers = [3, 11, 27, 41]
        actual = search(collection=numbers, target=41)

        self.assertEqual(3, actual)

    def test_tuples(self):
        numbers = (1, 4, 99, 101)
        actual = search(collection=numbers, target=4)

        self.assertEqual(1, actual)

    def test_repeating_numbers(self):
        numbers = [1, 3, 3, 6]
        actual = search(collection=numbers, target=3)

        self.assertEqual(1, actual)

    def test_letters(self):
        letters = ['a', 'c', 'f', 'j', 'r']
        actual = search(collection=letters, target='j')

        self.assertEqual(3, actual)


if __name__ == '__main__':
    unittest.main()