"""Contains Test_test_NumberSystemConverter class."""


import unittest
from roman_numerals.number_system_converter import (
        NumberSystemConverter as converter)


class Test_test_NumberSystemConverter(unittest.TestCase):
    """Test function of NumberSystemConverter."""

    def test_integer_to_roman(self):
        """Test function of integer_to_roman method."""
        expected_value = "Input can not be None."

        roman = converter.integer_to_roman(None)
        self.assertEqual(roman, expected_value)

        expected_value = "Input must be any positive integer from 1 to 3999."

        roman = converter.integer_to_roman(3.5)
        self.assertEqual(roman, expected_value)

        expected_value = "MDCLXVI"

        roman = converter.integer_to_roman(1666)
        self.assertEqual(roman, expected_value)

        expected_value = "CMXCIX"

        roman = converter.integer_to_roman(999)
        self.assertEqual(roman, expected_value)

        expected_value = "CDXLIV"

        roman = converter.integer_to_roman(444)
        self.assertEqual(roman, expected_value)

    def test_roman_to_integer(self):
        """Test function of roman_to_integer method."""
        expected_value = 0

        integer = converter.roman_to_integer(None)
        self.assertEqual(integer, expected_value)

        integer = converter.roman_to_integer(1)
        self.assertEqual(integer, expected_value)

        integer = converter.roman_to_integer("MCXIIII")
        self.assertEqual(integer, expected_value)

        integer = converter.roman_to_integer("IXI")
        self.assertEqual(integer, expected_value)

        expected_value = 3888

        integer = converter.roman_to_integer("MMMDCCCLXXXVIII")
        self.assertEqual(integer, expected_value)

        expected_value = 999

        integer = converter.roman_to_integer("CMXCIX")
        self.assertEqual(integer, expected_value)

        expected_value = 444

        integer = converter.roman_to_integer("CDXLIV")
        self.assertEqual(integer, expected_value)
