import unittest

from algorithms.sorting.selection.python.selection import sort
from helpers.objects.python.contrived import Contrived


class TestSelectionSort(unittest.TestCase):

    def test_sorting_empty_list_returns_empty_list(self):
        collection = []
        
        sort(collection)

        self.assertFalse(collection)

    def test_none_throws_exception(self):
        with self.assertRaises(TypeError):
            sort(None)

    def test_one_element_collection(self):
        collection = [-99]

        sort(collection)

        self.assertEqual(collection[0], -99)

    def test_sorting_sorts_in_order(self):
        collection = [3, 14, 1]
        expected = [1, 3, 14]
        
        sort(collection)

        self.assertListEqual(collection, expected)

    def test_sorting_sorts_repeating(self):
        collection = [-41, 99, 11, -41, 2]
        expected = [-41, -41, 2, 11, 99]

        sort(collection)

        self.assertListEqual(collection, expected)

    def test_custom_objects(self):
        items = [Contrived("a", 3), Contrived("a", 1), Contrived("b", 13)]
        expected = [Contrived("a", 1), Contrived("a", 3), Contrived("b", 13)]

        sort(items)

        self.assertListEqual(items, expected)


if __name__ == '__main__':
    unittest.main()
