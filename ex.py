"""Example file to test decryption & encryption."""
from morse import MorseTranslator

translator = MorseTranslator()

text = 'this is a test program, see for yourself'

# Translate text to morse code
morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)
