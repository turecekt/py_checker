"""
Skript s unit testy.

Pro program pro preklad textu na morseovku a naopak.
Petr Marak a Pavel Cuba, 2020
"""

from source import encode, decode


# unit testy
def test_encode():
    """Unit test 1."""
    assert encode("sos") == "...|---|..."
    assert encode("ahoj") == ".-|....|---|.---"
    assert encode("wikipedia") == ".--|..|-.-|..|.--.|.|-..|..|.-"
    assert encode("encyklopedie") == \
           ".|-.|-.-.|-.--|-.-|.-..|---|.--.|.|-..|..|."
    assert encode("xbmc 0451") == "-..-|-...|--|-.-.||-----|....-|.....|.----"
    assert encode("!?#") is None


def test_decode():
    """Unit test 2."""
    assert decode("...|---|...") == "sos"
    assert decode(".-|....|---|.---") == "ahoj"
    assert decode(".--|..|-.-|..|.--.|.|-..|..|.-") == "wikipedia"
    assert decode(".|-.|-.-.|-.--|-.-|.-..|---|.--.|.|-..|..|.") == \
           "encyklopedie"
    assert decode("-..-|-...|--|-.-.||-----|....-|.....|.----") == "xbmc 0451"
    assert decode("!?#") is None
