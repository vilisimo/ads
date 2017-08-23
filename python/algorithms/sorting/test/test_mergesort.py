import unittest

from algorithms.sorting.mergesort import mergesort
from helpers.contrived import Contrived


class MergeSortTest(unittest.TestCase):

    def test_sorting_empty_list_returns_empty_list(self):
        collection = []

        collection = mergesort(collection)

        self.assertFalse(collection)

    def test_almost_sorted(self):
        collection = [0, 21, 53, 99, -3, -4, 101]
        expected = [-4, -3, 0, 21, 53, 99, 101]

        collection = mergesort(collection)

        self.assertEqual(collection, expected)

    def test_none_collection_throws_exception(self):
        with self.assertRaises(TypeError):
            mergesort(None)

    def test_one_element_collection(self):
        collection = [-99]

        collection = mergesort(collection)

        self.assertEqual(collection[0], -99)

    def test_sorting_sorts_in_order(self):
        collection = [3, 14, 1]
        expected = [1, 3, 14]

        collection = mergesort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_repeating(self):
        collection = [-41, 99, 11, -41, 2]
        expected = [-41, -41, 2, 11, 99]

        collection = mergesort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_sorted(self):
        collection = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        collection = mergesort(collection)

        self.assertEqual(collection, expected)

    def test_custom_objects(self):
        items = [Contrived("a", 3), Contrived("a", 1), Contrived("b", 13)]
        expected = [Contrived("a", 1), Contrived("a", 3), Contrived("b", 13)]

        items = mergesort(items)

        self.assertListEqual(items, expected)


if __name__ == '__main__':
    unittest.main()