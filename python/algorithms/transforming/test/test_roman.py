import unittest

from algorithms.transforming.roman import generate


class TestRoman(unittest.TestCase):

    def test_converts_int_to_roman(self):
        result = generate(1)
        self.assertEqual(result, 'I')

        result = generate(3999)
        self.assertEqual(result, 'MMMCMXCIX')

    def test_does_not_allow_incorrect_type(self):
        with self.assertRaises(ValueError):
            generate('one')

    def test_does_not_allow_lower_than_one(self):
        with self.assertRaises(ValueError):
            generate(0)

    def test_does_not_allow_higher_than_three_nine_nine_nine(self):
        with self.assertRaises(ValueError):
            generate(4000)
