"""PrekladacMorzeovejAbecedy."""

morse = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', "&": ".-...", "'": ".----.",
    "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-",
    "!": "-.-.--", ".": ".-.-.-", "-": "-....-",
    "+": ".-.-.", '"': ".-..-.", "?": "..--..",
    "/": "-..-."
}

# Funkcia na zakodovanie retazca
# podla morzeovej abecedy


def encrypt(sprava):
    """Funkcia na zakodovanie retazca podla morzeovej abecedy."""
    zasifruj = ''
    for letter in sprava:
        if letter != ' ':

            # Najde v prilusny znak a prida ho
            zasifruj += morse[letter] + ' '
        else:
            # 1 medzera znamena iny znak
            # a 2 medzery znamenaju nove slova
            zasifruj += ' '

    return zasifruj


# Funkcia na odkodovanie retazca
# z morzeovej abecedy
def decrypt(sprava):
    """Funkcia na odkodovanie retazca z morzeovej abecedy."""
    global i
    sprava += ' '

    odsifruj = ''
    citext = ''
    for letter in sprava:

        # kontroluje medzery
        if letter != ' ':

            # pocitadlo na medzery
            i = 0

            # u
            citext += letter

            # v pripade medzery
        else:
            # if i = 1 novy znak
            i += 1

            # if i = 2 nove slovo
            if i == 2:

                # pridanie medzery na oddelenie slov
                odsifruj += ' '
            else:

                # odkodovanie
                odsifruj += \
                    list(morse.keys())[list(morse.values()).index(citext)]
                citext = ''

    return odsifruj


# Funkcia na spustenie programu
def main():
    """Funkcia na spustenie programu."""
    sprava = input("Zadajte text na zakodovanie:")
    result = encrypt(sprava.upper())
    print(result)

    sprava = input("Zadajte text na odkodovanie:")
    result = decrypt(sprava)
    print(result)


# Vykona main funkciu
if __name__ == '__main__':
    main()
