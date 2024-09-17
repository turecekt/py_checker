"""Unit test for MorseCode."""
import unittest
from morse import MorseCodeTranslator


class TestMorseCodeTranslator(unittest.TestCase):
    """Unit tests."""

    # Morse code to text
    def test_morse_to_text_no_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ""
        expected_output = "You must provide a string of text to translate"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_numbers(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_punctuation(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".-... .--.-. -.--.- -.--. -...- -.-.-- -....- .-.-. ..--.."
        x = "&@)(=!-+?"
        self.assertEqual(translator.translate_morse(morse), x)

    def test_morse_to_punctuation1(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".----. ---... --..-- .-.-.- .-..-. -..-."
        x = "':,.\"/"
        self.assertEqual(translator.translate_morse(morse), x)

    def test_morse_to_text_not_strict(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.translate_morse(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Unable to translate morse code."
        )
        self.assertEqual(
            translator.translate_morse(morse, strict=True), expected_output
        )

    def test_morse_to_text1(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = "!<testing>!?"
        x = "-.-.-- - . ... - .. -. --. -.-.-- ..--.."
        self.assertEqual(translator.translate_text(morse), x)

    def test_morse_to_text2(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = "12 & 4 56 7+8"
        x = ".---- ..---   .-...   ....-   ..... -....   --... .-.-. ---.."
        self.assertEqual(translator.translate_text(morse), x)

    def test_morse_to_text3(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = "(this) is?"
        x = "-.--. - .... .. ... -.--.-   .. ... ..--.."
        self.assertEqual(translator.translate_text(morse), x)

    # Text to morse code
    def test_text_to_morse_no_text(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = ""
        expected_output = "You must provide a morse code string to translate"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_text_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_numbers_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "1234567890"
        exp_out = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        self.assertEqual(translator.translate_text(text), exp_out)

    def test_punctuation_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "&@)(=!-+?"
        x = ".-... .--.-. -.--.- -.--. -...- -.-.-- -....- .-.-. ..--.."
        self.assertEqual(translator.translate_text(text), x)

    def test_punctuation_to_morse1(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "':,.\"/"
        x = ".----. ---... --..-- .-.-.- .-..-. -..-."
        self.assertEqual(translator.translate_text(text), x)

    def test_all_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "Hello world.."
        x = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.. .-.-.- .-.-.-"
        self.assertEqual(translator.translate_text(text), x)

    def test_all_to_morse1(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "12 & 4 56 7+8"
        x = ".---- ..---   .-...   ....-   ..... -....   --... .-.-. ---.."
        self.assertEqual(translator.translate_text(text), x)

    def test_all_to_morse2(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "(this) is?"
        x = "-.--. - .... .. ... -.--.-   .. ... ..--.."
        self.assertEqual(translator.translate_text(text), x)

    def test_all_to_morse3(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "'Just' @#,.:"
        x = ".----. .--- ..- ... - .----.   .--.-. --..-- .-.-.- ---..."
        self.assertEqual(translator.translate_text(text), x)

    def test_all_to_morse4(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "!<testing>!?"
        x = "-.-.-- - . ... - .. -. --. -.-.-- ..--.."
        self.assertEqual(translator.translate_text(text), x)


if __name__ == "__main__":
    unittest.main()
