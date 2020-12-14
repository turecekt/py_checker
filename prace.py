"""Kodovani a dekodovaní morseovy text."""

"""Abeceda potřebná na překlad na Morse"""
morseABECEDA = {
    ' ': '/',
    'A': '.–/',
    'B': '–.../',
    'C': '–.–./',
    'D': '–../',
    'E': './',
    'F': '..–./',
    'G': '––./',
    'H': '..../',
    'CH': '––––/',
    'I': '../',
    'J': '.–––/',
    'K': '–.–/',
    'L': '.–../',
    'M': '––/',
    'N': '–./',
    'O': '–––/',
    'P': '.––./',
    'Q': '––.–/',
    'R': '.–./',
    'S': '.../',
    'T': '−/',
    'U': '..–/',
    'V': '...–/',
    'W': '.––/',
    'X': '–..–/',
    'Y': '–.––/',
    'Z': '––../'
}

"""Abeceda potřebná na překlad na text"""
ABECEDAmorse = {
    '/': ' ',
    '.–': 'A',
    '–...': 'B',
    '–.–.': 'C',
    '–..': 'D',
    '.': 'E',
    '..–.': 'F',
    '––.': 'G',
    '....': 'H',
    '––––': 'CH',
    '..': 'I',
    '.–––': 'J',
    '–.–': 'K',
    '.–..': 'L',
    '––': 'M',
    '–.': 'N',
    '–––': 'O',
    '.––.': 'P',
    '––.–': 'Q',
    '.–.': 'R',
    '...': 'S',
    '−': 'T',
    '..–': 'U',
    '...–': 'V',
    '.––': 'W',
    '–..–': 'X',
    '–.––': 'Y',
    '––..': 'Z'
}


def Txt_do_Morse(slovo):
    """Přeložení text do morse."""
    code = [morseABECEDA[i.upper()] + '' for i in slovo
            if i.upper() in morseABECEDA.keys()]
    morse = ''.join(code)
    print(morse)
    return morse


def Morse_do_Txt(slovo):
    """Přeložení morse na text."""
    novy = slovo.split('/')
    code = [ABECEDAmorse[i] + '' for i in novy if i in ABECEDAmorse.keys()]
    morse = ''.join(code)
    print(morse)
    return morse


print('''\n1- Prelozit text na Morseovku \n2- Prelozit Morseovku na text ''')

"""Vybrání možnosti překladu text do morse nebo morse na text."""
while True:
    try:
        selection = int(input('Vyberte si co na co chcete prekladat:'))
        if selection == 1:
            slovo = input('Napiš slovo')
            Txt_do_Morse(slovo)
            break
        elif selection == 2:
            slovo = input('Napiš slovo')
            Morse_do_Txt(slovo)
            break
        else:
            print('Spatna volba')
    except Exception:
        print('Spatna volba')


def test_Txt_do_Morse():
    """Předklad text na morse."""
    assert Txt_do_Morse('AHOJ') == '.–/..../–––/.–––/'
    assert Txt_do_Morse("DOMOV") == "–../–––/––/–––/...–/"
    assert Txt_do_Morse("DNES JE HEZKE POCASI") == \
           "–../–././...//.–––/.//...././––../–.–/.//.––./–––/–.–./.–/.../../"


def test_Morse_do_Txt():
    """Překlad morse na text."""
    assert Morse_do_Txt("−/–––/––/.//.–––/.–/–.–//.–––/./") == "TOMEJAKJE"
    assert Morse_do_Txt("–././.–./.–/–..//.––./.–./.–/–.–./..–/.–––/..–/") \
           == "NERADPRACUJU"
    assert Morse_do_Txt(".–./–.––/–.–./..../.–.././/–././–.../–––//.––."
                        "/–––/––/.–/.–../..–/") == "RYCHLENEBOPOMALU"
