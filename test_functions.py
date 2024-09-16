"""Unittesty funkcí."""

# Inport frameworku unittest a souboru functions
import unittest
import functions


# Třída pro unittesty na délky stran trojúhelníku
class TestDelkaStrany(unittest.TestCase):
    """Unittest na délku stran AB, BC, AC."""

    """Unittest na délku strany AB"""
    def test_delkaStranyAB(self):
        """Unittesty pro stranu AB."""
        self.assertEqual(functions.delkaStranyAB(2, 5, 5, 9), 5)
        self.assertEqual(functions.delkaStranyAB(2, -6, -13, -19), 10)
        self.assertEqual(functions.delkaStranyAB(-2.6, -2.6, 119, 130), 11)

    """Unittest na délku strany |BC|."""
    def test_delkaStranyBC(self):
        """Unittesty pro stranu BC."""
        self.assertEqual(functions.delkaStranyBC(5, 13, 232, 238), 10)
        self.assertEqual(functions.delkaStranyBC(-70, -81, -3, -3), 11)
        self.assertEqual(functions.delkaStranyBC(16, 19, -4, -8), 5)

    """Unittest na délku strany |AC|."""
    def test_delkaStranyAC(self):
        """Unittesty pro stranu AC."""
        self.assertEqual(functions.delkaStranyAC(-3.38, -3.38, -1, 10), 11)
        self.assertEqual(functions.delkaStranyAC(67, 71, 310, 313), 5)
        self.assertEqual(functions.delkaStranyAC(4, -2, -4, -12), 10)


# Třída pro unittesty na obvod a obsah trojúhelníku
class TestObvodObsah(unittest.TestCase):
    """Unittest na obvod a obsah."""

    """Unittest na obvod"""
    def test_obvod(self):
        """Unittesty pro obvod."""
        self.assertEqual(functions.obvodTroj(0, 8, 0, 6, 0, 0), 24)
        self.assertEqual(functions.obvodTroj(0, 3, 0, 4, 0, 0), 12)

    """Unittest na obsah."""
    def test_obsah(self):
        """Unittesty pro obsah."""
        self.assertEqual(functions.obsahTroj(1, 9, 1, 7, 1, 1), 24)
        self.assertEqual(functions.obsahTroj(17, 20, 17, 21, 17, 17), 6)


# Třída pro unittest na zkoušku pravoúhlosti
class TestPravouhlosti(unittest.TestCase):
    """Unittest na zkoušku pravoúhlosti."""

    def test_pravouhlosti(self):
        """Unittesty pro zkoušku pravoúhlosti."""
        self.assertEqual(functions.zkPravouhlosti(0, 3, 0, 4, 0, 0), 1)
        self.assertEqual(functions.zkPravouhlosti(-8, 24, 19, 0, -74, 67), 0)


# Třída pro unittest na zkoušku vstupu
class TestVstupu(unittest.TestCase):
    """Unittest na zkoušku vstupu."""

    def test_vstupy(self):
        """Unittest pro zkoušku vstupu."""
        self.assertEqual(functions.soJeCi("7", "8", "9", "7", "-8", "12"), 1)
        self.assertEqual(functions.soJeCi("7", "", "ju", "*1s", "fk", "re"), 0)
