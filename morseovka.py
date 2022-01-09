""" Morseova abeceda """

MORSEOVA_ABECEDA = {
                    ' ': '/', 'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '@': '.--.-.',
                    '  ': '|', '=': '-...-'
                }

def sifrovani():
 #   """Šifrovaní textu do morseovky"""
    textNaSifrovani = input("Text pro šifrování do morseovy abecedy: ")
    sifra = [MORSEOVA_ABECEDA[i.upper()] + ' ' for i in textNaSifrovani if i.upper()
           in MORSEOVA_ABECEDA.keys()]
    vysledek = ''.join(sifra)
    print(vysledek)

#"""def desifrovani()"""
 #   """Dešifrování textu z moreovky"""
    



"""Výběrové menu"""
print('''\n Vyber možnost: 
             1 - Šifrování do morseovy abecedy
             2 - Dešifrování morseovy abecedy
             3 - konec''')



opakovat = True
while opakovat:
    volba = int(input("Zadej možnost 1-3: "))
    if __name__ == '__main__':
     if volba == 1:
      print(sifrovani())
      opakovat = False
     elif volba == 2:
      print("výběr dešifrování")
      opakovat = False
     elif volba == 3:
      print("ukončení programu")
      opakovat = False
     else: 
      print("Špatná možnost, opakuj výběr.")
    else:
     print('Znova')
