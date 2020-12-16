"""Unit tests for the main.py module."""

import main
import unittest.mock as mock
from point import Point


def test_print_triangle_info():
    """Unit test for the print_triangle_info function."""
    point_a = Point(5, 10)
    point_b = Point(10, 20)
    point_c = Point(50, -10)
    main.print_triangle_info(point_a, point_b, point_c)


class InputGenerator:
    """A class used to simulate user input in the CLI.

    The main.request_point() function has an infinite loop that keeps
    repeating until the user enters a valid value. This class is used to
    simulate the user entering 2 invalid values and then a valid value.
    """

    def __init__(self):
        """Initialize the iterator attribute."""
        self.iterator = 0

    def get_input(self):
        """Return a string to simulate user input.

        Return (str)
            the input string
        """
        self.iterator = self.iterator + 1
        if self.iterator == 1:
            return "0"
        if self.iterator == 2:
            return "0 abc"
        else:
            return "0 100"


def test_request_point():
    """Unit test for the request_point function."""
    generator = InputGenerator()
    with mock.patch("builtins.input", wraps=generator.get_input):
        point = main.request_point("A")
        assert point.x == 0


def test_init():
    """Unit test for the init function."""
    with mock.patch.object(main, "__name__", "__main__"), \
            mock.patch.object(main.sys, 'exit') as mock_exit, \
            mock.patch.object(main, 'print_triangle_info'), \
            mock.patch("main.request_point", return_value=Point(50, 50)):
        with mock.patch.object(main.sys, 'argv',
                               ["main", 0, 0, 100, 0, 0, 100]):
            main.init()
            assert mock_exit.call_args[0][0] == 0  # check the exit code

        with mock.patch.object(main.sys, 'argv',
                               ["main", 0, 0, "abc", 0, 0, 100]):
            main.init()
            assert mock_exit.call_args[0][0] != 0  # check the exit code

        with mock.patch.object(main.sys, 'argv', ["main", 0, 0]):
            main.init()
            assert mock_exit.call_args[0][0] != 0  # check the exit code

        with mock.patch.object(main.sys, 'argv', ["main"]):
            main.init()
            assert mock_exit.call_args[0][0] == 0  # check the exit code
