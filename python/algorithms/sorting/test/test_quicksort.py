import unittest

from algorithms.sorting.quicksort import sort, quicksort, qsort
from helpers.contrived import Contrived


class TestQuicksort(unittest.TestCase):
    def test_sorting_empty_list_returns_empty_list(self):
        collection = []

        collection = sort(collection)

        self.assertFalse(collection)

    def test_none_throws_exception(self):
        with self.assertRaises(TypeError):
            sort(None)

    def test_one_element_collection(self):
        collection = [-99]

        collection = sort(collection)

        self.assertEqual(collection[0], -99)

    def test_sorting_sorts_in_order(self):
        collection = [3, 14, 1]
        expected = [1, 3, 14]

        collection = sort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_repeating(self):
        collection = [-41, 99, 11, -41, 2]
        expected = [-41, -41, 2, 11, 99]

        collection = sort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_sorted(self):
        collection = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        collection = sort(collection)

        self.assertEqual(collection, expected)

    def test_custom_objects(self):
        items = [Contrived("a", 3), Contrived("a", 1), Contrived("b", 13)]
        expected = [Contrived("a", 1), Contrived("a", 3), Contrived("b", 13)]

        collection = sort(items)

        self.assertListEqual(collection, expected)


class TestQuicksortInPlace(unittest.TestCase):
    def test_sorting_empty_list_returns_empty_list(self):
        collection = []

        quicksort(collection)

        self.assertFalse(collection)

    def test_almost_sorted(self):
        collection = [0, 21, 53, 99, -3, -4, 101]
        expected = [-4, -3, 0, 21, 53, 99, 101]

        quicksort(collection)

        self.assertEqual(collection, expected)

    def test_none_collection_throws_exception(self):
        with self.assertRaises(TypeError):
            quicksort(None)

    def test_one_element_collection(self):
        collection = [-99]

        quicksort(collection)

        self.assertEqual(collection[0], -99)

    def test_sorting_sorts_in_order(self):
        collection = [3, 14, 1]
        expected = [1, 3, 14]

        quicksort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_repeating(self):
        collection = [-41, 99, 11, -41, 2]
        expected = [-41, -41, 2, 11, 99]

        quicksort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_sorted(self):
        collection = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        quicksort(collection)

        self.assertEqual(collection, expected)

    def test_custom_objects(self):
        items = [Contrived("a", 3), Contrived("a", 1), Contrived("b", 13)]
        expected = [Contrived("a", 1), Contrived("a", 3), Contrived("b", 13)]

        quicksort(items)

        self.assertListEqual(items, expected)


class TestFirstElementPivotQuickSort(unittest.TestCase):
    def test_sorting_empty_list_returns_empty_list(self):
        collection = []

        qsort(collection)

        self.assertFalse(collection)

    def test_almost_sorted(self):
        collection = [0, 21, 53, 99, -3, -4, 101]
        expected = [-4, -3, 0, 21, 53, 99, 101]

        qsort(collection)

        self.assertEqual(collection, expected)

    def test_none_collection_throws_exception(self):
        with self.assertRaises(TypeError):
            qsort(None)

    def test_one_element_collection(self):
        collection = [-99]

        qsort(collection)

        self.assertEqual(collection[0], -99)

    def test_sorting_sorts_in_order(self):
        collection = [3, 14, 1]
        expected = [1, 3, 14]

        qsort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_repeating(self):
        collection = [-41, 99, 11, -41, 2]
        expected = [-41, -41, 2, 11, 99]

        qsort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_sorted(self):
        collection = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        qsort(collection)

        self.assertEqual(collection, expected)

    def test_custom_objects(self):
        items = [Contrived("a", 3), Contrived("a", 1), Contrived("b", 13)]
        expected = [Contrived("a", 1), Contrived("a", 3), Contrived("b", 13)]

        qsort(items)

        self.assertListEqual(items, expected)


if __name__ == '__main__':
    unittest.main()
