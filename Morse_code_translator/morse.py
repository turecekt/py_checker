"""Závěrečný projekt - ZM.

This code translates text to morse/morse to text with letters,
 numbers and punctuation.
"""


class MorseCodeTranslator:
    """Text to morse vocabulary."""

    #  Morse code
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
        """Translate morse code to english.

        Accepts:
            morse (str): A string of morse code to translate
            strict (bool): If True, parse and return morse code with 4 spaces
        Returns:
            str: A translated string of text
        """
        if morse == "":
            return "You must provide a string of text to translate"

        if "    " in morse:
            if strict:
                return "Unable to translate morse code."
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
        """Translate text to morse code.

        Accepts:
            text (str): A string of text to translate
        Returns:
            str: A translated string of morse code
        """
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
