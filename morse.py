"""Hlavni modul kod na preklad morseovky."""


class MorseCodeTranslator:
    """Definice prekladu znaku."""

    morse = {
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
        """
        Prelozi morseovku na text.

        Vraci:
            str: Prelozeny string textu
        """
        if morse == "":
            return "Musite vlozit string na preklad!"

        if "    " in morse:
            if strict:
                return "Chyba! Nalezeny 4 mezery ve stringu."
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
        """
        Prelozi text do morseovky.

        Vraci:
            str: Prelozeny string morseovky
        """
        if text == "":
            return "Musite vlozit string na preklad!"

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
