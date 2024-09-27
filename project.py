"""@package docstring.

@file             project.py
@author           Ondrej Marecek <o_marecek@utb.cz>
@version          1.0
@brief            Morse Code Translator

@section LICENSE

This program is free to use....

@section DESCRIPTION

Morse code encryptor to and from morse code

"""
import sys

library = {'A': '.-', 'B': '-...',
           'C': '-.-.', 'D': '-..', 'E': '.',
           'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.',
           'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--',
           'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....',
           '7': '--...', '8': '---..', '9': '----.',
           '0': '-----', ', ': '--..--', '.': '.-.-.-',
           '?': '..--..', '/': '-..-.', '-': '-....-',
           '(': '-.--.', ')': '-.--.-', ' ': '.....'}


def morseencrypt(txt):
    """Convert morse code to latin from user inserted txt.

    Args:
        txt: string

    Returns: Translated user inputed string of morse code to latin
    >>> morseencrypt('.- -- ..... ---..')
    'AM 8'
    """
    translation = ''
    lib_encrypt = dict([(v, k) for k, v in library.items()])
    txt = txt.split(' ')
    for x in txt:
        translation += lib_encrypt.get(x)
    return translation.strip()


def morsedecrypt(txt):
    """Convert latin to morse code from user inserted txt.

    Args:
        txt: string

    Returns: Translated output of user inserted string to morse code
    >>> morsedecrypt('ABCD')
    '.- -... -.-. -..'
    >>> morsedecrypt('ABF1')
    '.- -... ..-. .----'
    """
    translation = ''
    txt = txt.upper()
    for x in txt:
        translation += library.get(x) + ' '
    return translation.strip()


def startMenu(parametr):
    """Generate output of translation.

    Args:
        parametr: Get info from user

    Returns: Translation of user or static string
    >>> startMenu('text')
    False
    >>> startMenu('start')
    Menu: (Zadejte číslo, popřípadě zmáčkněte enter)
    1: Překlad z morseovky do abecedy
    2: Překlad z abecedy do morseovky
    """
    if parametr == 'start':
        print("Menu: (Zadejte číslo, popřípadě zmáčkněte enter)")
        print("1: Překlad z morseovky do abecedy")
        print("2: Překlad z abecedy do morseovky")
    else:
        return False


def menuVyber(vyber):
    """Check if valid input is inserted.

    Args:
        vyber: Get string from user

    Returns: Choice in menu if user wants to translate to or from morse
    >>> menuVyber('')
    False
    >>> menuVyber('1')
    Zadejte morseovku/text který chcete přeložit
    '1'
    """
    if vyber == '':
        return False
    else:
        print("Zadejte morseovku/text který chcete přeložit")
        return vyber


def vypisText(text, menuVyber):
    """Show translated user text.

    Args:
        text: Get user inputed text that will  be translated
        menuVyber: Get choice from before that is needed in translation

    Returns: String of translated user input
    >>> vypisText('A', '2')
    .-
    >>> vypisText('A', '')
    False
    >>> vypisText('.-', '1')
    A
    """
    if menuVyber == '1':
        print(morseencrypt(text))
    elif menuVyber == '2':
        print(morsedecrypt(text))
    else:
        return False


arg = sys.argv
if 'menu' not in arg:
    print('Překlad slova Ahoj do morseovky:')
    text = 'Ahoj'
    print(morsedecrypt(text))
else:
    startMenu('start')
    vyber = (input(':'))
    menuVyber(vyber)
    vypisText(input(':'), menuVyber(vyber))
