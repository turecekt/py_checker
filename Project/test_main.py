"""Test module."""
import main


def test_convert_binary():
    """Test function convert_binary."""
    assert main.convert_binary(78) == "1001110"
    assert main.convert_binary(1) == "1"
    assert main.convert_binary(100) == "1100100"
    assert main.convert_binary(2020) == "11111100100"
    assert main.convert_binary(2020) == "11111100100"


def test_convert_octal():
    """Test function convert decimal num to octal."""
    assert main.convert_octal(156) == "234"
    assert main.convert_octal(0) == "0"
    assert main.convert_octal(123456789) == "726746425"
    assert main.convert_octal(2020) == "3744"


def test_convert_hexadecimal():
    """Test function convert_hexadecimal."""
    assert main.convert_hexadecimal(0) == "0"
    assert main.convert_hexadecimal(1) == "01"
    assert main.convert_hexadecimal(2) == "02"
    assert main.convert_hexadecimal(3) == "03"
    assert main.convert_hexadecimal(4) == "04"
    assert main.convert_hexadecimal(5) == "05"
    assert main.convert_hexadecimal(6) == "06"
    assert main.convert_hexadecimal(7) == "07"
    assert main.convert_hexadecimal(8) == "08"
    assert main.convert_hexadecimal(9) == "09"
    assert main.convert_hexadecimal(10) == "0A"
    assert main.convert_hexadecimal(11) == "0B"
    assert main.convert_hexadecimal(12) == "0C"
    assert main.convert_hexadecimal(13) == "0D"
    assert main.convert_hexadecimal(14) == "0E"
    assert main.convert_hexadecimal(15) == "0F"
