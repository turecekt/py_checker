"""Unit testy pro prekladac moserseovky."""

import unittest
from morse import MorseCodeTranslator


class TestMorseCodeTranslator(unittest.TestCase):
    """Testy prekladu morseovky na text."""

    def test_morse_to_text_no_morse(self):
        """Test na prazdny vstup."""
        translator = MorseCodeTranslator()
        morse = ""
        expected_output = "Musite vlozit string na preklad!"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text(self):
        """Test morseovky na text."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_numbers(self):
        """Test morseovky na cisla."""
        translator = MorseCodeTranslator()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_punctuation(self):
        """Test morseovky na znaky."""
        translator = MorseCodeTranslator()
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.--"
        expected_output = "&'@)(:,=!"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text_not_strict(self):
        """Test morseovky na text bez kontroly mezer."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.translate_morse(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        """Test morseovky na text s kontrolou mezer."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Chyba! Nalezeny 4 mezery ve stringu."
        )
        self.assertEqual(
            translator.translate_morse(morse, strict=True), expected_output
        )

    """Testy prekladu textu na morseovku."""

    def test_text_to_morse_no_text(self):
        """Test na prazdny vstup."""
        translator = MorseCodeTranslator()
        text = ""
        expected_output = "Musite vlozit string na preklad!"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_text_to_morse(self):
        """Test textu na morseovku."""
        translator = MorseCodeTranslator()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_numbers_to_morse(self):
        """Test cisel na morsovku."""
        translator = MorseCodeTranslator()
        text = "12345678"
        expected_output = ".---- ..--- ...-- ....- ..... -.... --... ---.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_punctuation_to_morse(self):
        """Test znaku na morseovku."""
        translator = MorseCodeTranslator()
        text = "&'@)(:,"
        expected_output = ".-... .----. .--.-. -.--.- -.--. ---... --..--"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_all_to_morse(self):
        """Test kombinace symbolu na morseovku."""
        translator = MorseCodeTranslator()
        text = "1h+"
        expected_output = ".---- .... .-.-."
        self.assertEqual(translator.translate_text(text), expected_output)


if __name__ == "__main__":
    unittest.main()
