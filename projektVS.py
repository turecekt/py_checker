"""@file projektVS.py.

@brief Prekladac morseovky.
@author Lahoda, Slovak, Netbal, Masar.
"""


def toMorse(message):
    """Prevedeni textu do morseovky.

    Parametr[message] textovy retezec
    Returs prevedeny text do morseovky
    """
    Morseovka = {
        # Pismena
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Cisla
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Specialniznaky
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        " ": "",
    }
    vysledek = ""
    message = message.lower()
    for c in message:
        vysledek += Morseovka.get(c, ";") + " "
    if(vysledek.find(";") != -1):
        vysledek = "chybne zadany vstup"

    return vysledek


def testZkouska():
    """Unit test."""
    assert toMorse("a  b") == ".-   -... "


def toWord(morseMessage):
    """Prevadi z morseovky do textoveho retezce.

    param[morseMessage] retezec znaku v morseovce
    return prevedeny text z morseovky

    >>> toWord(".- -... -.-.")
    'abc'
    """
    Morseovka = {
        # Pismena
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Cisla
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Specialniznaky
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        " ": "",
    }
    vysledek = ""

    pom = morseMessage.split(" ")
    listValue = Morseovka.values()

    for x in pom:
        if(x in listValue != -1):
            vysledek += list(Morseovka.keys())[list(listValue).index(x)]
        else:
            vysledek = "Chybne zadany vstup: " + x
            break

    return vysledek


def testToMorse():
    """Unit test."""
    assert toMorse("a") == ".- "
    assert toMorse("I") == ".. "


def testLower():
    """Unit test."""
    assert "M".lower() == "m"


def testToMorseDalsi():
    """Unit test."""
    assert toMorse("Ahoj") == ".- .... --- .--- "
    assert toMorse("Ahoj svete") == ".- .... --- .---  ... ...- . - . "
    assert toMorse("1234") == ".---- ..--- ...-- ....- "


def testToMorseSlovo():
    """Unit test."""
    assert toMorse("Ahoj") == ".- .... --- .--- "
    assert toMorse("joha") == ".--- --- .... .- "


def testToMorse2Slova():
    """Unit test."""
    assert toMorse("ahoj svete") == ".- .... --- .---  ... ...- . - . "
    assert toMorse("Ahoj svete") == ".- .... --- .---  ... ...- . - . "


def testToWord():
    """Unit test."""
    assert toWord(".-") == "a"
    assert toWord("..") == "i"


def testDalsi():
    """Unit test."""
    assert toWord(".- .... --- .---") == "ahoj"
    assert toWord(".- .... --- .---  ... ...- . - .") == "ahoj svete"


def testToWordSlovo():
    """Unit test."""
    assert toWord(".- .... --- .---") == "ahoj"
    assert toWord(".- .--. .---- ...- ...") == "ap1vs"


def testToWord2Slova():
    """Unit test."""
    assert toWord(".- .... --- .---  ... ...- . - .") == "ahoj svete"
    assert toWord(".--- .-  - -.--  --- -.") == "ja ty on"


def testKontrola():
    """Unit test."""
    assert toMorse(";;;;") == "chybne zadany vstup"
    assert toWord(".----...-.-.") == "Chybne zadany vstup: .----...-.-."
    assert toMorse("   ") == "   "
    assert toWord("  ") == "   "


def testZnaky():
    """Unit test."""
    assert toMorse("&@") == ".-... .--.-. "


def main():
    """Funkce main slouzi pro zadavani vstupu od uzivatele.

    funkce main v soube vola metody toMorse() a toWord()
    """
    print('Vítej v našem dekodéru morseovky')

    chcePokracovat = True

    while(chcePokracovat):
        print("Kódování-[1] Dekódování-[2]")
        vstup = int(input())
        if(vstup == 1):
            print('Zadej co chces prelozit do morseovky: ')
            a = input()
            a = a.lower()
            print(a)
            d = toMorse(a)
            print(d)

            print("Chcete ukončit program? [y,n]")
            vyber = input()
            vyber = vyber.lower()
            if(vyber == "y"):
                chcePokracovat = False
            elif(vyber == "n"):
                chcePokracovat = True
            else:
                print("Už končím nemám na tebe náladu")
                chcePokracovat = False
        elif(vstup == 2):
            b = input("zadej text v morseovce: ")
            print(toWord(b))
            print("Chcete ukončit program? [y,n]")
            vyber = input()
            vyber = vyber.lower()
            if(vyber == "y"):
                chcePokracovat = False
            elif(vyber == "n"):
                chcePokracovat = True
            else:
                print("Už končím nemám na tebe náladu")
                chcePokracovat = False
        else:
            print("Chybný vstup!")
            print("Chcete ukončit program? [y,n]")
            vyber = input()
            vyber = vyber.lower()
            if(vyber == "y"):
                chcePokracovat = False
            elif(vyber == "n"):
                chcePokracovat = True
            else:
                print("Už končím nemám na tebe náladu")
                chcePokracovat = False


def testMain():
    """Unit test."""
    pass


if __name__ == '__main__':
    main()
