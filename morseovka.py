
"""Morseova abeceda."""


MORSEOVA_ABECEDA = {'A': '.-',  'B': '-...', 'C': '-.-.',
                    'D': '-..', 'E': '.', 'F': '..-.',
                    'G': '--.', 'H': '....', 'I': '..',
                    'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-', 'R': '.-.',
                    'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def sifrovani():
    """Sifrovani textu do morseovky."""
    text = input("Text pro sifrovani do morseovy abecedy: ")
    sifra = [MORSEOVA_ABECEDA[i.upper()] + " " for i in text if i.upper()
             in MORSEOVA_ABECEDA.keys()]
    vysledek = "".join(sifra)
    print(vysledek)


def desifrovani():
    """Desifrovani textu z moreovky."""
    textNaDesifrovani = input("Text pro desifrovani z morseovy abecedy: ")
    desifra = [j for i in textNaDesifrovani.split() for j, k
               in MORSEOVA_ABECEDA.items() if i == k]
    vysledek = "".join(desifra)
    print(vysledek)


"""Vyberove menu"""
print("""Vyber moznost:
1 - Sifrovani do morseovy abecedy
2 - Desifrovani morseovy abecedy""")


def main():
    """Vyber sifrovani = 1, desifrovani = 2."""
    volba = int(input("Zadej moznost 1-2: "))
    if volba == 1:
        print(sifrovani())
    elif volba == 2:
        print(desifrovani())


if __name__ == "__main__":

    main()


def test_sifrovani1():
    """Test testujici string o jednom slove."""
    ocekavanyVysledek = "- . ... -"
    assert sifrovani
    ("test") == ocekavanyVysledek


def test_sifrovani2():
    """Test testujici string o vice slovech."""
    ocekavanyVysledek2 = "--.. -.- --- ..- ... -.- .- / - . ... -..-"
    assert sifrovani
    ("zkouska testu") == ocekavanyVysledek2


def test_sifrovani3():
    """Test testujici string o vete."""
    ocekavanyVysledek3 = """-.. -. . ... -.- .- / .--- .
    / .--. . -.- -. -.--/ -.. . -."""
    assert sifrovani
    ("dneska je pekny den") == ocekavanyVysledek3


def test_sifrovani4():
    """Test testujici cisel."""
    ocekavanyVysledek5 = "..--- -.... ....-"
    assert sifrovani
    ("264") == ocekavanyVysledek5


def test_desifrovani1():
    """Test testujici desifrovani stringu o jednom slove."""
    ocekavanyVysledek4 = "test"
    assert desifrovani
    ("- . ... -") == ocekavanyVysledek4


def test_desifrovani2():
    """Test testujici desifgitrovani stringu o dvou slovech."""
    ocekavanyVysledek5 = "test prosel"
    assert desifrovani
    ("- . ... - / .--. .-. --- ... . .-.. ") == ocekavanyVysledek5


def test_desifrovani3():
    """Test testujici desifrovani stringu o vete."""
    ocekavanyVysledek6 = "budeto urcite fungovat"
    assert desifrovani
    ("""-... ..- -.. . / ..- .-. -.-. .. - . /
    ..-. ..- -. --. --- ...- .- -""") == ocekavanyVysledek6
