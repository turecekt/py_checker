"""Translator.

This module will encode alphabet letters into morse code
and decode morse code back into alphabet letters.
"""

# dictionary used for translating alphabet letters into morse code
Characters = {"A": ".-",
              "B": "-...",
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----",
              "?": "..--..",
              ",": "--..--",
              ".": ".-.-.-",
              ";": "-.-.-.",
              "/": "-..-.",
              "=": "-...-",
              "-": "-....-",
              "'": ".----.",
              "(": "-.--.",
              ")": "-.--.-",
              ":": "---...",
              "_": "..--.-",
              "+": ".-.-.",
              "@": ".--.-."}


def encode_morse(message):
    """Translate alphabet letters into morse code.

    Args:
        - message - Input of the function, string in quotation marks

    Returns:
        - encoded_message - Output of the function, message encoded
        into morse code
    """
    encoded_message = ""
    for char in message.upper():
        if char != " ":
            if char in Characters:
                encoded_message += Characters[char] + " "
            else:
                encoded_message += char + " "
        else:
            encoded_message += " "
    print(encoded_message.strip())
    return encoded_message.strip()


def decode_morse(message):
    """Translate morse code back to alphabet letters.

    Args:
        - message - Input of the function, string in quotation marks

    Returns:
        - decoded_message - Output of the function, message decoded
        from morse code into alphabet
    """
    message += " "
    decoded_message = ""
    letter = ""
    space = 0
    for char in message:
        if char != " ":
            letter += char
            space = 0
        else:
            space += 1
            if space > 1:
                # when there are two spaces, we found the end of the word
                # and a space is added to decoded message
                decoded_message += " "
            else:
                for key, value in Characters.items():
                    if letter == value:
                        decoded_message += key
                        letter = ""
    print(decoded_message.strip())
    return decoded_message.strip()


def main():
    """Process user input."""
    print("For encoding a message press 1.")
    print("For decoding a message press 2.")
    print("To close the program press 3.")
    x = input()
    if x == "1":
        print("Write a string that you want to encode into morse.")
        message = input()
        encode_morse(message)
    elif x == "2":
        print("Write a string that you want to decode from morse.")
        message = input()
        decode_morse(message)
    elif x == "3":
        return
    else:
        print("Wrong input.")
    main()
    return


if __name__ == "__main__":
    main()
