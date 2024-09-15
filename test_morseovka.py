"""Unittest pro morseovku."""

import unittest
import morseovka


class TestMorseovka(unittest.TestCase):
    """Tato trida funguje jako testovaci trida."""

    def test_5(self):
        """Testovani pro vyber pismena a kodu."""
        self.assertEqual(morseovka.Text_To_Code("A"), ".- ")

    def test_4(self):
        """Testovani prekladu kodu do textu."""
        self.assertEqual(morseovka.Code_To_Text("... --- ... "), "SOS")

    def test_3(self):
        """Testovani prekladu do morseovky."""
        self.assertEqual(morseovka.Text_To_Code("sos"), "... --- ... ")

    def test_1(self):
        """Testovani zvetsovani pismen."""
        self.assertEqual("abc".upper(), "ABC")
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())

    def test_2(self):
        """Prevod na rozlozeni textu."""
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "main":
    unittest.main()
