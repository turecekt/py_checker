"""Unittesty funkcí."""

# Inport frameworku unittest a souboru functions
import unittest
import functions

# Rychlý způsob, jak napsat modul, který jde jak importovat, tak spustit
if __name__ == '__main__':
    unittest.main()


# Třída pro unittesty na délky stran trojúhelníku
class TestDelkaStrany(unittest.TestCase):
    """Unittest na délku stran AB, BC, AC."""
