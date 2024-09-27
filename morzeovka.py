"""Morse Coder/Decoder."""
import pytest


"""Pole znaků morseovky pro šifrování a dešifrování."""
ZnakyMorseovy = {"A": ".-",
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
                 " ": "/",
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
                 ".": ".-.-.-",
                 ",": "--..--",
                 ":": "---...",
                 "?": "..--..",
                 "'": ".----.",
                 "-": "-....-",
                 "/": "-..-.",
                 "@": ".--.-.",
                 "=": "-...-"}

"""Inverze pole znaků pro použití v dešifrovací metodě."""
inverseZnakyMorseovy = dict((v, k) for (k, v) in ZnakyMorseovy.items())


def Desifrovat(morseKod, poziceRetezce=0):
    """Dekóduje/dešifruje vložený řetězec ve znacích morseovky."""
    if poziceRetezce < len(morseKod):
        znakMorseovky = ""
        for key, char in enumerate(morseKod[poziceRetezce:]):
            if char == " ":
                poziceRetezce = key + poziceRetezce + 1
                letter = inverseZnakyMorseovy[znakMorseovky]
                return letter + Desifrovat(morseKod, poziceRetezce)
            else:
                znakMorseovky += char
    else:
        return ""


def Zasifrovat(zprava):
    """Šifruje zprávu do znaků morseovky."""
    zasifrovanaZprava = ""
    for char in zprava[:]:
        zasifrovanaZprava += ZnakyMorseovy[char.upper()] + " "
    zasifrovanaZprava = zasifrovanaZprava[:-1]
    return zasifrovanaZprava


def GetInput(text):
    """Vrací input při a po výběru možnosti."""
    return input(text)


def if1(morseZprava):
    """Když se vybere možnost 1. spustí se dešifrovací metoda.

    >>> if1("- . ... - .----")
    TEST1
    """
    morseZprava += " "
    print(Desifrovat(morseZprava, 0))


def if2(textZprava):
    """
    Když se vybere možnost 2. spustí se šifrovací metoda.

    >>> if2("AUTOBUS")
    .- ..- - --- -... ..- ...
    """
    print(Zasifrovat(textZprava))


def ifRandom():
    """
    Při výběru jakékoliv jiné možnosti než 1 a 2 vyhodí hlášku.

    >>> ifRandom()
    ##########################
    Zadal jste špatnou hodnotu
    ##########################
    """
    print("##########################")
    print("Zadal jste špatnou hodnotu")
    print("##########################")


def multiif():
    """Output při spuštění programu."""
    print("#### Morse Translator ####")
    print("1 Dešifrovat")
    print("2 Zašifrovat")
    vstup = GetInput("Vyberte jednu z možností: ")
    if vstup == "1":
        morseZprava = GetInput("Zadejte kód morseovky: ")
        return if1(morseZprava)
    if vstup == "2":
        textZprava = GetInput("Zadejte zprávu k zašifrování: ")
        return if2(textZprava)
    else:
        return ifRandom()


def main():
    """Metoda main."""
    multiif()


@pytest.mark.parametrize("test_Zasifrovat_input, test_Zasifrovat_output",
                         [("TEST1", "- . ... - .----"),
                          ("TEST2", "- . ... - ..---"),
                          ("TEST3", "- . ... - ...--"),
                          ("TEST4", "- . ... - ....-"),
                          ("TEST5", "- . ... - ....."),
                          ("TEST6", "- . ... - -...."),
                          ("TEST7", "- . ... - --..."),
                          ("TEST8", "- . ... - ---.."),
                          ("TEST9", "- . ... - ----."),
                          ("TEST.", "- . ... - .-.-.-"),
                          ("TEST@", "- . ... - .--.-."),
                          ("TEST=", "- . ... - -...-")])
def test_Zasifrovani(test_Zasifrovat_input, test_Zasifrovat_output):
    """Test funkčnosti šifrovací metody."""
    vysledekSifry = Zasifrovat(test_Zasifrovat_input)
    assert vysledekSifry == test_Zasifrovat_output


@pytest.mark.parametrize("test_Desifrovat_output, test_Desifrovat_input",
                         [(".- ..- - --- -... ..- ... ", "AUTOBUS"),
                          (".-.-.- --..-- ---... ", ".,:"),
                          (".- .... --- .--- ", "AHOJ"),
                          ("..--.. .----. -....- ", "?'-"),
                          ("..--- ...-- ----- ", "230"),
                          (". -- .- .. .-.. .--.-. . -- .- .. .-.. ",
                           "EMAIL@EMAIL"),
                          (".---- ..--- ..... ...-- ", "1253"),
                          ("... - .-. .- -. -.- .- .-.-.- -.-. --- -- ",
                           "STRANKA.COM"),
                          (".- -... -.-. -.. . ", "ABCDE"),
                          ("-. --. ..- -.-- . -. ", "NGUYEN"),
                          ("..-. --. .... .--- -.- .-.. ", "FGHJKL"),
                          (".- ..-. ... .-- ", "AFSW"),
                          ("-- .. -.-. .... .- .-.. ", "MICHAL")])
def test_Desifrovat(test_Desifrovat_output, test_Desifrovat_input):
    """Test funkčnosti dešifrovací metody."""
    vysledekDesifry = Desifrovat(test_Desifrovat_output, 0)
    assert vysledekDesifry == test_Desifrovat_input


if __name__ == "__main__":
    main()
