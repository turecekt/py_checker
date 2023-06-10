"""Projekt MORSEOVKA.

Zadani
Vytvořte program, který umí kódovat i dekódovat Morseovu abecedu.
VSTUP
Textový řetězec
Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu.
VÝSTUP
Zakódovaná, případně dekódovaná morseovka
"""


MORSEOVKA = {
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}


def prevodDoMorseovky(vstup):
    """Funkce pro převod zadaneho textu do Morseovy abecedy.

    >>> prevodDoMorseovky("RADIM") == ".-. .- -.. .. -- "
    True
    """
    vystup = ''
    for znak in vstup:
        vystup = vystup + MORSEOVKA[znak] + ' '

    return vystup


def prevodZMorseovky(vstup):
    """Funkce pro převod z Morseovy abecedy do Morseovy abecedy.

    >>> prevodZMorseovky(".-. .- -.. .. --") == "RADIM"
    True
    >>> prevodZMorseovky(".-. .- -.. .. --") == "RDI"
    False
    """
    vstup += ' '
    vystup = ''
    pomocna = ''
    for znak in vstup:
        if (znak != ' '):
            i = 0
            pomocna += znak
        else:
            i += 1
            if i == 2:
                vystup += ' '
            else:
                vystup += list(
                    MORSEOVKA.keys())[list(MORSEOVKA.values()).index(pomocna)]
                pomocna = ''

    return vystup


if __name__ == '__main__':
    volba = input("1 pro zakódování, 2 pro dekódování z Morseovy abecedy: ")
    if volba == '1':
        print(prevodDoMorseovky
              (input("Zadej text pro převod do Morseovy abecedy: ").upper()))
    elif volba == '2':
        print(prevodZMorseovky
              (input("Zadej znaky morseovy abecedy pro převod : ")))
    else:
        print("nezvolil jsi správnou klávesu (1 nebo 2), program končí")

"""Otestovani kodu pomoci unit testů."""


def test_prevodDoMorseovky():
    """Unit test pro zakodovani do morseovky."""
    assert prevodDoMorseovky("RADIM") == ".-. .- -.. .. -- "
    assert prevodDoMorseovky("13578") == ".---- ...-- ..... --... ---.. "
    assert prevodDoMorseovky("AHOJ14") == ".- .... --- .--- .---- ....- "


def test_prevodZMorseovky():
    """Unit test pro dekodovani z morseovky."""
    assert prevodZMorseovky(".-. .- -.. .. --") == "RADIM"
    assert prevodZMorseovky(".---- ...-- ..... --... ---..") == "13578"
    assert prevodZMorseovky(".- .... --- .--- .---- ....-") == "AHOJ14"
