"""Testy na funkci Morseovka."""


from morseovka import sifrovani, desifrovani


def test_sifrovani1():
    """Test testujici string o jednom slove."""
    expected1 = "- . ... -"
    assert sifrovani
    ("test") == expected1


def test_sifrovani2():
    """Test testujici string o vice slovech."""
    expected2 = "-.. .-. .-- .... -.-- / - . ... -"
    assert sifrovani
    ("druhy test") == expected2


def test_desifrovani1():
    """Test testujici desifrovani stringu o dvou slovech."""
    expected3 = "TEST PROSEL"
    assert desifrovani
    ("- . ... - / .--. .-. --- ... . .-.. ") == expected3


def test_desifrovani2():
    """Test testujici desifrovani stringu s cisly."""
    expected4 = "TEST 415 3 5 7"
    assert desifrovani
    ("- . ... - / ....- .---- ..... / ...-- / ..... / --...") == expected4


def test_sifrovani3():
    """Test sifrovani function."""
    expected5 = "Deliciae populi, magno "
    "notissima circo Quintia, vibratas docta "
    assert sifrovani
    ("-.. . .-.. .. -.-. .. .- . / .--. --- .--. ..- .-.. .. /"
     " -- .- --. -. --- / -. --- - .. ... ... .. -- .- /"
     " -.-. .. .-. -.-. --- / --.- ..- .. -. - .. .- /"
     "...- .. -... .-. .- - .- ... / -.. --- -.-. - .-|") == expected5

    expected6 = " My e-mail address is: sample@gmail.com, "
    " but you can call me - fakeDell - ; "

    assert sifrovani
    ("-- -.-- / . -....- -- .- .. .-.. / .- -.. -.. .-. . ... ... /"
     " .. ... / ... .- -- .--. .-.. . .--.-. --. -- .- .. "
     ".-.. .-.-.- -.-. --- -- / -... ..- - / -.-- --- ..- /"
     "-.-. .- -. / -.-. .- .-.. .-.. / -- . /"
     " -....- ..-. .- -.- . -.. . .-.. .-.. -....-") == expected6


def test_desifrovani3():
    """Test get_key function."""
    expected7 = "J"
    assert desifrovani
    (".---") == expected7


def test_desifrovani3b():
    """Test get_key function b."""
    expected8 = "6"
    assert desifrovani
    ("-....") == expected8


def test_desifrovani3c():
    """Test get_key function c."""
    expected9 = "@"
    assert desifrovani
    (".--.-.") == expected9


def test_desifrovani4():
    """Test desifrovani function."""
    expected10 = "The quick brown fox jumps over the lazy dog.  "
    assert desifrovani
    ("- .... . / --.- ..- .. -.-. -.- /"
     " -... .-. --- .-- -. / ..-. --- -..- /"
     " .--- ..- -- .--. ... / --- ...- . .-. /"
     " - .... . / .-.. .- --.. -.-- /"
     " -.. --- --. .-.-.- / /") == expected10

    expected11 = "4 / (8 - 6) = 2  "
    assert desifrovani
    ("....- / -..-. / -.--. ---.. / -....- /"
     " -.... -.--.- / -...- / ..--- / /") == expected11
