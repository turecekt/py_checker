"""Import zdrojového souboru."""

import morseovka


def test_prelozit_do():
    """Test na ověření funkčnosti programu pro překlad z abecedy do Mors."""
    # ověření překladače, jestli zvládne přeložit jednotlivé znaky
    assert morseovka.prelozit_do('A') == '.- '
    # ověření překladače, jestli zvládne přeložit slova s mezerou
    assert morseovka.prelozit_do('tomas hnanicek') == ('- --- -- .- ... | ....'
                                                       ' -. .- -. .. -.-. .'
                                                       ' -.- ')
    # ověření překladače, jestli zvládne přeložit jednotlivé znaky oddělené
    # mezerami
    assert morseovka.prelozit_do('A H O J') == '.- | .... | --- | .--- '
    # ověření překladače, jestli zvládne přeložit symboly#
    assert morseovka.prelozit_do('/,?)(') == ('-..-. --..-- ..--.. '
                                              '-.--.- -.--. ')
    # ověření překladače, jestli zvládne přeložit různé symboly,
    # čísla a znaky ve větě
    assert morseovka.prelozit_do('lor em 4 ipsum dolor sit amet , 6'
                                 ' consectetuer adipiscing elit? Cras el)'
                                 'ementum. Nulla accumsa'
                                 'n, 5') == ('.-.. --- .-. | . -- | ....- |'
                                             ' .. .--. ... ..- -- | -.. --- '
                                             '.-.. --- .-. | ... .. - | .- -- '
                                             '. - | --..-- | -.... | -.-. --- '
                                             '-. ... . -.-. - . - ..- . '
                                             '.-. | .- -.. .. .--. .. ... '
                                             '-.-. .. -. --. | . .-.. .. - '
                                             '..--.. | -.-. .-. .- ... | . '
                                             '.-.. -.--.- . -- . -. - ..- '
                                             '-- .-.-.- | -. ..- .-.. .-.. .- '
                                             '| .- -.-. -.-. ..- -- ... .- '
                                             '-. --..-- | ..... ')
    # ověření překladače, jestli zvládne přeložit čísla oddělené mezerami
    assert morseovka.prelozit_do('1 2 3 4') == ('.---- | ..--- | ...-- | '
                                                '....- ')


def test_prelozit_z():
    """Test na ověření funkčnosti programu pro překlad do abecedy."""
    # ověření překladače, jestli zvládne přeložit jednotlivé
    # znaky z Morseovy abecedy
    assert morseovka.prelozit_z('.-') == 'A'
    # ověření překladače, jestli zvládne přeložit celé slovo
    assert morseovka.prelozit_z('- --- -- .- ...') == 'TOMAS'
    # ověření překladače, jestli zvládne přeložit čísla oddělené mezerami
    assert morseovka.prelozit_z('.---- | ..--- | ...-- | ....-') == '1 2 3 4'
    # ověření překladače, jestli zvládne přeložit symboly
    assert morseovka.prelozit_z('..--.. -..-. -....- .-.-.-') == '?/-.'
    # ověření překladače, jestli zvládne přeložit slova oddělená mezerou
    assert morseovka.prelozit_z('- --- -- .- ... | .... -. .- -. .. ' +
                                '-.-. . -.-') == 'TOMAS HNANICEK'
    # ověření překladače, jestli zvládne přeložit větu
    assert morseovka.prelozit_z('.-.. --- .-. . -- | .. .--. ... ..- -- | ' +
                                '-.. --- .-.. --- .-. | ... .. - | ' +
                                '.- -- . -') == 'LOREM IPSUM DOLOR SIT AMET'
