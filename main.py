"""Kodovaní a dekodovaní morseovky."""

abc = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'ch': '----',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' '
}


def domorse(preloz):
    """Kodavaní abcd... do morseovky."""
    zprava = ''  # proměna do ktere budeme dosazovat hodnoty
    # za každe písmeno v preloz se uděla příkaz pod tím.
    # Do proměne zpravy se zapisuje pismeno
    for pismeno in preloz:
        zprava += abc[pismeno] + ' '

    return zprava


def zmorse(preloz):
    """Dekodvaní morseovky do abcd."""
    global i
    preloz += ' '
    slovo = ''
    a = ''
    for letter in preloz:  # zas loop

        # na rozlišovani nových slov bereme
        if letter != ' ':

            # proměna pro přepinaní
            i = 0

            #
            a += letter

        # jestli tam nastane mezera
        else:
            # k i se připočte 1 indikuje novou hodnotu
            i += 1

            # jestli i=2 nové slovo
            if i == 2:

                #
                slovo += ' '
            else:

                # k vracene proměne se přípočíta klíč pomocí value
                # kde index hledá tečky čárky
                slovo += list(abc.keys())[list(abc.values()).index(a)]
                a = ''

    return slovo


def main():
    """Vybíraní programu a zadavni hodnot."""
    moznost = input("Zakodovat(a) přeložit(b)")
    if moznost == "a":
        preloz = input("")
        result = domorse(preloz.lower())
        print(result)
        input("")

    if moznost == "b":
        print("přiklad:.-. .-.. -.-- ")
        preloz = input(" ")
        result = zmorse(preloz)
        print(result.capitalize())
        input("")


if __name__ == '__main__':
    main()
