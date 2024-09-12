"""Autori Petr Loukota a Natalie Vatterova."""


TEXT_DO_MORS = {'A': '.-',
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
                '0': '-----',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.'}


MORS_DO_TEXT = {}
for key, value in TEXT_DO_MORS.items():
    MORS_DO_TEXT[value] = key


def text_do_mors(zprava):
    """Preklad morzeovky."""
    mors = []
    for char in zprava:
        if char in TEXT_DO_MORS:
            mors.append(TEXT_DO_MORS[char])
    return " ".join(mors)


def mors_do_text(zprava):
    """Preklad textu do morzeovky."""
    zprava = zprava.split(" ")
    text = []
    for code in zprava:
        if code in MORS_DO_TEXT:
            text.append(MORS_DO_TEXT[code])
    return " ".join(text)


def main():
    """Zobrazenie 1 alebo 2 podla toho co si vyberieme."""
    while True:
        response = input("Morseovku na text(1) Text na morseovku(2)?").upper()
        if response == "1" or response == "2":
            break

    if response == "1":
        print("Napiste morseovku (s mezerou mezi kazdym pismenem): ")
        mors = input("")
        text = mors_do_text(mors)
        print("Text prevedeny z morseovky je:  ")
        print(text)

    elif response == "2":
        print("Napište text: ")
        text = input("").upper()
        mors = text_do_mors(text)
        print("Morseovka prevedena z textu je:  ")
        print(mors)


if __name__ == "__main__":
    main()
