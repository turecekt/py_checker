"""
SEMESTRALNI PROJEKT DO AP1VS.

FilipJadrnicek_MorseCode.py

version:    10

Authors: Filip Jadrnicek <https://github.com/gearszero>

---------------------------------------------------

THIS PROJECT CODES AND DECODES MORSE CODE IN PYTHON.
PROJECT WAS MADE SINGLE-HANDEDLY BY FILIP JADRNICEK.

---------------------------------------------------

---------------------------------------------------

HOW TO USE:
    INPUT EXAMPLE: abcd or AaBbCc or AaBbCc123654.
    Please don't use anything else then alphabet or numbers.

    INPUT EXAMPLE:.-|-...|-.-.|
    This input will decode morse code.

    !PLEASE DON'T COMBINE MORSE CODE AND ALPHABET!

---------------------------------------------------

This document owns University of Thomas Bata in Zlin (UTB FAI).

"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1",
           "2", "3", "4", "5", "6", "7", "8", "9", " "]

morseCode = [".-|", "-...|", "-.-.|", "-..|", ".|", "...-.|",
             "--.|", "....|", "..|", ".---|", "-.-|", ".-..|",
             "--|", "-.|", "---|", ".--.|", "--.-|", ".-.|",
             "...|", "-|", "..-|", "...-|", ".--|", "-..-|",
             "-.--|", "--..|", "-----|", ".----|", "..---|",
             "...--|", "....-|", ".....|", "-....|", "--...|",
             "---..|", "----.|", " "]


def is_code(letter):
    """Use this function for checking if input is morse code or not."""
    if letter == "." or letter == "-":
        return True

    else:
        return False


def convert_to_code(letter):
    """Use this function for converting input in letters to morse code."""
    global letters

    if letter not in letters:
        return -1

    i = letters.index(letter)
    return morseCode[i]


def convert_to_letter(code):
    """Use this function for converting morse code input to letters."""
    global morseCode

    tmp = code.split("|")
    tmp.pop(len(tmp) - 1)

    for x in range(len(tmp)):
        tmp[x] += "|"
        if tmp[x] not in morseCode:
            return -1

        i = morseCode.index(tmp[x])
        tmp[x] = letters[i]

    return tmp


def test_unit():
    """Use this function for unit testing the code."""
    checks = 0
    stringCheck = "abcdefghijklmnopqrstuvwxyz0123456789"
    morseCodeCheck = ".-|-...|-.-.|-..|.|...-.|--.|....|..|.---|-.-" \
                     "|.-..|--|-.|---|.--.|--.-|.-.|" \
                     "...|-|..-|...-|.--|-..-|-.--|--..|-----|.----" \
                     "|..---|...--|....-|.....|-....|--...|---..|----.|"
    checkMorse = []

    morseCodeCheckFinal = convert_to_letter(morseCodeCheck)
    morseCodeCheckFinal = ''.join(morseCodeCheckFinal)

    if stringCheck.upper() == morseCodeCheckFinal:
        checks += 1

    assert stringCheck.upper() == morseCodeCheckFinal
    for i in range(len(stringCheck)):
        checkMorse += convert_to_code(stringCheck[i].upper())

    checkMorse = ''.join(checkMorse)

    if checkMorse == morseCodeCheck:
        checks += 1

    assert checkMorse == morseCodeCheck
    if checks == 2:
        return True
    else:
        return False


def launch(message):
    """Use this message for lunch."""
    if test_unit():
        if message == "":
            # Checking if unit test return true.
            code = input("Enter morse code or sentence: ")
        else:
            # Checking if unit test return true.
            code = message

        # Checking what is first char in input, if it is . or -
        # it will use convert to letter function
        if is_code(code[0]):
            final = convert_to_letter(code)
            if final == -1 or final == '':
                print("ERROR INVALID INPUT, PLEASE USE THIS SYNTAX "
                      "exp: ...|---|...| for sos")
            else:
                final = ''.join(final)
                return final
        # Else it will use convert to code function
        else:
            finalLetter = []
            for i in range(len(code)):

                tmp = convert_to_code(code[i].upper())

                if tmp == -1:
                    print("ERROR INVALID INPUT, PLEASE USE THIS SYNTAX "
                          "exp: ...|---|...| for sos")
                    break

                else:
                    finalLetter += tmp

            finalLetter = ''.join(finalLetter)
            return finalLetter
    else:
        print("ERROR HAS OCCURRED WHILE UNIT TESTING")


def test_is_code():
    """Use this function for testing code."""
    assert is_code(".")


def test_convert_to_letter():
    """Use this function for testing covert to letter function."""
    convert_to_letter_text = convert_to_letter(".-|")
    assert convert_to_letter_text == ["A"]


def test_convert_to_code():
    """Use this function for testing convert to code function."""
    convert_to_code_test = convert_to_code("A")
    assert convert_to_code_test == ".-|"


def test_launch():
    """Use this for test launch."""
    launch_test = launch("A")
    assert launch_test == ".-|"


if __name__ == '__main__':
    print(launch(""))
