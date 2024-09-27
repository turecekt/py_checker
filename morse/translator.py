"""Main logic of the morse encoder/decoder."""
from chars import letters_to_morse, morse_to_letters


def encode(letters):
    """Letters are encoded to morse code.

    cycles through all the letters one by one
    sets each morse code for given letter to output variable
    returns morse code that is in the output variable.
    """
    letters = letters.lower()
    output = ''
    for i in letters:
        if i not in letters_to_morse:
            output = 'Data not formatted properly'
            break
        else:
            output += letters_to_morse[i] + ' '
    return output


def decode(morse):
    """Morse code is decoded to text.

    cycles through all the morse codes one by one
    sets each letter for given morse code to output variable
    returns decoded text that is in the output variable.
    """
    words = ''
    output = ''
    for i in morse:
        if i != ' ':
            words = words + i
            if i not in morse_to_letters:
                output = 'Data not formatted properly'
                break
        else:
            output += morse_to_letters[words] + ''
            words = ''
    return output
