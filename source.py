"""
Program pro preklad textu na morseovku a naopak.

1. priklad - input:
"sos"
1. ocekavany output:
"...|---|..."
2. priklad - input:
"Wikipedia is a free online encyclopedia"
2. ocekavany output:
".--|..|-.-|..|.--.|.|-..|..|.-||..|...||.-||..-.|.-.|.|.||---|-.|.-..|..|-.|.||.|-.|-.-.|-.--|-.-.|.-..|---|.--.|.|-..|..|.-"

Petr Marak a Pavel Cuba, 2020
"""

table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
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
    ' ': '',
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
}


def get_letter_by_value(search_value):
    """
    Vyhleda ve slovniku table odpovidajici hodnotu.

    :parametr search_value: je hodnota, ktera se ma vyhledat ve slovniku table.
    :return: vraci odpovidajici klic (pismeno) ze slovniku, jinak None
    """
    for key, value in table.items():
        if value == search_value:
            return key
    return None


def encode(text):
    """Zakoduje zadany text do morseovy abecedy."""
    translated_text = ""
    global valid

    for i in text:
        # pokud je znak ve slovniku "table"
        if i in table:
            translated_text += table[i] + '|'
        else:
            print("Text neni validni")
            valid = False
            return None
            break
    # smaze posledni znak ktery je "|"
    translated_text = translated_text[0: len(translated_text) - 1]
    return translated_text


def decode(text):
    """Dekoduje (prevede) zadane znaky z morseovy abecedy na text."""
    translated_text = ""
    global valid
    buffer = ""

    for i in text:
        if i == '-' or i == '.':
            buffer += i
        # pokud to je konec slova
        elif i == '|':
            key = get_letter_by_value(buffer)
            if key:
                translated_text += key
                buffer = ""
            else:
                print("Text neni validni")
                valid = False
                return None
                break
        else:
            print("Text neni validni")
            valid = False
            return None
            break
    translated_text += get_letter_by_value(buffer)
    return translated_text


if __name__ == "__main__":
    text = input("Zadejte text: ").lower()
    valid = True

    # pokud prvni index je znak abecedy
    is_alphabet = True
    try:
        list(table.keys()).index(text[0])
    except ValueError:
        is_alphabet = False

    # prekladani
    if is_alphabet:
        translated_text = encode(text)

    else:
        translated_text = decode(text)

    if valid:
        print("Prelozeny text: ")
        print(translated_text)
