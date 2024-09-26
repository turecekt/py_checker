# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:40:00 2020.

@author: pavel
"""

import unittest
import morse


class TestMorse(unittest.TestCase):
    """Trida unit-testu."""

    def test_morse_na_text(self):
        """Test z morseovky na text."""
        result = morse.decryption(".- -... -.-. -.. . ..-. --. .... .. .--- "
                                  "-.- .-.. -- -. --- .--. --.- .-. ... - ..- "
                                  "...- .-- -..- -.-- --..")
        self.assertEqual(result, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_morse_na_cisla(self):
        """Test z morseovky na cisla."""
        result = morse.decryption(".---- ..--- ...-- ....- ..... -.... --... "
                                  "---.. ----. -----")
        self.assertEqual(result, "1234567890")

    def test_morse_na_znaky(self):
        """Test z morseovky na znaky."""
        result = morse.decryption(".-... .----. .--.-. -.--.- -.--. ---... "
                                  "--..-- -...- -.-.-- .-.-.- -....- .-.-. "
                                  "..--.. -..-.")
        self.assertEqual(result, "&'@)(:,=!.-+?/")

    def test_text_na_morse(self):
        """Test z textu na morseovku."""
        result = morse.encryption("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(result, ".- -... -.-. -.. . ..-. --. .... .. .--- "
                         "-.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- "
                         ".-- -..- -.-- --.. ")

    def test_cisla_na_morse(self):
        """Test z cisel na morseovku."""
        result = morse.encryption("1234567890")
        self.assertEqual(result, ".---- ..--- ...-- ....- ..... -.... --... "
                         "---.. ----. ----- ")

    def test_znaky_na_morse(self):
        """Test ze znaku na morseovku."""
        result = morse.encryption("&'@)(:,=!.-+?/")
        self.assertEqual(result, ".-... .----. .--.-. -.--.- -.--. ---... "
                         "--..-- -...- -.-.-- .-.-.- -....- .-.-. "
                         "..--.. -..-. ")


if __name__ == "__main__":
    unittest.main()
