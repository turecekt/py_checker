"""Unit tests."""

import primeCheck
import unittest
from unittest.mock import patch


class Test(unittest.TestCase):
    """Tests."""

    @patch('builtins.print')
    def test_isPrime(self, mock_print):
        """Check method isPrime."""
        number = 7
        approach = 'Deterministic'
        primeCheck.isPrimeAndRepeat(number, approach)
        mock_print.assert_called_with(number,
                                      "is a prime number.",
                                      approach, "approach.")

    @patch('builtins.print')
    def test_isNotPrime(self, mock_print):
        """Check isNotPrime."""
        number = 8
        approach = 'Deterministic'
        primeCheck.isNotPrimeAndRepeat(number, approach)
        mock_print.assert_called_with(number,
                                      "is not a prime number.",
                                      approach, "approach.")

    def test_isInteger(self):
        """Check method isInteger."""
        self.assertEqual(primeCheck.isInteger(8), True)

    def test_isNotInteger(self):
        """Check method isNotInteger."""
        self.assertEqual(primeCheck.isInteger('AA'), False)

    def test_prime(self):
        """Check program with input 7."""
        self.assertEqual(primeCheck.start(7), 'PRIME')

    def test_notPrime(self):
        """Check program with input 8."""
        self.assertEqual(primeCheck.start(8), 'NOT PRIME')

    @patch('builtins.print')
    def test_isNotValidInput(self, mock_print):
        """Check method isNotValidInput."""
        primeCheck.start('')
        mock_print.assert_called_with('Not valid input')

    @patch('builtins.print')
    def test_isZero(self, mock_print):
        """Check if input is zero."""
        primeCheck.start(0)
        mock_print.assert_called_with('0 is not a valid input')


if __name__ == '__main__':
    unittest.main()
