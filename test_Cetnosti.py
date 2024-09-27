"""Test fuknci z CetnostZnaky."""


import unittest
from CetnostZnaku import PocetZnak, MinZnak, MaxZnak, PocetKazdyZnak


class TestCases(unittest.TestCase):
    """TestClass pro testovani funkci z CetnostZnaky."""

    def test_PocetZnak(self):
        """Test počtu znaků ze vstupním z textu."""
        vstup = "AAAAAAAA#"
        self.assertEqual(PocetZnak(vstup), 8)

    def test_PocetZnakFromFile(self):
        """Test počtu znaků ze vstupním souboru."""
        vstup = "test_file.txt"
        self.assertEqual(PocetZnak(vstup), 0)

    def test_MinZnak(self):
        """Test informace o minimálním počtu znaků ve vstupním textu."""
        vstup = "Python jeden#"
        self.assertEqual(MinZnak(vstup), ['P', 'Y',
                                          'T', 'H', 'O', 'J', 'D', '#'])

    def test_MinZnakNoHash(self):
        """Test o minimálním počtu znaků bez validniho ukonceni."""
        vstup = "AA"
        self.assertEqual(MinZnak(vstup), 0)

    def test_MaxZnakText(self):
        """Test informace o maximálním počtu znaků ve vstupním textu."""
        vstup = "Python ma spustu AAAAAAA#"
        self.assertEqual(MaxZnak(vstup), ['A'])

    def test_MaxZnakFile(self):
        """Test informace o maximálním počtu znaků ve vstupním soubor."""
        vstup = "test_fileMax.txt"
        self.assertEqual(MaxZnak(vstup), ['A'])

    def test_MinZnakNoHashinFile(self):
        """Test informace o minimálním počtu znaků ze souboru."""
        vstup = "test_file.txt"
        self.assertEqual(MinZnak(vstup), 0)

    def test_PocetKazdyZnakInFile(self):
        """Test funkce ktera vypise pocet kazdeho znaku z vlozeneho file."""
        vstup = "test_filePocet.txt"
        self.assertEqual(PocetKazdyZnak(vstup), {'T': 5, 'E': 4,
                                                 'X': 1, 'P': 2, 'R': 1,
                                                 'O': 2, 'S': 1, 'F': 1,
                                                 'N': 2, 'C': 2,
                                                 'K': 2, 'A': 2, 'Z': 2,
                                                 'D': 1, 'Y': 1, '#': 1})

    def test_PocetKazdyZnakInText(self):
        """Test funkce ktera vypise pocet kazdeho znaku z vlozeneho textu."""
        vstup = "Python max znaku#"
        self.assertEqual(PocetKazdyZnak(vstup), {'P': 1, 'Y': 1, 'T': 1,
                                                 'H': 1, 'O': 1,  'N': 2,
                                                 'M': 1, 'A': 2, 'X': 1,
                                                 'Z': 1, 'K': 1, 'U': 1,
                                                 '#': 1})


if __name__ == '__main__':
    unittest.main()
