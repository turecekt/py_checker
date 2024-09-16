"""Unit testy."""
import unittest

from main import domorse
from main import zmorse


class MyTestCase(unittest.TestCase):
    """Unit testy."""

    def test_something3(self):
        """Unit test na mezeru u metody zmorese."""
        self.assertEqual(zmorse(".-  .- "), "a a ")

    def test_something2(self):
        """Unit test na metodu zmorse."""
        self.assertEqual(zmorse(".-"), "a")

    def test_something1(self):
        """Unit test na metodu domorse."""
        self.assertEqual(domorse("a"), ".- ")


if __name__ == '__main__':
    unittest.main()
