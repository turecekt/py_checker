# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:21:11 2020.

@author: pavel.
"""

# Slovnik morseovy abecedy.

morse = {
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
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-."
}


def encryption(message):
    """Funkce pro preklad textoveho retezce do morseovy abecedy."""
    encrypt = ''
    for letter in message:
        if letter != ' ':
            # Prideleni prislusneho znaku
            encrypt += morse[letter] + ' '
        else:
            encrypt += ' '
    return encrypt


def decryption(message):
    """Funkce pro preklad morseovy abecedy do textoveho retezce."""
    # sledovani poctu mezer
    global i
    message += ' '
    decrypt = ''
    crtext = ''
    for letter in message:
        if letter != ' ':
            # Pokud znak neni mezera, i se vynuluje
            i = 0
            crtext += letter
        else:
            # Kdyz i je rovno 1, prida se novy znak
            i += 1
            if i == 2:
                # Kdyz i je rovno 2, zapocne nove  slovo
                # Pridani mezery pro odliseni slov
                decrypt += ' '
            else:
                # proces desifrovani
                decrypt += \
                    list(morse.keys())[list(morse.values()).index(crtext)]
                crtext = ''
    return decrypt


def main():
    """Hlavní funkce programu."""
    # Input pro preklad textoveho retezce do morseovy abecedy
    message = input("Zadajte text, ktery chcete zasifrovat:")
    result = encryption(message.upper())
    print(result)
    # Input pro preklad morseovy abecedy do textoveho retezce
    message = input("Zadajte morseovu abecedu, kterou chcete odsifrovat:")
    result = decryption(message)
    print(result)


# Zavolani main funkce
if __name__ == '__main__':
    main()
