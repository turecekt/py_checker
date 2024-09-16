"""Unittesty."""

import unittest
from Morseovka import texttomorse, morsetotext


class TestMorseovka(unittest.TestCase):
    """Spusteni testu."""

    def test_texttomorse(self):
        """Prelozeni z textu do kodu morse."""
        self.assertEqual(texttomorse(
            "qwerty"), "--.- .-- . .-. - -.-- ")

    def test_texttomorse1(self):
        """Prelozeni z textu s mezerami do kodu morse."""
        self.assertEqual(texttomorse(
            "qwerty asdfg zxcv"),
            "--.- .-- . .-. - -.-- |"
            " .- ... -.. ..-. --. | --.. -..- -.-. ...- ")

    def test_morsetotext(self):
        """Prelozeni z kodu morse do textu."""
        self.assertEqual(morsetotext(
            "--.- .-- . .-. - -.--"),
            "qwerty")

    def test_morsetotext1(self):
        """Prelozeni z kodu morse s mezerami do textu."""
        self.assertEqual(morsetotext(
            "--.- .-- . .-. - -.-- | -.-- - .-. . .-- --.-"),
            "qwerty ytrewq")


if __name__ == '__main__':
    unittest.main()
