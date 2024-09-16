"""This is the module for transfering arabic numbers to roman.

The module supplies one function: prevod(cislo). For example,

>>> prevod(3)
'III'
"""
import unittest


# funkce pro prevod arabskeho cisla na rimska
def prevod(cislo):
    """Metoda ktera konvertuje arabska cisla na rimska."""
    rimska = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    # arabska cisla
    arabska = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    rimska_cislice = ''
    i = 0
    # zacneme loop dokud neni cislo 0
    while cislo > 0:
        # do stringu zapiseme ekvivalent arabskeho cisla rimskym
        # a ubereme z puvodniho cisla
        for _ in range(cislo // arabska[i]):
            rimska_cislice += rimska[i]
            cislo -= arabska[i]
        i += 1
    # vracime hotovy string
    return rimska_cislice


# try/except je zde kvuli moznosti nezadani cisla
try:
    print("Rimska cislice: ", prevod(int(input("Zadej cislo: "))))
except Exception:
    print("Spatne zadana hodnota! Hodnota musi byt cislo!")


class Test(unittest.TestCase):
    """Class for testing this program."""

    def test_prevod(self):
        """Provede unit test."""
        self.assertEqual(prevod(1), "I")
        self.assertEqual(prevod(10), "X")
        self.assertEqual(prevod(24), "XXIV")
        self.assertEqual(prevod(24998), "MMMMMMMMMMMMMMMMMMMMMMMMCMXCVIII")
        self.assertEqual(prevod(19), "XIX")
        self.assertNotEqual(prevod(19), "XI")
