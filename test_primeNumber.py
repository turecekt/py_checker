"""Module unit tests.

This module is use for do unit test to each function from primeNumber.py
"""
# Author:   Barbana Klimekova <b_klimekova@utb.cz>
#           Lucia Kubaskova <l_kubaskova@utb.cz>
#           Tomas_Prikasky <t_prikasky@utb.cz>
#
# Description:  Create unit tests to validate units from primeNumber.py
#               Units: functions isPrimeNumber(), printDivisors()
#               TestCases: 1. prime number validation
#                          2. non-prime number validation
#                          3. dividors validation
#                          4. printed outputs validation
import builtins
from primeNumber import isPrimeNumber, getDivisors, main
import unittest
from unittest.mock import patch


class TestPrimeNumber(unittest.TestCase):
    """Class TestPrimeNumber for testing function primeNumber().

    ...
    Attributes
    ----------
            - number : int
                - we are testing numbers 5 and 10, 5 as prime number,
                10 as non-prime number
            - vypis: str
                - the string value that is printed as a result into console
    Methods
    -------
            test_fiveIsPrimeNumber(self, ):
                - Function validates that entered number 5 is prime number
            test_tenIsNotPrimeNumber(self, ):
                - Function validates that number 10 is non-prime number
    """

    def test_isPrime(self, ):
        """Function test for isPrimeNumber.

        Parameters:
            - number (int): tested number 5
        Returns:
            - output (str): String printed into console,
        statement if number is prime number
        """
        self.assertEqual(isPrimeNumber(5), True)
        self.assertEqual(isPrimeNumber(6), False)
        self.assertEqual(isPrimeNumber(8), False)

    def test_getDivisors(self, ):
        """Function test for isPrimeNumber.

        Parameters:
                - number (int): tested number 5
        Returns:
                - output (str): String printed into console,
                statement if number is prime number
        """
        self.assertEqual(getDivisors(5), [1, 5])
        self.assertEqual(getDivisors(6), [1, 2, 3, 6])


class TestPrintedValues(unittest.TestCase):
    """Class TestPrintedValues for testing function printDivisors().

    ...
    Attributes
    ----------
            - number : int
                - We are testing numbers 5 and 44, 5 for evaluating
                number of divisors and 44 for evaluating values of divisors
            - dividers: int[]
                - List of integers - dividers
            - counter: int
                - Number of dividers
    Methods
    -------
            test_numberOfDivisors(self, ):
                - Function validates the number of dividers
            test_printedValues(self, ):
                - Function validates if after evaluation the
                divisors are printed into console
    """

    @patch('builtins.input', side_effect=['-1'])
    def test_main_negative(self, _):
        """Function for negative main test usecase."""
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        main()
        assert print_values == ["Nebylo zadáno kladne číslo"]

    @patch('builtins.input', side_effect=['foo'])
    def test_main_string(self, _):
        """Function for string test usecase."""
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        main()
        assert print_values == ["Nebylo zadáno číslo"]

# print documentation using pydoc.
# print documentation for class
