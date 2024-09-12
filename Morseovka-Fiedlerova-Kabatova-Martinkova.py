"""Program for encryption the english text to Morse code and vice versa."""
MORSE_CODE_DICT = {
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
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    }


def encryption(message):
    """Encrypts text to Morse code."""
    if len(message) == 0:
        return ''

    my_cipher = ''
    for myletter in message.upper():
        if myletter != ' ':
            my_cipher += MORSE_CODE_DICT[myletter] + ' '
        else:
            my_cipher += ' '
    return my_cipher.strip()


# This function is used to decrypt
# Morse code to English

def decryption(message):
    """Decrypts message in Morse code to text."""
    if len(message) == 0:
        return ''

    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:

        # checks for space

        if myletter != ' ':
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += \
                    list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mycitext)]  # noqa: E501
                mycitext = ''
    return decipher


def main():
    """Program encrypts message to Morse code, then decrypts message from Morse code to text."""  # noqa: E501
    my_message = 'python-program'
    output = encryption(my_message)
    print(output)
    my_message = \
        '.--. -.-- - .... --- -. -....- .--. .-. --- --. .-. .- --'
    output = decryption(my_message)
    print(output)


# Executes the main function

if __name__ == '__main__':
    main()


def testEncryption():
    """Pytest funkce encryption."""
    result = encryption('test')
    expected = '- . ... -'
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def testDecryption():
    """Pytest funkce decryption."""
    result = decryption('- . ... -')
    expected = 'TEST'
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def test2Encryption():
    """Pytest funkce encryption."""
    result = encryption('')
    expected = ''
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def test2Decryption():
    """Pytest funkce decryption."""
    result = decryption('')
    expected = ''
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess
