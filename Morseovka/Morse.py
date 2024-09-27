"""@package docstring.

@file             Morse.py
@author           Jiri Einspigl <j_einspigl@utb.cz>
@version          1.0
@brief            Morse Code Translator
"""
import pytest
import collections


"""Zdroj hodnot."""
knihovnaZnaku = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
                 '.': '.-.-.-', '?': '..--..', '(': '-.--.', ')': '-.--.-',
                 '/': '-..-.', '-': '-....-'}


def zasifruj(zprava):
    """Šifruje.

    >>> zasifruj('TEST')
    '- . ... -'
    """
    # proměná pro zašifrovanou zprávu
    sifra = ''
    # for postupně vybere každý znak ze zprávy
    for znak in zprava:
        if znak != ' ':
            # pokud je znak z knihovny - přiřadí znak z morseovy abecedy
            # a přidá za něj mezeru
            sifra += knihovnaZnaku[znak] + ' '
        else:
            # pokud je znak mezera - zapíše mezeru
            sifra += ' '
    sifra = sifra[:-1]
    # vrací zašifrovanou zprávu
    return sifra


# Unit testy metody zasifruj()
@pytest.mark.parametrize("test_sifrovani_input, test_sifrovani_output",
                         [('TEST', '- . ... -'),
                          ('TESTT', '- . ... - -'),
                          ('TTESTT', '- - . ... - -'),
                          ('TEEST', '- . . ... -')])
def test_sifovani(test_sifrovani_input, test_sifrovani_output):
    """Unit test pro šifrování."""
    Svysledek = zasifruj(test_sifrovani_input)
    assert Svysledek == test_sifrovani_output


def desifruj(zprava):
    """Dešifruje."""
    # přidá za zprávu mezeru pro zpřístupnění posledního znaku
    zprava += ' '
    # proměná pro dešifrovanou zprávu
    desifrovano = ''
    # proměná kam se ukládá jeden znak morseovky
    mznak = ''
    # for postupně vybere každý znak ze zprávy
    for znak in zprava:
        # kontroluje zda je znak mezera
        if (znak != ' '):
            # řeší mezery mezi znaky
            i = 0
            # zapíše znak ze zprávy do znaku morseovky
            mznak += znak
        else:
            # pokud je i = 1 - nový charakter morseovky
            i += 1
            # pokud je i = 2 - nové slovo
            if i == 2:
                # přidá mezeru mezi slova
                desifrovano += ' '
            else:
                # ošetřuje nepovolené znaky
                try:
                    # přiřadí hodnotu morseovky ke znaku abecedy
                    # a zapíše do proměné desifrovano
                    desifrovano += list(knihovnaZnaku.keys())[list(
                        knihovnaZnaku.values()).index(mznak)]
                    # vynuluje znak morseovky
                    mznak = ''
                except ValueError:
                    print('Chyba... nepovolený znak')
    desifrovano = desifrovano[:-1]
    # vrací dešifrovanou zprávu
    return desifrovano


# Unit testy metody desifruj()
@pytest.mark.parametrize("test_desifrovani_input, test_desifrovani_output",
                         [('- . ... - ', 'TEST'),
                          ('- . ... - - ', 'TESTT'),
                          ('- - . ... - - ', 'TTESTT'),
                          ('- . . ... - ', 'TEEST')])
def test_desifovani(test_desifrovani_input, test_desifrovani_output):
    """Unit test pro dešifrování."""
    Dvysledek = desifruj(test_desifrovani_input)
    assert Dvysledek == test_desifrovani_output


def spustenisifrovani(zprava):
    """Spouští šifrování.

    >>> spustenisifrovani('TEST')
    šifruji...
    Výsledek: - . ... -
    """
    vysledek = zasifruj(zprava.upper())
    print('šifruji...')
    print('Výsledek: ' + vysledek)


def spustenidesifrovani(zprava):
    """Spouští dešifrování.

    >>> spustenidesifrovani('- . ... - ')
    dešifruji...
    Výsledek: test
    """
    vysledek = desifruj(zprava)
    print('dešifruji...')
    print('Výsledek: ' + vysledek.lower())


def vypisknihovny():
    """Vypíše knihovnu znaků.

    >>> vypisknihovny()
    A = .-
    B = -...
    C = -.-.
    D = -..
    E = .
    F = ..-.
    G = --.
    H = ....
    I = ..
    J = .---
    K = -.-
    L = .-..
    M = --
    N = -.
    O = ---
    P = .--.
    Q = --.-
    R = .-.
    S = ...
    T = -
    U = ..-
    V = ...-
    W = .--
    X = -..-
    Y = -.--
    Z = --..
    1 = .----
    2 = ..---
    3 = ...--
    4 = ....-
    5 = .....
    6 = -....
    7 = --...
    8 = ---..
    9 = ----.
    0 = -----
    , = --..--
    . = .-.-.-
    ? = ..--..
    ( = -.--.
    ) = -.--.-
    / = -..-.
    - = -....-
    """
    temp = collections.Counter(knihovnaZnaku)
    for z in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.?()/-':
        print(z, '=', temp[z])


def dotaz(start):
    """Menu - dotaz.

    >>> dotaz('start')
    Chcete:
    [1] Zašifrovat zprávu
    [2] Dešifrovat zprávu
    [3] Automatický překlad zprávy (může chybovat)
    [4] Vypsat knihovnu znaků

    >>> dotaz('x')
    False
    """
    if(start == 'start'):
        # dotaz na akci
        print('Chcete:')
        print('[1] Zašifrovat zprávu')
        print('[2] Dešifrovat zprávu')
        print('[3] Automatický překlad zprávy (může chybovat)')
        print('[4] Vypsat knihovnu znaků')
    else:
        return False


def odpoved(dotaz):
    """Menu - odpoved.

    >>> odpoved('4')
    A = .-
    B = -...
    C = -.-.
    D = -..
    E = .
    F = ..-.
    G = --.
    H = ....
    I = ..
    J = .---
    K = -.-
    L = .-..
    M = --
    N = -.
    O = ---
    P = .--.
    Q = --.-
    R = .-.
    S = ...
    T = -
    U = ..-
    V = ...-
    W = .--
    X = -..-
    Y = -.--
    Z = --..
    1 = .----
    2 = ..---
    3 = ...--
    4 = ....-
    5 = .....
    6 = -....
    7 = --...
    8 = ---..
    9 = ----.
    0 = -----
    , = --..--
    . = .-.-.-
    ? = ..--..
    ( = -.--.
    ) = -.--.-
    / = -..-.
    - = -....-

    >>> odpoved('5')
    Neplatná hodnota
    """
    # if ... pro vybrání akce
    if (dotaz == '1' or dotaz == '1.'):
        zprava = input('Zadejte zprávu, kterou chcete zašifrovat' +
                       '(bez diakritiky): \n')
        spustenisifrovani(zprava)
    elif (dotaz == '2' or dotaz == '2.'):
        zprava = input('Zadejte zašifrovanou zprávu: \n')
        zprava += ' '
        spustenidesifrovani(zprava)
    elif (dotaz == '3' or dotaz == '3.'):
        zprava = input('Zadejte zprávu: \n')
        # rozhoduje zda je zpráva zašifrovaná
        if (zprava.startswith('.') or zprava.startswith('-')):
            zprava += ' '
            spustenidesifrovani(zprava)
        else:
            spustenisifrovani(zprava)
    elif (dotaz == '4' or dotaz == '4.'):
        vypisknihovny()
    else:
        print('Neplatná hodnota')


def konec(x):
    """Konec.

    Y - spouší znovu main() / N - ukončuje program
    >>> konec('X')
    Chyba...
    """
    if (x == 'N' or x == 'n'):
        exit(0)
    elif(x == 'Y' or x == 'y'):
        main()
    else:
        print('Chyba...')


def main():
    """Spuštění."""
    dotaz('start')
    Dotaz = input('')
    odpoved(Dotaz)
    x = input('Chcete pokračovat? [Y]/[N] \n')
    konec(x)


# Spuštění programu
if __name__ == '__main__':
    main()
