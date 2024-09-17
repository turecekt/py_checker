"""Input text or morse code .Output translated text or morse."""
from morse import MorseCodeTranslator

if __name__ == "__main__":
    translator = MorseCodeTranslator()
    # Insert text for translation to morse
    text = input("Zadejte text: ")
    # Insert morse for translation to text
    morse = input("Zadejte morse code: ")
    # Translate text to morse code
    translated_morse = translator.translate_text(text)
    # Translate morse code to text
    translated_text = translator.translate_morse(morse)
    print(translated_morse)
    print(translated_text)
