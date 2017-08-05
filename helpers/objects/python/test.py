import unittest

from helpers.objects.python.contrived import Contrived


class TestContrivedInitialization(unittest.TestCase):

    def test_happy_path(self):
        contrived = Contrived('a', 1)

        self.assertEqual(contrived.letter, 'a')
        self.assertEqual(contrived.number, 1)

    def test_multiple_characters_refused(self):
        with self.assertRaises(TypeError):
            Contrived('aa', 1)

    def test_non_ascii_refused(self):
        with self.assertRaises(TypeError):
            Contrived('ą', 1)

    def test_non_number_refused(self):
        with self.assertRaises(TypeError):
            Contrived('a', 'b')

    def test_non_int_refused(self):
        with self.assertRaises(TypeError):
            Contrived('a', 1.1)

    def test_letter_as_none_raises_exception(self):
        with self.assertRaises(TypeError):
            Contrived(None, 1)

    def test_number_as_none_raises_exception(self):
        with self.assertRaises(TypeError):
            Contrived('a', None)


class TestContrivedComparison(unittest.TestCase):
    def test_happy_path(self):
        lesser = Contrived('a', 1)
        greater = Contrived('b', 2)

        self.assertTrue(lesser < greater)

    def test_equality(self):
        one = Contrived('a', 1)
        two = Contrived('a', 1)

        self.assertEqual(one, two)

    def test_same_letters_different_numbers(self):
        lesser = Contrived('a', 1)
        greater = Contrived('a', 2)

        self.assertTrue(lesser < greater)

    def test_same_numbers_different_letters(self):
        lesser = Contrived('a', 1)
        greater = Contrived('b', 1)

        self.assertTrue(lesser < greater)


if __name__ == '__main__':
    unittest.main()
