"""Překladač."""
# Mapování písmen abecedy na znaky Morseovy abecedy
alphabetMorse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "ch": "----",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

# Mapování znaků Morseovy abecedy na písmena abecedy
morseAlphabet = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "----": "ch",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z"
}

# Mezera
space = " "
# Oddělovač znaků Morseovy abecedy
charSeparator = "|"


def isAlphabetTranslation():
    """Funkce, která zajišťuje správný výběr překladu."""
    print("Translate from:")
    print("1 - Alphabet")
    print("2 - Morse code")
    while True:
        # Kontrola, jestli je uživatelský vstup číslo
        try:
            index = int(input("Enter the translation number: "))
        except ValueError:
            print("Not an integer!")
            continue
        if (index == 1):
            return True
        elif (index == 2):
            return False
        else:
            continue


def alphabetTranslation(text):
    """Funkce překládá z abecedy do Morseovy abecedy."""
    result = ""
    for char in text.lower():
        if char in alphabetMorse:
            result += alphabetMorse[char]
        elif char == space:
            result += space
    return result


def morseCodeTranslation(text):
    """Funkce překládá z Morseovy abecedy do abecedy."""
    result = ""
    chars = text.split(charSeparator)
    for char in chars:
        if char in morseAlphabet:
            result += morseAlphabet[char]
        elif char == space:
            result += space
    return result


def translation(text, isAlphabet):
    """Funkce překládá text z Abecedy do Morseovy abecedy a naopak."""
    if text is None:
        return ""

    # Odstranění uvozovek na začátku a konci
    modifyText = text[1:-1].strip()
    # Kontrola prázdného řetězce
    if modifyText == "":
        return ""
    return (morseCodeTranslation(modifyText) if not isAlphabet else
            alphabetTranslation(modifyText))


def mainLoop(isRepeat):
    """Funkce s logikou hlavní smyčky programu."""
    # Menu (základní nastavení pro kódování a dekódování)
    (print("Welcome to the Translator!\n") if not isRepeat else
        print("Translator\n"))
    isAlphabet = isAlphabetTranslation()
    print()

    if not isAlphabet:
        print("Character separator \"|\".")
    text = input("Enter text between \"\": ")
    print()

    print("Translation:")
    print(translation(text, isAlphabet))


def run():
    """Hlavní smyčka programu."""
    isRepeat = False
    exitCode = 'n'

    # Spuštění hlavní smyčky
    while exitCode != 'y':
        mainLoop(isRepeat)
        exitCode = input("\nDo you want exit program (y/n): ").lower()
        print()
        isRepeat = True


if __name__ == '__main__':
    run()
