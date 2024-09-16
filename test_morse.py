"""Unit testy."""

import unittest

import morse


class Test(unittest.TestCase):
    """Class testy."""

    # Morseova abeceda na text
    def test_morse_na_cisla(self):
        """Unit test."""
        prekladac = morse.decrypt(".---- ..--- ...-- ....- ..... ")
        self.assertEqual(prekladac, "12345 ")

    def test_morse_na_text(self):
        """Unit test."""
        prekladac = morse.decrypt(".- .... --- .---  ... ...- . - ")
        self.assertEqual(prekladac, "AHOJ SVET ")

    def test_morse_na_znaky(self):
        """Unit test."""
        prekladac = morse.decrypt(".-... .----. .--.-. -.--.- -.--. "
                                  "---... --..-- -...- -.-.-- .-.-.- "
                                  "-....- .-.-. ..--.. -..-. ")
        self.assertEqual(prekladac, "&'@)(:,=!.-+?/ ")

    # Text na morseovu abecedu
    def test_cisla_na_morse(self):
        """Unit test."""
        prekladac = morse.encrypt("67890")
        self.assertEqual(prekladac, "-.... --... ---.. ----. ----- ")

    def test_text_na_morse(self):
        """Unit test."""
        prekladac = morse.encrypt("AHOJ SVET ")
        self.assertEqual(prekladac, ".- .... --- .---  ... ...- . -  ")

    def test_mix_na_morse(self):
        """Unit test."""
        prekladac = morse.encrypt("AHOJ 123 SVET")
        self.assertEqual(prekladac, ".- .... --- .---  .---- ..--- ...-- "
                                    " ... ...- . - ")

    def test_znaky_na_morse(self):
        """Unit test."""
        prekladac = morse.encrypt("&'@)(:,=!.-+?/")
        self.assertEqual(prekladac, ".-... .----. .--.-. -.--.- -.--. ---... "
                                    "--..-- -...- -.-.-- .-.-.- -....- "
                                    ".-.-. ..--.. -..-. ")


if __name__ == "__main__":
    unittest.morse()
