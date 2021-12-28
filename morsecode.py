

#Překladač textu do morseova kodu


#Funkce pro pro překlad textu do morse
def tomorse():

    # Abeceda pro překlad textu do morse 
    abeceda = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
               "k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
               "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---", "3":"...--",
               "4":"....-","5":".....","6":"-....","7":"--...","8":"---..", "9":"----.","0":"-----",",":"--..--",
               ".":".-.-.-","?":"..--..","/":"-..-.","-":"-....-","(":"-.--.",")":"-.--.-",":":"---...",";":"-.-.-.",
               "+":".-.-.","=":"-...-"}
               
    return abeceda

abeceda = tomorse()


# Vstup pro zadání textu
text = input("Zadej text který chceš přenést do morseovky : ")

morse_code = ""

for pismeno in text:
    if pismeno.lower() in abeceda.keys():
        morse_code += abeceda[pismeno.lower()] + " "
    else:
        morse_code += pismeno.lower() + " "
        
# Výstup překladače    
print(morse_code)

import unittest   # Importování Unit testu

if __name__ == '__main__':
    unittest.main()

