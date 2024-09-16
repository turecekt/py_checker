"""
This project is made for translate text to morse code and morse code to text.

Author: Jan Baslar
"""

translator = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'CH': '----', 'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
              'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.',
              ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
              '?': '..--..', '!': '--...-', '-': '-....-', '/': '-..-.',
              '=': '-...-', '_': '..--.-', '(': '-.--.', ')': '-.--.-',
              '@': '.--.-.', '"': '.-..-.', ' ': ''}


def remove_diacritics(text: str) -> str:
    """Remove diacritics from text.

    Return uppercase text without diacritics
    """
    text = text.upper()
    diacritics = 'ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ'
    without = 'ACDEEINORSTUUYZ'
    for i in range(len(text)):
        if text[i] in diacritics:
            text = text.replace(text[i], without[diacritics.index(text[i])])
    return text


def alphabet_to_morse(text: str) -> str:
    """Translate text to morse code.

    Return text translated to morse code
    """
    result = ''
    text = remove_diacritics(text)
    index = 0
    while index < len(text):
        char = text[index]

        if index < len(text) - 1:
            if text[index: index + 2] == 'CH':
                char = 'CH'
                index += 1

        if char in translator:
            result += translator[char] + '|'
        index += 1

    return result


def get_key(letter: str, dictionary: dict) -> str:
    """Get key from dictionary.

    Return key from dictionary by value.
    """
    for key, value in dictionary.items():
        if letter == value:
            return key


def is_it_morse(text: str) -> bool:
    """Detect if the text is morse code.

    Return True if the text is morse code.
    """
    valid = '.-/| '
    for char in text:
        if char not in valid:
            return False
    return True


def find_splitter(text: str) -> str:
    """Find splitter of the morse code.

    Return '|' or ' ' or '/' as splitter.
    """
    valid = '| /'
    for char in text:
        if char in valid:
            return char
    return ' '


def morse_to_alphabet(text: str) -> str:
    """Translate text from morse code.

    Return text translated from morse code.
    """
    splitter = find_splitter(text)
    text = text.split(splitter + splitter)
    code = []
    for word in text:
        code += [word.split(splitter)]

    result = ''
    for word in code:
        for letter in word:
            result += get_key(letter, translator)
        result += ' '
    return result.lower().capitalize()


def main() -> None:
    """Get user input and translate it.

    Return None.
    """
    print('Zadejte text k přeložení z/do morseovy abecedy:')
    print()
    text = input()
    print()

    if is_it_morse(text):
        print(morse_to_alphabet(text))
    else:
        print(alphabet_to_morse(text))

    print()
    print('Press enter key to exit...')
    input()


def test_remove_diacritics() -> None:
    """Test remove_diacritics function."""
    assert (remove_diacritics('áčďéěíňóřšťúůýž') == 'ACDEEINORSTUUYZ')
    assert (remove_diacritics('Příliš žluťoučký kůň úpěl ďábelské ódy.')
            == 'PRILIS ZLUTOUCKY KUN UPEL DABELSKE ODY.')


def test_alphabet_to_morse() -> None:
    """Test alphabet_to_morse function."""
    assert (alphabet_to_morse('Nechť již hříšné saxofony ďáblů rozezvučí síň '
                              'úděsnými tóny waltzu, tanga a quickstepu.')
            == '-.|.|----|-||.---|..|--..||....|.-.|..|...|-.|.|'
               '|...|.-|-..-|---|..-.|---|-.|-.--|'
               '|-..|.-|-...|.-..|..-||.-.|---|--..|.|--..|...-|..-|-.-.|..|'
               '|...|..|-.||..-|-..|.|...|-.|-.--|--|..|'
               '|-|---|-.|-.--||.--|.-|.-..|-|--..|..-|--..--||-|.-|-.|--.|.-|'
               '|.-||--.-|..-|..|-.-.|-.-|...|-|.|.--.|..-|.-.-.-|')
    assert (alphabet_to_morse('My e-mail address is: stuart_little@utb.cz, '
                              'but you can call me "Steve";')
            == '--|-.--||.|-....-|--|.-|..|.-..||.-|-..|-..|.-.|.|...|...|'
               '|..|...|---...||...|-|..-|.-|.-.|-|..--.-|.-..|..|-|-|.-..|.|'
               '.--.-.|..-|-|-...|.-.-.-|-.-.|--..|--..--||-...|..-|-|'
               '|-.--|---|..-||-.-.|.-|-.||-.-.|.-|.-..|.-..||--|.|'
               '|.-..-.|...|-|.|...-|.|.-..-.|-.-.-.|')


def test_get_key() -> None:
    """Test get_key function."""
    assert (get_key('.---', translator) == 'J')
    assert (get_key('-....', translator) == '6')
    assert (get_key('.--.-.', translator) == '@')


def test_is_it_morse() -> None:
    """Test is_it_morse function."""
    assert (is_it_morse('-..|---|--.|.-.-.-|') is True)
    assert (is_it_morse('-.. --- --. .-.-.- ') is True)
    assert (is_it_morse('-../---/--./.-.-.-/') is True)
    assert (is_it_morse('dog.') is False)
    assert (is_it_morse('-.. --- G .-.-.- ') is False)


def test_find_splitter() -> None:
    """Test find_splitter function."""
    assert (find_splitter('-..|---|--.|.-.-.-|') == '|')
    assert (find_splitter('-.. --- --. .-.-.- ') == ' ')
    assert (find_splitter('-../---/--./.-.-.-/') == '/')
    assert (find_splitter('.-.-.-') == ' ')


def test_morse_to_alphabet() -> None:
    """Test morse_to_alphabet function."""
    assert (morse_to_alphabet('-|....|.||--.-|..-|..|-.-.|-.-|'
                              '|-...|.-.|---|.--|-.||..-.|---|-..-|'
                              '|.---|..-|--|.--.|...||---|...-|.|.-.|'
                              '|-|....|.||.-..|.-|--..|-.--|'
                              '|-..|---|--.|.-.-.-|')
            == 'The quick brown fox jumps over the lazy dog.  ')
    assert (morse_to_alphabet('....-||-..-.||-.--.|---..||-....-|'
                              '|-....|-.--.-||-...-||..---|')
            == '4 / (8 - 6) = 2  ')


if __name__ == '__main__':
    main()
