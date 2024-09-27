"""Morse translator run file."""
from translator import encode, decode

if __name__ == '__main__':
    text_for_encoding = input("Insert text for encoding: ")

    morse_code = encode(text_for_encoding)
    print(morse_code)

    back_to_text = decode(morse_code)
    print(back_to_text)
