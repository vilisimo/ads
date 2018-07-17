import unittest

from algorithms.transforming.roman import generate, transform


class TestIntegerToRoman(unittest.TestCase):

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


class TestRomanToInteger(unittest.TestCase):

    def test_simple_roman(self):
        five = transform('V')
        ten = transform('X')
        fifty = transform('L')

        self.assertEqual(five, 5)
        self.assertEqual(ten, 10)
        self.assertEqual(fifty, 50)

    def test_combined_numerals(self):
        result = transform('CL')
        self.assertEqual(result, 150)

    def test_complex_combined_numerals(self):
        result = transform('CXL')
        self.assertEqual(result, 140)

    def test_edge_case(self):
        result = transform('MMMCMXCIX')
        self.assertEqual(result, 3999)

    def test_incorrect_type(self):
        with self.assertRaises(ValueError):
            transform(1213)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            transform('')

    def test_incorrect_numeral(self):
        with self.assertRaises(ValueError):
            transform('H')

    def test_incorrect_sequence(self):
        with self.assertRaises(ValueError):
            transform('DD')
