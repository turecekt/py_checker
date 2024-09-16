"""Prekladac z/do textu do/z kodu morse."""

# Pridani slovniku
Slovnik = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'ch': '----',
    'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-',
    'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '|', '': ''
}


def texttomorse(prelozeni):
    """Prelozeni textu do kodu Morse."""
    retezec = ''
    # pro kazdy zapsany symbol nachazi svuj kod Morse
    for symbol in prelozeni:
        retezec += Slovnik[symbol] + ' '
    return retezec


def morsetotext(prelozeni):
    """Prelozeni kodu Morse do textu."""
    n = 0
    slovo = ''
    promena = ''
    prelozeni += ' '

    for symbol in prelozeni:

        # Kontroluje jestli uzivatel zapsal specialni symbol mezery
        if symbol != ' ':
            n = 0
            promena += symbol

        # Jestli se tam objevi symbol mezery, udela tam mezeru
        else:
            n += 1
            if n == 2:
                slovo += ' '
            else:
                # Preklada kod Morse na odpovidajici symbol
                slovo += list(Slovnik.keys())[list(
                    Slovnik.values()).index(promena)]
                promena = ''
    # Pak vraci prelozeny text z kodu Morse
    return slovo


def main():
    """Tato funkce umoznuje vyber ze dvou cest."""
    vyber = input("1 - TEXT -> MORSE" "\n2 - MORSE -> TEXT")
    if vyber == "1":
        retezec = input("Zapiste vetu: ")
        vysledek = texttomorse(retezec.lower())
        print(vysledek)
    elif vyber == "2":
        retezec = input("Zapiste kod Morse: ")
        vysledek = morsetotext(retezec)
        print(vysledek)


if __name__ == '__main__':
    main()
