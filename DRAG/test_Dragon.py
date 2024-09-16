"""Module (file) docstring."""
import unittest
from Dragon import sides, input_data


class TestDragonCurve(unittest.TestCase):
    """Class for testing individual program functions Dragon.py."""

    def test_sides2(self):
        """Function test, with the number of iterations equal to two."""
        q = sides(2)
        self.assertEqual(q, 'rrl')

    def test_sides3(self):
        """Function test, with the number of iterations equal to three."""
        q = sides(3)
        self.assertEqual(q, 'rrlrrll')

    def test_sider4(self):
        """Function test, with the number of iterations equal to four."""
        q = sides(4)
        self.assertEqual(q, 'rrlrrllrrrllrll')

    def test_sider5(self):
        """Function test, with the number of iterations equal to five."""
        q = sides(5)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrll')

    def test_sider6(self):
        """Function test, with the number of iterations equal to six."""
        q = sides(6)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrr'
                            'rlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider7(self):
        """Function test, with the number of iterations equal to seven."""
        q = sides(7)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrlllrrl'
                            'rrllrrrllrlllrrlrrlllrrllrll')

    def test_sider8(self):
        """Function test, with the number of iterations equal to eight."""
        q = sides(8)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrl'
                            'lrrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrl'
                            'llrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrlll'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlll'
                            'rrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider9(self):
        """Function test, with the number of iterations equal to nine."""
        q = sides(9)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrl'
                            'lrrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrl'
                            'llrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrlll'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlll'
                            'rrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrllr'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlllr'
                            'rlrrllrrrllrlllrrlrrlllrrllrlllr'
                            'rlrrllrrrllrllrrrlrrlllrrllrllrrr'
                            'lrrllrrrllrlllrrlrrlllrrllrlllrr'
                            'lrrllrrrllrllrrrlrrlllrrllrlllrrlr'
                            'rllrrrllrlllrrlrrlllrrllrll')

    def test_color(self):
        """Function test color."""
        q = input_data
        default = "default"
        empty_value = ""
        value = "value"
        self.assertEqueal(default, q(empty_value, default))
        self.assertEqueal(value, q(value, default))

    def assertEqueal(self, default, param):
        """color."""
        pass


if __name__ == '__main__':
    unittest.main()
