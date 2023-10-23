"""This is module to Ncode alphabet messages to morse code and vice versa.

module contains "asserts" alphanum chars
as morse code strings also my added separators codes

also contains multiple functions:

split_to_letters()
myArgParser()
checkConditions()
morseDecode()
morseNcode()

"""


import argparse
import re
import sys

# AlphNum list of Morse code
MORSE_ALPNUM = {
                    'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..',
                    'E': '.', 'F': '..-.',
                    'G': '--.', 'H': '....',
                    'CH': '----', 'I': '..',
                    'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--',
                    'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...',
                    'T': '-', 'U': '..-',
                    'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--',
                    'Z': '--..',
                    '1': '.----', '2': '..---',
                    '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..',
                    '9': '----.', '0': '-----',
                    ' ': '....----', '|': '----....'
                    }


def split_to_letters(my_string):
    """Functon split_to_letters returns list using argument my_string.

    Args:
        -my_string - Input string
    Returns:
        - list of separated characters
    """
    return list(my_string)


def myArgParser(args):
    """Functon myArgParser returns obj using argument args.

    Obj with parsed argument (which should be string)
    also checks if the string contains valid characters
    (alphanumeric chars, dots, dashes, verticals[as separators])
    takes argument from command line.

    Args:
        -args - Command line argument
    Returns:
        - st.MorseStr - input string
    """
    """
    This had to be because python (more like unix) doesnt
    take anything that starts wit dash as a string but
    it expects something to go after so I had to check for it. """

    args = sys.argv[1]
    if args.startswith("-"):
        if(" " not in args and "|" not in args) and args != "-h":
            if args in MORSE_ALPNUM.values():
                my_index = list(MORSE_ALPNUM.values()).index(args)
                message = list(MORSE_ALPNUM.keys())[my_index]
                sys.exit(message)
            else:
                sys.exit("please enter right morse code")
        elif("|" in args):
            return args

    msg = "type in string consist of morse code or alphanumeric characters"
    hlp = 'a string to decode/Ncode from/to morse code'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('MorseStr', metavar='String', type=str, help=hlp)

    st = parser.parse_args()

    errorObj = re.search(r'[^a-zA-Z0-9 \-\.\|]', st.MorseStr, re.I)
    if errorObj:
        sys.exit("please type in right characters")

    return st.MorseStr


def checkConditions(st):
    """Functon checkConditions returns lengths of string st.

    st is already stripped to characters without separators and
    string with separators.
    Returns string which is stripped
    it checks if is used only whitespaces or verticals
    and also if you want to only Ncode or Decode ...
    you cant do both at the same time
    then magic with verticals and spaces happens

    Args:
        -st - input string

    Returns:
        -len_basic_string - number of characters in string
        -len_splitString - number of characters in stripped string
        -splitString - stripped string (without separators)
    """
    separatorObj = re.search(r'[\|]+', st)
    whitespaceObj = re.search(r'[\s]+', st)
    morseObj = re.search(r'[.\-]', st, re.I)
    alphabetObj = re.search(r'[a-zA-Z0-9]', st, re.I)

    if separatorObj and whitespaceObj:
        sys.exit("please use only one way to split letters/words")

    if morseObj and alphabetObj:
        sys.exit("please use only alphanum characters or morse code")

    if separatorObj:
        st = re.sub(r'\|\|\|+', "||", st)
        newString = re.sub(r'\|\|', "|----....|", st)
        splitString = newString.split("|")
    elif whitespaceObj:
        newString = re.sub(r'\s\s', " ....---- ", st)
        splitString = newString.split()
    else:
        newString = st
        splitString = newString.split()

    len_splitString = len(splitString)
    len_basic_string = len(split_to_letters(st))

    return len_splitString, len_basic_string, splitString


def morseDecode(len_splitString, len_string, splitString, st):
    """Functon morseDecode returns printed Decoded message from morse code.

    it goes through the string and checks if
    you start or end with separators (not valid)
    also it checks if you use valid morse code which is written above
    Args:
        -st - input string
        -len_string - number of characters in none stripped input string
        -len_splitString - number of substrings in stripped input string
        -splitString - stripped input string into substrings from alphabet

    Returns:
        - message - returns the decoded message

    """
    letters = split_to_letters(st)
    message = ""
    for i in range(len_string):
        if i == 0 and (letters[i] == " " or letters[i] == "|"):
            sys.exit("please do not start with separators")
        if i == len_string-1 and (letters[i] == " " or letters[i] == "|"):
            sys.exit("please do not end with separators")

    for j in range(len_splitString):
        if splitString[j] not in MORSE_ALPNUM.values():
            sys.exit("please fill in right morse code")
        else:
            my_index = list(MORSE_ALPNUM.values()).index(splitString[j])
            message += list(MORSE_ALPNUM.keys())[my_index]
            # I was looking for some easy way to cooperate with the table ...
            # I found this at
            # (https://www.geeksforgeeks.org/morse-code-translator-python/)
            # and changed it for my code#
    return message


def morseNcode(len_splitString, len_basic_string, st):
    """Functon morseNcode ncodes the alphabet message.

    to the morse code it uses verticals as separators
    also it goes through the string and checks if you
    start or end with separators
    then it checks if the character is separator if not
    it replaces alphanum chars with morse chars

    Args:
        -st - input string
        -len_basic_string - number of characters in none stripped input string
        -len_splitString - number of substrings in stripped input string

    Returns:
        -ncode_message - morse coded message

    """
    st = st.upper()
    subStr = split_to_letters(st)
    ncode_message = ""

    for i in range(len_basic_string):
        if i != 0:
            ncode_message += "|"
        else:
            if subStr[i] == " " or subStr[i] == "|":
                sys.exit("please do not start with separators")
        if i == len_basic_string-1 and (subStr[i] == " " or subStr[i] == "|"):
            sys.exit("please do not end with separators")
        if subStr[i] != " " and subStr[i] != "|":
            ncode_message += MORSE_ALPNUM[subStr[i]]

    return ncode_message


def main():
    """Functon main runs the program.

    And all the functions are called
    """
    default_arg = sys.argv[0:]
    if default_arg == ['morseCode.py']:
        sys.exit("please fill in string argument type -h for help")
    myStr = myArgParser(sys.argv[1])

    morseObj = re.search(r'[.\-]', myStr, re.I)
    alphabetObj = re.search(r'[a-zA-Z0-9]', myStr, re.I)

    num_sub_str, len_b_string, splitString = checkConditions(myStr)

    if morseObj:
        message = morseDecode(num_sub_str, len_b_string, splitString, myStr)
    elif alphabetObj:
        message = morseNcode(num_sub_str, len_b_string, myStr)
    else:
        message = sys.argv[1]

    print(message)


if __name__ == '__main__':
    main()

"""
unit tests begin here
"""


def testSplitToLetters():
    """Functon testSplitToLetters runs test.

    It tests the first function split_to_letters
    """
    assert split_to_letters("....") == ['.', '.', '.', '.']
    assert split_to_letters("aaaa") == ['a', 'a', 'a', 'a']


def testCheckConditions():
    """Functon testCheckConditions runs test.

    It tests the second function checkConditions
    """
    value = (4, 12, ['....', '....----', '....----', '....'])
    assert(checkConditions("ahoj H") == (2, 6, ['ahoj', 'H']))
    assert(checkConditions("....    ....") == value)


def testMorseDecode():
    """Functon testMorseDecode runs test.

    It tests the function morseDecode
    """
    teStr = ".... ...."
    num_substring, basic_str_len, splitString = checkConditions(teStr)
    asStr = morseDecode(num_substring, basic_str_len, splitString, teStr)
    assert(asStr == "HH")
    test_string = "....||-...|-.--|-..|.-..|..||...-||..-|.-..|..|-.-.|..|"
    test_string += "|-.-.|---|..-|.--.|-.-|---|...-|-.--|-.-.|....|"
    test_string += "|----.|-----"
    num_substring, basic_str_len, splitString = checkConditions(test_string)
    asStr = morseDecode(num_substring, basic_str_len, splitString, test_string)
    assert(asStr == "H|BYDLI|V|ULICI|COUPKOVYCH|90")


def testMorseNcode():
    """Functon testMorseNcode runs test.

    It tests the function morseNcode
    """
    value = "....|.|.-..|.-..|---"
    num_substring, basic_str_len, splitString = checkConditions("hello")
    assert(morseNcode(num_substring, basic_str_len, "hello") == value)
    num_substring, basic_str_len, splitString = checkConditions("hello there")
    value = "....|.|.-..|.-..|---||-|....|.|.-.|."
    assert(morseNcode(num_substring, basic_str_len, "hello there") == value)
    teStr = "ulice coupkovych 8"
    value = "..-|.-..|..|-.-.|.||-.-.|---|..-|.--.|-.-|"
    value += "---|...-|-.--|-.-.|....||---.."
    num_substring, basic_str_len, splitString = checkConditions(teStr)
    assert(morseNcode(num_substring, basic_str_len, teStr) == value)
    teStr = "zitra|me|nevezes|do|bystrice"
    value = "--..|..|-|.-.|.-||--|.||-.|.|...-|.|--..|.|...|"
    value += "|-..|---||-...|-.--|...|-|.-.|..|-.-.|."
    num_substring, basic_str_len, splitString = checkConditions(teStr)
    assert(morseNcode(num_substring, basic_str_len, teStr) == value)
