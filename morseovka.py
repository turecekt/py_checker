"""Aplikace pro preklad morseovky."""

SLOVNIK_MORSEOVKA = {"A": ".-", "B": "-...",
                     "C": "-.-.", "D": "-..", "E": ".",
                     "F": "..-.", "G": "--.", "H": "....",
                     "I": "..", "J": ".---", "K": "-.-",
                     "L": ".-..", "M": "--", "N": "-.",
                     "O": "---", "P": ".--.", "Q": "--.-",
                     "R": ".-.", "S": "...", "T": "-",
                     "U": "..-", "V": "...-", "W": ".--",
                     "X": "-..-", "Y": "-.--", "Z": "--..",
                     "1": ".----", "2": "..---", "3": "...--",
                     "4": "....-", "5": ".....", "6": "-....",
                     "7": "--...", "8": "---..", "9": "----.",
                     "0": "-----", ", ": "--..--", ".": ".-.-.-",
                     "?": "..--..", "/": "-..-.", "-": "-....-",
                     "(": "-.--.", ")": "-.--.-"}

"""Dale definujeme prvni funkci.
Jako prvni vec definujeme text, kterenu mame doplnit text pro kodovani.
Dale vytvorime prevodovy text na kod.
Vytvorime string k danemu codu.
A string nechame precist."""


def Text_To_Code(text):
    """Fce pro preklad do morseovky."""
    text2 = str(text)
    code2 = [SLOVNIK_MORSEOVKA[i.upper()]
             + " " for i in text2 if i.upper() in SLOVNIK_MORSEOVKA.keys()]
    morseovka = "".join(code2)
    return morseovka


"""Stejny zpusob pouzijeme i zde i dekodovani nami zadaneho textu."""
"""Vytvorime zde to, ze nami zadany kod program rozlozi na jednotky."""
"""Opet nechame udelat string z code a nechame ho vypsat."""


def Code_To_Text(text):
    """Fce pro preklad morseovky."""
    text1 = str(text)
    code1 = [k for i in text1.split() for k,
             v in SLOVNIK_MORSEOVKA.items() if i == v]
    novytext = "".join(code1)
    return novytext


"""Vypiseme menu pro vyber, co chceme aby program delal."""
"""Na zaver vypisime cyklus, ktery nam k menu ve stringu priradi i funkce."""
"""Zvolili jsme fci else, ktera nam pokryje jinou moznost nez-li 1-3."""


print("""\n1 - TEXT KE KODOVANI\n2 - KOD K ROZKODOVANI\n3 - KONEC\n""")

if __name__ == "__main__":

    while True:

        vyber = int(input("TVUJ VYBER: "))

        if vyber == 1:
            print(Text_To_Code(input("Napiste slova, ktera chcete kodovat: ")))

        elif vyber == 2:
            print(Code_To_Text(input("Napiste kod, ktery chcete kodovat: ")))

        elif vyber == 3:
            print("UKONCUJI")
            exit()

        else:
            print("SPATNA VOLBA, ZKUSTE ZNOVU")
