"""Dictionary representing the morse code chart."""


MORSE_CODE_DICT = {'A': '.-',  'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..',
                   'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                   'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    """Funckia na zakryptovanie do morse kódu."""
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


def decrypt(message):
    """Funckia na dekryptovanie morse kódu do normálneho textu.

    pridané extra miesto na dekryptovanie posledného znaku

    """
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[
                            list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


def main():
    """Hlavna funkcia."""
    message = input("Zadaj nieco: ")
    result = encrypt(message.upper())
    print(result)

    message = "-.. .- -. .. . .-.. ...- .- ... -.- ---"
    result = decrypt(message)
    print(result)


# Executes the main function
if __name__ == '__main__':

    main()


def test_answer():
    """Unit test zakryptovania."""
    assert encrypt("35") == "...-- ..... "


def test_answer2():
    """Unit test dekryptovania."""
    assert decrypt(".-") == "A"


def test_answer3():
    """Unit test mix."""
    assert encrypt("A35") == ".- ...-- ..... "
