"""Importovani knihovny unittest."""
import unittest


class TestMethods(unittest.TestCase):
    """Trida urcena k testovani cisel a k nim prirazenym hodnot."""

    def test1(self):
        """Kontrola správné hodnoty."""
        assert prevod(1) == 'I'

    def test2(self):
        """Kontrola správné hodnoty."""
        assert prevod(2) == 'II'

    def test3(self):
        """Kontrola správné hodnoty."""
        assert prevod(3) == 'III'

    def test4(self):
        """Kontrola správné hodnoty."""
        assert prevod(4) == 'IV'

    def test5(self):
        """Kontrola správné hodnoty."""
        assert prevod(5) == 'V'

    def test6(self):
        """Kontrola správné hodnoty."""
        assert prevod(9) == 'IX'

    def test7(self):
        """Kontrola správné hodnoty."""
        assert prevod(10) == 'X'

    def test8(self):
        """Kontrola správné hodnoty."""
        assert prevod(40) == 'XL'

    def test9(self):
        """Kontrola správné hodnoty."""
        assert prevod(50) == 'L'

    def test10(self):
        """Kontrola správné hodnoty."""
        assert prevod(90) == 'XC'

    def test11(self):
        """Kontrola správné hodnoty."""
        assert prevod(100) == 'C'

    def test12(self):
        """Kontrola správné hodnoty."""
        assert prevod(400) == 'CD'

    def test13(self):
        """Kontrola správné hodnoty."""
        assert prevod(500) == 'D'

    def test14(self):
        """Kontrola správné hodnoty."""
        assert prevod(900) == 'CM'

    def test15(self):
        """Kontrola správné hodnoty."""
        assert prevod(1000) == 'M'


"""Prevod na rimske cislo."""


def prevod(cislo):
    """Prevod promenne cislo.

    >>> prevod(1)
    'I'
    """
    """Seznamy znaku a jejich hodnot."""
    hodnota = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    znak = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
            "IV", "I"]
    """Vystup prevodu na rimske cislo."""
    rimske_cislo = ''
    """Promenna urcujici pozici v seznamech."""
    pozice = 0
    while cislo > 0:
        """Hodnota vydeli celociselne se zaokrouhlenim dolu vstup."""
        a = (cislo // hodnota[pozice])
        b = 0
        for b in range(a):
            rimske_cislo = rimske_cislo + znak[pozice]
            cislo = cislo - hodnota[pozice]
        pozice = pozice + 1
    return rimske_cislo


if __name__ == '__main__':
    unittest.main(exit=False)
    cislo = int(input("Zadej čislo: "))
    if cislo < 0:
        print("Číslo nemůže bý záporné")
    elif cislo == 0:
        print("Číslo nesmí být nula")
    else:
        print(prevod(cislo))
