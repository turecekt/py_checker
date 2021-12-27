"""Welcome to 'MorseCode' module.

This module encode all ASCII alphabet characters,numbers
and special characters where letters are separated with '|'
character, words are separated with '||' character.
Module also supplies function: encode().

For example:

>>> encode("ahoj")
'.-|....|---|.---'
"""
import unicodedata
morseCodeDictionary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                       "e": ".", "f": "..-.", "g": "--.", "h": "....",
                       "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                       "m": "--", "n": "-.", "o": "---", "p": ".--.",
                       "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                       "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                       "y": "-.--", "z": "--..", " ": "",
                       "0": "-----", "1": ".----", "2": "..---", "3": "...--",
                       "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                       "8": "---..", "9": "----.",
                       ".": ".-.-.-", ",": "--..--", "?": "..--..",
                       "!": "--...-", ";": "-.-.-.", ":": "---...",
                       "(": "-.--.", ")": "-.--.-", "\"": ".-..-.",
                       "-": "-....-", "_": "..--.-", "@": ".--.-."}


def encode(text):
    """Return encoded morse code of argumet text as string.

    Args:
        - text - Some text for encoding

    Returns:
        - encoded string
    """
    morseCodetList = []
    text = removeDiacritic(text.lower())
    for letter in text:
        morseCodetList.append(morseCodeDictionary.get(letter))

    return "|".join(morseCodetList)


def removeDiacritic(text):
    """Return text with removed diacritic.

    Args:
        - text - Some text for encoding

    Returns:
        - string with removed diacritic
    """
    nfkdForm = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkdForm if not unicodedata.combining(c)])
