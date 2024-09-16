"""Pytest pro main.py."""

import main
import pytest


def test_parseToRomanNumeral_success():
    """Test function for parsing."""
    assert main.parseToRomanNumeral("2356") == "MMCCCLVI"


def test_parseToRomanNumeral_fail():
    """Test function for parsing."""
    with pytest.raises(Exception):
        assert main.parseToRomanNumeral("invalidni text")


def test_checkInputAndPrintRomanNumeral_success(capfd):
    """Test for valid input and parsing to roman numerals."""
    main.checkInputAndPrintRomanNumeral("1994")
    out, err = capfd.readouterr()
    assert out == "MCMXCIV\n"


def test_checkInputAndPrintRomanNumeral_invalidInput():
    """Test for invalid input raising exception."""
    with pytest.raises(Exception):
        assert main.checkInputAndPrintRomanNumeral("invalidni text")
