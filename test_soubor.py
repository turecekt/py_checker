"""Unit tests."""

import soubor


def test_fileExists():
    """File_exists unit test."""
    text = "ahoj"
    actual = soubor.fileExists("ahoj.txt")
    assert(actual.read() == text)


def test_TextIntoVar():
    """Text_into_var unit test."""
    file = 'ahoj'
    actual = soubor.textIntoVar('ahoj.txt')
    assert(actual == file)


def test_CharNum():
    """Char_num unit test."""
    assert soubor.charNum("Nikolas") == 7


def test_mostFreq():
    """Most_freq unit test."""
    assert soubor.mostFreq('Nina') == ('n', 2)


def test_leastFreq():
    """Least_freq unit test."""
    assert soubor.leastFreq('Uz je to tady') == 'u'


def test_numOfEachChar():
    """Num_of_each_char unit test."""
    assert soubor.numOfEachChar("Uz je to tady") == {'u': 1, 'z': 1, ' ': 3,
                                                     'j': 1, 'e': 1, 't': 2,
                                                     'o': 1, 'a': 1, 'd': 1,
                                                     'y': 1}


def test_avarage():
    """Average unit test."""
    each = "Nikolas"
    assert soubor.average(each) == 7
