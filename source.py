"""PREKLADAC MORSEOVKY."""

slovnik = {
    # slovnik, obsahujici odpovidajici znaky v morseove abecede
    # pismena
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
    # cisla
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
    # jine znaky
    '&': ".-...",
    "'": ".----.",
    '@': ".--.-.",
    ')': "-.--.-",
    '(': "-.--.",
    ':': "---...",
    ',': "--..--",
    '=': "-...-",
    '!': "-.-.--",
    '.': ".-.-.-",
    '-': "-....-",
    '+': ".-.-.",
    '"': ".-..-.",
    '?': "..--..",
    '/': "-..-.",
}


def sifrovani(text):
    """Funkce sifrovani.

    funkce rozpozna znaky ve vlozenem
    retezci a kazdemu z nich priradi
    prislusny znak ze slovniku
    return: sifrovany text
    """
    sifrovany_text = ""
    for znak in text.upper():
        if znak != " ":
            # hleda znak v retezci
            sifrovany_text += slovnik[znak] + ' '
        else:
            # pokud najde mezeru, vlozi mezeru
            sifrovany_text += " "

    return sifrovany_text


def desifrovani(text):
    """Funkce desifrovani.

    funkce rozpozna vlozeny kod v morseovce
    a kazdemu znaku priradi prislusny znak
    ze slovniku
    return: desifrovany text
    """
    global mezery
    text += " "

    morse = ""
    desifrovany_text = ""
    for znak in text:
        if znak != " ":
            morse += znak
            mezery = 0
        else:
            # pokud najde 1 mezeru, pozna ze zacina novy znak
            mezery += 1
            if mezery == 2:
                # pokud 2 mezery, zacina nove slovo
                desifrovany_text += " "
            else:
                desifrovany_text += \
                    list(slovnik.keys())[list(slovnik.values()).index(morse)]
                morse = ""
    return desifrovany_text


# vstup od uzivatele:


def main():
    """Funkce na spousteni programu.

    uzivatel zada textove retezec,
    funkce vypise prelozene textove retezce
    """
    print("\n\t\t PREKLADAC MORSEOVKY")
    text = input("Vlozte text k sifrovani:")
    vysledek = sifrovani(text.upper())
    print(vysledek)

    text = input("Vlozte kod k desifrovani:")
    vysledek = desifrovani(text)
    print(vysledek)


if __name__ == '__main__':
    main()
