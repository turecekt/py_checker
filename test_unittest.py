"""pytest."""
from Main import text_do_mors, mors_do_text, main


pole = "priklad"


def test_main_chec_text_do_mors():
    """Definuje text."""
    text_do_mors(pole)


def test_main_chec_mors_do_text():
    """Definuje mors."""
    mors_do_text(pole)


def test_mors_do_text1():
    """Zakodovanie slova SOS test."""
    mors1 = "... --- ..."
    assert mors_do_text
    ("S O S") == mors1


def test_mors_do_text2():
    """Zakodovanie slova AHOJ test."""
    mors1 = ".- .... --- .---"
    assert mors_do_text
    ("S O S") == mors1


def test_text_do_mors1():
    """Dekodovanie SOS."""
    text1 = "S O S"
    assert text_do_mors
    ("... --- ...") == text1


def test_main():
    """Testovanie response."""
    response = "1"
    assert main
    ("Napiste morseovku (s mezerou mezi kazdym pismenem): ") == response


def test_main2():
    """Testovanie či funguje 2."""
    response2 = "2"
    assert main
    ("Napište text: ") == response2
