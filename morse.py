"""
Hello, this is a morse code translator.

Works from morse to english and from english to morse.

Go ahead and try it through the ex.py file
Thanks for your attention
"""
import unittest


class MorseTranslator:
    """Define all letters and characters and their morse equivalents."""

    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }

    def translate_morse(self, morse, strict=True):
        """Translate morse code to text."""
        if morse == "":
            return "You must provide a string of text to translate"

        if "    " in morse:
            if strict:
                return "Can't translate morse code. Found 4 spaces in string"
            else:
                morse.replace("    ", "   ")

        translation = ""

        words = morse.split("   ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.morse.items():
                    if char == v:
                        translation += k
            translation += " "

        return translation.rstrip()

    def translate_text(self, text):
        """Translate text to morse code."""
        if text == "":
            return "You must provide a morse code string to translate"

        translation = ""

        words = text.split(" ")

        for word in words:
            w = list()
            for char in word:
                if char.lower() in self.morse:
                    w.append(self.morse[char.lower()])

            translation += " ".join(w)
            translation += "   "

        return translation.rstrip()


class TestMorseTranslator(unittest.TestCase):
    """Unit tests for all functions are here."""

    # Morse code to text
    def test_morse_to_text_no_morse(self):
        """Test morse code to text (no input)."""
        translator = MorseTranslator()
        morse = ""
        expected_output = "You must provide a string of text to translate"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text(self):
        """Test morse code to text (with input)."""
        translator = MorseTranslator()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_numbers(self):
        """Test morse code to numbers."""
        translator = MorseTranslator()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_punctuation(self):
        """Test morse code to punctuation."""
        translator = MorseTranslator()
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- " \
                "-.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:,=!.-+\"?/"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text_not_strict(self):
        """Test morse code to text (not strict)."""
        translator = MorseTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.translate_morse(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        """Test morse code to text (strict)."""
        translator = MorseTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Can't translate morse code. Found 4 spaces in string"
        )
        self.assertEqual(
            translator.translate_morse(morse, strict=True), expected_output
        )

    # Text to morse code
    def test_text_to_morse_no_text(self):
        """Test text to morse code (no text input)."""
        translator = MorseTranslator()
        text = ""
        expected_output = "You must provide a morse code string to translate"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_text_to_morse(self):
        """Test text to morse code (with input)."""
        translator = MorseTranslator()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_numbers_to_morse(self):
        """Test numbers to morse code."""
        translator = MorseTranslator()
        text = "1234567890"
        expected_output = ".---- ..--- ...-- ....- ..... -.... --... ---.." \
                          " ----. -----"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_punctuation_to_morse(self):
        """Test punctuation to morse code."""
        translator = MorseTranslator()
        text = "&'@)(:,=!.-+?/"
        expected_output = ".-... .----. .--.-. -.--.- -.--. ---... --..-- " \
                          "-...- -.-.-- .-.-.- -....- .-.-. ..--.. -..-."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_all_to_morse(self):
        """Test everything combined to morse code."""
        translator = MorseTranslator()
        text = "Hello .. 12 & 7+8 9 10, (this) is? 'Just' @ some testing!"
        expected_output = ".... . .-.. .-.. ---   " \
                          ".-.-.- .-.-.-   .---- ..---   .-...   " \
                          "--... .-.-. ---..   ----." \
                          "   .---- ----- --..--   -.--. - .... .. ..." \
                          " -.--.-   .. ... ..--..   .----. .--- ..- ..." \
                          " - .----.   .--.-.   ... --- -- .   - . ... -" \
                          " .. -. --. -.-.--"
        self.assertEqual(translator.translate_text(text), expected_output)


if __name__ == "__main__":
    unittest.main()
