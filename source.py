"""Program pro převod z Morseovky do abecedy a naopak."""
import unittest


def prevod(vstup):
    """Funkce pro tuto akci."""
    # Vytvoření dictionary pro morseovku
    morseovka = {
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': ' '}

    g = ""

    # Převedení z morseovky na text
    if vstup.startswith('.') or vstup.startswith('-'):

        # Rozdělení morseovky na jednotlivé kombinace
        rozdVstup = vstup.split(' ')

        # Vytvoření cyklu pro převod z morseovky na text
        for prvek in rozdVstup:
            if prvek not in morseovka.values():
                # Ošetření vstupu
                print('Zadaná nesprávná kombince znaků')
                exit()
            for i in morseovka:
                if prvek == morseovka[i]:
                    g = g + i

        return g

    # Převedení z textu do morseovky
    else:

        # Převedení textu na velká písmena
        vstupV = vstup.upper()

        # Převedení textu na pole znaků
        rozdVstup = list(vstupV)

        # Vytvoření cyklu for pro převod zadaných znaků do morseovky

        for prvek in rozdVstup:
            if prvek not in morseovka:
                # Ošetření vstupu
                g = 'Zadaná nesprávná kombince znaků'
                return g
            for i in morseovka:
                if prvek == i:
                    g = g + morseovka[i] + ' '

        return g


def main():
    """Hlavní funkce pro spuštění programu."""
    # Vytvoření vstupu
    print('--KODÉR A DEKODÉR MORSEOVKY--')
    vstup = input('Zadejte text pro převod: ')

    # Výstup
    print(prevod(vstup))


"""Testování source."""
# Testovácí class


class TestMorseovky(unittest.TestCase):
    """Tato class funguje pro testování našeho source."""

    # PŘEVODY Z ABECEDY DO MORSEOVKY
    def test_1(self):
        """Jen písmena všechna malá."""
        result = prevod("sos")
        self.assertEqual(result, "... --- ... ")

    def test_2(self):
        """Jen písmena všechna velká."""
        result = prevod("AHOJ")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_3(self):
        """Kombinace velkých a malých písmen."""
        result = prevod("AhOj")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_4(self):
        """Jen čísla."""
        result = prevod("365")
        self.assertEqual(result, "...-- -.... ..... ")

    def test_5(self):
        """Čísla a písmena."""
        result = prevod("Mam 20 let")
        self.assertEqual(result, "-- .- --   ..--- -----   .-.. . - ")

    # PŘEVODY Z MORSEOVKY DO ABECEDY
    def test_6(self):
        """Jen písmena."""
        result = prevod(".- .... --- .---")
        self.assertEqual(result, "AHOJ")

    def test_7(self):
        """Jen čísla."""
        result = prevod("...-- -.... .....")
        self.assertEqual(result, "365")

    def test_8(self):
        """Čísla a písmena."""
        result = prevod("-- .- -- ..--- ----- .-.. . -")
        self.assertEqual(result, "MAM20LET")

    def test_9(self):
        """Čísla, písmena."""
        result = prevod("-.. -. . ... -.- .- .--- . .--. ."
                        " -.- -. -.-- -.. . -. .- .--- . ..--- "
                        "---.. ... - ..- .--. -. ..-")
        self.assertEqual(result, "DNESKAJEPEKNYDENAJE28STUPNU")

    def test_10(self):
        """Nepovolené znaky na začátku."""
        result = prevod("?ahoj")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')

    def test_11(self):
        """Nepovolené znaky uprostřed."""
        result = prevod("ah?oj")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')

    def test_12(self):
        """Nepovolené znaky na konci."""
        result = prevod("ahoj?")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')


if __name__ == '__main__':
    main()
