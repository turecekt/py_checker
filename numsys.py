"""Převodník numerických soustav."""

import sys


def main(argv):
    """Funkce která spustí UI programu.

    Podle zadaných parametrů provádí převod
    """
    if len(argv) > 2:
        return "Too much arguments"

    elif len(argv) < 2:
        return "Too few arguments"

    userDimensionChoice = argv[0]
    userValueToConvert = argv[1]

    if userDimensionChoice == "1":
        try:
            return convertToBinary(int(userValueToConvert))
        except ValueError:
            return "You must type in round number"

    elif userDimensionChoice == "2":
        try:
            return convertToOctal(int(userValueToConvert))
        except ValueError:
            return "You must type in round number"

    elif userDimensionChoice == "3":
        try:
            return convertToHexadecimal(int(userValueToConvert))
        except ValueError:
            return "You must type in round number"

    else:
        return "Wrong dimension choice"


def convertToBinary(number):
    """Vrací zadané číslo převedené do dvojkové soustavy.

    Arguments:
    number - číslo určené pro převod do dvojkové soustavy
    Returns:
    convertedNumber - číslo převedené do dvojkové soustavy
    """
    if not isinstance(number, int):
        return "number parameter must be round(int)"
    if number < 0:
        return "number parameter cant be negative"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 2 == 0:
            convertedNumber = "0" + convertedNumber
        else:
            convertedNumber = "1" + convertedNumber
        remainder = int(remainder / 2)

    return convertedNumber


def convertToOctal(number):
    """Vrací zadané číslo převedené do osmičkové soustavy.

    Arguments:
    number - číslo určené pro převod do osmičkové soustavy
    Returns:
    convertedNumber - číslo převedené do osmičkové soustavy
    """
    if not isinstance(number, int):
        return "number parameter must be round(int)"
    if number < 0:
        return "number parameter cant be negative"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 8 == 0:
            convertedNumber = "0" + convertedNumber
        if remainder % 8 == 1:
            convertedNumber = "1" + convertedNumber
        if remainder % 8 == 2:
            convertedNumber = "2" + convertedNumber
        if remainder % 8 == 3:
            convertedNumber = "3" + convertedNumber
        if remainder % 8 == 4:
            convertedNumber = "4" + convertedNumber
        if remainder % 8 == 5:
            convertedNumber = "5" + convertedNumber
        if remainder % 8 == 6:
            convertedNumber = "6" + convertedNumber
        if remainder % 8 == 7:
            convertedNumber = "7" + convertedNumber
        remainder = int(remainder / 8)

    return convertedNumber


def convertToHexadecimal(number):
    """Vrací zadané číslo převedené do šestnástkové soustavy.

    Arguments:
    number - číslo určené pro převod do šestnástkové soustavy
    Returns:
    convertedNumber - číslo převedené do šestnástkové soustavy
    """
    if not isinstance(number, int):
        return "number parameter must be round(int)"
    if number < 0:
        return "number parameter cant be negative"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 16 == 0:
            convertedNumber = "0" + convertedNumber
        if remainder % 16 == 1:
            convertedNumber = "1" + convertedNumber
        if remainder % 16 == 2:
            convertedNumber = "2" + convertedNumber
        if remainder % 16 == 3:
            convertedNumber = "3" + convertedNumber
        if remainder % 16 == 4:
            convertedNumber = "4" + convertedNumber
        if remainder % 16 == 5:
            convertedNumber = "5" + convertedNumber
        if remainder % 16 == 6:
            convertedNumber = "6" + convertedNumber
        if remainder % 16 == 7:
            convertedNumber = "7" + convertedNumber
        if remainder % 16 == 8:
            convertedNumber = "8" + convertedNumber
        if remainder % 16 == 9:
            convertedNumber = "9" + convertedNumber
        if remainder % 16 == 10:
            convertedNumber = "A" + convertedNumber
        if remainder % 16 == 11:
            convertedNumber = "B" + convertedNumber
        if remainder % 16 == 12:
            convertedNumber = "C" + convertedNumber
        if remainder % 16 == 13:
            convertedNumber = "D" + convertedNumber
        if remainder % 16 == 14:
            convertedNumber = "E" + convertedNumber
        if remainder % 16 == 15:
            convertedNumber = "F" + convertedNumber
        remainder = int(remainder / 16)

    return convertedNumber


if __name__ == "__main__":
    print(main(sys.argv[1:]))
