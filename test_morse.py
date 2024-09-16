"""Unit testy."""

import unittest

import source


class Test(unittest.TestCase):
    """Class tests."""

    def test_sifrovani(self):
        """Unit test pro sifrovaci funkci."""
        vstup = source.sifrovani("test")
        self.assertEqual(vstup, "- . ... - ")

    def test_sifrovani_1(self):
        """Unit test pro sifrovaci funkci."""
        vstup = source.sifrovani("1, 2, 3, 4")
        self.assertEqual(vstup, ".---- --..--  "
                                "..--- --..--  ...-- --..--  ....- ")

    def test_sifrovani_2(self):
        """Unit test pro sifrovaci funkci."""
        vstup = source.sifrovani("text s mezerami")
        self.assertEqual(vstup, "- . -..- -  ...  -- . --.. . .-. .- -- .. ")

    def test_sifrovani_3(self):
        """Unit test pro sifrovaci funkci."""
        vstup = source.sifrovani(",? )( !")
        self.assertEqual(vstup, "--..-- ..--..  -.--.- -.--.  -.-.-- ")

    def test_desifrovani(self):
        """Unit test pro desifrovaci funkci."""
        vstup = source.desifrovani("- . ... -")
        self.assertEqual(vstup, "TEST")

    def test_desifrovani_1(self):
        """Unit test pro desifrovaci funkci."""
        vstup = source.desifrovani("----- -----  .----  ..---  ...--  ....-")
        self.assertEqual(vstup, "00 1 2 3 4")

    def test_desifrovani_2(self):
        """Unit test pro desifrovaci funkci."""
        vstup = source.desifrovani(".-.-.- --..-- ..--.. -.-.-- -.--."
                                   "- -.--. -..-.")
        self.assertEqual(vstup, ".,?!)(/")

    def test_sifrovani_4(self):
        """Unit test pro desifrovaci funkci."""
        vstup = source.sifrovani("TEST VELKYCH PISMEN")
        self.assertEqual(vstup, "- . ... -  ...- . .-.. -.- "
                                "-.-- -.-. ....  .--. .. ... -- . -. ")


if __name__ == '__main__':
    unittest.source()
