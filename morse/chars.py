"""Letters and their corresponding morse codes."""
letters_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '.': '.-.-.-',
    '?': '..--..', ',': '--..--', ' ': '/'
}

morse_to_letters = {
    '....': 'h', '.-': 'a', '-...': 'b', '-.-.': 'c',
    '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
    '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
    '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
    '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z', '.-.-.-': '.',
    '..--..': '?', '--..--': ',', '/': ' '
}
