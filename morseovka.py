"""Seminarni prace - prekladac do Morseovy abecedy a zpet."""

MORSEUV_SLOVNIK = {
                    ' ': '/', 'A': '.-', 'B': '-...',
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
                    '(': '-.--.', ')': '-.--.-', '@': '.--.-.',
                    '  ': '|', '=': '-...-'
                }


# urceni prekladace
def sifrovani():
    """Přeložení do Morseovy abecedy."""
    text = input('Napis text pro Morseovo sifrovani : ')
    kod = [MORSEUV_SLOVNIK[i.upper()] + ' ' for i in text if i.upper()
           in MORSEUV_SLOVNIK.keys()]
    morseovka = ''.join(kod)
    print(morseovka)


# desifrovani na text
def desifrovani():
    """Přeložení z Morseovy abecedy."""
    text = input('Napis Morseuv kod pro desifrovani do textu: ')
    kod = [j for i in text.split()
           for j, k in MORSEUV_SLOVNIK.items() if i == k]
    text2 = ''.join(kod)

    print(text2)


print('''\n1 - Napis text pro Morseovo sifrovani
        \n2 - Napis Morseuv kod pro desifrovani do textu\n3 - Konec\n ''')


if __name__ == '__main__':

    vyber = int(input('Zvol moznost 1-3 a potvrd klavesou ENTER: '))
    if vyber == 1:
        print(sifrovani())

    elif vyber == 2:
        print(desifrovani())

    elif vyber == 3:
        print('Ukonceni')

    else:
        print('Spatne zadani, opakujte volbu')

else:
    print('Zadna volba nevyhovuje pozadavkum, zkuste to znova.')
