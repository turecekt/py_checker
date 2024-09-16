"""Soubor pro funkce s unit testy."""

from soustava import prevod


def test_soustava8():
    """Funkce pro otestování prevodu do 8-ové soustavy."""
    assert prevod(405, 8) == '625'
    assert prevod(793, 8) == '1431'
    assert prevod(25, 8) == '31'
    assert prevod(6320, 8) == '14260'
    assert prevod(78, 8) == '116'
    assert prevod(156, 8) == '234'
    assert prevod(435, 8) == '663'
    assert prevod(35, 8) == '43'
    assert prevod(932, 8) == '1644'
    assert prevod(2250, 8) == '4312'


def test_soustava2():
    """Funkce pro otestování prevodu do 2-ové soustavy."""
    assert prevod(405, 2) == '110010101'
    assert prevod(58, 2) == '111010'
    assert prevod(1025, 2) == '10000000001'
    assert prevod(1100, 2) == '10001001100'
    assert prevod(2250, 2) == '100011001010'
    assert prevod(435, 2) == '110110011'
    assert prevod(35, 2) == '100011'
    assert prevod(932, 2) == '1110100100'


def test_soustava3():
    """Funkce pro otestování prevodu do 3-ové soustavy."""
    assert prevod(405, 3) == '120000'
    assert prevod(58, 3) == '2011'
    assert prevod(1025, 3) == '1101222'
    assert prevod(12, 3) == '110'
    assert prevod(2250, 3) == '10002100'
    assert prevod(435, 3) == '121010'
    assert prevod(35, 3) == '1022'
    assert prevod(932, 3) == '1021112'


def test_soustava12():
    """Funkce pro otestování prevodu do 12-ové soustavy."""
    assert prevod(405, 12) == '299'
    assert prevod(58, 12) == '4A'
    assert prevod(1025, 12) == '715'
    assert prevod(12, 12) == '10'
    assert prevod(2250, 12) == '1376'
    assert prevod(435, 12) == '303'
    assert prevod(35, 12) == '2B'
    assert prevod(932, 12) == '658'


def test_soustava16():
    """Funkce pro otestování prevodu do 16-ové soustavy."""
    assert prevod(405, 16) == '195'
    assert prevod(58, 16) == '3A'
    assert prevod(1025, 16) == '401'
    assert prevod(12, 16) == 'C'
    assert prevod(2250, 16) == '8CA'
    assert prevod(435, 16) == '1B3'
    assert prevod(35, 16) == '23'
    assert prevod(932, 16) == '3A4'
