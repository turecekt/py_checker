"""Test funkce rimskeCislice ze souboru main.py."""


import unittest
from main import rimskeCislice


class TestRimskeCislice(unittest.TestCase):
    """Třída, ve které se testují funkce."""

    def testRimskeCislice23(self):
        """.

        Funkce, ve které se volá funkce,
        která přebýrá jako první parametr funkci rimskeCislice
        a jako druhý parametr, očekávaný výstup.

        """
        self.assertEqual(rimskeCislice(23), "XXIII")

    def testRimskeCislice1234(self):
        """Další test funkce s očekávaným výstupem."""
        self.assertEqual(rimskeCislice(1234), "MCCXXXIV")
