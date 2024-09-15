"""Modul pro spousteni kodu."""

from morse import MorseCodeTranslator

if __name__ == "__main__":
    translator = MorseCodeTranslator()

    text = input("Zadej string na preklad do morseovky a zpet: ")

    # Prelozi text do morseovky
    morse = translator.translate_text(text)

    # Prelozi morseovku na text
    translated_text = translator.translate_morse(morse)

    print(morse)
    print(translated_text)
